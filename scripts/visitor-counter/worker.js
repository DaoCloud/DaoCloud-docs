/**
 * docs-counter — DaoCloud 文档站访问计数 Worker
 *
 * 端点：
 *   POST /hit    页面 beacon。Body: {"c": "<client uuid>", "p": "<path>"}
 *                返回 {"pv": <累计>, "uv": <累计>}；Origin 不在白名单 → 403
 *                UA 原样入库（截断 120 字符），不做过滤——展示口径保持全量
 *   GET  /stats  回写用。Header: X-Stats-Token: <STATS_TOKEN secret>
 *                返回 {"pv", "uv", "updated", "daily": {...}, "bots": {...}, "ua_top": [...]}
 *                bots/ua_top 为审计口径：展示数字不过滤 UA，爬虫占比看这里
 *   scheduled    每天 03:00 UTC 清理 180 天前明细（PV/UV 累计在 counter 表，不受影响）
 *
 * 口径（2026-11-26 与维护者定稿）：
 *   PV = 传统口径，每次 /hit 成功写入 +1（同一人同天同页重复访问也计）
 *   UV = 按 client uuid 全时间窗去重，写入时固化进 counter.uv（明细清理后数字不缩水）
 *   限流 = 同 client 60 秒内 >30 次：返回当前数字但不写库（isolate 内存窗口，够用）
 */

const ALLOWED_ORIGINS = [
  'https://docs.daocloud.io',
  'https://deploy-preview-7867--daocloud.netlify.app',
];
// preview 域名按需追加；也可放宽为 /--daocloud\.netlify\.app$/ 模式
const PREVIEW_RE = /^https:\/\/deploy-preview-\d+--daocloud\.netlify\.app$/;

const RATE_LIMIT = 30;        // 次 / 窗口
const RATE_WINDOW_MS = 60_000;
const DETAIL_RETENTION_DAYS = 180;
const DAILY_DAYS = 14;        // /stats 返回的日增量天数
const UA_TOP = 8;             // /stats 返回的 top UA 条数

/** 爬虫 UA 识别：SQL（LIKE）与 JS（RE）两份同源，改一处必须同步另一处 */
const BOT_SQL =
  "ua LIKE '%bot%' OR ua LIKE '%crawl%' OR ua LIKE '%spider%' OR ua LIKE '%slurp%'" +
  " OR ua LIKE '%HeadlessChrome%' OR ua LIKE '%python-requests%' OR ua LIKE '%python-urllib%'" +
  " OR ua LIKE '%curl%' OR ua LIKE '%wget%' OR ua LIKE '%Go-http-client%' OR ua LIKE '%Java/%'" +
  " OR ua LIKE '%okhttp%' OR ua LIKE '%axios%' OR ua LIKE '%monitor%' OR ua LIKE '%uptime%'" +
  " OR ua LIKE '%pingdom%' OR ua LIKE '%lighthouse%' OR ua LIKE '%phantomjs%'" +
  " OR ua LIKE '%puppeteer%' OR ua LIKE '%playwright%'";
const BOT_RE =
  /bot|crawl|spider|slurp|headlesschrome|python-requests|python-urllib|curl|wget|go-http-client|java\/|okhttp|axios|monitor|uptime|pingdom|lighthouse|phantomjs|puppeteer|playwright/i;

/** isolate 内存限流窗口：client -> [timestamps] */
const rate = new Map();

const corsHeaders = (origin) => ({
  'Access-Control-Allow-Origin': origin,
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
});

const json = (data, status = 200, origin = ALLOWED_ORIGINS[0]) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {'Content-Type': 'application/json', ...corsHeaders(origin)},
  });

function checkOrigin(request) {
  const origin = request.headers.get('Origin') || '';
  return ALLOWED_ORIGINS.includes(origin) || PREVIEW_RE.test(origin) ? origin : null;
}

/** 简单滑动窗口限流（单 isolate 近似；多 isolate 下放宽为 N 倍，可接受） */
function rateLimited(client) {
  const now = Date.now();
  const arr = (rate.get(client) || []).filter((t) => now - t < RATE_WINDOW_MS);
  if (arr.length >= RATE_LIMIT) {
    arr.push(now);
    rate.set(client, arr);
    return true;
  }
  arr.push(now);
  rate.set(client, arr);
  return false;
}

/** 清洗与校验 beacon 参数；非法返回 null */
function parseHit(body) {
  if (!body || typeof body !== 'object') return null;
  const c = typeof body.c === 'string' ? body.c : '';
  const p = typeof body.p === 'string' ? body.p : '';
  if (!/^[A-Za-z0-9-]{8,64}$/.test(c)) return null;
  if (!p.startsWith('/') || p.length > 200) return null;
  const path = p.split('#')[0].split('?')[0].slice(0, 200);
  return {client: c, path};
}

