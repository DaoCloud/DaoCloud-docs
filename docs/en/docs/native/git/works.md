# TW Work Description

!!! tip

    TW = Technical Writer, i.e., Documentation Engineer, Content Expert, Content Marketing Expert, etc.

We currently have 2 websites:

- [DCE 5.0 Website](https://docs.daocloud.io/): DCE external product documentation and news portal
- [d.run Website](https://docs.d.run/): d.run external product documentation and news portal

GitHub hosts 3 repositories related to Technical Writer:

- [DaoCloud/DaoCloud-docs](https://github.com/DaoCloud/DaoCloud-docs): Source files for DCE 5.0 website
- [DaoCloud/daocloud-api-docs](https://github.com/DaoCloud/daocloud-api-docs): Open API documentation for DCE 5.0
- [d-run/drun-docs](https://github.com/d-run/drun-docs): Source files for d.run website

## Product Documentation Work

**Chinese:**

- All operation steps, screenshots, parameter descriptions, videos must be consistent with the actual product. TW needs to verify these contents to ensure documentation is always in sync with the product
- [Download Center](../../download/index.md) and [Installation Steps](../../install/index.md) are entry points, these contents should be prioritized for accuracy
- Ensure all links in the documentation site are correct. You can run `mkdocs serve` command in zh/docs or en/docs directory to check links
- Update at least 2 [blogs](../../blogs/index.md) per month
- [DaoCloud Open Source Ecosystem](../../community/index.md) should be consistent with community projects. For example, if Kubean joins Sandbox, related pages should also be updated
- [Cloud Native Institute](../../native/knowledge/index.md) collects community news like KubeCon, some beginner tutorials, common Git commands and regular expressions
- [OpenAPI Documentation](https://docs.daocloud.io/openapi/index.html): After each monthly release, remember to merge PRs of related modules, then regularly update nav and index pages
- [d.run Documentation](https://docs.d.run/) should also be consistent with the UI. This is a new project with fast development iterations, documentation should keep up
- Product whitepapers, software copyright, SOP process documentation, and documentation support for presales and delivery colleagues
