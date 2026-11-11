"""为每个构建产出的页面注入 Open Graph / Twitter Card meta 标签。

主题本身不带任何 og: / twitter: 标记，链接分享到 X/Twitter、LinkedIn、
Slack、Telegram、飞书等平台时只会显示裸 URL，没有预览卡片。本 hook 在
``on_post_page`` 中注入：

- ``og:type`` / ``og:site_name`` / ``og:title`` / ``og:url`` / ``og:image``
  / ``og:locale``（并用对方语言填充 ``og:locale:alternate``）
- ``og:description``：页面 frontmatter 的 ``description`` 优先，其次取
  渲染后页面的正文首段，最后兜底站点级描述。
- ``twitter:card``（``summary``，目前只有方形 logo）+ 与 og 一致的
  title / description。

同时把每页的 ``<meta name="description">`` 替换为与 ``og:description``
相同的每页专属文本——mkdocs 原样拷贝站点级 ``site_description``，导致全站
每页共用同一句描述，搜索引擎会直接忽略。

本 hook 在 minify 插件之后执行（hooks 追加在插件列表末尾），正则对压缩后
的 HTML 保持宽容。已含 ``og:title`` 的页面直接跳过。
"""

import html
import re
from urllib.parse import urljoin

_MAX_DESC = 160

# 站点级 description meta 标签（mkdocs 产出，可能已被压缩）。
_SITE_DESC_RE = re.compile(r'<meta\s+name=["\']?description["\']?\s+content="[^"]*"\s*>')


def _first_paragraph(page_output):
    """提取 <article> 内第一个非空 <p> 的纯文本，取不到返回 None。"""
    article = page_output.find("<article")
    if article == -1:
        return None
    # 用 `<p[\s>]` 而不是 `<p[^>]*>`，避免误匹配 SVG 的 `<path>` 等标签。
    m = re.search(r"<p(?:\s[^>]*)?>(.*?)</p>", page_output[article:], re.DOTALL)
    if not m:
        return None
    # 剥离标题里 toc 的 permalink 锚点（"¶"），它们可能出现在段落之前。
    seg = re.sub(r'<a[^>]*class="[^"]*headerlink[^"]*"[^>]*>.*?</a>', "", m.group(1), flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", seg)
    text = re.sub(r"[¶]", " ", html.unescape(text))
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def _truncate(text, limit=_MAX_DESC):
    if len(text) <= limit:
        return text
    cut = text[:limit]
    # 优先在词边界截断；中文没有空格，直接按长度截断。
    space = cut.rfind(" ", 40)
    if space != -1:
        cut = cut[:space]
    return cut.rstrip(" ,;、，。.;:：-") + "…"


def _og_locale(language):
    return {"zh": "zh_CN", "en": "en_US"}.get(language, "en_US")


def on_post_page(output, page, config, **kwargs):
    if not output or "</head>" not in output:
        return output
    if 'property="og:title"' in output or "property='og:title'" in output:
        return output

    desc = (
        page.meta.get("description")
        or _first_paragraph(output)
        or config.site_description
        or ""
    )
    desc = _truncate(re.sub(r"\s+", " ", html.unescape(desc)).strip())

    locale = _og_locale(config.theme.get("language") or "en")
    alternate = "en_US" if locale == "zh_CN" else "zh_CN"
    site_name = config.site_name or ""
    title = str(page.title or site_name)
    url = getattr(page, "canonical_url", None) or config.site_url
    logo = config.theme.get("logo") or "images/DaoCloud.png"
    image = urljoin(config.site_url or "", logo)

    tags = (
        '<meta property="og:type" content="website">'
        f'<meta property="og:site_name" content="{html.escape(site_name, quote=True)}">'
        f'<meta property="og:title" content="{html.escape(title, quote=True)}">'
        f'<meta property="og:url" content="{html.escape(url, quote=True)}">'
        f'<meta property="og:image" content="{html.escape(image, quote=True)}">'
        f'<meta property="og:locale" content="{locale}">'
        f'<meta property="og:locale:alternate" content="{alternate}">'
        f'<meta property="og:description" content="{html.escape(desc, quote=True)}">'
        '<meta name="twitter:card" content="summary">'
        f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">'
        f'<meta name="twitter:description" content="{html.escape(desc, quote=True)}">'
    )

    # 用每页专属描述替换站点级通用描述。replacement 必须用 callable：
    # re.sub 会把字符串 replacement 里的反斜杠当转义/组引用解释，页面文本
    # 含 "C:\docs" 这类内容时会导致构建报错（re.error: bad escape）。
    if desc:
        output = _SITE_DESC_RE.sub(
            lambda _m: f'<meta name="description" content="{html.escape(desc, quote=True)}">',
            output,
            count=1,
        )

    return output.replace("</head>", tags + "</head>", 1)
