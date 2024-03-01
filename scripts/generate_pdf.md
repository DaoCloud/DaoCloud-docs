# Batch Production of Word and PDF Files

English | [中文](./generate_pdf_zh.md)

## Conversion to Word

### Generating Word Files for All Documents (Not Recommended)

The following command can be used to batch generate a complete Word file that includes all documents.

```bash
cd /path/to/this/repo
python3 scripts/md2doc-v2.py docs/zh/docs # Generate Word files
```

However, the resulting Word file will contain all the content from docs.daocloud.io, making it difficult to read.

> Currently, this command generates a large number of Word files. Make sure not to commit them to GitHub.

It is recommended to run the following command before submitting a PR to remove cached Word files:

```bash
find ./docs -type f -name "*.docx" ! -name "TiDBonHwameiStor.docx" | xargs rm -f
```

### Generating Word File for Specific Folder (Recommended)

```bash
cd /path/to/this/repo
python3 scripts/md2doc-v2.py docs/zh/docs/kpanda # Generate Word files
```

> The above is an example to generate documentation for the `kpanda` folder.

If there are any errors during export, you can try running the following command to install the required dependencies:

```bash
pip install python-docx
brew install pandoc
```

## Conversion to PDF

### Generating PDF Files for All Documents (Not Supported)

Currently, generating a full PDF file for all documents fails due to the large size of the complete documentation.

> Not supported at the moment.

### Generating PDF File for Specific Folder (Recommended)

1. Modify the [pdf.yaml](../docs/zh/pdf.yaml) file, only modifying 2 fields:
   - `docs_dir` for the folder name to be read
   - `output_path` for the location to export the PDF
2. Run the `mkdocs build` command, ensuring that the poetry environment is properly configured
   1. Use `poetry install` to install the dependencies
   2. Run `poetry run mkdocs build -f pdf.yaml` to generate the PDF files

The secondary development of the documentation site is based on an open-source project. Currently, the supported features are limited, but they will be improved in the future.
