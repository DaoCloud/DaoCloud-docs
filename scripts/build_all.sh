#!/usr/bin/env bash
# 并行构建中英双语站点，输出仍是 public/ 与 public/en/，与原先顺序执行的结果一致。
#
# 为什么能并行：mkdocs 单进程只用一个核，而 GitHub 公共仓库的标准 runner 是 4 vCPU，
# 顺序跑 zh + en 时大部分核心闲置。两个进程并行后，墙钟时间 ≈ max(zh, en) 而非 zh + en。
#
# 为什么两边都用 --dirty：mkdocs 默认会在构建前清空自己的 site_dir，
# 而 en 的 site_dir（public/en/）位于 zh 的 site_dir（public/）内部 ——
# 并行时 zh 的清空动作会把 en 已经写好的产物删掉。改用 --dirty 后不再清空，
# 改由本脚本在开头显式 `rm -rf public` 保证「干净构建」的语义不变（CI 是全新工作区，本地也能得到干净结果）。
#
# 用法：
#   bash scripts/build_all.sh [build|build-path]
# 环境变量：
#   MKDOCS="uv run mkdocs"   覆盖 mkdocs 调用方式
#   SERIAL_BUILD=1           强制串行（排查问题时用）
#   WORK_DIR=<dir>           日志目录，默认 mktemp -d
set -uo pipefail

FLAVOR="${1:-build}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT" || exit 1

case "$FLAVOR" in
  build)
    ZH_CFG="docs/zh/mkdocs.yml"
    EN_CFG="docs/en/mkdocs.yml"
    ;;
  build-path)
    ZH_CFG="docs/zh/mkdocs.path.yaml"
    EN_CFG="docs/en/mkdocs.path.yaml"
    ;;
  *)
    echo "用法: bash scripts/build_all.sh [build|build-path]" >&2
    exit 2
    ;;
esac

for cfg in "$ZH_CFG" "$EN_CFG"; do
  if [ ! -f "$cfg" ]; then
    echo "ERROR: 找不到配置文件 $cfg" >&2
    exit 2
  fi
done

MKDOCS="${MKDOCS:-uv run mkdocs}"
WORK_DIR="${WORK_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/docs-build.XXXXXX")}"
mkdir -p "$WORK_DIR"

echo "并行构建：zh → public/   en → public/en/"
echo "  配置文件 : $ZH_CFG | $EN_CFG"
echo "  日志目录 : $WORK_DIR"
echo "  mkdocs   : $MKDOCS"

# 与 mkdocs 默认的「构建前清空 site_dir」等价，且不会误删 en 的产物
rm -rf public

build_one() {
  local name="$1" cfg="$2" out="$3" log="$4"
  local start end rc
  start=$(date +%s)
  # shellcheck disable=SC2086
  $MKDOCS build --dirty -f "$cfg" -d "$out" > "$log" 2>&1
  rc=$?
  end=$(date +%s)
  echo "$((end - start))" > "${log}.secs"
  echo "$rc" > "${log}.rc"
}

if [ "${SERIAL_BUILD:-0}" = "1" ]; then
  echo "  （SERIAL_BUILD=1，串行执行）"
  build_one zh "$ZH_CFG" "../../public/"        "$WORK_DIR/zh.log"
  build_one en "$EN_CFG" "../../public/en/"     "$WORK_DIR/en.log"
else
  build_one zh "$ZH_CFG" "../../public/"        "$WORK_DIR/zh.log" &
  ZH_PID=$!
  build_one en "$EN_CFG" "../../public/en/"     "$WORK_DIR/en.log" &
  EN_PID=$!
  wait "$ZH_PID"
  wait "$EN_PID"
fi

FAILED=0
for name in zh en; do
  rc="$(cat "$WORK_DIR/$name.log.rc" 2>/dev/null || echo 1)"
  secs="$(cat "$WORK_DIR/$name.log.secs" 2>/dev/null || echo '?')"
  warn="$(grep -c '^WARNING' "$WORK_DIR/$name.log" 2>/dev/null)"
  printf '  %-3s exit=%-3s %5ss  WARNING=%s\n' "$name" "$rc" "$secs" "$warn"
  [ "$rc" != "0" ] && FAILED=1
done

if [ "$FAILED" != "0" ]; then
  echo
  echo "==================== 构建失败，以下是日志尾部 ===================="
  for name in zh en; do
    rc="$(cat "$WORK_DIR/$name.log.rc" 2>/dev/null || echo 1)"
    [ "$rc" = "0" ] && continue
    echo "-------------------- $name ($name.log) --------------------"
    tail -n 60 "$WORK_DIR/$name.log"
  done
  echo "================================================================="
  echo "完整日志保留在：$WORK_DIR"
  exit 1
fi

for dir in public public/en; do
  if [ ! -d "$dir" ]; then
    echo "ERROR: 期望的产物目录不存在：$dir" >&2
    exit 1
  fi
done

echo "OK 双语文档构建完成（日志：$WORK_DIR）"
