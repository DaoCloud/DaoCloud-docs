---
hide:
  - toc
---

# d.run AI 操作系统

d.run 依托全球前三的 Kubernetes 调度技术与 vLLM 等主流开源推理引擎核心贡献积淀，统一纳管多元异构算力，
实现颗粒化调度、全栈推理优化与全链路 Token 治理，算力利用率超 80%，将算力高效转化为可管可控的 Token 化 AI 生产力；
平台汇聚全球主流大模型生态，配备可视化运营驾驶舱与 d.run Copilot 智能助手，面向企业全部门输出稳定高效的 AI 服务，
全方位支撑业务智能化长期升级。

<style>
.tf-arch-card{min-width:calc(25% - 6px) !important}
.tf-arch{overflow:visible !important}
.tf-arch-card{overflow:visible !important}
.tf-arch-card::after{display:none !important}
.tf-arch-layer:first-child{border-radius:14px 14px 0 0 !important}
.tf-arch-layer:last-child{border-radius:0 0 14px 14px !important}
.tf-arch-card-tip{
  opacity:0;
  position:absolute;
  bottom:calc(100% + 8px);
  left:50%;
  transform:translateX(-50%);
  background:rgba(0,0,0,0.85);
  color:#fff;
  padding:0.35rem 0.65rem;
  border-radius:6px;
  font-size:0.72rem;
  font-weight:500;
  white-space:nowrap;
  z-index:100;
  pointer-events:none;
  box-shadow:0 4px 12px rgba(0,0,0,0.2);
  transition:opacity 0.2s ease
}
.tf-arch-card-tip::after{
  content:"";
  position:absolute;
  top:100%;
  left:50%;
  transform:translateX(-50%);
  border:5px solid transparent;
  border-top-color:rgba(0,0,0,0.85)
}
.tf-arch-card:hover .tf-arch-card-tip{
  opacity:1
}
</style>

<div class="tf-arch tf-arch--compact">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">云原生 AI</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="hydra/intro/">
        <span class="tf-arch-card-title">大模型服务平台</span>
        <span class="tf-arch-card-tip">模型部署与运维管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="baize/intro/">
        <span class="tf-arch-card-title">AI Lab</span>
        <span class="tf-arch-card-tip">云原生训推一体化</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">推理加速</span>
        <span class="tf-arch-card-tip">推理加速与引擎管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
        <span class="tf-arch-card-title">ClawOS</span>
        <span class="tf-arch-card-tip">多智能体运行与治理</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">云原生底座</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
        <span class="tf-arch-card-title">容器管理</span>
        <span class="tf-arch-card-tip">集群与工作负载管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
        <span class="tf-arch-card-title">镜像仓库</span>
        <span class="tf-arch-card-tip">镜像托管与集成</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
        <span class="tf-arch-card-title">设备管理</span>
        <span class="tf-arch-card-tip">硬件设备统一纳管</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="network/intro/">
        <span class="tf-arch-card-title">云原生网络</span>
        <span class="tf-arch-card-tip">多 CNI 融合网络</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="storage/">
        <span class="tf-arch-card-title">云原生存储</span>
        <span class="tf-arch-card-tip">容器化存储与 CSI</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">运营管理</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="copilot/">
        <span class="tf-arch-card-title">Copilot</span>
        <span class="tf-arch-card-tip">智能运维助手</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="crane/intro/">
        <span class="tf-arch-card-title">驾驶舱</span>
        <span class="tf-arch-card-tip">运营数据可视化</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">运维管理</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="insight/intro/">
        <span class="tf-arch-card-title">可观测性</span>
        <span class="tf-arch-card-tip">指标日志链路观测</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
        <span class="tf-arch-card-title">全局管理</span>
        <span class="tf-arch-card-tip">用户权限与平台设置</span>
      </a>
    </div>
  </div>
</div>

作为面向企业输出的 AI 操作系统，d.run 将算力调度、大模型推理与运营治理融为一体。
平台统一纳管英伟达及国产异构算力，依靠颗粒化调度与全栈推理优化，把分散 GPU 算力转化为低成本、高稳定的 Token 服务；
配备可视化运营驾驶舱，实时呈现算力消耗、模型调用与 Token 产出全链路数据；
内置 d.run Copilot 智能助手，降低企业全部门使用 AI 的门槛，推动业务智能化长期升级。

![d.run AI 操作系统全景图](images/drun-modules.svg)

## 客户成功故事

