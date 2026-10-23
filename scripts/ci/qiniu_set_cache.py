#!/usr/bin/env python3
"""修正已上传到七牛 Kodo 的 HTML / 搜索索引的 Cache-Control，并按需刷新 CDN 缓存。

为什么需要这一步：
    七牛 Kodo 对没有设置元数据的对象，一律输出
    `Cache-Control: public, max-age=31536000`（1 年）。
    站点资源分两类，长缓存只对其中一类成立：
      - 静态资源（/assets/**）文件名带内容哈希，URL 变了才会失效 → 1 年没问题；
      - HTML、search_index.json、sitemap.xml 每次构建都变，URL 却不变
        → 浏览器与 CDN 边缘会一直复用旧副本，用户必须强制刷新才能看到新内容。
    对象自身的元数据优先于空间默认值，所以只要给这些文件补上
    `cacheControl`，即可在不改动上传流程的前提下修正缓存行为。

做法：
    1) 元数据：上传完成后调用七牛的「批量操作」接口（POST /batch），
       批量执行 /chgm 写入 cacheControl（单请求最多 1000 个操作）。
       为避免每次部署都重刷上万次接口，脚本把「已处理过的内容指纹」记在状态文件里，
       只处理新增或内容变化的文件：首次运行等于全量兜底，之后即为增量。
    2) CDN 刷新：只对「元数据已生效、但还没为当前内容刷新过」的 URL 提交刷新。
       七牛的刷新配额很小（文件刷新 500 个/天、单次最多 20 个），
       因此按配额感知分批提交；本次没刷完的会留在状态里，下次部署继续，不会丢。

    ★ 两件事的状态分开记录：`keys`（元数据已设）与 `refreshed`（CDN 已刷）。
      合并成一个布尔值会导致「配额不足跳过刷新 → 记成已处理 → 以后永远不再刷」。

用法：
    python3 scripts/ci/qiniu_set_cache.py <site_dir> [选项]

选项：
    --state PATH          状态文件路径（默认 .qiniu-cache-state.json）
    --dry-run             只打印将要执行的操作，不发任何请求
    --refresh URL_PREFIX  处理完后刷新 CDN，需完整前缀（如 https://docs.daocloud.io/）
                          当前 CI 不启用：该域名是 Kodo 源站直连（未接 CDN），
                          刷新接口恒返回 400032。缓存由「空间 maxAge=300 兜底 +
                          本脚本把 HTML 设为 no-cache」两层保证，无需刷新。
    --max-refresh N       每个自然日（北京时间）最多刷新 N 个 URL，
                          跨当天多次部署累计；默认 0 = 仅受当日剩余配额约束
                          配额由同一账号下的所有业务共享，故应留出余量
    --strict              任一操作失败即返回非 0（默认：部分失败只告警）
    --selftest            用官方文档给出的测试向量校验签名算法，然后退出

环境变量：
    QINIU_ACCESS_KEY / QINIU_SECRET_KEY / QINIU_BUCKET
"""

from __future__ import annotations

import argparse
import base64
import datetime
import hashlib
import hmac
import json
import os
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# 七牛资源管理接口（rs，管理鉴权）与 CDN 接口（fusion，QBox 鉴权）
RS_HOST = "rs.qiniuapi.com"
FUSION_HOST = "fusion.qiniuapi.com"

# 只对「每次构建都变、URL 却不变」的产物关闭缓存。
# 其余资源保持七牛默认的长缓存：/assets/** 文件名含内容哈希，安全。
CACHE_POLICY = "no-cache"
NO_CACHE_FILES = {"search_index.json", "sitemap.xml", "sitemap.xml.gz"}
NO_CACHE_SUFFIXES = {".html"}

CHUNK = 1 << 20  # 1 MiB
# 七牛 /batch 单次请求的操作数上限（各官方 SDK 统一取 1000）
BATCH_MAX = 1000
# 七牛 CDN「文件刷新」单次请求的 URL 上限（官方硬限制，超了报 400034）
REFRESH_BATCH_MAX = 20
# 官方默认日配额；实际以接口返回的 urlSurplusDay 为准，这里只作兜底
REFRESH_DAILY_FALLBACK = 500
# 刷新配额按北京时间自然日重置，而 CI runner 跑在 UTC。
# 不显式换算的话，北京 00:00–08:00 的部署会被算进「前一天」，
# 同一个自然日会被发放两份预算，等于没限额。
CST = datetime.timezone(datetime.timedelta(hours=8))
# 状态文件格式版本；v1 只有 keys，没有 refreshed；v3 起带当日刷新预算
STATE_VERSION = 3


def urlsafe_base64_encode(data: bytes) -> str:
    """七牛要求的 URL 安全 Base64（保留 = 填充）。"""
    return base64.urlsafe_b64encode(data).decode()


