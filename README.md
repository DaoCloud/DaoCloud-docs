# DaoCloud Enterprise 5.0 Documentation

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

[中文版](README_zh.md) ｜ English

DaoCloud is a Certified Kubernetes Service Provider (KCSP). DCE has been certified with the following releases:

Current releases:

[![1.23](./docs/zh/docs/images/1.23.png)](https://github.com/cncf/k8s-conformance/pull/2072)
[![1.24](./docs/zh/docs/images/1.24.png)](https://github.com/cncf/k8s-conformance/pull/2239)
[![1.25](./docs/zh/docs/images/1.25.png)](https://github.com/cncf/k8s-conformance/pull/2240)

Legacy releases:

[![1.7](./docs/zh/docs/images/1.7.png)](https://github.com/cncf/k8s-conformance/pull/68)
[![1.9](./docs/zh/docs/images/1.9.png)](https://github.com/cncf/k8s-conformance/pull/210)
[![1.13](./docs/zh/docs/images/1.13.png)](https://github.com/cncf/k8s-conformance/pull/418)
[![1.15](./docs/zh/docs/images/1.15.png)](https://github.com/cncf/k8s-conformance/pull/794)
[![1.18](./docs/zh/docs/images/1.18.png)](https://github.com/cncf/k8s-conformance/pull/1144)
[![1.20](./docs/zh/docs/images/1.20.png)](https://github.com/cncf/k8s-conformance/pull/1463)

DCE 5.0 website is created with MkDocs. All pages are written in markdown.
We use GitOps to control workflow and versions.

## Open a PR

This website uses Pull Request (PR) to modify, translate, and manage all pages.

1. Click `Fork` to create a fork
2. Run `git clone` to clone this fork to your computer
3. Edit one or more pages locally and preview it
4. Run git commands, such as `git add`, `git commit`, and `git push`, to submit your changes
5. Open a PR in this repo
6. Successfully merge after reviewing, thanks.

## Preview locally

This section describes how you can preview your changes before commit.

### With Docker

1. Install and run [Docker](https://www.docker.com/).
2. Run `make serve` and preview your changes.

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
- Care about links to avoid any null or dead link
- Give a consistent experience to explore all pages herein

For more details refer to [DaoCloud Style Guide of Writing](./style.md).

## Acknowledgements

We sincerely thank all the contributors who contribute to DaoCloud website.
Once a PR you opened have been successfully merged, your ID will appear at the bottom of the page as an author.

If any problem, feel free to reach out to us: [support@daocloud.io](mailto:support@daocloud.io?subject=FROM_DOCS_README) or scan the QR code to chat with developers:

![](./docs/zh/docs/images/assist.png)

## References

- [DaoCloud Style Guide of Writing](./style.md)
- [Contribution Guideline](./CONTRIBUTING.md)

## Release notes of this website

[Release v1.0](docs/README.md)
