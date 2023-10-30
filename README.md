# DaoCloud Enterprise 5.0 Documentation

[![Contributors](https://img.shields.io/github/contributors/daocloud/daocloud-docs?color=purple)](CONTRIBUTING.md)
[![Build](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/DaoCloud/DaoCloud-docs/actions/workflows/main.yml)

[中文版](README_zh.md) ｜ English

DaoCloud is a Certified Kubernetes Service Provider (KCSP). DCE has been certified with the following releases:

Current releases maintained by K8s community:

[![1.25](./images/1.25.png)](https://github.com/cncf/k8s-conformance/pull/2240)
[![1.26](./images/1.26.png)](https://github.com/cncf/k8s-conformance/pull/2451)
[![1.27](./images/1.27.png)](https://github.com/cncf/k8s-conformance/pull/2666)
[![1.28](./images/1.28.png)](https://github.com/cncf/k8s-conformance/pull/2835)

Legacy versions that are no longer maintained by the K8s community but will continue to be maintained by DaoCloud's [KLTS](https://klts.io/):

[![1.7](./images/1.7.png)](https://github.com/cncf/k8s-conformance/pull/68)
[![1.9](./images/1.9.png)](https://github.com/cncf/k8s-conformance/pull/210)
[![1.13](./images/1.13.png)](https://github.com/cncf/k8s-conformance/pull/418)
[![1.15](./images/1.15.png)](https://github.com/cncf/k8s-conformance/pull/794)
[![1.18](./images/1.18.png)](https://github.com/cncf/k8s-conformance/pull/1144)
[![1.20](./images/1.20.png)](https://github.com/cncf/k8s-conformance/pull/1463)
[![1.23](./images/1.23.png)](https://github.com/cncf/k8s-conformance/pull/2072)
[![1.24](./images/1.24.png)](https://github.com/cncf/k8s-conformance/pull/2239)

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
4. Preview with <http://0.0.0.0:8000/>

## Naming conventions

This section lists some conventions about a file or folder name for your reference:

- **Only contain** English lower cases and hyphens (`-`)
- **Do not** contain any of these characters like:
    - Chinese chars
    - spaces
    - special chars like `*`, `?`, `\`, `/`, `:`, `#`, `%`, `~`, `{`, `}`
- Connect words with a hyphen (`-`)
- Keep short：up to 5 English words, avoid repetition, use abbreviations
- Be descriptive: easy to understand and reflect the doc's subject

| No                                 | Yes              | Why                                      |
| ---------------------------------- | ---------------- | ---------------------------------------- |
| ConfigName                         | config-name      | Use small letters and hyphens            |
| 创建 秘钥                          | create-secret    | No Chinese words and other macro symbols |
| quick-start-install-online-install | online-install   | Keep short                               |
| c-ws                               | create-workspace | Be descriptive                           |
| update_image                       | update-image     | Connect words with hyphens               |

## Tips about writing

- Indent 4 spaces for bullets
- Provide a space between zh and en chars
- Provide a blank line before and after a para, an image, a heading, or a list
- Do not add any punctuation by the end of a heading
- Care about links to avoid any null or dead link
- Give a consistent experience to explore all pages herein

For more details refer to [DaoCloud Style Guide of Writing](./style.md).

## References

- [docs.daocloud.io Release v1.0](docs/README.md)
- [DaoCloud Style Guide of Writing](./style.md)
- [Contribution Guideline](./CONTRIBUTING.md)
- [Citizen Code of Conduct](./CODE_OF_CONDUCT.md)
- [Export Word and PDF](./scripts/generate_pdf.md)
- [Automatic Page Translation](./scripts/README.md); ChatGPT is recommended to use for better translation

## Thanks to all contributors ❤

<a href="https://github.com/daocloud/daocloud-docs/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=daocloud/daocloud-docs" />
</a>

## Proudly using Netlify

[![Netlify](https://www.netlify.com/img/global/badges/netlify-color-accent.svg)](https://www.netlify.com)

| Site | Status
|------|-------
| daocloud-docs | [![Netlify Status](https://api.netlify.com/api/v1/badges/d193c503-c2f6-4c8f-99ee-db0371f90ceb/deploy-status)](https://app.netlify.com/sites/daocloud-docs/deploys)
