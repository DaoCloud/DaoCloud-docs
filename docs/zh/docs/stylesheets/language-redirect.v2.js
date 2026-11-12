/*
 * 语言切换器增强脚本。
 *
 * 设计原则：页面加载时零副作用。
 * 本脚本不做任何自动跳转——不看浏览器语言（navigator.language），
 * 不看 localStorage，不改写 URL。原因：链接预览抓取器（飞书、微信、
 * Slack 等）会执行页面 JS，任何自动跳转都会让分享卡片抓到另一种语言的
 * 页面，或抓到 404。
 *
 * 唯一职责：用户点击语言切换器时，跳转目标语言并保留 query 与 hash
 * （锚点、筛选参数），这些是浏览器原生链接跳转会丢掉的部分。
 */
(function () {
  "use strict";

  // 目标 URL：保持当前路径，只增删 /en 前缀；不带 query/hash。
  function targetFor(lang) {
    const path = window.location.pathname;
    if (lang === "en") {
      return path.startsWith("/en/")
        ? path
        : "/en" + (path === "/" ? "" : path);
    }
    return path.startsWith("/en/") ? path.replace(/^\/en/, "") || "/" : path;
  }

  document.addEventListener("click", function (event) {
    // hreflang 已被 og_meta_hook.py 改名为 data-lang（消除对爬虫的语言线索），
    // 两个都认，保证没有挂 hook 的构建同样可用。
    const langSwitcher = event.target.closest(
      ".md-select__link[data-lang], .md-select__link[hreflang]"
    );
    if (!langSwitcher) return;

    const newLang =
      langSwitcher.getAttribute("data-lang") ||
      langSwitcher.getAttribute("hreflang");
    if (!newLang) return;

    // 原生链接会丢掉 query 与 hash，这里接管并补回。
    event.preventDefault();
    window.location.href =
      targetFor(newLang) + window.location.search + window.location.hash;
  });
})();