async function readCounter(DB) {
  const row = await DB.prepare('SELECT pv, uv FROM counter WHERE rowid = 1').first();
  return {pv: row?.pv ?? 0, uv: row?.uv ?? 0};
}

async function handleHit(request, env) {
  const origin = checkOrigin(request);
  if (!origin) return json({error: 'forbidden'}, 403, ALLOWED_ORIGINS[0]);
  if (request.method === 'OPTIONS') return new Response(null, {status: 204, headers: corsHeaders(origin)});

  let body;
  try {
    body = await request.json();
  } catch {
    return json({error: 'bad request'}, 400, origin);
  }
  const hit = parseHit(body);
  if (!hit) return json({error: 'bad request'}, 400, origin);

  const current = await readCounter(env.DB);
  if (rateLimited(hit.client)) return json(current, 200, origin);   // 超限：返回数字但不写库

  // UV 写入时固化：该 client 历史首次出现才 uv+1（明细后续被清理也不影响）
  const seen = await env.DB.prepare('SELECT 1 FROM hits WHERE client = ? LIMIT 1')
    .bind(hit.client)
    .first();

  const stmts = [
    env.DB.prepare('INSERT INTO hits (ts, client, path, ua) VALUES (?, ?, ?, ?)')
      .bind(Date.now(), hit.client, hit.path,
            (request.headers.get('User-Agent') || '').slice(0, 120)),
    env.DB.prepare('UPDATE counter SET pv = pv + 1 WHERE rowid = 1'),
  ];
  if (!seen) {
    stmts.push(env.DB.prepare('UPDATE counter SET uv = uv + 1 WHERE rowid = 1'));
  }
  await env.DB.batch(stmts);   // D1 batch = 事务

  return json({pv: current.pv + 1, uv: current.uv + (seen ? 0 : 1)}, 200, origin);
}

async function handleStats(request, env) {
  const token = request.headers.get('X-Stats-Token') || '';
  if (token !== env.STATS_TOKEN) return json({error: 'unauthorized'}, 401);
  const {pv, uv} = await readCounter(env.DB);
  const since = Date.now() - DAILY_DAYS * 86_400_000;
  const {results} = await env.DB.prepare(
    "SELECT strftime('%Y-%m-%d', ts / 1000, 'unixepoch') AS day, COUNT(*) AS pv, COUNT(DISTINCT client) AS uv, " +
    `SUM(CASE WHEN ${BOT_SQL} THEN 1 ELSE 0 END) AS bot ` +
    'FROM hits WHERE ts >= ? GROUP BY day ORDER BY day'
  )
    .bind(since)
    .all();
  const daily = {};
  for (const r of results) daily[r.day] = {pv: r.pv, uv: r.uv, bot: r.bot || 0};
  // 审计口径：爬虫累计（部署 ua 列之前的历史行 ua 为空串，计入非爬虫）
  const botsRow = await env.DB.prepare(
    `SELECT SUM(CASE WHEN ${BOT_SQL} THEN 1 ELSE 0 END) AS pv, ` +
    `COUNT(DISTINCT CASE WHEN ${BOT_SQL} THEN client END) AS uv FROM hits`
  ).first();
  const {results: uaRows} = await env.DB.prepare(
    'SELECT ua, COUNT(*) AS n FROM hits GROUP BY ua ORDER BY n DESC LIMIT ?'
  )
    .bind(UA_TOP)
    .all();
  const ua_top = uaRows
    .filter((r) => r.ua)
    .map((r) => ({ua: r.ua.slice(0, 80), n: r.n, bot: BOT_RE.test(r.ua)}));
  return json({
    pv, uv,
    updated: new Date().toISOString(),
    daily,
    bots: {pv: botsRow?.pv || 0, uv: botsRow?.uv || 0},
    ua_top,
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/hit') return handleHit(request, env);
    if (url.pathname === '/stats') return handleStats(request, env);
    return json({error: 'not found'}, 404);
  },

  async scheduled(event, env, ctx) {
    // 每天 03:00 UTC（wrangler.toml cron）：清理 180 天前明细。
    // 累计 PV/UV 在 counter 表写入时已固化，清理不影响数字。
    const cutoff = Date.now() - DETAIL_RETENTION_DAYS * 86_400_000;
    await env.DB.prepare('DELETE FROM hits WHERE ts < ?').bind(cutoff).run();
  },
};
