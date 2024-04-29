# TW 工作说明

!!! tip

    TW = Technical Writer，即文档工程师、内容专家、内容营销专家等

我们目前有 2 个网站：

- [DCE 5.0 Website](https://docs.daocloud.io/)：DCE 对外的产品文档和新闻门户
- [d.run Website](https://docs.d.run/)：d.run 对外的产品文档和新闻门户

GitHub 上托管了 3 个仓库跟 Technical Writer 有关：

- [DaoCloud/DaoCloud-docs](https://github.com/DaoCloud/DaoCloud-docs)：DCE 5.0 网站的源文件
- [DaoCloud/daocloud-api-docs](https://github.com/DaoCloud/daocloud-api-docs)：DCE 5.0 有关的 Open API 文档
- [d-run/drun-docs](https://github.com/d-run/drun-docs)：d.run 网站的源文件

## 产品文档工作

**中文：**

- 所有操作步骤、截图、参数说明、视频等必须与真实的产品保持一致，TW 需要验证这些内容，确保文档与产品时刻一致
- [下载中心](../../../download/index.md)和[安装步骤](../../../install/index.md)属于入口，这些内容要优先保证正确
- 保证文档站所有 link 正确，可以在 zh/docs 或 en/docs 目录运行 `mkdocs serve` 命令检查链接
- 每月更新至少两篇[博客](../../../blogs/index.md)
- [DaoCloud 开源生态](../../../community/index.md)要与社区项目保持一致，比如最近 Kubean 加入了 Sandbox，那相关页面也要更新
- [云原生研究院](../../../native/knowledge/index.md)会收录一些社区新闻，比如 KubeCon，还有一些新手教程，常用的 Git 命令和正则表达式等
- [OpenAPI 文档](https://docs.daocloud.io/openapi/index.html)：每月发版后，要记得 merge 相关模块的 PR，然后定期更新 nav 和 index 页面
- [d.run 文档](https://docs.d.run/)同样要与 UI 界面保持一致，这是个新项目，开发迭代比较快，那文档也要跟上进度
- 产品白皮书、软件著作权、SOP 流程文档以及对售前交付等同事的文档支持
- 确保从 Google、百度能搜到你编辑的内容，只要你活跃度够高，搜索结果就会在前面

**英文：**

- 保持与中文内容一致，文字先用 GPT 翻译，然后经过人工校对即 MTPE，目前校对比例为 `250/1200 = 约 20%`，质量差距还很大
- 补充英文截图
- 每月都会更新部分中文页面，那相应英文也要更新，参照[批量检测中英同步问题](./lsync.md)
- 紧跟社区动态，转载国外行业新闻到[博客频道](../../../blogs/index.md)
- 英文官网和对外营销 PPT 英文审核

## 开源项目文档支持

DaoCloud 现有 [10 多个开源项目](../../../community/index.md)，
特别是已加入 CNCF Sandbox 和 Landscape 的七八个项目，TW 需要对其提供文档支持，协助社区建设。

## 视频剪辑

- [视频教程](../../../videos/index.md)：每月会用剪映或 PR 剪辑出来一些操作视频
- 补充英文视频，可以上传到 YouTube，然后以 iframe 嵌入到文档站

## UI i18n 翻译

- 补充产品 20 多个模块的英文，这些仓库都放在 GitLab，需要先把这 20 个仓库全部克隆下来，每月去[检查 i18n 百分比](https://ndx.gitpages.daocloud.io/product/frontend-i18n-counter/)
- 走查所有 UI 中英文字，定期维护，UI 文字要简短易懂，要跟社区主流项目用词保持一致

## 他山之石

多借鉴社区和名企的优秀做法：

- [k8s.io](https://kubernetes.io/)
- [istio.io](https://istio.io/)
- [opentelemetry.io](https://opentelemetry.io/)
- [huggingface.co](https://huggingface.co/)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- 多去参加 CNCF 社区活动，跟同行交流才会有进步和成长

![KCD 2024](../../images/kcd.jpeg)
