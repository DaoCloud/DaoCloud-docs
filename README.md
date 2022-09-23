
# DaoCloud Enterprise 5.0 Documentation

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

[中文版](README_zh.md) ｜ English

DCE 5.0 docsite is created with MkDocs. All pages are written in markdown. We use GitOps to control workflow and versions.

## Open a PR

This docsite uses Pull Request (PR) to modify, translate, and manage all pages.

1. Click `Fork` to create a fork
2. Run `git clone` to clone this fork to your computer
3. Edit one or more pages locally and preview it
4. Run git commands, such as `git add`, `git commit`, and `git push`, to submit your changes
5. Open a PR in this repo
6. Successfully merge after reviewing, thanks.

Please read through [writing style](http://docs-static.daocloud.io/write-docs) before any change.

## Create a local preview environment

### With Docker

1. Install and run Docker
2. Run `make serve` and preview your changes

### With Git repo

See [MkDocs documents to install](https://squidfunk.github.io/mkdocs-material/getting-started/)。

1. Install Poetry and Python 3.9+
   1. Configure Poetry: `poetry config virtualenvs.in-project true`
   2. Enable venv: `poetry env use 3.9`
2. Install dependencies: `poetry install`
3. Run `poetry run mkdocs serve -f mkdocs.yml` in the repo folder locally
4. Preview with http://127.0.0.1:8000/

## Tips about writing

- Indent 4 spaces for bullets
- Provide a space between zh and en chars
- Provide a blank line before and after a para, an image, a heading, or a list
- Do not add any punctuation by the end of a heading
- Do not your a null link

## Acknowledgements

We sincerely thank all the contributors who contribute to DaoCloud docsite. Once a PR you opened have been successfully merged, your ID will appear at the bottom of the page as an author.

If any problem, feel free to reach out to us: [support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README)