<style>
/* 客户成功故事卡片 */
.md-typeset .story-marquee{display:grid;margin:1.2rem 0 2rem;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.md-typeset .story-track{display:flex;width:max-content;animation:story-move 46s linear infinite}
.md-typeset .story-marquee:hover .story-track{animation-play-state:paused}
.md-typeset .story-group{display:flex;gap:1rem;padding-right:1rem;align-items:stretch}
.md-typeset .story-card{width:330px;flex:none;display:flex;flex-direction:column;border-radius:12px;overflow:hidden;border:1px solid var(--md-default-fg-color--lightest);background:var(--md-default-bg-color);transition:transform .2s ease,border-color .2s ease}
.md-typeset .story-card:hover{transform:translateY(-3px);border-color:var(--s1)}
.md-typeset .story-card-top{display:flex;align-items:center;justify-content:space-between;gap:.5rem;height:62px;padding:0 .9rem;background:linear-gradient(120deg,var(--s1),var(--s2))}
.md-typeset .story-card-high{font-size:.78rem;font-weight:600;color:rgba(255,255,255,.95);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.md-typeset .story-card-ind{font-size:.62rem;color:rgba(255,255,255,.92);background:rgba(255,255,255,.18);padding:.14rem .55rem;border-radius:999px;white-space:nowrap;flex:none}
.md-typeset .story-card-body{display:flex;flex-direction:column;flex:1;padding:.7rem .9rem .85rem}
.md-typeset .story-card-name{font-weight:700;font-size:.95rem;margin:0}
.md-typeset .story-card-desc{font-size:.75rem;line-height:1.55;color:var(--md-default-fg-color--light);margin:.3rem 0 .7rem}
.md-typeset .story-card-metrics{display:flex;gap:1rem;margin-top:auto;flex-wrap:wrap}
.md-typeset .story-card-metrics span{font-size:.62rem;color:var(--md-default-fg-color--light)}
.md-typeset .story-card-metrics b{display:block;font-size:1rem;font-weight:700;color:var(--s1)}
@keyframes story-move{from{transform:translateX(0)}to{transform:translateX(-50%)}}
[data-md-color-scheme="slate"] .md-typeset .story-card{border-color:rgba(148,163,184,.18);background:rgba(148,163,184,.06)}
[data-md-color-scheme="slate"] .md-typeset .story-card-metrics b{color:var(--s2)}
@media (prefers-reduced-motion: reduce){.md-typeset .story-marquee{overflow-x:auto;-webkit-mask-image:none;mask-image:none}.md-typeset .story-track{animation:none;width:auto}.md-typeset .story-group[aria-hidden="true"]{display:none}}
</style>

<div class="story-marquee" aria-label="客户成功故事">
  <div class="story-track">
    <div class="story-group">
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">全链路方案</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">金融资产管理集团</p><p class="story-card-desc">中国 500 强金融资产管理集团，从 GPU 选型规划到大模型适配的全链路方案</p><div class="story-card-metrics"><span><b>稳定</b>算力供应</span><span><b>多场景</b>AI 智能</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 一体机</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">液晶屏制造巨头</p><p class="story-card-desc">半导体液晶屏行业领军企业，以 AI 一体机构建高性能 GPU 集群，落地制造业场景化模型应用</p><div class="story-card-metrics"><span><b>30%</b>软件研发效率提升</span><span><b>10,000+</b>AI 智能体</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 知识库</span><span class="story-card-ind">日本</span></div>
        <div class="story-card-body"><p class="story-card-name">欧姆龙</p><p class="story-card-desc">全球知名的自动化控制及电子设备制造领军企业，打造工业制造与企业行政双场景 AI 知识库</p><div class="story-card-metrics"><span><b>65%</b>知识整理工时节约</span><span><b>60%</b>客服处理效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">港产大模型</span><span class="story-card-ind">香港</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">联合港科大打造支撑首个港产大模型落地的高效能算力集群，全面赋能 HKGAI Studio</p><div class="story-card-metrics"><span><b>90%</b>GPU 利用率</span><span><b>60%</b>模型微调效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">算力服务平台</span><span class="story-card-ind">上海</span></div>
        <div class="story-card-body"><p class="story-card-name">模速空间</p><p class="story-card-desc">全国首个大模型创新生态社区的算力资源服务平台，通过资源池化、弹性调度与成本优化降低创新门槛</p><div class="story-card-metrics"><span><b>一站式</b>算力-模型-应用</span><span><b>全国首个</b>大模型创新生态社区</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">智算超节点</span><span class="story-card-ind">国产算力</span></div>
        <div class="story-card-body"><p class="story-card-name">Shanghai Cube</p><p class="story-card-desc">联合国产算力厂商研发国内首款开放架构智算超节点，软硬深度协同推进国产算力规模化应用</p><div class="story-card-metrics"><span><b>80%</b>性能达进口高端设备</span><span><b>全栈</b>“芯片-系统-平台”国产化</span></div></div>
      </div>
    </div>
    <div class="story-group" aria-hidden="true">
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">全链路方案</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">金融资产管理集团</p><p class="story-card-desc">中国 500 强金融资产管理集团，从 GPU 选型规划到大模型适配的全链路方案</p><div class="story-card-metrics"><span><b>稳定</b>算力供应</span><span><b>多场景</b>AI 智能</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 一体机</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">液晶屏制造巨头</p><p class="story-card-desc">半导体液晶屏行业领军企业，以 AI 一体机构建高性能 GPU 集群，落地制造业场景化模型应用</p><div class="story-card-metrics"><span><b>30%</b>软件研发效率提升</span><span><b>10,000+</b>AI 智能体</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 知识库</span><span class="story-card-ind">日本</span></div>
        <div class="story-card-body"><p class="story-card-name">欧姆龙</p><p class="story-card-desc">全球知名的自动化控制及电子设备制造领军企业，打造工业制造与企业行政双场景 AI 知识库</p><div class="story-card-metrics"><span><b>65%</b>知识整理工时节约</span><span><b>60%</b>客服处理效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">港产大模型</span><span class="story-card-ind">香港</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">联合港科大打造支撑首个港产大模型落地的高效能算力集群，全面赋能 HKGAI Studio</p><div class="story-card-metrics"><span><b>90%</b>GPU 利用率</span><span><b>60%</b>模型微调效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">算力服务平台</span><span class="story-card-ind">上海</span></div>
        <div class="story-card-body"><p class="story-card-name">模速空间</p><p class="story-card-desc">全国首个大模型创新生态社区的算力资源服务平台，通过资源池化、弹性调度与成本优化降低创新门槛</p><div class="story-card-metrics"><span><b>一站式</b>算力-模型-应用</span><span><b>全国首个</b>大模型创新生态社区</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">智算超节点</span><span class="story-card-ind">国产算力</span></div>
        <div class="story-card-body"><p class="story-card-name">Shanghai Cube</p><p class="story-card-desc">联合国产算力厂商研发国内首款开放架构智算超节点，软硬深度协同推进国产算力规模化应用</p><div class="story-card-metrics"><span><b>80%</b>性能达进口高端设备</span><span><b>全栈</b>“芯片-系统-平台”国产化</span></div></div>
      </div>
    </div>
  </div>
</div>

## 学习路径

<style>
.drun-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.drun-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.drun-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.drun-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.drun-path-step:last-child::after{display:none}
.drun-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.drun-path-title{font-weight:700;font-size:0.95rem}
.drun-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.drun-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.drun-path-step::after{display:none}}
</style>

<div class="drun-path">
  <a class="drun-path-step" style="--path-c:#2196f3" href="install/">
    <span class="drun-path-num">1</span>
    <span class="drun-path-title">部署平台</span>
    <span class="drun-path-desc">离线安装 d.run AI 操作系统</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#00acc1" href="kpanda/intro/">
    <span class="drun-path-num">2</span>
    <span class="drun-path-title">纳管算力</span>
    <span class="drun-path-desc">接入集群，纳管异构 GPU 算力</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#43a047" href="hydra/intro/">
    <span class="drun-path-num">3</span>
    <span class="drun-path-title">部署模型</span>
    <span class="drun-path-desc">模型广场选型，一键部署推理服务</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#fb8c00" href="clawos/intro/">
    <span class="drun-path-num">4</span>
    <span class="drun-path-title">部署智能体</span>
    <span class="drun-path-desc">编排多智能体，落地业务场景</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#8e24aa" href="crane/intro/">
    <span class="drun-path-num">5</span>
    <span class="drun-path-title">运营洞察</span>
    <span class="drun-path-desc">驾驶舱看全链路 Token 运营</span>
    <span class="drun-path-go">Go →</span>
  </a>
</div>

[下载 d.run AI 操作系统离线包](https://docs.daocloud.io/download/drun/){ .md-button }
[安装 d.run AI 操作系统](install/index.md){ .md-button }
[查阅 d.run AI 操作系统彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/drun.pdf){ .md-button }
{: .tf-footer-cta }
