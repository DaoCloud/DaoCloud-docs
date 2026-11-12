"""为每个构建产出的页面注入 Open Graph / Twitter Card meta 标签。

主题本身不带任何 og: / twitter: 标记，链接分享到 X/Twitter、LinkedIn、
Slack、Telegram、飞书等平台时只会显示裸 URL，没有预览卡片。本 hook 在
``on_post_page`` 中注入：

- ``og:type`` / ``og:site_name`` / ``og:title`` / ``og:url`` / ``og:image``
  / ``og:locale``
- ``og:description``：页面 frontmatter 的 ``description`` 优先，其次取
  渲染后页面的正文首段，最后兜底站点级描述。
- ``twitter:card``（``summary``，目前只有方形 logo）+ 与 og 一致的
  title / description。

同时把每页的 ``<meta name="description">`` 替换为与 ``og:description``
相同的每页专属文本——mkdocs 原样拷贝站点级 ``site_description``，导致全站
每页共用同一句描述，搜索引擎会直接忽略。

另外做三件"去语言线索"和站级修正的事，起因是飞书把中文页卡片抓成了英文：

1. 移除 ``extra.alternate`` 生成的 head 内 hreflang 声明。它们用的是相对
   URL 且指向站点根，本身就是无效声明（Google 要求绝对 URL 且必须页级
   对应），副作用却是实打实的：飞书据此把 URL 按语言前缀改写，中文页
   ``/tf/hydra/intro/`` 被改写为 ``/en/tf/hydra/intro/`` 去抓，卡片显示成
   英文；英文版不存在时（``/en/drun/hydra/finetune/``）抓到的就是一条
   ``{"error":"Document not found"}``。
2. 语言下拉 ``<a href="/en/" hreflang="en">`` 上的 hreflang 改名为 ``data-lang``
   （只改名不删除）。``docs/*/docs/stylesheets/language-redirect.js`` 的点击
   处理器以 ``.md-select__link[hreflang]`` 为选择器、并用属性值作为"用户选择
   的语言"，删掉属性会让下拉退化成裸 href 跳转；改名后交互完全不变，而
   ``data-*`` 对抓取方没有语言语义。
3. 不输出 ``og:locale:alternate``：语义是"本页还有另一种语言版本"，同样会
   引导抓取方去找英文页，而它对 SEO 无实际价值。

最后补齐缺失的 ``rel="canonical"``。

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

# 语言切换下拉里的 <a href="/en/" hreflang="en"> 同样在向抓取器声明"有英文版"，
# 而且这里直接给出了 /en/ 这个路径，会诱导预览抓取方把当前 URL 加上 /en/ 前缀。
#
# 但 hreflang 是 docs/*/docs/stylesheets/language-redirect.js 的点击选择器依赖
# （.md-select__link[hreflang]），且该属性的值被用作"用户选择的语言"。直接删掉
# 会让下拉框退化成裸 href 跳转：用户选择不落盘、query/hash 丢失、且下次访问会
# 被浏览器语言自动跳转覆盖。所以这里只做【改名】：hreflang → data-lang。
# 属性值原样保留，JS 侧同步改为读 data-lang（见那两个 js 文件），视觉与交互不变，
# 而 data-* 对爬虫没有任何语义。
_A_HREFLANG_RE = re.compile(
    # 前瞻要求整个标签里出现 md-select__link，即只针对语言切换器；
    # 正文里 <a href="/fr/" hreflang="fr"> 这类合法的语言标注不受影响。
    r"""(<a\b(?=[^>]*\bmd-select__link\b)[^>]*?)(\s+)hreflang\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)""",
    re.IGNORECASE,
)


def _rename_hreflang(match):
    """把 <a> 上的 hreflang 改名为 data-lang（已存在 data-lang 时保持原样）。"""
    head, gap, value = match.group(1), match.group(2), match.group(3)
    if "data-lang" in head.lower():
        return match.group(0)
    # 保留原属性之间的空白（可能有换行和缩进），只替换属性名。
    return f"{head}{gap}data-lang={value}"

# 主题已输出的 canonical（中文站有，英文站此前没有）。
_CANONICAL_RE = re.compile(r'<link\b[^>]*\brel=["\']?canonical["\']?[^>]*>', re.IGNORECASE)

# 语言切换脚本的文件名（允许版本后缀，如 language-redirect.v2.js）。
_SWITCHER_JS_RE = re.compile(r"language-redirect(?:\.v\d+)?\.js$")


def _switcher_js_enabled(config):
    """本次构建是否加载了 language-redirect.js（它负责消费 data-lang）。

    hreflang 是切换脚本的点击选择器依赖，只有在脚本存在时改名才安全；
    没有脚本的构建（如漏配 extra_javascript 的配置）保持原样，避免出现
    "属性改了但没人消费"的半吊子状态。
    """
    items = getattr(config, "extra_javascript", None) or []
    for item in items:
        if isinstance(item, dict):
            path = item.get("path")
        else:
            path = getattr(item, "path", None) or item
        # 允许带版本后缀的文件名（如 language-redirect.v2.js）：改文件名是
        # 为了绕开 CDN 与抓取器的旧 JS 缓存。
        if path and _SWITCHER_JS_RE.search(str(path)):
            return True
    return False


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

    # 语言下拉 <a> 上的 hreflang 改名为 data-lang：属性对爬虫静默，
    # 但切换脚本仍能据 data-lang 在点击时保留 query/hash。
    # 仅在本次构建确实加载了切换脚本时才改名（见 _switcher_js_enabled）：
    # 没有脚本的构建里 hreflang 是唯一选择器，改了反而没人消费。
    if _switcher_js_enabled(config):
        output = _A_HREFLANG_RE.sub(_rename_hreflang, output)

    # 补齐缺失的 canonical（英文站此前完全没有）。
    if url and not _CANONICAL_RE.search(output):
        output = output.replace(
            "</head>", f'<link rel="canonical" href="{html.escape(url, quote=True)}">' + "</head>", 1
        )

    return output.replace("</head>", tags + "</head>", 1)
