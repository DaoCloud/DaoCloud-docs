# 混迹 GitHub 社区技巧

GitHub 号称有一亿开发者活跃，如何能在目标社区展露头角？

一方面需要你自己的专业水平过硬，另一方面需要了解一些社区礼仪和基本技巧。

## 在社区留痕

- PR 和 Issue

    提了一个 PR 或 Issue 后，如果有人留下 comments，一定要及时回复和处理！

    因为社区的 8000 万人，90% 的时间都在用 comments 交流。
    想象一下，如果你在企业微信给同事留了一条言，而对方 10 天半个月才答复，你是什么感受？？？

- Comment 评论

    看到一个 PR 或 Issue 时，如果心中有所疑问，或看出了什么问题，要积极留下 comments。

    1. 点击每一行左侧的 `+` 号

        ![comments](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/comments1.png)
    
    2. 点击 `Add a suggestion` 图标，修改代码后，点击 `Start a review`

        ![comments](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/comments2.png)

        !!! warning

            尽量不要点击 `Add single comment`，除非你真的只有一条 comment。
            这是因为你每一条 comment，都会给这个 PR 的作者、Reviwer、关注者群发一封邮件！
            如果你连续点击 `Add single comment`，将对这些人的邮箱形成轰炸效果，Spam!!!

    3. 看完全文，做了所有 comment 之后，点击右上角 `Finish your review`，勾选 `Comment` 后点击 `Submit review`。

        ![comments](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/comments3.png)

- 表示关注

    如果你对某个 PR 感兴趣，但暂时没有合适的 comment，可以用表情符号来留下痕迹。

    ![comments](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/comments4.png)

!!! tip

    走过路过，千万不要沉默！！！让大家知道你来过！！！

## 在社区成长

当你初入 GitHub 可能会有些茫然，数百万个 Repo 仓库，一亿开发者汇聚，怎么找到热点呢？

对于 DaoCloud 的船员，主要混迹于 CNCF 社区，特别是以 K8s 为首的各个项目。
每个项目都有这些文件：

- [README.md](https://github.com/DaoCloud/DaoCloud-docs)
- [CONTRIBUTING.md](https://github.com/kubernetes/website/blob/main/CONTRIBUTING.md)

慢慢你会发现 member -> reviewer -> approver/maintainer -> lead/chair -> committee 等成长路线。

如果你能在著名项目有所建树，那不亚于另一张文凭。

## 贡献统计

- [K8s 贡献统计 Devstatus](https://k8s.devstats.cncf.io/d/13/developer-activity-counts-by-repository-group?orgId=1&var-period_name=Last%20year&var-metric=contributions&var-repogroup_name=SIG%20Docs&var-repo_name=kubernetes&var-country_name=All)
- [Istio 贡献统计 Devstatus](https://istio.teststats.cncf.io/d/66/developer-activity-counts-by-companies?orgId=1&var-period_name=Last%20year&var-metric=contributions&var-repogroup_name=All&var-country_name=All&var-companies=All)
- [OSSinsight 仪表盘](https://ossinsight.io/)

## 社区资源

- [K8s 文档](https://kubernetes.io/)
- [Istio 文档](https://istio.io/)
- [CNCF 词汇表](https://glossary.cncf.io/)
- [Prometheus 文档](https://prometheus.io/docs/introduction/overview/)
