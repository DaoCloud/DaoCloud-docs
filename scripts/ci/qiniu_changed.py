#!/usr/bin/env python3
"""按内容指纹比对，挑出本次构建中真正变化的产物，供增量上传使用。

用法：
    python scripts/ci/qiniu_changed.py <site_dir> <manifest.json> <staging_dir>

原理：
    1. 对 <site_dir> 下每个文件算 blake2b 内容指纹，得到 {相对路径: "size:hash"}；
    2. 与上一次的 <manifest.json> 比对（不存在则视为全部新增）；
    3. 把「新增或内容变化」的文件**硬链接**到 <staging_dir>，保持相对路径不变；
    4. 写出新的 manifest，供下一次比对。

为什么用硬链接：不复制字节、不占额外磁盘，上传工具读到的内容与 public/ 完全一致。
为什么用内容指纹而不是 mtime：mkdocs 每次构建都会重写全部文件，mtime 必然变化、毫无区分度。

退出码：0 = 成功（无论有没有变化）；非 0 = 出错。
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

CHUNK = 1 << 20  # 1 MiB


def fingerprint(path: Path) -> str:
    h = hashlib.blake2b(digest_size=16)
    size = 0
    with path.open("rb") as fh:
        while True:
            block = fh.read(CHUNK)
            if not block:
                break
            size += len(block)
            h.update(block)
    return f"{size}:{h.hexdigest()}"


def build_manifest(site: Path) -> dict[str, str]:
    manifest: dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(site):
        dirnames.sort()
        for name in sorted(filenames):
            full = Path(dirpath) / name
            if not full.is_file():  # 跳过悬空符号链接等
                continue
            rel = full.relative_to(site).as_posix()
            manifest[rel] = fingerprint(full)
    return manifest


def link_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2

    site = Path(sys.argv[1]).resolve()
    manifest_path = Path(sys.argv[2]).resolve()
    staging = Path(sys.argv[3]).resolve()

    if not site.is_dir():
        print(f"ERROR: site dir not found: {site}")
        return 1

    new_manifest = build_manifest(site)

    old_manifest: dict[str, str] = {}
    if manifest_path.is_file():
        try:
            old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"WARN: manifest unreadable ({exc}); 视为首次全量上传")
            old_manifest = {}

    changed = [rel for rel, sig in new_manifest.items() if old_manifest.get(rel) != sig]
    removed = [rel for rel in old_manifest if rel not in new_manifest]

    # 重建 staging 目录（每次都是全量重建，避免残留）
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)

    for rel in sorted(changed):
        link_or_copy(site / rel, staging / rel)

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(new_manifest, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )

    print("增量上传清单：")
    print(f"  site 文件总数 : {len(new_manifest)}")
    print(f"  本次需上传   : {len(changed)}")
    print(f"  未变已跳过   : {len(new_manifest) - len(changed)}")
    if removed:
        print(f"  远端已失效   : {len(removed)}（本工具不删除远端对象，仅提示）")
    if old_manifest:
        saved = 100.0 * (1 - len(changed) / max(len(new_manifest), 1))
        print(f"  节省上传量   : {saved:.1f}%")
    else:
        print("  首次运行（无历史清单）→ 全量上传")

    if changed:
        print("  变化样例     : " + ", ".join(changed[:5]) + (" ..." if len(changed) > 5 else ""))

    # 供 GitHub Actions 使用
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as fh:
            fh.write(f"changed={len(changed)}\n")
            fh.write(f"total={len(new_manifest)}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