def management_token(
    method: str,
    path: str,
    host: str,
    access_key: str,
    secret_key: str,
    content_type: str | None = None,
    body: str | None = None,
) -> str:
    """生成七牛管理凭证（用于 rs.qiniuapi.com）。

    待签名字符串的拼装规则见
    https://developer.qiniu.com/kodo/manual/1201/access-token
    """
    signing_str = f"{method} {path}\nHost: {host}\n"
    if content_type:
        signing_str += f"Content-Type: {content_type}\n"
    signing_str += "\n"
    # 官方 SDK 只在「有 Content-Type 且不是 octet-stream」时才把 body 签进去
    if body and content_type and content_type != "application/octet-stream":
        signing_str += body

    sign = hmac.new(
        secret_key.encode("utf-8"), signing_str.encode("utf-8"), hashlib.sha1
    ).digest()
    return f"{access_key}:{urlsafe_base64_encode(sign)}"


def qbox_token(path: str, access_key: str, secret_key: str) -> str:
    """生成七牛 QBox 凭证（用于 fusion.qiniuapi.com）。

    与 management_token 是两套算法，不能混用：
      - 签名串只有「接口路径 + query + 换行」一项，
        **不含**域名、协议、Content-Type 和请求体；
      - 头部前缀是 `QBox`，不是 `Qiniu`。
    依据：https://developer.qiniu.com/fusion/13360/fusion-api-auth-guide
    （只有 application/x-www-form-urlencoded 的请求体参与签名，
      CDN 接口一律是 JSON，故请求体不参与。）
    """
    signing_str = f"{path}\n"
    sign = hmac.new(
        secret_key.encode("utf-8"), signing_str.encode("utf-8"), hashlib.sha1
    ).digest()
    return f"{access_key}:{urlsafe_base64_encode(sign)}"


def encoded_entry_uri(bucket: str, key: str) -> str:
    """EncodedEntryURI = urlsafe_base64("<bucket>:<key>")。"""
    return urlsafe_base64_encode(f"{bucket}:{key}".encode("utf-8"))


def chgm_op(bucket: str, key: str, cache_control: str) -> str:
    """/chgm 操作指令：/chgm/<EncodedEntryURI>/cacheControl/<EncodedCacheControl>。"""
    return (
        f"/chgm/{encoded_entry_uri(bucket, key)}"
        f"/cacheControl/{urlsafe_base64_encode(cache_control.encode('utf-8'))}"
    )


def batch_body(bucket: str, keys: list[str], cache_control: str) -> str:
    """构造 /batch 的请求体：`op=<urlencoded op>&op=<urlencoded op>...`。

    op 里含 base64 的 `=` 填充，必须整体做百分号编码后再拼进表单体。
    """
    return "&".join(
        "op=" + urllib.parse.quote(chgm_op(bucket, key, cache_control), safe="")
        for key in keys
    )


