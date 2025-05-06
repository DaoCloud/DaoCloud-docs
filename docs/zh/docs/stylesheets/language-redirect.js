(function () {
  const userSelectedLang = localStorage.getItem("userSelectedLang");
  const currentPath = window.location.pathname;

  if (userSelectedLang) {
    if (userSelectedLang === "en" && !currentPath.startsWith("/en/")) {
      const newPath = "/en" + (currentPath === "/" ? "" : currentPath);
      window.location.replace(newPath);
      return;
    } else if (userSelectedLang === "zh" && currentPath.startsWith("/en/")) {
      const newPath = currentPath.replace(/^\/en/, "") || "/";
      window.location.replace(newPath);
      return;
    }
    return;
  }

  const userLang = (
    navigator.language ||
    navigator.userLanguage ||
    "en"
  ).toLowerCase();
  const langPrefix = userLang.split("-")[0];

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
})();

document.addEventListener("click", function (event) {
  const langSwitcher = event.target.closest(".md-select__link[hreflang]");
  if (langSwitcher) {
    event.preventDefault();

    const newLang = langSwitcher.getAttribute("hreflang");
    localStorage.setItem("userSelectedLang", newLang);

    const currentPath = window.location.pathname;
    let newPath;

    if (newLang === "en") {
      newPath = currentPath.startsWith("/en/")
        ? currentPath
        : "/en" + (currentPath === "/" ? "" : currentPath);
    } else {
      newPath = currentPath.startsWith("/en/")
        ? currentPath.replace(/^\/en/, "") || "/"
        : currentPath;
    }

    const queryAndHash = window.location.search + window.location.hash;

    window.location.href = newPath + queryAndHash;
  }
});
