"""Emit an additional ".html" redirect for every entry in redirect_maps.

mkdocs-redirects writes exactly one HTML file per redirect_maps entry: with
``use_directory_urls: true`` it creates "``<old>``/index.html" (a directory
URL), so the classic "``<old>``.html" URL keeps returning 404.

Several compatibility entries in ``resources/links-on-ui.yaml`` reference these
".html" URLs -- they were authored when the site still built with
``use_directory_urls: false`` -- so both forms must resolve. This hook writes a
meta-refresh "``<old>``.html" stub that points at the same target as the
directory-form redirect already produced by the plugin.

In ``use_directory_urls: false`` configs the plugin already emits "``<old>``.html"
directly, so this hook is a no-op for them.
"""

import os
import posixpath

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <link rel="canonical" href="{url}">
    <script>var anchor=window.location.hash.substr(1);location.href="{url}"+(anchor?"#"+anchor:"")</script>
    <meta http-equiv="refresh" content="0; url={url}">
</head>
<body>
You're being redirected to a <a href="{url}">new destination</a>.
</body>
</html>
"""


def _split_hash_fragment(path):
    path, hash, after = path.partition("#")
    return path, hash + after


def _relative_target(page_old, page_new, plugin):
    page_new = str(page_new)
    if page_new.lower().startswith(("http://", "https://")):
        return page_new
    target_path, fragment = _split_hash_fragment(page_new)
    file = plugin.doc_pages.get(target_path)
    if file is None:
        return None
    html_dir = posixpath.dirname(posixpath.splitext(page_old)[0] + ".html")
    relative = posixpath.relpath(file.url.lstrip("/"), html_dir)
    return relative + fragment


def on_post_build(config, **kwargs):
    if not config.get("use_directory_urls"):
        return
    try:
        plugin = config["plugins"].get("redirects")
    except Exception:
        return
    if plugin is None:
        return

    for page_old, page_new in plugin.redirects.items():
        html_path = posixpath.splitext(page_old)[0] + ".html"
        if html_path == page_old:
            continue
        target = _relative_target(page_old, page_new, plugin)
        if target is None:
            continue
        abs_path = os.path.join(config["site_dir"], html_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.format(url=target))