def batch_set_cache_control(
    bucket: str,
    keys: list[str],
    cache_control: str,
    access_key: str,
    secret_key: str,
) -> tuple[set[str], dict[str, str]]:
    """用 /batch 一次修改多个对象的 Cache-Control。

    请求体为 `op=<op>&op=<op>...`（form-urlencoded），响应是同序的 JSON 数组，
    每项形如 {"code": 200} 或 {"code": 4xx, "data": {"error": "..."}}。

    返回 (成功的 key 集合, {失败的 key: 错误信息})。
    """
    path = "/batch"
    content_type = "application/x-www-form-urlencoded"
    body = batch_body(bucket, keys, cache_control)

    def all_failed(message: str) -> tuple[set[str], dict[str, str]]:
        return set(), {key: message for key in keys}

    token = management_token(
        "POST", path, RS_HOST, access_key, secret_key, content_type, body
    )
    req = urllib.request.Request(
        f"https://{RS_HOST}{path}",
        data=body.encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Qiniu {token}",
            "Content-Type": content_type,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return all_failed(f"HTTP {exc.code} {exc.read().decode(errors='replace')}")
    except OSError as exc:
        # 覆盖 URLError、超时，以及 RemoteDisconnected 这类 http.client 异常
        # （它不是 URLError 的子类，只捕获 URLError 会漏掉）
        return all_failed(f"连接失败：{getattr(exc, 'reason', exc)}")

    try:
        results = json.loads(payload)
    except json.JSONDecodeError:
        return all_failed(f"响应无法解析：{payload[:200]}")

    if not isinstance(results, list) or len(results) != len(keys):
        return all_failed(f"响应条数与请求不符（{len(results)} != {len(keys)}）")

    ok: set[str] = set()
    errors: dict[str, str] = {}
    for key, item in zip(keys, results):
        if item.get("code") == 200:
            ok.add(key)
        else:
            data = item.get("data") or {}
            errors[key] = str(data.get("error") or f"code {item.get('code')}")
    return ok, errors


def refresh_cdn(
    urls: list[str], access_key: str, secret_key: str
) -> dict[str, object]:
    """调用 CDN 缓存刷新接口（POST /v2/tune/refresh）。

    鉴权是 **QBox**（路径签名），不是管理接口的 Qiniu 前缀 + 完整签名串；
    混用会稳定返回 401，而旧实现只打一行 WARN，问题会被完全掩盖。

    返回值是接口的 JSON 响应（dict）。成功时含 code=200 与 urlSurplusDay
    （当日剩余刷新额度），失败时 code 为业务错误码或 HTTP 状态码。
    """
    path = "/v2/tune/refresh"
    body = json.dumps({"urls": urls}, ensure_ascii=False, separators=(",", ":"))
    req = urllib.request.Request(
        f"https://{FUSION_HOST}{path}",
        data=body.encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"QBox {qbox_token(path, access_key, secret_key)}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        # 业务错误（如 400031 invalid url）既可能以 HTTP 200 + code 返回，
        # 也可能以 HTTP 4xx + JSON 体返回；后者必须取 body 里的 code，
        # 否则会丢掉 invalidUrls，把「部分 URL 无效」误当成普通失败而反复重试。
        try:
            parsed = json.loads(detail)
        except json.JSONDecodeError:
            parsed = None
        if isinstance(parsed, dict):
            parsed.setdefault("code", exc.code)
            return parsed
        return {"code": exc.code, "error": f"HTTP {exc.code} {detail[:200]}"}
    except OSError as exc:
        return {"code": -1, "error": f"连接失败：{getattr(exc, 'reason', exc)}"}

    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return {"code": -1, "error": f"响应无法解析：{payload[:200]}"}
    if not isinstance(data, dict):
        return {"code": -1, "error": f"响应格式异常：{payload[:200]}"}
    return data


def collect_targets(site: Path) -> dict[str, Path]:
    """挑出需要关闭缓存的文件，返回 {相对 key: 本地路径}。"""
    targets: dict[str, Path] = {}
    for path in sorted(site.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in NO_CACHE_SUFFIXES or path.name in NO_CACHE_FILES:
            targets[path.relative_to(site).as_posix()] = path
    return targets


def fingerprint(path: Path) -> str:
    """内容指纹，格式与 qiniu_changed.py 保持一致：<size>:<blake2b>。"""
    digest = hashlib.blake2b(digest_size=16)
    size = 0
    with path.open("rb") as fh:
        while True:
            block = fh.read(CHUNK)
            if not block:
                break
            size += len(block)
            digest.update(block)
    return f"{size}:{digest.hexdigest()}"


def _str_map(value: object) -> dict[str, str]:
    """只接受 {str: str}，其余一律当作损坏数据丢掉。"""
    if not isinstance(value, dict):
        return {}
    return {
        str(k): str(v)
        for k, v in value.items()
        if isinstance(k, str) and isinstance(v, str)
    }


def today_cst() -> str:
    """北京时间自然日。七牛刷新配额按这个日界重置。"""
    return datetime.datetime.now(CST).date().isoformat()


def resolve_budget(
    budget: dict[str, object], today: str, daily_limit: int
) -> tuple[dict[str, object], int | None]:
    """跨自然日重置当日预算，返回 (新的预算记录, 本次可用额度)。

    可用额度为 None 表示不限（``--max-refresh 0``）。
    跨日判断只比日期字符串：时区已在 ``today_cst()`` 里统一到北京时间。
    """
    used = 0
    if budget.get("day") == today:
        raw = budget.get("used")
        # bool 是 int 的子类，必须排除，否则 true 会被当成 1
        if isinstance(raw, int) and not isinstance(raw, bool):
            used = max(0, raw)
    left = max(0, daily_limit - used) if daily_limit > 0 else None
    return {"day": today, "used": used}, left


def load_state(path: Path) -> tuple[dict[str, str], dict[str, str], dict[str, object]]:
    """读取状态，返回 (元数据已生效的 {key: 指纹}, CDN 已刷新的 {key: 指纹}, 当日预算)。

    策略变更（例如以后改成 no-store）时旧记录全部失效，触发一次全量重设。
    v1 状态没有 refreshed 字段 —— 那些页面从未刷过 CDN，按「待刷新」处理，
    由调用方在配额内逐步补齐，而不是假装已刷。
    """
    if not path.is_file():
        return {}, {}, {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        ci_warning(f"状态文件不可读（{exc}）；本次按全量处理")
        return {}, {}, {}
    if not isinstance(data, dict):
        ci_warning("状态文件格式异常；本次按全量处理")
        return {}, {}, {}
    if data.get("policy") != CACHE_POLICY:
        return {}, {}, {}
    budget_raw = data.get("budget")
    budget: dict[str, object] = {}
    if isinstance(budget_raw, dict) and isinstance(budget_raw.get("day"), str):
        used = budget_raw.get("used")
        budget = {
            "day": str(budget_raw["day"]),
            # bool 是 int 的子类，要显式排除，否则 true 会被当成 1
            "used": int(used) if isinstance(used, int) and not isinstance(used, bool) else 0,
        }
    return (
        _str_map(data.get("keys")),
        _str_map(data.get("refreshed")),
        budget,
    )


def save_state(
    path: Path,
    keys: dict[str, str],
    refreshed: dict[str, str],
    budget: dict[str, object] | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, object] = {
        "version": STATE_VERSION,
        "policy": CACHE_POLICY,
        "keys": keys,
        "refreshed": refreshed,
    }
    if budget:
        payload["budget"] = budget
    path.write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )


def refresh_url_for(key: str, base: str) -> str:
    """对象 key → 用户实际访问的 URL。

    MkDocs 默认 use_directory_urls：`drun/index.html` 对外暴露的是 `/drun/`，
    用户和站内链接访问的都是目录形式。CDN 缓存键跟着 URL 走，
    刷 `drun/index.html` 不会让 `/drun/` 的旧副本失效 —— 所以只刷目录形式。
    顺带把 URL 数量减半，而配额只有 500 个/天。

    key 里的非 ASCII 字符（中文文件名）与空格按浏览器行为做百分号编码，
    否则接口会判 400031 invalid url。
    """
    if key == "index.html":
        return f"{base}/"
    if key.endswith("/index.html"):
        key = key[: -len("index.html")]
    return f"{base}/{urllib.parse.quote(key, safe='/')}"


def refresh_backlog(
    targets: dict[str, Path],
    applied: dict[str, str],
    refreshed: dict[str, str],
) -> list[str]:
    """还没为「当前内容」刷过 CDN 的 key，按浅层优先排序。

    排序理由：配额有限时先刷首页与一级目录页（访问量最大），
    深层页面排在后面，必要时跨天补齐。站点根首页永远排第一。
    """
    keys = [
        key
        for key in targets
        if applied.get(key) and refreshed.get(key) != applied[key]
    ]
    keys.sort(key=lambda k: (0 if k == "index.html" else 1 + k.count("/"), k))
    return keys


def ci_warning(message: str) -> None:
    """打印告警；在 GitHub Actions 里同时输出注解，确保不会被日志淹没。"""
    print(f"  WARN {message}")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::warning::{message}")


def ci_error(message: str) -> None:
    print(f"  ERROR {message}")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::error::{message}")


def ci_notice(message: str) -> None:
    """提示当前配置现状（不是本次运行的异常），Actions 里用 notice 而非 warning。"""
    print(f"  INFO {message}")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::notice::{message}")


def selftest() -> int:
    """校验签名算法、/batch 请求体、刷新 URL 映射与状态读写，无需网络和凭据。"""
    failures: list[str] = []

    # 1) 管理凭证：官方文档给出的测试向量
    path = "/move/bmV3ZG9jczpmaW5kX21hbi50eHQ=/bmV3ZG9jczpmaW5kLm1hbi50eHQ="
    token = management_token(
        "POST", path, "rs.qiniu.com", "MY_ACCESS_KEY", "MY_SECRET_KEY"
    )
    expected = "MY_ACCESS_KEY:1uLvuZM6l6oCzZFqkJ6oI4oFMVQ="
    if token != expected:
        failures.append(f"管理凭证不符\n    期望: {expected}\n    实际: {token}")

    # 2) QBox 凭证：签名串只有「路径 + 换行」。
    #    这个向量同时是一道回归阀 —— 一旦有人把 Host / Content-Type / body
    #    拼进签名串（即当初那个 401 的写法），这里立刻会挂。
    qbox_expected = "MY_ACCESS_KEY:ckTB2xiIyIHZmi4O4iN3XjXr7t8="
    qbox = qbox_token("/v2/tune/refresh", "MY_ACCESS_KEY", "MY_SECRET_KEY")
    if qbox != qbox_expected:
        failures.append(f"QBox 凭证不符\n    期望: {qbox_expected}\n    实际: {qbox}")

    # 3) 操作指令格式
    op_expected = (
        "/chgm/"
        + urlsafe_base64_encode(b"mybucket:drun/index.html")
        + "/cacheControl/"
        + urlsafe_base64_encode(b"no-cache")
    )
    op = chgm_op("mybucket", "drun/index.html", "no-cache")
    if op != op_expected:
        failures.append(f"chgm op 不符\n    期望: {op_expected}\n    实际: {op}")

    # 4) 请求体构成与往返解码
    body = batch_body("mybucket", ["a.html", "b.html"], "no-cache")
    parts = body.split("&")
    if len(parts) != 2 or not all(p.startswith("op=") for p in parts):
        failures.append(f"batch 请求体结构不符: {body}")
    else:
        for part, key in zip(parts, ["a.html", "b.html"]):
            decoded = urllib.parse.unquote_plus(part[len("op=") :])
            if decoded != chgm_op("mybucket", key, "no-cache"):
                failures.append(f"batch 请求体往返解码不符: {decoded}")

    # 5) 刷新 URL 映射：index 页要落到目录形式
    base = "https://docs.daocloud.io"
    for key, want in [
        ("index.html", "https://docs.daocloud.io/"),
        ("drun/index.html", "https://docs.daocloud.io/drun/"),
        ("en/drun/install/index.html", "https://docs.daocloud.io/en/drun/install/"),
        ("404.html", "https://docs.daocloud.io/404.html"),
        ("search/search_index.json", "https://docs.daocloud.io/search/search_index.json"),
        # 中文/空格路径必须做百分号编码，否则接口判 400031 invalid url
        (
            "docs/中文 页.html",
            "https://docs.daocloud.io/docs/%E4%B8%AD%E6%96%87%20%E9%A1%B5.html",
        ),
    ]:
        got = refresh_url_for(key, base)
        if got != want:
            failures.append(f"刷新 URL 映射不符（{key}）\n    期望: {want}\n    实际: {got}")

    # 6) 状态读写：keys / refreshed / budget 三者必须各自独立往返
    with tempfile.TemporaryDirectory() as tmp:
        state_path = Path(tmp) / "state.json"
        save_state(
            state_path,
            {"a.html": "1:aa"},
            {"a.html": "0:old"},
            {"day": "2026-10-19", "used": 120},
        )
        keys, refreshed, budget = load_state(state_path)
        if keys != {"a.html": "1:aa"}:
            failures.append(f"状态 keys 往返不符: {keys}")
        if refreshed != {"a.html": "0:old"}:
            failures.append(f"状态 refreshed 往返不符: {refreshed}")
        if budget != {"day": "2026-10-19", "used": 120}:
            failures.append(f"状态 budget 往返不符: {budget}")

        # 损坏数据不应让脚本崩，只当没读到
        state_path.write_text('{"policy": "no-cache", "keys": [1, 2]}', "utf-8")
        if load_state(state_path) != ({}, {}, {}):
            failures.append("状态文件损坏时应返回空状态")

        # v2 旧状态没有 budget 字段：必须能读，且预算按 0 起算（不能崩、不能当满额）
        state_path.write_text(
            '{"version": 2, "policy": "no-cache", "keys": {"a.html": "1:aa"}}', "utf-8"
        )
        legacy = load_state(state_path)
        if legacy[2].get("used", 0) != 0:
            failures.append(f"旧状态缺 budget 时应按 0 起算: {legacy[2]}")

    # 7) 每日预算：跨日重置、超限夹到 0、0 表示不限
    for stored, today, limit, want_used, want_left, label in [
        ({"day": "2026-10-19", "used": 150}, "2026-10-19", 200, 150, 50, "同日续算"),
        ({"day": "2026-10-18", "used": 150}, "2026-10-19", 200, 0, 200, "跨日重置"),
        ({"day": "2026-10-19", "used": 250}, "2026-10-19", 200, 250, 0, "已超额夹到 0"),
        ({"day": "2026-10-19", "used": 200}, "2026-10-19", 0, 200, None, "0 表示不限"),
        ({}, "2026-10-19", 200, 0, 200, "空状态"),
        ({"day": "2026-10-19", "used": True}, "2026-10-19", 200, 0, 200, "bool 不算用量"),
    ]:
        fresh, left = resolve_budget(dict(stored), today, limit)
        if fresh["used"] != want_used or left != want_left:
            failures.append(
                f"预算计算不符（{label}）\n"
                f"    期望 used={want_used} left={want_left}\n"
                f"    实际 used={fresh['used']} left={left}"
            )
    if len(today_cst()) != 10 or today_cst()[4] != "-" or today_cst()[7] != "-":
        failures.append(f"today_cst 格式应为 YYYY-MM-DD: {today_cst()}")

    # 8) 没有 Content-Type 时不得把 body 签进管理凭证（对齐官方 SDK）
    with_body = management_token("POST", "/x", RS_HOST, "AK", "SK", None, "BODY")
    without_body = management_token("POST", "/x", RS_HOST, "AK", "SK", None, None)
    if with_body != without_body:
        failures.append("无 Content-Type 时仍把 body 签入了管理凭证")

    if failures:
        print("自检失败：")
        for item in failures:
            print(f"  - {item}")
        return 1
    print(
        "自检通过（管理凭证 / QBox 凭证 / op 构造 / batch 编码 / "
        "刷新 URL / 状态读写 / 每日预算 / 凭证边界）"
    )
    return 0


def parse_args(argv: list[str]) -> tuple[argparse.Namespace, argparse.ArgumentParser]:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("site", nargs="?", help="构建产物目录（如 public）")
    parser.add_argument(
        "--state", default=".qiniu-cache-state.json", metavar="PATH", help="状态文件路径"
    )
    parser.add_argument("--dry-run", action="store_true", help="只打印计划，不发请求")
    parser.add_argument(
        "--refresh", metavar="URL_PREFIX", help="处理后刷新 CDN（如 https://docs.daocloud.io/）"
    )
    parser.add_argument(
        "--max-refresh",
        type=int,
        default=0,
        metavar="N",
        help="每个自然日（北京时间）最多刷新 N 个 URL，跨多次部署累计；"
        "默认 0 = 只受当日剩余配额约束",
    )
    parser.add_argument(
        "--strict", action="store_true", help="任一操作失败即返回非 0"
    )
    parser.add_argument(
        "--selftest", action="store_true", help="校验签名算法后退出"
    )
    return parser.parse_args(argv), parser


def apply_cache_control(
    keys: list[str],
    bucket: str,
    access_key: str,
    secret_key: str,
) -> tuple[set[str], dict[str, str]]:
    """分批下发 cacheControl，返回 (成功集合, 失败字典)。"""
    applied: set[str] = set()
    errors: dict[str, str] = {}
    total = -(-len(keys) // BATCH_MAX)
    for idx, start in enumerate(range(0, len(keys), BATCH_MAX), 1):
        chunk = keys[start : start + BATCH_MAX]
        ok, errs = batch_set_cache_control(
            bucket, chunk, CACHE_POLICY, access_key, secret_key
        )
        applied |= ok
        errors |= errs
        print(f"  批次 {idx}/{total}：{len(ok)}/{len(chunk)} 成功")
    return applied, errors


def run_refresh(
    backlog: list[str],
    applied: dict[str, str],
    refreshed: dict[str, str],
    url_prefix: str,
    access_key: str,
    secret_key: str,
    max_refresh: int,
    budget: dict[str, object],
) -> tuple[bool, str, str]:
    """在当日配额内分批刷新，返回 (是否需要立即失败, 停止原因, 类别)。

    ``max_refresh`` 是**每自然日**上限，不是单次运行上限：配额由同一账号下的
    所有业务共享（本仓、api-docs、download-docs、其他项目都吃这 500 个），
    单看一次运行去限额，一天部署三次就会把当天配额吃光。
    已用量累加进 ``budget["used"]``，由调用方持久化，跨部署续算。

    类别（第三项）供调用方决定「打 INFO 还是打 WARN」：
    - ``""``            正常结束
    - ``"quota"``       当日配额耗尽，次日续跑，属于预期内
    - ``"unsupported"`` 域名未接入七牛 CDN（400032）——刷新对该域名**永久无效**
    - ``"invalid_url"`` 整批 URL 被判无效，多为 --refresh 前缀配错
    - ``"auth"``        凭据无效（QBox 签名错误或密钥过期）
    - ``"error"``       其它错误

    第一个返回值只对「必须马上修」的问题为真（401/403、整批 URL 无效）。

    ``"unsupported"`` 必须与 ``"quota"`` 严格区分：域名直连 Kodo 源站时
    （CNAME 指向 ``iovip*.qiniuio.com``），刷新永远不可能成功，
    此时再报「配额不足、后续部署会继续补齐」是彻头彻尾的误导。
    """
    base = url_prefix.rstrip("/")
    limit = len(backlog)
    if max_refresh > 0:
        left_today = max(0, max_refresh - int(budget.get("used", 0)))
        limit = min(limit, left_today)
    if limit <= 0:
        return False, "", ""

    quota_left = REFRESH_DAILY_FALLBACK
    sent = 0
    while sent < limit and quota_left > 0:
        size = min(REFRESH_BATCH_MAX, limit - sent, quota_left)
        chunk = backlog[sent : sent + size]
        urls = [refresh_url_for(key, base) for key in chunk]
        data = refresh_cdn(urls, access_key, secret_key)
        code = data.get("code")

        if code == 200:
            task_ids = data.get("taskIds") or {}
            accepted = set(task_ids) if isinstance(task_ids, dict) else set()
            invalid = data.get("invalidUrls") or []
            bad = (
                {u for u in invalid if isinstance(u, str)}
                if isinstance(invalid, list)
                else set()
            )
            # 整批都无效 = 前缀配错，重试也不会好，直接失败
            if bad and not accepted and len(bad) >= len(urls):
                return True, (
                    f"{len(bad)} 个 URL 全部被判无效，请检查 --refresh 前缀"
                    f"（例如 {sorted(bad)[0]}）"
                ), "invalid_url"
            for key, url in zip(chunk, urls):
                # 接口没回 taskIds 时按全部受理处理；
                # 被判无效的 URL 也记成已处理，否则每次部署都会占用配额重试
                if not accepted or url in accepted or url in bad:
                    refreshed[key] = applied[key]
            if bad:
                ci_warning(f"{len(bad)} 个 URL 被判无效，已跳过（例如 {sorted(bad)[0]}）")
            surplus = data.get("urlSurplusDay")
            quota_left = (
                surplus
                if isinstance(surplus, int)
                else max(0, quota_left - len(urls))
            )
            sent += len(urls)
            budget["used"] = int(budget.get("used", 0)) + len(urls)
            print(
                f"  CDN 刷新 {len(urls)} 个 URL 已提交"
                f"（当日剩余额度：{quota_left}）"
            )
        elif code == 400037:
            # URL 已在刷新队列中 —— 视为已提交，避免无限重试
            for key in chunk:
                refreshed[key] = applied[key]
            sent += len(urls)
            budget["used"] = int(budget.get("used", 0)) + len(urls)
            quota_left = max(0, quota_left - len(urls))
            print(f"  {len(urls)} 个 URL 已在刷新队列中，跳过")
        elif code in (400033, 400034, 400035, 400038):
            return False, (
                f"刷新配额已用尽或目录刷新未开通（code {code}：{data.get('error')}）"
            ), "quota"
        elif code == 400032:
            # 域名没接 CDN / 前缀写错：重试无用，且对「直连源站」的域名永久无效。
            # 单独归类为 unsupported，避免调用方误报成「配额不足」。
            return False, (
                f"CDN 刷新对该域名无效（code 400032：{data.get('error')}）。"
                f"若 --refresh 的域名尚未接入七牛 CDN（CNAME 指向 iovip*.qiniuio.com "
                f"即为源站直连），刷新永远不会生效；需要 CDN 加速请在七牛控制台"
                f"绑定「自定义 CDN 加速域名」并把 CNAME 改为 *.qiniudns.com。"
                f"在此之前可去掉 --refresh 以省掉这次无效请求"
            ), "unsupported"
        elif code == 400031:
            # URL 被判无效：只把无效的那些记成已处理，
            # 否则同一批坏 URL 会让刷新永远卡在队头
            invalid = data.get("invalidUrls") or []
            bad = (
                {u for u in invalid if isinstance(u, str)}
                if isinstance(invalid, list)
                else set()
            )
            if not bad:
                return False, (
                    f"CDN 刷新失败（code 400031：{data.get('error')}）"
                ), "error"
            if len(bad) >= len(urls):
                return True, (
                    f"{len(bad)} 个 URL 全部被判无效，请检查 --refresh 前缀"
                    f"（例如 {sorted(bad)[0]}）"
                ), "invalid_url"
            for key, url in zip(chunk, urls):
                if url in bad:
                    refreshed[key] = applied[key]
            sent += len(urls)
            # 无效 URL 实际不占配额，但按「已尝试」计入预算更保守，
            # 保证单日占用不会因为反复的重试批次越过上限
            budget["used"] = int(budget.get("used", 0)) + len(urls)
            quota_left = max(0, quota_left - len(urls))
            ci_warning(f"{len(bad)} 个 URL 被判无效，已跳过（例如 {sorted(bad)[0]}）")
            continue
        elif code in (401, 403, 401001, 401002):
            return True, (
                f"CDN 刷新鉴权失败（code {code}：{data.get('error')}）"
            ), "auth"
        else:
            return False, f"CDN 刷新失败（code {code}：{data.get('error')}）", "error"

    # 因配额或 --max-refresh 提前结束时不必再报一次：调用方会用「仍有 N 个待刷新」汇总
    return False, "", ""


def main(argv: list[str] | None = None) -> int:
    args, parser = parse_args(sys.argv[1:] if argv is None else argv)

    if args.selftest:
        return selftest()
    if not args.site:
        parser.print_help()
        return 2

    site = Path(args.site)
    state_path = Path(args.state)

    if args.refresh is not None and not args.refresh.startswith(("http://", "https://")):
        print("ERROR: --refresh 需要完整前缀，例如 https://docs.daocloud.io/")
        return 2
    if not site.is_dir():
        print(f"ERROR: 站点目录不存在：{site}")
        return 1

    targets = collect_targets(site)
    stored_keys, stored_refreshed, budget = load_state(state_path)
    # 丢掉已从站点移除的 key，避免状态文件无限膨胀
    applied = {k: v for k, v in stored_keys.items() if k in targets}
    refreshed = {k: v for k, v in stored_refreshed.items() if k in targets}

    # 跨自然日重置当日刷新预算（北京时间，与七牛配额重置口径一致）。
    # state 丢失/未命中时会从 0 重新计数，所以这只是「本仓自律」的软上限：
    # 真正的硬上限仍是接口返回的 urlSurplusDay 与 400034。
    # CI 的常态是不传 --refresh（域名未接 CDN），此时整个预算机制都不启动。
    today = today_cst()
    budget_left: int | None = None
    if args.refresh:
        budget, budget_left = resolve_budget(budget, today, args.max_refresh)
        if budget_left is not None:
            print(
                f"当日 CDN 刷新预算：已用 {int(budget.get('used', 0))} / "
                f"{args.max_refresh}（{today}），本次可用 {budget_left}"
            )

    pending: dict[str, str] = {}
    for key, path in targets.items():
        current = fingerprint(path)
        if applied.get(key) != current:
            pending[key] = current

    print(f"待修正 Cache-Control 的文件：{len(pending)} / {len(targets)}（其余已处理过）")

    access_key = os.environ.get("QINIU_ACCESS_KEY", "")
    secret_key = os.environ.get("QINIU_SECRET_KEY", "")
    bucket = os.environ.get("QINIU_BUCKET", "")
    has_creds = bool(access_key and secret_key and bucket)

    if not args.dry_run and not has_creds and (pending or args.refresh):
        print("ERROR: 需要设置 QINIU_ACCESS_KEY / QINIU_SECRET_KEY / QINIU_BUCKET")
        return 1

    # ---- 阶段一：设置 cacheControl ----
    if pending:
        if args.dry_run:
            for key in sorted(pending)[:5]:
                op = chgm_op(bucket or "<bucket>", key, CACHE_POLICY)
                print(f"  [dry-run] /batch op={op}")
            if len(pending) > 5:
                print(f"  [dry-run] …… 其余 {len(pending) - 5} 个同上")
            print(
                f"  [dry-run] 共 {len(pending)} 个操作，"
                f"拆成 {-(-len(pending) // BATCH_MAX)} 次 /batch 请求"
            )
        else:
            ok, errors = apply_cache_control(
                sorted(pending), bucket, access_key, secret_key
            )
            for key in ok:
                applied[key] = pending[key]
            # 只把成功的写进状态：失败的 key 没落盘，下次部署会自动重试
            # 不跑 CDN 刷新时（CI 的常态）不写 budget，避免状态文件里留无意义的记录
            save_state(state_path, applied, refreshed, budget if args.refresh else None)

            if errors:
                ci_warning(f"{len(errors)} 个对象设置 Cache-Control 失败，下次部署自动重试")
                for key, message in sorted(errors.items())[:5]:
                    print(f"    {key}: {message}")
                if not ok:
                    ci_error("全部操作失败，请检查凭据与空间配置")
                    return 1
                if args.strict:
                    return 1

    # ---- 阶段二：CDN 刷新（即使本次没有改动也要跑，否则欠账永远补不上）----
    if args.refresh:
        planned = dict(applied)
        if args.dry_run:
            # dry-run 不会真的改元数据，但计划里要按「本次全部成功」推算待刷量
            planned.update(pending)
        backlog = refresh_backlog(targets, planned, refreshed)
        todo = len(backlog) if budget_left is None else min(len(backlog), budget_left)
        if not backlog:
            print("  CDN 刷新：无待刷新 URL（均已是当前内容）")
        elif budget_left == 0:
            # 本仓每日自律预算已用完：不再发请求，把配额让给同账号下的其他业务。
            # 这与「账号配额耗尽」不是一回事，所以用 notice 而不是 WARN。
            ci_notice(
                f"当日刷新预算 {args.max_refresh} 个已用完（{today}），"
                f"仍有 {len(backlog)} 个 URL 待刷新，明日部署继续"
            )
        elif args.dry_run:
            example = refresh_url_for(backlog[0], args.refresh.rstrip("/"))
            # 只有真发一次请求才知道当日剩余额度，这里按官方默认配额估个上界
            today_quota = min(todo, REFRESH_DAILY_FALLBACK)
            print(
                f"  [dry-run] CDN 待刷新 {len(backlog)} 个 URL；本次预计提交 {today_quota} 个"
                f"（{REFRESH_BATCH_MAX}/批，约 {-(-today_quota // REFRESH_BATCH_MAX)} 次请求），"
                f"例如 {example}"
            )
            if len(backlog) > today_quota:
                days = -(-(len(backlog) - today_quota) // REFRESH_DAILY_FALLBACK)
                print(
                    f"  [dry-run] 其余 {len(backlog) - today_quota} 个受每日配额约束，"
                    f"由后续部署继续补齐（约 {days} 天）"
                )
        else:
            fatal, reason, kind = run_refresh(
                backlog,
                applied,
                refreshed,
                args.refresh,
                access_key,
                secret_key,
                args.max_refresh,
                budget,
            )
            save_state(state_path, applied, refreshed, budget)
            if reason and fatal:
                ci_error(reason)
                return 1
            if kind == "unsupported":
                # 域名未接入七牛 CDN：对该域名刷新永久无效，不是「欠账」。
                # 所以既不报「配额不足、后续会补齐」（那是假的），也不用 WARN
                # （每次部署都刷一条黄字，会训练大家忽略告警）。
                ci_notice(reason)
                if args.strict:
                    return 1
            else:
                left = len(refresh_backlog(targets, applied, refreshed))
                if left:
                    if args.max_refresh > 0:
                        ci_warning(
                            f"仍有 {left} 个 URL 待刷新（本仓每日上限 "
                            f"{args.max_refresh} 个；账号总额度 "
                            f"{REFRESH_DAILY_FALLBACK} 个/天需与同账号其他业务共享），"
                            f"后续部署会继续补齐"
                        )
                    else:
                        ci_warning(
                            f"仍有 {left} 个 URL 待刷新（配额 {REFRESH_DAILY_FALLBACK} 个/天），"
                            f"后续部署会继续补齐；如需一次性刷完，可在控制台申请提升配额"
                        )
                if reason:
                    ci_warning(reason)
                    if args.strict:
                        return 1

    print("完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
