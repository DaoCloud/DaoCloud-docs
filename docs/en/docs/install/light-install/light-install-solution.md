# Lightweight Deployment Trimming Plan Verification

Considering that in some scenarios, especially in the military industry, cloud software deployment faces stringent resource constraints, this document introduces a lightweight trimming and verification plan for deploying **DCE 5.0 Community Edition**, aiming to meet customers' requirements for lightweight deployment.

This trimming plan is verified step by step through four phases, detailed as follows:

## Verification Environment

* Operating System: Kylin Linux Advanced Server V10 (Halberd) for ARM
* CPU: 10C
* Memory: 17Gi

## Installed Components and Resource Statistics

The installation components, trimming plan, and phased trimming approach for DCE 5.0 are as follows:

Full view of Phase 1 lightweight trimming:

## Optimization Measures

1. Under the premise of maintaining normal monitoring capabilities, the following Pods of **Insight** can be stopped:

    | Pod name                                                 | Mem Size   |
    | :------------------------------------------------------- | ---------- |
    | insight-agent-fluent-bit-5x2rn                           | 99.62 MiB  |
    | insight-agent-otel-kubernetes-collector-69f67cc745-xt5hj | 74.94 MiB  |
    | insight-agent-tailing-sidecar-operator-6f85f7bb75-67xc8  | 46.81 MiB  |
    | insight-elastic-alert-64bbb468dc-l4mk5                   | 30.38 MiB  |
    | insight-jaeger-collector-5cd5b94dcc-mwgcl                | 32.50 MiB  |
    | insight-jaeger-query-5495c59bbd-fk287                    | 28.88 MiB  |
    | insight-opentelemetry-collector-5d47dd6c6b-nk54t         | 62.12 MiB  |
    | Optimizable memory                                       | 375.25 MiB |

2. Remove the Istio sidecar via the script [clean_istio_proxy.sh](https://gitlab.daocloud.cn/bo.jiang/installer-tools/-/blob/master/clean_istio_proxy.sh)

3. Disable the Seed **kind-cluster** and **elasticsearch** components

    1. Before installer deployment, disable the elasticSearch component in `manifest.yaml`

        [Not feasible] `insight-server` has a strong dependency on ES

    2. After installer deployment, shut down the kind-cluster container

        [Feasible] There is a hidden issue in the image pull policy; it needs to be changed to **IfNotPresent**

4. Deploy **registry** in Global, managed via **kangaroo** [Feasible]

5. Deploy single-instance **MySQL**, using an external MySQL instance managed outside the container [Feasible]

### Phase Optimizations

**Phase1 Optimization**

Phase1 trims non-essential components in **infrastructure & components**.

1. Resource usage within Seed

2. Resource usage of Global + kind Seed


According to the script statistics, total memory consumption: **13.6 GiB**

Theoretical memory usage of removable components:

!!! note

    The calculated statistics may differ from actual deployment usage, as dynamic cache generated during system operation also affects real memory consumption.

| Component     | Usage                  |
| :------------ | ---------------------- |
| elasticsearch | 2460.38 MiB (2.40 GiB) |
| kind-cluster  | 1005.62 MiB (0.98 GiB) |
| insight       | 2655.17 MiB (2.59 GiB) |
| kangaroo      | 277.25 MiB (0.27 GiB)  |
| Total         | 6.24 GiB               |

If these four types of components are not installed, the memory consumption is expected to be **7.36 GiB**.
However, previous community version trimming (without these four components) showed that **8G** memory can barely run it, but it is unstable.

**Phase2 Optimization**

In Phase2, MySQL is consolidated from dual instances to a single instance, while trimming and optimizing some **Insight** components.

**Phase3 Optimization**

Optimization item: Remove **ES** (replica = 0), according to [issue 2268](https://gitlab.daocloud.cn/ndx/engineering/insight/insight/-/issues/2268#note_558331)

**Phase4 Optimization**


## Conclusion

This lightweight plan is derived by progressively trimming and scaling down a full **K8s + DCE5 Community Edition** environment under sufficient memory, reaching an idle state. Based on the memory statistics, the total memory just meets the requirements.

In actual real-world scenarios, with an **8Gi memory environment**, installation proceeds sequentially (adaptive trimming).
However, since some steps at the end require manually executing scripts, it triggers **deploy rolling updates**, causing a temporary surge in memory demand.
Additionally, the operating system itself consumes part of the dynamic memory resources.

Therefore, in summary, running the **DCE5 lightweight trimmed environment** in an **8G memory** setup still lacks sufficient resources.

That is, **installation memory requirement ≠ idle state memory usage**

Using **Phase 4** as the final trimming goal, at least **10G+ memory** is required.
Using **Phase 3** as the final trimming goal (including observability components), at least **12G+ memory** is required.

For how to achieve lightweight deployment through the installer, refer to
[Installer Lightweight Deployment Plan](./install-light.md).
