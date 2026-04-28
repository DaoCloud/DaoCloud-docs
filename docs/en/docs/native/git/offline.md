---
hide:
  - navigation
---

# Building Offline Documentation Site

DCE 5.0 documentation is completely open source. All original Markdown files are hosted on [GitHub](https://github.com/DaoCloud/DaoCloud-docs),
using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) static compiler,
following GitHub standardized CI process, built with [Netlify](https://www.netlify.com/), the compiled HTML
files are stored on UCloud for customers in China and abroad.

Some enterprises need to build offline documentation sites, or need to build personalized navigation directories. Refer to this page to download/modify documentation data and build/run documentation site镜像 locally.

## Fork and Clone

1. Open the documentation repository [https://github.com/DaoCloud/DaoCloud-docs](https://github.com/DaoCloud/DaoCloud-docs), click the **Fork** button

    ![fork](./images/offline01.png)

1. After simple configuration, click **Create fork**

    ![fork](./images/offline02.png)

1. Click **Code** on the right, choose a method, such as copying the HTTPS address

    ![clone](./images/offline03.png)

1. Create a new folder locally, enter command line mode, and run the following command to clone the data:
