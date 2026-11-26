# visitor-counter 部署说明

DaoCloud 文档站 footer 访问计数器（Cloudflare Worker + D1）。

## 口径（2026-11-26 定稿）

- **PV**：传统口径，每次 `/hit` 成功写入 +1（同页刷新也计）
- **UV**：按浏览器 localStorage 匿名 UUID 全时间窗去重，写入时固化（明细清理后数字不缩水）
- **限流**：同 client 60 秒 >30 次 → 返回当前数字但不写库
- **明细保留**：180 天（cron 每天 03:00 UTC 清理；累计值在 counter 表不受影响）

## 部署步骤

1. Cloudflare 控制台建 D1 库 `docs-counter`，执行：

   ```sql
   CREATE TABLE hits (ts INTEGER NOT NULL, client TEXT NOT NULL, path TEXT NOT NULL);
   CREATE INDEX idx_client ON hits (client);
   CREATE TABLE counter (pv INTEGER DEFAULT 0, uv INTEGER DEFAULT 0);
   INSERT INTO counter (pv, uv) VALUES (0, 0);
   ```

2. 本目录下执行：

   ```bash
   wrangler login
   wrangler d1 create docs-counter        # database_id 填进 wrangler.toml
   wrangler secret put STATS_TOKEN        # 自定长随机串，GitHub 侧同名 secret 用
   wrangler deploy                        # 输出 workers.dev 端点
   ```

3. 回填三处占位符 `<SUBDOMAIN>`（全局搜 `<SUBDOMAIN>`）：
   - `docs/{zh,en}/theme/overrides/assets/javascripts/visitor.js` 的 `ENDPOINT`
   - `.github/workflows/stats.yml` 的 `ENDPOINT` 环境变量

4. GitHub repo：Settings → Secrets → Actions → 新建两个 secret：
   - `COUNTER_TOKEN`（值 = STATS_TOKEN，访问 Worker /stats 接口）
   - `STATS_PAT`（管理员的 fine-grained PAT，仅本仓 + Contents 读写；main 有分支保护，
     内置 github-actions[bot] 加不进绕过名单，workflow 用该 PAT checkout/push 绕过）

5. 控制台确认 Worker 的 Cron Trigger：`0 3 * * *`（wrangler.toml 已声明，deploy 自动创建）。

## 验证

```bash
curl -X POST https://<端点>/hit -H "Origin: https://docs.daocloud.io" \
  -H "Content-Type: application/json" -d '{"c":"test-uuid-1","p":"/"}'
# 期望 {"pv":1,"uv":1}；同 client 再打 pv=2 uv 仍=1；无 Origin → 403；/stats 无 token → 401
```

## 文件清单

| 文件 | 作用 |
|---|---|
| `worker.js` | `/hit` 计数 + `/stats` 回写接口 + cron 清理 |
| `wrangler.toml` | D1 绑定 + cron |
| `.github/workflows/stats.yml` | 每 6h 拉 `/stats` → 写 `docs/zh/docs/stats.json`（构建后为站点根 `/stats.json`，visitor.js 兜底读取，en 站同样读这份），无变化不 commit |
| `docs/{zh,en}/theme/overrides/assets/javascripts/visitor.js` | footer 脚本：先读 `/stats.json` 兜底，再 `/hit` 回填实时值 |
| `docs/{zh,en}/theme/partials/copyright.html` | footer 加 `visit-counter` span + script 引用 |
| `docs/{zh,en}/docs/stylesheets/custom.css` | `.visit-counter` 样式 |

## 注意

- `*.workers.dev` 在中国大陆可达性不稳定，上线前先国内实测；不可达则把端点平移到国内 serverless（逻辑不变）
- stats.json 公开可读，只存聚合数，不放明细
