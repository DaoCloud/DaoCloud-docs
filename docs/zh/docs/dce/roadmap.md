---
hide:
  - toc
---

# DCE 5.0 产品特性 Roadmap

本页列出 DCE 5.0 部分模块未来几个月的功能特性开发计划。

!!! tip

    有关过去几年的开发记录，请查阅 [DCE 5.0 Release Notes](./dce-rn/20240830.md)。
    如有任何建议或想法，欢迎[提交 Issue](https://github.com/DaoCloud/DaoCloud-docs/issues)。

<div class="grid cards" markdown>

-   :material-microsoft-azure-devops:{ .lg .middle } __工作台__

    ---

    - 提高研发效能，在概览面板展示更多维度的统计分析
    - 保存应用模板（Helm Chart）
    - 增加更多自定义步骤、自定义模版

    [:octicons-arrow-right-24: 查看工作台 Release Notes](../amamba/intro/release-notes.md)

-   :octicons-container-16:{ .lg .middle } __容器__

    ---

    - 支持 GPU Volcano 调度策略
    - 推动 [Hami](../community/hami.md) 实现 vGPU 配额、支持 GPU 节点二次调度、动态申请 GPU 资源等
    - 支持 DRA 网络

    [:octicons-arrow-right-24: 查看容器 Release Notes](../kpanda/intro/release-notes.md)

-   :material-train-car-container:{ .lg .middle } __虚拟机__

    ---

    - 提供虚拟机仪表盘，直观体现虚拟机状态和资源使用情况
    - 支持配置虚拟机的存活性和可用性健康检查
    - 支持虚拟机备份

    [:octicons-arrow-right-24: 查看虚拟机 Release Notes](../virtnest/intro/release-notes.md)

-   :material-engine:{ .lg .middle } __微服务__

    ---

    - 微服务网关 API 的版本管理
    - 提供微服务网关实例级别的黑白名单

    [:octicons-arrow-right-24: 查看微服务 Release Notes](../skoala/intro/release-notes.md)

-   :material-monitor-dashboard:{ .lg .middle } __可观测性__

    ---

    - 展示全链路 span 数据
    - 支持自定义日志采集配置、日志脱敏
    - 告警支持基于不同的集群、命名空间级别等标签发送给不同的用户

    [:octicons-arrow-right-24: 查看 Insight Release Notes](../insight/intro/release-notes.md)

-   :material-slot-machine:{ .lg .middle } __AI Lab__

    ---

    - 多模态大模型 Agent 工作流编排
    - LLMOps 模型推理服务网关

    [:octicons-arrow-right-24: 查看 AI Lab Release Notes](../baize/intro/release-notes.md)

-   :fontawesome-brands-edge:{ .lg .middle } __云边协同__

    ---

    - 支持 CSI 存储标准
    - 边端节点支持轻量级 Pod 运维能力（查看和重启 Pod）
    - kantadm 支持前置容器运行时初始化

    [:octicons-arrow-right-24: 查看云边协同 Release Notes](../kant/intro/release-notes.md)

-   :fontawesome-solid-user-group:{ .lg .middle } __全局管理__

    ---

    - 公有云模式中，在文件夹下创建用户
    - 构建新版本 License Secret 体系

    [:octicons-arrow-right-24: 查看全局管理 Release Notes](../ghippo/intro/release-notes.md)

</div>

![roadmap](./images/roadmap.jpg)
