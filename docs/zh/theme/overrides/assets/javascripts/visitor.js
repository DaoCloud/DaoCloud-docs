/**
 * visitor.js — footer 访问计数器（中英两份 theme 共用同一份内容）
 * 端点部署后把 ENDPOINT 换成实际 workers.dev 地址。
 * 失败全部静默：计数器不工作不影响页面任何功能。
 */
(function () {
  'use strict';
  var ENDPOINT = 'https://docs-counter.daocloud.workers.dev';

  var pvEl = document.getElementById('visit-pv');
  var uvEl = document.getElementById('visit-uv');
  if (!pvEl || !uvEl) return;

  function fmt(n) {
    try { return Number(n).toLocaleString(); } catch (e) { return String(n); }
  }

  function render(pv, uv) {
    pvEl.textContent = fmt(pv);
    uvEl.textContent = fmt(uv);
  }

  // 兜底：构建时部署的快照（由 Actions 每 6h 更新 repo 里的 docs/{zh,en}/docs/stats.json）
  fetch('/stats.json', {cache: 'no-store'})
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { if (d) render(d.pv, d.uv); })
    .catch(function () {});

  // 实时：发 beacon 并用返回的最新累计值覆盖兜底数字
  var cid = null;
  try {
    cid = localStorage.getItem('vcid');
    if (!cid) {
      cid = (crypto.randomUUID && crypto.randomUUID()) ||
            'v-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 12);
      localStorage.setItem('vcid', cid);
    }
  } catch (e) {
    cid = 'v-anon-' + Math.random().toString(36).slice(2, 14);   // 隐私模式：不落盘，当一次性访客
  }

  fetch(ENDPOINT + '/hit', {
    method: 'POST',
    keepalive: true,
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({c: cid, p: location.pathname}),
  })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { if (d && typeof d.pv === 'number') render(d.pv, d.uv); })
    .catch(function () {});
})();
