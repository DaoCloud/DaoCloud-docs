---
hide:
  - toc
---
# 云原生存储

云原生代表了容器化、碎片化的趋势，存储是持久化数据的媒介。

DCE 5.0 全面支持云原生存储，兼容并蓄各类容器化存储解决方案。
目前除了 DaoCloud 完全自研并开源的 [HwameiStor 本地存储](./hwameistor/intro/what.md)之外，还可以从应用商店，按需安装众多开源存储解决方案：

- Ceph Rook
- NFS Subdir External Provisioner
- Longhorn

存储文档施工一览：

```mermaid
graph LR

stor[云原生存储] --> intro[介绍]
    intro --> what1[什么是云原生存储]
    intro -.-> back[背景和挑战]
stor --> hwa[本地存储]
    hwa --> what2[什么是 HwameiStor]
    hwa -.-> feature[功能总览]
    hwa -.-> benefit[竞争优势]
    hwa --> install[安装管理]
        install --> prepare[准备工作]
        install --> step[安装步骤]
        install --> check[安装后检查]
        install --> upgrade[升级]
        install --> uninstall[卸载]
    hwa --> parts[组件介绍]
    hwa --> resources[资源介绍]
    hwa --> sce[应用场景]
    hwa --> faq[常见问题]
    hwa --> om[运维管理]
        om --> pool[存储池管理]
        om --> node[存储节点扩展]
        om --> migrate[数据卷迁移]
        om --> scale[数据卷扩容]
        om --> disk[磁盘扩展]
stor --> open[开源存储方案集成]
    open -.-> ceph[Ceph-Rook 相关]
    open -.-> nfs[NFS Subdir<br>External Provisioner]
    open --> long[Longhorn]
        long --> intro1[Longhorn 简介]
        long -.-> ins[安装部署]
        long -.-> use[使用说明]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class back,open,ceph,nfs,ins,use,feature,benefit plain;
class what1,what2,prepare,step,check,upgrade,uninstall,parts,resources,sce,faq,pool,node,migrate,scale,disk,intro1 cluster
class stor,intro,hwa,install,om,long k8s

click what1 "https://docs.daocloud.io/storage/intro/"
click what2 "https://docs.daocloud.io/storage/hwameistor/intro/what/"
click prepare "https://docs.daocloud.io/storage/hwameistor/install/prereq/"
click step "https://docs.daocloud.io/storage/hwameistor/install/deploy/"
click check "https://docs.daocloud.io/storage/hwameistor/install/post-check/"
click upgrade "https://docs.daocloud.io/storage/hwameistor/install/upgrade/"
click uninstall "https://docs.daocloud.io/storage/hwameistor/install/uninstall/"
click parts "https://docs.daocloud.io/storage/hwameistor/intro/ldm/"
click resources "https://docs.daocloud.io/storage/hwameistor/intro/resources/"
click sce "https://docs.daocloud.io/storage/hwameistor/application/overview/"
click faq "https://docs.daocloud.io/storage/hwameistor/faqs/"
click pool "https://docs.daocloud.io/storage/hwameistor/resources/storagepool/"
click node "https://docs.daocloud.io/storage/hwameistor/resources/node-expansion/"
click migrate "https://docs.daocloud.io/storage/hwameistor/resources/migrate/"
click scale "https://docs.daocloud.io/storage/hwameistor/resources/expand/"
click disk "https://docs.daocloud.io/storage/hwameistor/resources/disk-expansion/"
click intro1 "https://docs.daocloud.io/storage/longhorn/"
```

!!! tip

    上图中的蓝色文字可点击跳转，灰底表示正在制作中。