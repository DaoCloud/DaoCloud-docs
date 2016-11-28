---
title: 接入DCE集群
---

[DaoCloud Enterprise](https://www.daocloud.io/enterprise/dce.html) (DCE) 是 DaoCloud 提供的企业级容器集群解决方案。

[DaoCloud Services 精益版套餐](https://www.daocloud.io/pricing/public-lean.html)也包含了为互联网公司定制的 Cloud Edition DCE。

若您已拥有 DCE，可以通过接入 DaoCloud Services 享受云端的持续发布与 DCE 集群管理能力的结合。


1. 进入 DaoCloud Services 我的集群页面，添加 DCE 集群
![](Screen%20Shot%202016-11-28%20at%2011.47.39%20AM.png)

2. 在 DCE 控制节点上执行安装脚本
![](Screen%20Shot%202016-11-28%20at%2011.51.22%20AM.png)

3. 输入管理账号／密码进行授权
![](Screen%20Shot%202016-11-28%20at%2011.51.34%20AM.png)

4. 完成接入后，您可以使用 DaoCloud Services 进行CI、构建与安全扫描等操作，并设置自动化规则来发布新版本应用
![](Screen%20Shot%202016-11-28%20at%2011.53.50%20AM.png)

请参考 [代码构建](http://docs.daocloud.io/ci-image-build/start-ci-and-build)、[使用流水线持续发布](http://docs.daocloud.io/pipeline/continues-delivery)等章节

> 接入 DCE 后您可以点击集群 DCE 面板的设置来修改 DCE 的登陆地址，请确保设置正确