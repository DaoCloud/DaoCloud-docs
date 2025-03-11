# 批量生成 Docx

命令行工具：[mdctl](https://github.com/samzong/mdctl)

## 在 MacOS 上安装

```bash
brew tap samzong/tap
brew install samzong/tap/mdctl
```

!!! tip

    如果缺少依赖项，按提示安装，例如 `xcode-select --install`

下载并解压模板文件：[doc-template.docx](./images/doc-template.docx.zip)。
比如下载到默认目录：

```
~/Downloads/doc-template.docx
```

## 使用

安装完成后，在终端运行：

```bash
mdctl export -h
```

了解各项参数信息：

```console
Export markdown files to other formats like DOCX, PDF, EPUB.
Uses Pandoc as the underlying conversion tool.

Examples:
  mdctl export -f README.md -o output.docx
  mdctl export -d docs/ -o documentation.docx
  mdctl export -d docs/ -s mkdocs -o site_docs.docx
  mdctl export -d docs/ -o report.docx -t templates/corporate.docx
  mdctl export -d docs/ -o documentation.docx --shift-heading-level-by 2
  mdctl export -d docs/ -o documentation.docx --toc --toc-depth 4
  mdctl export -d docs/ -o documentation.pdf -F pdf

Usage:
  mdctl export [flags]

Flags:
  -d, --dir string                   Source directory containing markdown files to export
  -f, --file string                  Source markdown file to export
      --file-as-title                Use filename as section title
  -F, --format string                Output format (docx, pdf, epub) (default "docx")
  -h, --help                         help for export
  -n, --nav-path string              Specify the navigation path to export (e.g. 'Section1/Subsection2')
  -o, --output string                Output file path
      --shift-heading-level-by int   Shift heading level by N
  -s, --site-type string             Site type (basic, mkdocs, hugo, docusaurus) (default "basic")
  -t, --template string              Word template file path
      --toc                          Generate table of contents
      --toc-depth int                Depth of table of contents (default 3) (default 3)
  -v, --verbose                      Enable verbose logging
```

## 生成一个 docx

假如要将 Amamba 应用工作台的 Markdown 转换为 docx，先查看 navigation.yml，了解其 nav 结构：

```yaml
# Page tree
nav:
  - DaoCloud 官网: https://www.daocloud.io/
  - 产品文档:
      - 工作台:
          - 应用工作台:
...
```

```bash
mdctl export -d docs/zh/ -s mkdocs -o amamba.docx -n "产品文档/工作台/应用工作台" -t ~/Downloads/doc-template.docx -v
```

其中：

- `amamba.docx` 是生成的 docx 文件，位于当前 repo 的根目录
- `产品文档/工作台/应用工作台` 是 nav 中的层次结构
- `~/Downloads/doc-template.docx` 是模板文件，这个文件的样式可以自行定制

## 转换成 PDF

docx 文件的兼容性不太好，比如在欧美或阿拉伯地区的操作系统上打开，
某些中文字符会出现乱码，此时可以将其转换成 PDF 保留文档样式。
比如你可以：

- 使用 [I-love-pdf 在线转换 PDF](https://www.ilovepdf.com/word_to_pdf)
- 或使用 Adobe Acrobat Pro 在本地转换成 PDF

目前经转换的离线文档都位于[下载站](https://docs.daocloud.io/download/#_5)。
