(function () {
  "use strict";

  // 跳转目标：保持当前路径，只增删 /en 前缀。
  function targetFor(lang) {
    const path = window.location.pathname;
    if (lang === "en") {
      return path.startsWith("/en/")
        ? path
        : "/en" + (path === "/" ? "" : path);
    }
    return path.startsWith("/en/") ? path.replace(/^\/en/, "") || "/" : path;
  }

  // 链接预览抓取器 / 搜索引擎 / 自动化浏览器不应被语言跳转改写 URL。
  // 否则中文页会被抓成英文版，分享卡片显示英文（飞书等预览服务就是这样
  // 拿到英文页的）；英文版不存在时还会抓到 404。
  function isCrawler() {
    const ua = navigator.userAgent || "";
    if (navigator.webdriver === true) return true;
    if (/HeadlessChrome|PhantomJS/i.test(ua)) return true;
    return /bot|crawler|spider|crawling|preview|facebookexternalhit|facebookcatalog|twitterbot|slackbot|telegrambot|whatsapp|discordbot|linkedinbot|embedly|pinterest|redditbot|skypeuripreview|feishu|lark|dingtalk|wechat|micromessenger|yandex|baiduspider|applebot|jina/i.test(
      ua
    );
  }

  const currentPath = window.location.pathname;

  // 0) 爬虫 / 链接预览抓取器 / 自动化浏览器：一律不跳转。
  // 这类客户端没有真实用户偏好，任何跳转都只会让抓取结果偏离原始 URL
  // （中文页被带去 /en/ 导致分享卡片显示英文）。放在最前面，连"用户显式
  // 选择"分支也一并跳过——抓取器 profile 里残留的 localStorage 不该生效。
  if (isCrawler()) return;

  // 1) 只有用户通过语言切换器显式选过语言才跳转（localStorage 记忆）。
  // 不做按浏览器语言（navigator.language）的自动重定向：
  // 自动跳转会改写用户输入的 URL，破坏深链与分享预览，
  // 也曾把飞书等预览服务引到错误语言页面。
  // 未选择过就停留当前页，URL 原样保留（含 query 与 hash）。
  let userSelectedLang = null;
  try {
    userSelectedLang = localStorage.getItem("userSelectedLang");
  } catch (e) {
    // 隐私模式下 localStorage 不可读，按"未选择"处理
    userSelectedLang = null;
  }

  if (userSelectedLang === "en" || userSelectedLang === "zh") {
    const chosen = targetFor(userSelectedLang);
    if (chosen !== currentPath) {
      // 深链必须带上 query 和 hash（锚点、筛选参数），与下方点击处理器一致
      window.location.replace(
        chosen + window.location.search + window.location.hash
      );
    }
  }

  // 2) 语言切换器点击：跳转并记住选择。
  document.addEventListener("click", function (event) {
    // hreflang 已被 og_meta_hook.py 改名为 data-lang（消除对爬虫的语言线索），
    // 两个都认，保证没有挂 hook 的构建同样可用。
    const langSwitcher = event.target.closest(
      ".md-select__link[data-lang], .md-select__link[hreflang]"
    );
    if (!langSwitcher) return;

    event.preventDefault();

    const newLang =
      langSwitcher.getAttribute("data-lang") ||
      langSwitcher.getAttribute("hreflang");
    if (!newLang) return;

    try {
      localStorage.setItem("userSelectedLang", newLang);
    } catch (e) {
      // 写入失败不影响本次跳转
    }

    const queryAndHash = window.location.search + window.location.hash;
    window.location.href = targetFor(newLang) + queryAndHash;
  });
})();
