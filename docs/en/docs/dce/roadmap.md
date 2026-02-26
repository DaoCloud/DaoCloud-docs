---
hide:
  - toc
---

# DCE Product Roadmap

!!! note "Disclaimer"

    This roadmap reflects current planning directions. Features and timelines are subject to change. Refer to release notes for confirmed deliverables.

<style>
.roadmap-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid var(--md-default-fg-color--lightest);
  overflow: hidden;
  line-height: 1.6;
}
.roadmap-table thead th {
  background: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
  padding: 12px 16px;
  font-weight: 600;
  border: none;
  text-align: left;
}
.roadmap-table thead th:first-child {
  text-align: center;
  width: 64px;
}
.roadmap-table tbody td {
  vertical-align: top;
  padding: 14px 16px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  border-right: 1px solid var(--md-default-fg-color--lightest);
}
.roadmap-table tbody td:last-child {
  border-right: none;
}
.roadmap-table tbody tr:last-child td {
  border-bottom: none;
}
.roadmap-table .cat-label {
  font-weight: 700;
  text-align: center;
  letter-spacing: 2px;
  border-left-width: 4px;
  border-left-style: solid;
  background: var(--md-default-bg-color--light);
  border-right: 1px solid var(--md-default-fg-color--lightest);
}
.roadmap-table .cat-ai    { border-left-color: #00b267; color: #00894f; }
.roadmap-table .cat-infra { border-left-color: #2ecc71; color: #1fa85a; }
.roadmap-table .cat-plat  { border-left-color: #66d99a; color: #3cb371; }
.roadmap-table .cat-eco   { border-left-color: #a3e4be; color: #5dba8a; }
.roadmap-table ul {
  margin: 0;
  padding-left: 16px;
}
.roadmap-table li {
  margin-bottom: 4px;
}
.roadmap-table li::marker {
  color: var(--md-default-fg-color--lighter);
}
.roadmap-table a {
  color: var(--md-typeset-a-color);
  text-decoration: none;
  border-bottom: 1px dashed var(--md-accent-fg-color);
}
.roadmap-table a:hover {
  color: var(--md-accent-fg-color);
}
.roadmap-table mark {
  background: var(--md-accent-fg-color--transparent);
  color: inherit;
  padding: 1px 4px;
  border-radius: 3px;
}
.roadmap-table sup a {
  border-bottom: none;
  font-weight: 600;
  color: var(--md-accent-fg-color);
}
</style>

<table class="roadmap-table">
<thead>
<tr>
<th></th>
<th>H1 2026</th>
<th>H2 2026</th>
<th>2027+</th>
</tr>
</thead>
<tbody>
<tr>
<td class="cat-label cat-ai">AI</td>
<td><ul>
<li>Inference runtime integration (vLLM/SGLang), domestic GPU support</li>
<li>Model asset center MVP (user/project/repo management, model & dataset upload/download, CLI)</li>
<li>Pre-integrated domestic model repos (Qwen/GLM/Baichuan)</li>
<li>Inference acceleration: multi-level KV Cache, topology-aware scheduling (<a href="https://kueue.sigs.k8s.io/">Kueue</a>/Gang)</li>
<li>Training-inference co-location basics</li>
<li>AI fault diagnosis (multi-source log correlation + root cause analysis)</li>
<li>Predictive alerting (time-series anomaly detection, resource exhaustion warnings)</li>
</ul></td>
<td><ul>
<li><mark>DCE AI Runtime GA</mark></li>
<li>Unified inference API (OpenAI API/Llama Stack compatible)</li>
<li>Fine-tuning/LoRA support</li>
<li>Multi-modal inference (text-image, audio-video)</li>
<li>Model asset center enhancements (remote replication/sync, security scanning, pre-warming, i18n)</li>
<li><a href="https://github.com/matrixhub-ai/matrixhub">MatrixHub</a> CNCF submission<sup><a href="#fn-matrixhub">1</a></sup></li>
<li>AI Agent infrastructure Beta (sandbox, memory & context, semantic routing)</li>
<li>Fault self-healing (integrated training/inference framework auto-recovery)</li>
<li>Alert noise reduction (automatic correlated alert grouping)</li>
<li>LLM security (model access control, inference content safety policies)</li>
</ul></td>
<td><ul>
<li>Distributed inference</li>
<li>Training-inference co-location optimization</li>
<li>Full-stack AI automation (AutoML + Agent)</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-infra">Infra</td>
<td><ul>
<li><mark>MetaX GPU onboarding</mark> (network topology, Lustre GDS)</li>
<li>Ascend 910C NPU scheduling (CANN driver)</li>
<li>Hygon DCU GPU scheduling</li>
<li>AI high-performance storage (Lustre file system)</li>
<li>Kueue/Gang Scheduling/<a href="https://lws.sigs.k8s.io/">LWS</a>/DRA integration</li>
<li><a href="https://github.com/Project-HAMi/HAMi">HAMi</a> commercial edition integration<sup><a href="#fn-hami">2</a></sup></li>
<li>containerd enhancements (container disk limits)</li>
</ul></td>
<td><ul>
<li><mark>Domestic GPU full GA</mark> (MetaX/Ascend/Hygon/Biren)</li>
<li>MetaX supernode release</li>
<li>Supernode solution (8/16-card high-density, GPU sharing scheduler)</li>
<li>GPU Operator hybrid scheduling (CPU + GPU + NPU), utilization → 80%+</li>
<li>Distributed storage solution (cloud scenarios)</li>
</ul></td>
<td><ul>
<li>DPU/NPU unified scheduling</li>
<li>Computing network, multi-cluster compute federation</li>
<li>InfiniBand topology discovery (via UFM)</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-plat">Plat</td>
<td><ul>
<li>One-click install (Web UI + CLI, auto environment detection)</li>
<li>Preflight check framework (plugin-based, network/storage/permission checks)</li>
<li><a href="https://gateway-api.sigs.k8s.io/">Gateway API</a> migration start (Ingress retirement)</li>
<li>Log aggregation enhancements</li>
<li>Compute cloud operations platform admin console</li>
<li>Compute baseline review & billing model optimization</li>
<li>Ghippo admin console UI</li>
<li>CSP user two-factor authentication (2FA)</li>
</ul></td>
<td><ul>
<li>Rolling upgrades (zero-downtime, canary + rollback)</li>
<li><mark>Gateway API migration complete</mark></li>
<li>Deployment time → 15 min (from ~2 hours)</li>
<li>Compute cloud platform enhancements (tenant isolation, inventory management, billing conversion, GPU up/downgrade)</li>
<li>Bare-metal deployer (cluster provisioning, automated testing, single-node troubleshooting)</li>
</ul></td>
<td><ul>
<li>Lightweight kernel, edge-native</li>
<li>Self-adaptive platform (auto-tuning + self-healing)</li>
</ul></td>
</tr>
<tr>
<td class="cat-label cat-eco">Eco</td>
<td><ul>
<li>Kueue/LWS/Gang Scheduling K8s AI/ML SIG contributions</li>
<li><a href="https://github.com/spidernet-io/spiderpool">Spiderpool</a> DRA implementation, DRANet</li>
<li>Spiderpool MetaX GPU support</li>
<li>GAIE/NIXL/LMCache inference optimization project participation</li>
</ul></td>
<td><ul>
<li>MatrixHub Sandbox</li>
<li><a href="https://github.com/DaoCloud/unifabric">unifabric</a> 1.0 (network health check, disaster marking, KV Cache sync monitoring)</li>
<li>metal-deployer engineering delivery</li>
<li>GAIE/NIXL community seats</li>
</ul></td>
<td><ul>
<li>unifabric Sandbox, InfiniBand support</li>
<li>Low-code orchestration, natural language operations</li>
</ul></td>
</tr>
</tbody>
</table>

<small>

<span id="fn-matrixhub">**[1]** MatrixHub — DaoCloud's open-source model asset center, aiming to be for AI models what Harbor is for container images.</span>
<br>
<span id="fn-hami">**[2]** HAMi — Heterogeneous AI computing middleware for GPU sharing and isolation.</span>

</small>

---

## Strategic Direction

DCE already includes [AI Lab](../baize/intro/index.md) (training) and [LLM Studio](../hydra/intro/index.md) (model management & inference). In 2026, we focus on two priorities:

1. **AI Deepening** — Complete enterprise inference scenarios, support domestic GPUs, bridge training to inference
2. **Platform Deepening** — Operations experience, deployment efficiency, compute management — solidify existing capabilities

---

## DCE 5.0 Existing Capabilities

All modules can be upgraded independently without platform-wide downtime.

| Module | Capabilities | Docs |
|--------|-------------|------|
| **Container Management** | Multi-cluster management, cluster lifecycle, auto-scaling, Helm apps | [:material-book-open-outline:](../kpanda/intro/index.md) |
| **Workbench** | CI/CD pipelines, GitOps, canary releases | [:material-book-open-outline:](../amamba/intro/index.md) |
| **Multicloud Management** | Cross-cloud resource scheduling & app orchestration | [:material-book-open-outline:](../kairship/intro/index.md) |
| **Microservice Engine** | Spring Cloud/Dubbo management | [:material-book-open-outline:](../skoala/intro/index.md) |
| **Service Mesh** | Istio-based traffic governance & observability | [:material-book-open-outline:](../mspider/intro/index.md) |
| **Cloud Native Networking** | Multi-CNI, network policies, load balancing | [:material-book-open-outline:](../network/intro/index.md) |
| **Cloud Native Storage** | CSI standard, HwameiStor, multi-backend storage | [:material-book-open-outline:](../storage/index.md) |
| **Insight** | Metrics/logs/traces multi-dimensional alerting | [:material-book-open-outline:](../insight/intro/index.md) |
| **Middleware** | Redis, MySQL, Kafka, ElasticSearch, and PostgreSQL lifecycle management | [:material-book-open-outline:](../middleware/index.md) |
| **Container Registry** | Multi-instance management, Harbor compatible | [:material-book-open-outline:](../kangaroo/intro/index.md) |
| **Global Management** | Authentication, multi-tenancy, RBAC, audit | [:material-book-open-outline:](../ghippo/intro/index.md) |
| **Virtual Machines** | KubeVirt, VM management, snapshots, live migration | [:material-book-open-outline:](../virtnest/intro/index.md) |
| **AI Lab** | Training & inference, PyTorch/TensorFlow | [:material-book-open-outline:](../baize/intro/index.md) |
| **LLM Studio** | LLM deployment & operations, vLLM/SGLang | [:material-book-open-outline:](../hydra/intro/index.md) |
| **Cloud Edge Collaboration** | Edge clusters and nodes management | [:material-book-open-outline:](../kant/intro/index.md) |

---

## Operational Assurance

| Category | Details |
|----------|---------|
| **High Availability** | Multi-replica control plane + etcd cluster, auto-recovery on node failure |
| **Data Backup** | etcd snapshots, app-level backup (Velero), cross-cluster disaster recovery |
| **Offline Operation** | Fully offline deployment and operation, no external network dependency |
| **Upgrade Rollback** | One-click rollback for all version upgrades |
| **Security & Compliance** | MLPS Level 3, audit logs, image scanning, model access control |
| **Identity** | LDAP/OIDC/enterprise identity platform integration |
| **Technical Support** | [Documentation](https://docs.daocloud.io) + training certification + TAM + 7×24 emergency response |

---

## Ecosystem & Partnerships

**Open Source Contributions:** TOP 1 in China and TOP 3 globally for Kubernetes core repository contributions. Active in Istio/Cilium/[Spiderpool](https://github.com/spidernet-io/spiderpool)/[HwameiStor](https://hwameistor.io) and other CNCF projects. Active contributors to Kueue/LWS/Gang Scheduling and other K8s AI/ML SIG projects.

| Area | Partners |
|------|----------|
| Chips & Compute | Huawei Ascend, Hygon, Biren, MetaX, NVIDIA |
| Operating Systems | Kylin, UnionTech UOS |
| Databases & Middleware | DMDB, OceanBase, TiDB |

**Industry Coverage:** Finance · Manufacturing · Energy · Telecom · Government — serving 500+ enterprise customers.
