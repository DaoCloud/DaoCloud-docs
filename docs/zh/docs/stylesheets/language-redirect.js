document.addEventListener("DOMContentLoaded", function () {
  const cookies = document.cookie.split(";").reduce((acc, cookie) => {
    const [key, value] = cookie.trim().split("=");
    acc[key] = value;
    return acc;
  }, {});
  if (cookies.preferredLang) {
    return;
  }

  // 获取浏览器语言
  const userLang = (
    navigator.language ||
    navigator.userLanguage ||
    "en"
  ).toLowerCase();
  const langPrefix = userLang.split("-")[0];

  const currentPath = window.location.pathname;

  // 语言跳转逻辑
  if (langPrefix === "zh") {
    if (currentPath.startsWith("/en/")) {
      const newPath = currentPath.replace(/^\/en/, "") || "/";
      window.location.replace(newPath);
    }
  } else {
    if (!currentPath.startsWith("/en/")) {
      const newPath = "/en" + (currentPath === "/" ? "" : currentPath);
      window.location.replace(newPath);
    }
  }
});

document.addEventListener("click", function (event) {
  const langLink = event.target.closest("a[data-language]");
  if (langLink) {
    const selectedLang = langLink.getAttribute("data-language");
    document.cookie = `preferredLang=${selectedLang}; path=/; max-age=${
      30 * 24 * 60 * 60
    }`;
  }
});
