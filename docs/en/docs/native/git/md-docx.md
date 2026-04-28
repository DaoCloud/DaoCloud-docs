# Batch Generate Docx

Command line tool: [mdctl](https://github.com/samzong/mdctl)

## Install on MacOS

```bash
brew tap samzong/tap
brew install samzong/tap/mdctl
```

!!! tip

    If dependencies are missing, install them as prompted, e.g., `xcode-select --install`

Download and extract template file: [doc-template.docx](./images/doc-template.docx.zip).
For example, download to default directory:

```
~/Downloads/doc-template.docx
```

## Usage

After installation, run in terminal:

```bash
mdctl export -h
```

Learn about various parameters:

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

## Generate a Docx

To convert Amamba application workspace Markdown to docx, first check navigation.yml to understand its nav structure:

```yaml
# Page tree
nav:
  - DaoCloud Website: https://www.daocloud.io/
  - Product Documentation:
      - Workspace:
          - Application Workspace:
...
```

```bash
mdctl export -d docs/zh/ -s mkdocs -o amamba.docx -n "Product Documentation/Workspace/Application Workspace" -t ~/Downloads/doc-template.docx -v
```

Where:

- `amamba.docx` is the generated docx file, located in the root directory of the current repo
- `Product Documentation/Workspace/Application Workspace` is the hierarchical structure in nav
- `~/Downloads/doc-template.docx` is the template file, whose style can be customized

## Convert to PDF

Compatibility of docx files is not great. For example, on operating systems in Europe/America or Arab regions,
some Chinese characters may appear garbled. In this case, you can convert to PDF to preserve document style.
For example:

- Use [I-love-pdf online convert to PDF](https://www.ilovepdf.com/word_to_pdf)
- Or use Adobe Acrobat Pro to convert locally to PDF

Currently, converted offline documents are located at [Download Center](https://docs.daocloud.io/download/#_5).
