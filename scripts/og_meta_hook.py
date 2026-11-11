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

另外处理两处 ``<link>``：

1. 移除 ``extra.alternate`` 生成的全站级 hreflang 声明。它们用的是相对 URL
   且指向站点根，本身就是无效声明（Google 要求绝对 URL 且必须页级对应），
   副作用却是实打实的：飞书等平台的链接预览会据此把 URL 按语言前缀改写，
   于是中文页 ``/tf/hydra/intro/`` 被改写为 ``/en/tf/hydra/intro/`` 去抓，
   卡片显示成英文；若英文版不存在（如 ``/en/drun/hydra/finetune/``），
   抓到的就是一条 ``{"error":"Document not found"}``。
   删掉后抓取方只会抓原 URL。header 里的语言切换下拉不受影响（那是 body
   里的普通链接，不依赖 head 中的 hreflang）。
2. 补齐缺失的 ``rel="canonical"``：英文站此前一个都没有，中文站由主题输出。

本 hook 在 minify 插件之后执行（hooks 追加在插件列表末尾），正则对压缩后
的 HTML 保持宽容。已含 ``og:title`` 的页面直接跳过。
"""

import html
import re
from urllib.parse import urljoin

_MAX_DESC = 160

# 站点级 description meta 标签（mkdocs 产出，可能已被压缩）。
_SITE_DESC_RE = re.compile(r'<meta\s+name=["\']?description["\']?\s+content="[^"]*"\s*>')

# extra.alternate 生成的 hreflang 声明，形如
#   <link rel="alternate" href="/en/" hreflang="en">
# 压缩后可能丢掉属性引号、打乱属性顺序，因此用两个前瞻断言独立判断：
#   1. 必须带 hreflang 属性——这只删语言声明，不会误删 RSS/Atom feed
#      （<link rel="alternate" type="application/rss+xml">）或
#      alternate stylesheet 这类合法的 alternate 资源；
#   2. rel 必须恰好是 alternate 这个 token，而不是包含它。
_ALT_LINK_RE = re.compile(
    r"""<link\b(?=[^>]*\bhreflang\s*=)"""
    r"""(?=[^>]*\brel\s*=\s*(?:"alternate"|'alternate'|alternate(?=[\s>])))[^>]*>""",
    re.IGNORECASE,
)

# 主题已输出的 canonical（中文站有，英文站此前没有）。
_CANONICAL_RE = re.compile(r'<link\b[^>]*\brel=["\']?canonical["\']?[^>]*>', re.IGNORECASE)


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

    # 移除站点级 hreflang。相对 URL + 指向站点根 = 无效声明，却会诱导飞书等
    # 平台按语言前缀改写 URL 去抓另一语言的版本（详见模块 docstring）。
    output = _ALT_LINK_RE.sub("", output)

    # 补齐缺失的 canonical（英文站此前完全没有）。
    if url and not _CANONICAL_RE.search(output):
        output = output.replace(
            "</head>", f'<link rel="canonical" href="{html.escape(url, quote=True)}">' + "</head>", 1
        )

    return output.replace("</head>", tags + "</head>", 1)
