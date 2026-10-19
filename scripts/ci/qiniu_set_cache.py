#!/usr/bin/env python3
"""修正已上传到七牛 Kodo 的 HTML / 搜索索引的 Cache-Control。

为什么需要这一步：
    七牛 Kodo 对没有设置元数据的对象，一律输出
    `Cache-Control: public, max-age=31536000`（1 年）。
    站点资源分两类，长缓存只对其中一类成立：
      - 静态资源（/assets/**）文件名带内容哈希，URL 变了才会失效 → 1 年没问题；
      - HTML 与 /search/search_index.json 每次构建都变，URL 却不变
        → 浏览器会一直复用旧副本，用户必须强制刷新才能看到新内容。
    对象自身的元数据优先于空间默认值，所以只要给这些文件补上
    `cacheControl`，即可在不改动上传流程的前提下修正缓存行为。

做法：
    不改动上传流程，只在上传完成后调用七牛的「资源元信息修改」接口
    （POST /chgm）写入 cacheControl。为避免每次部署都重刷上万次接口，
    脚本把「已处理过的内容指纹」记在状态文件里，只处理新增或内容变化的文件：
    首次运行等于全量兜底（把历史遗留的 HTML 一并修正），之后即为增量。

用法：
    python3 scripts/ci/qiniu_set_cache.py <site_dir> [选项]

选项：
    --state PATH           状态文件路径（默认 .qiniu-cache-state.json）
    --dry-run              只打印将要执行的操作，不发任何请求
    --refresh URL_PREFIX   处理完后调用 CDN 刷新接口，逐条刷新被修改的 URL
    --selftest             用官方文档给出的测试向量校验签名算法，然后退出

环境变量：
    QINIU_ACCESS_KEY / QINIU_SECRET_KEY / QINIU_BUCKET
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# 七牛资源管理接口（rs）与 CDN 接口（fusion）
RS_HOST = "rs.qiniuapi.com"
FUSION_HOST = "fusion.qiniuapi.com"

# 只对「每次构建都变、URL 却不变」的产物关闭缓存。
# 其余资源保持七牛默认的长缓存：/assets/** 文件名含内容哈希，安全。
CACHE_POLICY = "no-cache"
NO_CACHE_FILES = {"search_index.json"}
NO_CACHE_SUFFIXES = {".html"}

CHUNK = 1 << 20  # 1 MiB
MAX_WORKERS = 32
# 七牛的 CDN 刷新有配额限制，超出就放弃刷新（只影响 CDN 边缘节点，不影响对象元数据本身）
MAX_REFRESH = 1000


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
    """生成七牛管理凭证。

    待签名字符串的拼装规则见
    https://developer.qiniu.com/kodo/manual/1201/access-token
    """
    signing_str = f"{method} {path}\nHost: {host}\n"
    if content_type:
        signing_str += f"Content-Type: {content_type}\n"
    signing_str += "\n"
    if body and content_type != "application/octet-stream":
        signing_str += body

    sign = hmac.new(
        secret_key.encode("utf-8"), signing_str.encode("utf-8"), hashlib.sha1
    ).digest()
    return f"{access_key}:{urlsafe_base64_encode(sign)}"


def encoded_entry_uri(bucket: str, key: str) -> str:
    """EncodedEntryURI = urlsafe_base64("<bucket>:<key>")。"""
    return urlsafe_base64_encode(f"{bucket}:{key}".encode("utf-8"))


def set_cache_control(
    bucket: str,
    key: str,
    cache_control: str,
    access_key: str,
    secret_key: str,
    dry_run: bool = False,
) -> bool:
    """调用 /chgm 修改单个对象的 Cache-Control。"""
    path = (
        f"/chgm/{encoded_entry_uri(bucket, key)}"
        f"/cacheControl/{urlsafe_base64_encode(cache_control.encode('utf-8'))}"
    )
    content_type = "application/x-www-form-urlencoded"

    if dry_run:
        return True

    token = management_token(
        "POST", path, RS_HOST, access_key, secret_key, content_type
    )
    req = urllib.request.Request(
        f"https://{RS_HOST}{path}",
        data=b"",
        method="POST",
        headers={
            "Authorization": f"Qiniu {token}",
            "Content-Type": content_type,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return 200 <= resp.status < 300
    except urllib.error.HTTPError as exc:
        print(f"  ERROR {key}: HTTP {exc.code} {exc.read().decode(errors='replace')}")
    except urllib.error.URLError as exc:
        print(f"  ERROR {key}: {exc.reason}")
    return False


def refresh_cdn(urls: list[str], access_key: str, secret_key: str) -> bool:
    """调用 CDN 刷新接口，让 CDN 节点回源拉取最新文件。

    注意：只有接入七牛 CDN 的域名才有缓存可刷。若域名直连 Kodo 源站，
    该接口会报错——调用方应容忍失败，不影响部署结果。
    """
    if not urls:
        return True

    path = "/v2/tune/refresh"
    content_type = "application/json"
    body = json.dumps({"urls": urls}, ensure_ascii=False)

    token = management_token(
        "POST", path, FUSION_HOST, access_key, secret_key, content_type, body
    )
    req = urllib.request.Request(
        f"https://{FUSION_HOST}{path}",
        data=body.encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Qiniu {token}",
            "Content-Type": content_type,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  CDN 刷新已提交：{len(urls)} 个 URL（HTTP {resp.status}）")
            return True
    except urllib.error.HTTPError as exc:
        print(f"  WARN CDN 刷新失败：HTTP {exc.code} {exc.read().decode(errors='replace')}")
    except urllib.error.URLError as exc:
        print(f"  WARN CDN 刷新失败：{exc.reason}")
    return False


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


def load_state(path: Path) -> dict[str, str]:
    """读取状态：{相对 key: 内容指纹}。

    策略变更（例如以后改成 no-store）时旧记录全部失效，触发一次全量重设。
    """
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"WARN: 状态文件不可读（{exc}）；本次按全量处理")
        return {}
    if data.get("policy") != CACHE_POLICY:
        return {}
    return data.get("keys", {})


def save_state(path: Path, keys: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {"policy": CACHE_POLICY, "keys": keys},
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )


def refresh_urls(url_prefix: str, keys: list[str]) -> list[str]:
    """把对象 key 转成 CDN 刷新用的 URL。

    index.html 需额外刷新其目录形式（/drun/index.html 同时刷 /drun/），
    因为用户访问的是目录 URL，Kodo 的索引文档机制才会命中该对象——
    只刷带 index.html 的 URL 不会让目录 URL 的缓存失效。
    """
    base = url_prefix.rstrip("/")
    urls: list[str] = []
    for key in keys:
        urls.append(f"{base}/{key}")
        if key == "index.html":
            urls.append(f"{base}/")
        elif key.endswith("/index.html"):
            urls.append(f"{base}/{key[: -len('index.html')]}")
    return urls


def selftest() -> int:
    """用官方文档的测试向量校验签名算法，无需网络和凭据。"""
    path = "/move/bmV3ZG9jczpmaW5kX21hbi50eHQ=/bmV3ZG9jczpmaW5kLm1hbi50eHQ="
    token = management_token(
        "POST", path, "rs.qiniu.com", "MY_ACCESS_KEY", "MY_SECRET_KEY"
    )
    expected = "MY_ACCESS_KEY:1uLvuZM6l6oCzZFqkJ6oI4oFMVQ="
    if token == expected:
        print("签名自检通过")
        return 0
    print(f"签名自检失败\n  期望: {expected}\n  实际: {token}")
    return 1


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()

    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2

    site = Path(args[0])
    dry_run = "--dry-run" in args

    state_path = Path(".qiniu-cache-state.json")
    if "--state" in args:
        idx = args.index("--state")
        if idx + 1 >= len(args):
            print("--state 需要跟文件路径")
            return 2
        state_path = Path(args[idx + 1])

    url_prefix = None
    if "--refresh" in args:
        idx = args.index("--refresh")
        if idx + 1 >= len(args):
            print("--refresh 需要跟 URL 前缀，例如 https://docs.daocloud.io/")
            return 2
        url_prefix = args[idx + 1]

    if not site.is_dir():
        print(f"ERROR: 站点目录不存在：{site}")
        return 1

    targets = collect_targets(site)
    state = load_state(state_path)
    pending = {
        key: path
        for key, path in targets.items()
        if state.get(key) != fingerprint(path)
    }

    print(f"待修正 Cache-Control 的文件：{len(pending)} / {len(targets)}（其余已处理过）")
    if not pending:
        return 0

    access_key = os.environ.get("QINIU_ACCESS_KEY", "")
    secret_key = os.environ.get("QINIU_SECRET_KEY", "")
    bucket = os.environ.get("QINIU_BUCKET", "")

    if not dry_run and not (access_key and secret_key and bucket):
        print("ERROR: 需要设置 QINIU_ACCESS_KEY / QINIU_SECRET_KEY / QINIU_BUCKET")
        return 1

    if dry_run:
        for key in sorted(pending)[:5]:
            print(f"  [dry-run] POST https://{RS_HOST}/chgm/<bucket>:{key} -> {CACHE_POLICY}")
        if len(pending) > 5:
            print(f"  [dry-run] …… 其余 {len(pending) - 5} 个同上")
    else:
        def apply(item: tuple[str, Path]) -> tuple[str, str, bool]:
            key, path = item
            ok = set_cache_control(
                bucket, key, CACHE_POLICY, access_key, secret_key, dry_run=False
            )
            return key, fingerprint(path), ok

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            results = list(pool.map(apply, sorted(pending.items())))

        failed = 0
        for key, fp, ok in results:
            if ok:
                state[key] = fp
            else:
                failed += 1
        save_state(state_path, state)
        print(f"  OK 已修正 {len(results) - failed} 个（失败 {failed} 个）")

        if failed:
            print("完成，但有失败项")
            return 1

    if url_prefix:
        keys = sorted(pending)
        if len(keys) > MAX_REFRESH:
            print(f"  WARN 待刷新 URL 过多（{len(keys)} > {MAX_REFRESH}），跳过 CDN 刷新")
        else:
            urls = refresh_urls(url_prefix, keys)
            if dry_run:
                print(f"  [dry-run] CDN 刷新 {len(urls)} 个 URL，例如 {urls[0]}")
            else:
                refresh_cdn(urls, access_key, secret_key)

    print("完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
