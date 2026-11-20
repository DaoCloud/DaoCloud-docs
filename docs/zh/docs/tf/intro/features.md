---
hide:
  - toc
---

# Token 工厂效能平台功能特性

本平台覆盖 Token 工厂的生产与运营流程，按角色提供操作入口和数据视图，支持业务使用、服务管理、生产运维和经营分析。

<div class="grid cards" markdown>

- :material-account-outline:{ .lg .middle } __业务用户__

    ---

    在模型广场试用并调用模型，一键部署专属推理服务，使用 AI 应用和 GPU 实例，随时查看自己的用量与消费记录。

- :material-cog-outline:{ .lg .middle } __服务管理员__

    ---

    负责模型上下架和服务接入，配置调用规则、路由策略和内容安全策略，并为不同团队分配访问权限。

</div>

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __运维人员__

    ---

    管理基础设施和资源调度，部署高性能推理服务，实时监测服务性能，及时处理告警与运行故障。

- :material-chart-box-outline:{ .lg .middle } __经营人员__

    ---

    分析产能、客户用量与消费、收入与成本及资金使用情况，开展预算管理和投资测算，让每一度算力都算得清、赚得到。

</div>

## 功能特性

| 分类 | 模块 | 功能特性 | 说明 |
| :--- | :--- | :--- | :--- |
| 云原生 AI | [模型服务](../hydra/intro/index.md) | [模型体验与选型](../hydra/exp.md) | 在模型广场查找文本生成、图片理解、图像生成等模型，选择适合业务的模型。通过在线试用和对比多个模型，在接入业务前检查回答效果 |
| | | [模型部署](../hydra/deploy/index.md) | 将主流开源、自研的模型部署为专属推理服务，并查看服务运行状态。支持采用多机多卡的分布式部署 |
| | | [API 接入](../hydra/api-call.md) | 提供 OpenAI 兼容 API 和调用示例，支持 Cherry Studio、Cline、LobeChat、Bob 等客户端，方便业务系统和开发工具调用模型 |
| | | [API Key 管理](../hydra/apikey.md) | 创建和管理调用密钥，控制应用对模型服务的访问权限 |
| | | [用量统计](../hydra/usage.md) | 按模型、API Key 和时间查看调用与 Token 消耗，了解各应用的使用情况，为预算管理和应用调整提供依据 |
| | [服务管理与 Token 治理](../hydra/intro/index.md) | [模型上下架](../hydra/models/model-manage.md) | 支持模型导入、创建、发布和下线，管理向用户开放的模型目录 |
| | | [MaaS 服务接入](../hydra/oam/maas.md) | 接入自建服务或上游模型 API，由平台统一向用户提供调用入口 |
| | | [智能路由](../hydra/oam/auto-route.md) | 通过路由、负载均衡和备用路径分配请求，提高服务可用性 |
| | | 调用限流 | 支持全局、租户和 API Key 等层级的流量限制，减少突发请求对共享服务的影响 |
| | | [内容安全](../hydra/oam/security-policy.md) | 通过敏感词检测、正则匹配、接入安全模型等内容策略，管理模型调用中的内容风险 |
| | | 分析中心 | 按模型、租户统计输入和输出 Token 用量，分析收入、成本及毛利的变化趋势 |
| | [推理加速服务](../inferx/index.md) | 高性能模型部署 | 在 NVIDIA 及多种国产算力上结合主流推理框架部署高性能推理服务，支持多机多卡和 P/D 分离，按预填充与解码的不同特点规划资源 |
| | | KV 缓存复用 | 通过 KV Cache 卸载及 Redhare 分层缓存复用重复前缀计算，结合本地与远端内存、存储资源扩大缓存空间，减少长上下文和多轮任务中的重复计算 |
| | | 优选模板库 | 围绕 vLLM、SGLang 及 LLM\-D、Dynamo 等主流推理引擎分布式编排框架，提供丰富的优选部署模板，缓解吞吐、显存及延迟瓶颈 |
| | | 模型验收测试 | 上线前验证模型 API 兼容性、功能与性能，使优化结果同时满足模型效果和服务质量要求，作为上线服务标准 |
| | | 服务观测 | 关联服务吞吐、P/D 队列、缓存命中、GPU 和网络指标，区分请求增长、计算不足、缓存及通信问题，为持续性模型性能优化与排障提供依据 |
| | [算力云](../zestu/index.md) | [实例管理](../zestu/instance.md) | 根据 GPU 需求选择实例规格创建实例，按任务需要管理运行资源 |
| | | [开发访问](../zestu/instance/jupyter.md) | 通过 JupyterLab、SSH 或 VS Code 访问实例，进行代码调试、算法实验和服务部署 |
| | | [付费方式](../zestu/instance-prepaid.md) | 支持按量付费或包年包月，分别满足短期实验和长期运行需要 |
| | [AI 应用](../dak/index.md) | [知识问答](../dak/user-guide/app-center/create-app.md) | 结合企业知识和对话上下文回答问题，支持回答评价与反馈 |
| | | 应用接入 | 通过应用链接、H5 页面使用服务，或通过 OpenAPI 接入业务系统 |
| 云原生底座 | [GPU 资源与调度](../kpanda/intro/index.md) | [异构 GPU 纳管](../kpanda/user-guide/gpu/index.md) | 统一识别和管理 NVIDIA GPU 及昇腾等国产 AI 加速设备，支持在同一集群中管理和调度不同卡型，适应多种硬件并存的算力环境 |
| | | [GPU 共享](../kpanda/user-guide/gpu/vgpu_quota.md) | 支持整卡、vGPU、MIG 等资源使用方式。在适用硬件上按显存或算力分配额度，让多个任务共享 GPU，减少资源闲置 |
| | | [AI 任务与服务调度](../kpanda/user-guide/gpu/volcano/volcano-gang-scheduler.md) | 结合任务的 GPU 需求和节点拓扑分配资源，支持 Gang 调度、拓扑感知调度等调度模式，支持多节点推理，满足不同规模模型的运行需求 |
| | [网络与存储](../network/intro/index.md) | 容器网络 | 通过多 CNI、Multus、SpiderPool 等组件配置网络，使用 IP 池管理地址分配 |
| | | 高性能通信 | 通过相应 RDMA 配置，满足 AI 任务对低延迟、高带宽通信的需求 |
| | | [持久化存储](../storage/index.md) | 通过 CSI 接入已有存储或云原生本地存储，为模型文件、数据集和有状态服务提供持久化卷 |
| 运营管理 | [驾驶舱](../crane/intro/index.md) | [产能与计费转化分析](../crane/user-guide/singlepage.md) | 对比可供给产能、实际产出和计费 Token，分析算力利用情况及产出向计费消费的转化 |
| | | 客户与模型分析 | 结合客户用量、收入贡献、消费集中度和模型排行，分析消费结构及不同模型的经营表现 |
| | | [成本效率比较](../crane/user-guide/finops.md) | 比较不同 GPU 型号的利用率、单卡产出和单位 Token 成本，评估资源和模型的运行效率。收益分析需使用完整的成本与消费数据 |
| | | [生产状态分析](../crane/user-guide/production-operations.md) | 查看吞吐、首 Token 延迟（TTFT）、每 Token 生成延迟（TPOT）、队列、GPU 池和 SLA。结合告警、调度及扩缩容事件，分析指标变化的原因 |
| | [Copilot 智能工作台](../copilot/index.md) | 平台信息查询 | 结合资源、服务、监控和消费数据回答问题，减少人工切换页面、收集信息的工作 |
| | | 问题分析 | 针对容量、性能、成本和运行异常分析可能原因，比较处理方案，列出还需核实的条件 |
| | | 投资测算 | 根据设备、吞吐、价格、负载和成本，计算年收入、净现金流及静态回本期，比较不同经营条件，并保留假设和数据来源 |
| | [费用中心](../leopard/index.md) | [计费与订单](../leopard/orders.md) | 按商品用量和规则计费，支持按量或周期付费，区分普通输入、输出和缓存 Token；记录服务购买及资源变更 |
| | | [账单与收支](../leopard/bills.md) | 支持按账号、产品、区域和账期汇总、筛选及导出账单，记录余额变化，方便消费对账与资金核对 |
| | | [账户与额度](../leopard/credit_limit.md) | 支持账户充值、余额提醒和主子账号资金共享，可为子账号分配使用额度，控制预算 |
| | | [优惠与奖励](../leopard/voucher.md) | 按活动规则记录邀请进度、发放代金券，并按有效期和适用范围抵扣消费，不足部分扣除现金余额 |
| 运维管理 | [可观测性](../insight/intro/index.md) | 推理性能监测 | 关注请求吞吐、首 Token 延迟（TTFT）、每 Token 生成延迟（TPOT）和请求错误，了解服务响应速度及稳定性 |
| | | GPU 资源监测 | 结合 GPU 利用率、显存占用及节点资源，分析推理负载与资源使用情况，为容量调整和性能优化提供依据 |
| | | 推理故障定位 | 关联请求链路、服务日志、资源指标和运行事件，排查请求变慢、调用失败及服务异常的原因 |
| | | [告警管理](../insight/user-guide/alert-center/index.md) | 针对服务延迟、错误及资源异常提供告警和通知，提醒运维人员及时处理服务故障 |
| | [全局管理](../ghippo/intro/index.md) | [身份与权限管理](../ghippo/user-guide/access-control/index.md) | 支持本地账号及 LDAP、OIDC、OAuth 2.0 等外部身份源，通过用户组、角色和工作空间分配权限，隔离不同用户的资源 |
| | | [平台治理与设置](../ghippo/user-guide/platform-setting/index.md) | 记录关键操作，支持安全审计与责任追溯，统一配置会话、密码策略、通知服务及平台外观 |
