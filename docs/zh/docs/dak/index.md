---
hide:
  - toc
---

# 什么是 AI 应用

d.run 智能问答（AI 应用）是基于 **RAG（Retrieval-Augmented Generation，检索增强生成）** 技术的智能对话产品。
它会先将您的专属语料库进行 **向量化处理**，并通过 **相似度搜索** 精准检索与问题相关的内容，再由
**大语言模型（LLM）** 生成自然流畅的答案。这种方式不仅显著减少了模型的“幻觉”现象，还能在保障
**隐私数据安全** 的同时，为您提供更精准、更个性化的回复。

无论是在线客服、知识管理，还是内部知识检索，d.run 智能问答都能帮助您快速构建 **高效、可信、可控** 的 AI 知识服务体系。

![应用中心](./images/app-center.jpg)

## 核心能力

<div class="grid cards" markdown>

- :material-application-brackets-outline:{ .lg .middle } __应用与插件__

    ---

    创建并管理智能问答应用的全生命周期，支持关联语料库、应用密钥、链接分享，并可开发分片插件扩展语料处理能力。

    [:arrow_forward: 创建应用](user-guide/app-center/create-app.md)

- :material-library-outline:{ .lg .middle } __语料库管理__

    ---

    支持文件导入、格式化导入、手工录入、图文导入等多种方式构建专属语料库，按分隔符或大小智能分片，并可设置访问级别保障数据安全与隔离。

    [:arrow_forward: 创建语料库](user-guide/corpus/create-corpus.md)

- :material-chat-processing-outline:{ .lg .middle } __智能对话__

    ---

    上下文感知的智能问答，支持评价、复制、重新生成、翻译与多语言回答，并支持组合应用进行意图识别。

    [:arrow_forward: 应用对话说明](user-guide/app-center/conversation.md)

- :material-cog-outline:{ .lg .middle } __系统配置__

    ---

    集中管理模型服务、检索策略等平台级配置，优化 AI 回答质量。

    [:arrow_forward: 系统配置](user-guide/system-config.md)

- :material-chart-box-outline:{ .lg .middle } __数据分析__

    ---

    通过问答次数、问答质量、分片命中率、分片质量等指标洞察应用运行状况，持续改进语料与问答质量。

    [:arrow_forward: 查看问答质量](data-analysis/qa-quality.md)

- :material-message-draw:{ .lg .middle } __我的反馈__

    ---

    在使用过程中随时提交评价与改进意见，帮助产品持续打磨体验。

    [:arrow_forward: 提交反馈](my-feedback/my-feedback.md)

</div>

## 使用流程

d.run 智能问答的使用分为 **知识与应用构建** 与 **使用与持续优化** 两个阶段：先导入专属语料并创建应用，应用发布后即可对外提供智能问答服务，再通过数据分析与用户反馈不断优化语料与应用配置。

```mermaid
flowchart LR
    subgraph BUILD["知识与应用构建"]
        direction LR
        A["① 创建语料库<br/>文件 · FAQ · 手工录入"] --> B["② 创建应用<br/>关联语料库 · 选择模型"]
    end
    subgraph USE["使用与持续优化"]
        direction LR
        C["③ 应用对话<br/>上下文 · 多语言"] --> D["④ 数据分析<br/>问答质量 · 命中率"]
    end
    B -->|发布应用| C
    D -->|优化语料与配置| A

    click A href "user-guide/corpus/create-corpus/"
    click B href "user-guide/app-center/create-app/"
    click C href "user-guide/app-center/conversation/"
    click D href "data-analysis/qa-quality/"
```

| 步骤 | 角色 | 说明 |
| --- | --- | --- |
| [① 创建语料库](user-guide/corpus/create-corpus.md) | 知识管理员 | 通过文件导入、格式化导入、手工录入、图文导入等方式构建专属语料库 |
| [② 创建应用](user-guide/app-center/create-app.md) | 应用管理员 | 创建应用并关联语料库、选择模型服务，支持应用密钥与链接分享 |
| [③ 应用对话](user-guide/app-center/conversation.md) | 业务用户 | 在对话窗口提问，支持上下文、重新生成、翻译与多语言回答 |
| [④ 数据分析](data-analysis/qa-quality.md) | 应用管理员 | 通过问答质量、分片命中率等指标持续优化语料与应用配置 |

## 快速上手

<style>
.dak-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.dak-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.dak-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.dak-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.dak-path-step:last-child::after{display:none}
.dak-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.dak-path-title{font-weight:700;font-size:0.95rem}
.dak-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.dak-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.dak-path-step::after{display:none}}
</style>

<div class="dak-path">
  <a class="dak-path-step" style="--path-c:#2196f3" href="user-guide/corpus/create-corpus/">
    <span class="dak-path-num">1</span>
    <span class="dak-path-title">创建语料库</span>
    <span class="dak-path-desc">导入文档 · FAQ · 手工录入</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#00acc1" href="user-guide/app-center/create-app/">
    <span class="dak-path-num">2</span>
    <span class="dak-path-title">创建应用</span>
    <span class="dak-path-desc">关联语料库 · 选择模型</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#43a047" href="user-guide/app-center/conversation/">
    <span class="dak-path-num">3</span>
    <span class="dak-path-title">应用对话</span>
    <span class="dak-path-desc">上下文问答 · 多语言</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#fb8c00" href="my-feedback/my-feedback/">
    <span class="dak-path-num">4</span>
    <span class="dak-path-title">我的反馈</span>
    <span class="dak-path-desc">提交评价与改进意见</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#8e24aa" href="data-analysis/qa-quality/">
    <span class="dak-path-num">5</span>
    <span class="dak-path-title">数据分析</span>
    <span class="dak-path-desc">问答质量 · 命中率</span>
    <span class="dak-path-go">Go →</span>
  </a>
</div>

## 更多资源

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __功能特性__

    ---

    一览智能问答在对话功能、应用中心与语料库管理上的完整功能清单。

    [:arrow_forward: 查看功能特性](features.md)

- :material-puzzle-outline:{ .lg .middle } __分片插件__

    ---

    了解分片插件的实现原理与集成方式，自定义语料分片逻辑。

    [:arrow_forward: 查看分片插件指南](user-guide/plugins/create-plugin.md)

- :material-comment-quote-outline:{ .lg .middle } __改进意见__

    ---

    查看用户反馈与改进建议的汇总分析，了解产品优化方向。

    [:arrow_forward: 查看改进意见](data-analysis/suggestions.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
[查看 AI 应用手册 PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/dak.pdf){ .md-button .md-button--primary }
