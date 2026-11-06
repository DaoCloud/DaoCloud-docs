---
hide:
  - toc
---

# What is Intelligent Q&A

The d.run Intelligent Q&A (AI App) product is an intelligent conversation solution built on **RAG (Retrieval-Augmented Generation)** technology.
It first vectorizes your dedicated corpus, precisely retrieves content relevant to a question through **similarity search**, and then generates natural, fluent answers with a
**large language model (LLM)**. This approach significantly reduces model hallucination while protecting the security of private data, providing you with more accurate and personalized responses.

Whether for online customer service, knowledge management, or internal knowledge retrieval, d.run Intelligent Q&A helps you quickly build an **efficient, trustworthy, and controllable** AI knowledge service system.

## Key Capabilities

<div class="grid cards" markdown>

- :material-application-brackets-outline:{ .lg .middle } __Apps and Plugins__

    ---

    Manage the full lifecycle of intelligent Q&A apps, with corpus association, app secrets, and link sharing, and extend corpus processing by developing sharding plugins.

    [:arrow_forward: Create an app](user-guide/app-center/create-app.md)

- :material-library-outline:{ .lg .middle } __Corpus Management__

    ---

    Build your dedicated corpus through file import, formatted import, manual entry, image-text import, and more. Chunks are split automatically by separator or size, and access levels can be set to ensure data security and isolation.

    [:arrow_forward: Create a corpus](user-guide/corpus/create-corpus.md)

- :material-chat-processing-outline:{ .lg .middle } __Intelligent Conversation__

    ---

    Context-aware Q&A with rating, copying, regeneration, translation, and multi-language answers, as well as combined apps for intent recognition.

    [:arrow_forward: Conversation guide](user-guide/app-center/conversation.md)

- :material-cog-outline:{ .lg .middle } __System Configuration__

    ---

    Centrally manage model services, retrieval strategies, and other platform-level settings to improve answer quality.

    [:arrow_forward: System configuration](user-guide/system-config.md)

- :material-chart-box-outline:{ .lg .middle } __Data Analysis__

    ---

    Gain insight into app performance through Q&A counts, Q&A quality, chunk hit ratio, and chunk quality metrics, and continuously improve your corpus and answer quality.

    [:arrow_forward: View Q&A quality](data-analysis/qa-quality.md)

- :material-message-draw:{ .lg .middle } __My Feedback__

    ---

    Submit ratings and improvement suggestions at any time to help polish the product experience.

    [:arrow_forward: Submit feedback](my-feedback/my-feedback.md)

</div>

## Workflow

Using d.run Intelligent Q&A involves two stages: **knowledge and app building** and **usage and continuous optimization**. First import your dedicated corpus and create an app; once the app is published it can serve intelligent Q&A, and data analysis and user feedback help you continuously improve the corpus and app configuration.

```mermaid
flowchart LR
    subgraph BUILD["Knowledge & App Building"]
        direction LR
        A["① Create a corpus<br/>Files · FAQ · manual entry"] --> B["② Create an app<br/>Corpus · model"]
    end
    subgraph USE["Usage & Optimization"]
        direction LR
        C["③ Conversation<br/>Context · multi-language"] --> D["④ Data analysis<br/>Q&A quality · hit ratio"]
    end
    B -->|Publish the app| C
    D -->|Improve corpus & settings| A
    click A href "user-guide/corpus/create-corpus/"
    click B href "user-guide/app-center/create-app/"
    click C href "user-guide/app-center/conversation/"
    click D href "data-analysis/qa-quality/"
```

| Step | Role | Description |
| ---- | ---- | ----------- |
| [① Create a corpus](user-guide/corpus/create-corpus.md) | Knowledge Administrator | Build a dedicated corpus through file import, formatted import, manual entry, image-text import, and more |
| [② Create an app](user-guide/app-center/create-app.md) | App Administrator | Create an app, associate a corpus, and select model services, with app secrets and link sharing |
| [③ Conversation](user-guide/app-center/conversation.md) | Business User | Ask questions in the chat window, with context, regeneration, translation, and multi-language answers |
| [④ Data analysis](data-analysis/qa-quality.md) | App Administrator | Continuously improve the corpus and app configuration through Q&A quality and chunk hit ratio metrics |

## Quick Start

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
    <span class="dak-path-title">Create a corpus</span>
    <span class="dak-path-desc">Import docs · FAQ · manual entry</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#00acc1" href="user-guide/app-center/create-app/">
    <span class="dak-path-num">2</span>
    <span class="dak-path-title">Create an app</span>
    <span class="dak-path-desc">Corpus association · model</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#43a047" href="user-guide/app-center/conversation/">
    <span class="dak-path-num">3</span>
    <span class="dak-path-title">Conversation</span>
    <span class="dak-path-desc">Context-aware Q&A · multi-language</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#fb8c00" href="my-feedback/my-feedback/">
    <span class="dak-path-num">4</span>
    <span class="dak-path-title">My Feedback</span>
    <span class="dak-path-desc">Ratings and suggestions</span>
    <span class="dak-path-go">Go →</span>
  </a>
  <a class="dak-path-step" style="--path-c:#8e24aa" href="data-analysis/qa-quality/">
    <span class="dak-path-num">5</span>
    <span class="dak-path-title">Data Analysis</span>
    <span class="dak-path-desc">Q&A quality · hit ratio</span>
    <span class="dak-path-go">Go →</span>
  </a>
</div>

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Features__

    ---

    A complete list of Intelligent Q&A features across conversation, App Center, and corpus management.

    [:arrow_forward: View features](features.md)

- :material-comment-quote-outline:{ .lg .middle } __Improvement Suggestions__

    ---

    Review aggregated user feedback and improvement suggestions to understand the product roadmap.

    [:arrow_forward: View suggestions](data-analysis/suggestions.md)

- :material-file-document-outline:{ .lg .middle } __AI App Manual__

    ---

    View or download the complete AI App user manual (PDF).

    [:arrow_forward: View the manual](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/dak.pdf)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button .md-button--primary }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button .md-button--primary }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button .md-button--primary }
