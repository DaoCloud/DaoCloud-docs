# Open source project

This page lists activity in cloud native open source projects in alphabetical order.

### A, B

- [Acorn: Acorn Labs open source K8s application packaging and deployment framework](https://acorn.io/introducing-acorn/)

     [Acorn](https://github.com/acorn-io/acorn) can package all application's Docker image, configuration and deployment specification into an Acorn image artifact, which can be pushed to any OCI registry.
     As a result, developers can move locally developed applications to production without switching tools or technology stacks.
     Acorn images are created by describing the application's configuration in an Acornfile, eliminating the boilerplate of Kubernetes YAML.

- [Aeraki Service Mesh v1.3.0 Released](https://github.com/aeraki-mesh/aeraki/releases/tag/1.3.0)

    Updates: Support for Istio version 1.16.x, support for multiplexing, support for MetaProtocol Layer 7 routing capability on Gateway, support for application-level service governance for Dubbo services, support for Redis traffic management.

- [Aeraki service mesh project v1.1.0 released (CNCF project)](https://www.aeraki.net/blog/2022/announcing-1.1.0/)

     The main new features of this version: support Istio 1.12.x version; support bRPC (better RPC) protocol, bRPC is Baidu's open source industrial-grade RPC framework; Pass the real IP of the server, etc.

- [AlterShield: change control platform open sourced by Ant Group](https://mp.weixin.qq.com/s/8L2LqxeRK9LCtfSkKG94wg)

    [AlterShield](https://github.com/traas-stack/altershield) is a one-stop control platform that integrates change awareness, change defense and change analysis. It aims to define change standard protocols and standardize change control processes, enabling users to quickly identify problems in changes and reduce the impact of failures in a timely manner. For cloud-native scenarios, AlterShield provides Operator to connect various CI/CD tools to OCMS (Open Change Management Specification) SDK, and Operator itself provides change flow control and exception rollback policy control.

- [Antrea CNI Plugin v1.12.0 Released (CNCF Project)](https://github.com/antrea-io/antrea/releases/tag/v1.12.0)

    Release features: Topology-aware and node IP address management features upgraded from Alpha to Beta and enabled by default; support for enabling multicast via a new Antrea proxy configuration parameter; added support for ExternalIP in AntreaProxy; added support for WireGuard tunneling mode for multiclusters; added support for EndpointSlice API for multicluster services. Add support for the EndpointSlice API for multicluster services.

- [Antrea CNI Plugin v1.11.0 Released (CNCF Project)](https://github.com/antrea-io/antrea/releases/tag/v1.11.0)

    Release features: ClusterSet scoped policy rules support namespace fields, L7 policy rules support traffic logging, support for handling DNS requests on TCP network packets, AntreaProxy's EndpointSlice feature upgraded to Beta, AntreaProxy supports handling endpoints in the process of termination ( ProxyTerminatingEndpoint), Egress policies support limiting the number of Egress IPs assigned to a node, and multiple traffic patterns are supported for multiple cluster gateways.

- [Antrea CNI plugin v1.10.0 released (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.10.0)

     The main new features in this release: L7 network policy functionality added, Antrea's CRD API can collect support bundle files on any K8s node or ExternalNode, support for network policies for cross-cluster traffic added, antrea-agent can be used as a runtime on Windows when using containerd When using containerd as a runtime on Windows, antrea-agent can be run as DaemonSet.

- [Antrea CNI plugin v1.9.0 release (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.9.0)

     Added multiple multicluster features, including inter-cluster Pod connections, node controllers supporting Gateway high availability, and allowing Pod IPs to serve as endpoints for multicluster services;
     Add service health check similar to kube-proxy; add rule name to audit log; a service supports 800+ endpoints.

- [Antrea CNI Plugin v1.8.0 released (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.8.0)

     The main new features of this version: add ExternalNode function, K8s network policy adds audit log support, supports the use of Antrea ClusterNetworkPolicy to control external access to NodePort services, allows logical grouping of different network endpoints, and generates a new Helm Chart version every time Antrea releases, Support topology awareness TopologyAwareHints, add status field in IPPool CRD.

- [Antrea CNI plugin v1.7.0 release (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.7.0)
  
     The main new features of this version: increase the TrafficControl feature to control the transmission of Pod traffic; support IPsec certificate authentication; enrich Antrea-native policies; enrich multicast features; increase multicluster gateway features; enrich secondary network IPAM features.

- [APISIX Cloud Native Gateway v3.2.0 Released](https://github.com/apache/apisix/releases/tag/3.2.0)

    Release features: support for service discovery on four layers, a new plugin to convert RESTful requests to GraphQL, support for setting log format on each logging plugin, new plugin to support interconversion between JSON and XML.

- [APISIX Cloud Native Gateway v3.1.0 Released](https://github.com/apache/apisix/blob/release/3.1/CHANGELOG.md#310)

     Major new features in this release: support for saving plugin-specific fields encrypted in etcd, allowing sensitive information to be stored in external security services, experimental support for gRPC-based etcd configuration synchronization, new Consul-based service discovery, and the addition of a built-in debugger plugin.
  
- [APISIX Cloud Native API Gateway v3.0 released](https://github.com/apache/apisix/blob/release/3.0/CHANGELOG.md#300)

     v3.0 adds Consumer Group to manage multiple consumers, supports configuring the order of DNS resolution domain name types, adds AI plane for intelligent analysis and visualization of configuration and traffic, fully supports ARM64, adds gRPC client, and implements data Complete separation of control plane and control plane, service discovery support for control plane, new xRPC framework, support for more four-layer observability, integration of OpenAPI specification, and full support for Gateway API.

- [APISIX Cloud Native API Gateway v2.15.0 released](https://github.com/apache/apisix/blob/release/2.15/CHANGELOG.md#2150)

     The main new features of this version: support for user-defined priority of plug-ins, support for determining whether plug-ins need to be executed through expressions, custom error responses, and allow collection of metrics on Stream Route.

- [Apollo Distributed Configuration Management System v2.0.0 release (CNCF project)](https://github.com/apolloconfig/apollo/releases/tag/v2.0.0)

     The main new features of this version: Add public namespace list view on the home page, grayscale rules support label matching when IP is not fixed, enable namespace export/import function, most lists have added `DeletedAt` column support Unique constraint index.

- [Arbiter: Speed Cloud Open Source Scalable Scheduling and Elasticity Tool Based on K8s](https://mp.weixin.qq.com/s/xF6Zij2FB2dq3QsZO6ch1g)

     [Arbiter](https://github.com/kube-arbiter/arbiter) aggregates various types of data based on which users can manage, schedule, or scale applications in a cluster. It can help Kubernetes users understand and manage the resources deployed in the cluster, thereby improving the resource utilization and operational efficiency of enterprise applications.

- [Argo CD continuous deployment tool v2.8.0 released (CNCF project)](https://github.com/argoproj/argo-cd/releases/tag/v2.8.0)

    Features: add kubelogin function, allow users to use ApplicationSet resources in any namespace, add health check for snapshot volume, add plugin generator function, support specifying listening address from environment variable or command line parameter, create job action, support refreshing ExternalSecret.

- [Argo CD GitOps Tool v2.6.0 Released (CNCF Project)](https://github.com/argoproj/argo-cd/releases/tag/v2.6.0)

    Release features: ApplicationSet resources add progressive release policies, allow users to provide multiple resources to an application, allow multiple CRDs to share health checks, support reverse proxy extensions, argocd CLI adds cross-platform support for the file encryption tool bcrypt.

- [Argo becomes a CNCF graduation project](https://mp.weixin.qq.com/s/l8veOjEZV4xlrtqdCWPljg)

     [Argo](https://github.com/argoproj) enables teams to declaratively deploy and run cloud-native applications and workflows on Kubernetes using GitOps.
     Argo adoption has grown 250% since it became a CNCF-incubated project and passed a third-party security audit in July of this year,
     Has become an important part of the cloud native technology stack and GitOps.

- [Argo CD GitOps Tools v2.5.0 release (CNCF project)](https://github.com/argoproj/argo-cd/releases/tag/v2.5.0)

     The main new features of this version: support for filtering applications based on clusters, adding Prometheus health checks, adding notification APIs, supporting custom application operations for CLI, adding support for default container annotations, restricting redis export rules, adding Gitlab PR generators webhook, new ApplicationSet Go template, new ArgoCD CLI local template.

- [Argo 2022 project security audit results released](https://mp.weixin.qq.com/s/m1-bnWKU54SYMfKW_xEkIA)

     The Argo team, CNCF, and software security firm Ada Logics partnered to conduct security audits of four of Argo's projects.
     A total of 26 issues were found: 7 for Argo CD, 6 for Argo Workflows, and 13 for Argo Events. Seven CVEs were issued for Argo CD and two CVEs for Argo Events.
     As of publication time of the report, all exploitable issues have been fixed and published as security advisories on [GitHub](https://github.com/orgs/argoproj/projects/19).
     Full text of the audit report: <https://github.com/argoproj/argoproj/blob/master/docs/argo_security_audit_2022.pdf>

- [Argo CD Continuous Deployment Tool v2.4.0 released (CNCF project)](https://github.com/argoproj/argo-cd/releases/tag/v2.4.0)

     The main new features of this version: UI adds a web terminal - you can start a shell in a running application container without leaving the web interface; introduce access control to Pod logs and web terminals; integrate OpenTelemetry Tracing.

- [Backstage Developer Portal Security Audit Report and Threat Model Release (CNCF Project)](https://backstage.io/blog/2022/08/23/backstage-security-audit)

     [Audit](https://backstage.io/blog/assets/22-08-23/X41-Backstage-Audit-2022.pdf) found 10 vulnerabilities in total.
     In Backstage [v1.5](https://backstage.io/docs/releases/v1.5.0), 8 of these vulnerabilities are fully fixed.
     Of the 4 open issues, 3 are related to rate limiting and internal DoS issues.
     [Threat Model](https://backstage.io/docs/overview/threat-model) summarizes key security considerations for operators, developers, and security researchers, covering trust models and roles involved in a typical Backstage setup, Responsibilities of integrators, common configuration issues, etc.

- [Backstage developer portal building platform v1.4.0 release (CNCF project)](https://github.com/backstage/backstage/releases/tag/v1.4.0)

     Main new features of this version: Search API upgraded to v1, new backend system (experimental), deprecation of a large number of command line and authorization backend symbols, added support for $ref processing in the OpenAPI specification, added Apollo Explorer support ( PoCs).

- [Beyla: Grafana Releases Open Source eBPF Automated Instrumentation Tool for Application Observability](https://mp.weixin.qq.com/s/H5yw6jSeJdLoLFc32OTeyA)

    Beyla is able to report spanning information and RED metrics (Rate-Error-Duration) for Linux HTTP/S and gRPC services, and does so without the need to insert probes to make code changes.Grafana Beyla supports HTTP and HTTPS services written in Go, NodeJS, Python, Rust, Ruby, . NET, etc. gRPC services written in Go are also supported.

### C

- [Calico CNI Plugin v3.26.0 Released (CNCF Project)](https://github.com/projectcalico/calico/blob/v3.26.0/release-notes/v3.26.0-release-notes.md)

    Release features: separates calico-node and calico-cni-plugin service accounts, reduces CPU usage on the system with kernel-level route filtering, supports Windows Server 2022, supports OpenStack Yoga.

- [Calico CNI Plugin v3.25.0 release (CNCF project)](https://github.com/projectcalico/calico/blob/v3.25.0/calico/_includes/release-notes/v3.25.0-release-notes.md)

    Key new features in this release: Optimization of the eBPF data plane to ensure that Connect Time Load Balancing works in larger, rapidly changing environments; Felix component support for overriding the internal readiness/liveness watchdog timeout; Typha component support for graceful shutdown.

- [Calico CNI plugin v3.24.0 release (CNCF project)](https://github.com/projectcalico/calico/blob/release-v3.24/calico/_includes/release-notes/v3.24.0-release-notes.md)

     The main new features of this version: support IPv6 network wireguard encryption, expose IPAM configuration and IPAM block affinity through API, add new fields to operator API, support split IP pool, and transition from pod security policy to pod security standard.

- [Carina cloud-native local storage project v0.11.0 released](https://github.com/carina-io/carina/releases/tag/v0.11.0)

     Main new features of this version: support Cgroup v2, remove HTTP Server, upgrade CSI official image version, remove ConfigMap synchronization controller, move carina image to a separate namespace, add carina e2e test to replace the original e2e test code ( In development and testing), optimize the pvc scheduling logic of Storageclass parameters.

- [Carina Local Storage Project v0.10.0 Release (CNCF Project)](https://github.com/carina-io/carina/releases/tag/v0.10.0)

     The main new features of this version: support for mounting bare disks into containers for direct use, support for velero backup storage volumes, new CRD resource NodeStorageResource to replace the original method of registering disk devices to Node nodes, and use job to generate webhook certificates to replace the original How the script generates the certificate, etc.

- [cdk8s+: AWS open source Kubernetes development framework officially available](https://aws.amazon.com/blogs/containers/announcing-general-availablecity-of-cdk8s-plus-and-support-for-manifest-validation/)

     [cdk8s+](https://github.com/cdk8s-team/cdk8s) allows users to define Kubernetes applications and reusable abstractions using familiar programming languages and object-oriented APIs.
     Compared with the beta version released last year, the new features of the official version include: isolate the pod network and only allow specified communication; improve the configuration mechanism for running multiple pods on the same node; integrate [Datree](https://github.com/datreeio/datree-cdk8s) plugin to check for misconfigurations in Kubernetes using third-party policy enforcement tools.

- [Cert-manager Cloud Native Certificate Management Project v1.12.0 Released (CNCF Project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.12.0)

    Release features: separate Go module for binaries and tests, added support for JSON logging, support for ephemeral service account tokens with Vault, support for ingressClassName field, new flags to specify which resources need to be injected into Kubernetes objects.

- [Cert-manager Cloud Native Certificate Management Project v1.11.0 Released (CNCF Project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.11.0)

    Major new features in this release: support for authentication using Azure Workload Identity Federation, support for specifying the trust store used by cert-manager when communicating with ACME servers, support for the gateway API v1beta1, and enabling testing against Kubernetes 1.26.

- [Cert-manager cloud native certificate management project v1.10.0 release (CNCF project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.10.0)

     The main new features of this version: use trivy to scan locally built containers; if the target Secret is misconfigured or created after the request, resynchronize the signing request; add the option to load the Vault CA Bundle from the Kubernetes Secret; support adding on all resources deployed by the chart same label.

- [Cert-manager cloud native certificate management project upgraded to CNCF incubation project](https://www.cncf.io/blog/2022/10/19/cert-manager-becomes-a-cncf-incubating-project/)

     Cert-manager is a plugin for Kubernetes that automates the management and issuance of TLS certificates from various sources, providing cryptographic protection for cloud-native workloads. Recently, the CNCF Technical Oversight Committee has voted to accept cert-manager as a CNCF incubation project.

- [Cert-manager cloud native certificate management project v1.9.0 release (CNCF project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.9.0)

     The main new features of this version: support for using cert-manager certificate (alpha), and support for configuring ingress-shim certificates through annotations on Ingress resources.

- [ChaosMeta Chaos Project v0.5 released](https://mp.weixin.qq.com/s/4VG5TkQPotr_BrweIznW_w)

    Version features: new platform interface component, mainly providing space management, user rights management, orchestration experiments, experiment results, etc.; new metrics component, providing the expected judgment on the value of monitoring items, the number of pods related to them, http requests, tcp requests; new traffic injection component, currently only supports injection of HTTP traffic, and it will be supplemented with other types of traffic such as RPC, DB client, redis client, etc. gradually. It will gradually add the ability to inject other types of traffic such as RPC, DB client, redis client, and so on.

- [Chaosblade Chaos Engineering Project v1.7.0 Release (CNCF Project)](https://github.com/rook/rook/releases/tag/v1.10.0)

     The main new features of this version: add time travel experiment, add plugins zookeeper and clickhouse, jvm performance optimization, support for mTLS authentication of blade server.

- [Chaos Mesh Chaos Engineering Platform v2.5.0 release (CNCF project)](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.5.0)

     The main new features of this version: support for multicluster chaos experiments, HTTPChaos adds TLS support, allows configuring Pod security contexts for controller manager and dashboards in Helm charts, and StressChaos supports cgroups v2.

- [Chaos Mesh Chaos Engineering Test Platform v2.2.0 Release (CNCF Project)](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.2.0)

     The main new features of this version: Add the StatusCheck feature to check the health of the application, and stop the chaos experiment when the application is unhealthy; support the use of `Chaosctl` for outbound forced recovery, and add workflows based on flow charts in the dashboard interface etc.

- [ChaosMeta: Ant Group's open source cloud-native automated chaos engineering platform](https://mp.weixin.qq.com/s/QUiWocMwbnSoUyfAu1z-cg)

    [ChaosMeta](https://github.com/traas-stack/chaosmeta) is designed to be a one-stop walkthrough comprehensive solution that includes the complete chaos engineering lifecycle, covering multiple phases such as admission checking, traffic injection, fault injection, fault metrics, recovery metrics and fault recovery. At this stage, ChaosMeta has opened up rich fault injection features to the public, supporting not only standalone deployments and Kubernetes cloud-native deployments, but also experiments with cloud-native fault cases such as Kubernetes itself and Operator.

- [Cilium CNI Plugin v1.14.0 Released (CNCF Project)](https://github.com/cilium/cilium/releases/tag/v1.14.0)

    Release features: support for two-way authentication, support for deploying Envoys as DaemonSets, support for WireGuard encryption of inter-node traffic and the ability to use Layer 7 policies on WireGuard, Cilium Mesh provides consistent network connectivity between the cloud and heterogeneous workloads, support for broadcasting external IP addresses to the local network via the Layer 2 transport protocol, and support for the Cilium CNI Plugin v1.14.0 (CNCF project). protocol to broadcast external IP addresses to the local network, support for multiple IPAM pools, and BIG TCP support for IPv4.

- [Cilium CNI Plugin v1.13.0 Released (CNCF Project)](https://github.com/cilium/cilium/releases/tag/v1.13.0)

    Release features: support Gateway API v0.5.1, add IPv6 BIG TCP support, support LoadBalancer IP address management, initial support for SCTP, support for fine-grained configuration of nodes based on tag selector, support for k8s 1.26, support for declaring LoadBalancer services via BGP control plane The following features are included: support for L7 load balancing of existing Kubernetes services through the built-in Envoy agent, Ingress resources can share Kubernetes LoadBalancer resources, datapath support for mTLS, support for internal service traffic policies, cosign signing of all images, and creation of SBOMs for each image. Create SBOMs for each image.

- [Cilium Releases Security Audit Report and Fuzz Test Audit Report](https://www.cncf.io/blog/2023/02/13/a-well-secured-project-cilium-security-audits-2022-published/)

    [Security Audit](https://github.com/cilium/cilium.io/blob/main/Security-Reports/CiliumSecurityAudit2022.pdf) and [Fuzz Testing](https://github.com/) cilium/cilium.io/blob/main/Security-Reports/CiliumFuzzingAudit2022.pdf) found a total of 30 issues, and no critical risk vulnerabilities were found.
    Of these, two were medium-risk issues, the first being the lack of easily accessible documentation on running Cilium securely, which [PR](https://github.com/cilium/cilium/pull/23599) is being addressed.
    The second is a possible failure to unlock a mutex in case of misconfiguration; this [issue](https://github.com/cilium/cilium/pull/23077) has been fixed. The rest are low-risk or informational issues.

- [Cilium 2022 Annual Report Released](https://github.com/cilium/cilium.io/raw/main/Annual-Reports/Cilium%20Annual%20Report%202022.pdf)

     The report documents the Cilium project's contributor growth, release highlights, user survey results, production landings, community activities, and where we are headed in 2023.
     In 2023, the Cilium service mesh will mature; kernel data captured through eBPF will help the surrounding ecosystem build a better platform for end users; and supply chain security features will be enhanced.

- [Cilium CNI Plugin v1.12.0 release (CNCF project)](https://github.com/cilium/cilium/releases/tag/v1.12.0)

     The main new features of this version: launch Cilium Service Mesh (multiple control planes, sidecar/borderless car, Envoy CRD), integrate Ingress Controller, add K8s service topology awareness prompt, initial NAT46/64 implementation, support Pod to enable BBR congestion control and Bandwidth Manager moved out of beta, supports dynamic allocation of pod CIDR in cluster pool v2 IPAM mode, supports setting service backend status, and upgrades egress gateway to stable status.

- [Cloud Custodian cloud resource management tool v0.9.20 release (CNCF project)](https://github.com/cloud-custodian/cloud-custodian/releases/tag/0.9.20.0)

     The main new features of this version: adding K8s admission controller mode, adding roles and cluster role resources.

- [Cloud Custodian cloud resource management tool upgraded to CNCF incubation project](https://mp.weixin.qq.com/s/Z3knP5tJ4om3nW1nqXEjsA)

     [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian) is a cloud governance as code tool that allows users to manage and automate cloud security, compliance, operations and cost optimization through code Policies, including writing policies to manage Kubernetes resources. Provides a very simple DSL to author policies and their consistency across cloud platforms compared to other cloud-based governance tools.

- [Cloud Native App Initializer: Alibaba Official Open Source Cloud Native Application Scaffolding](https://mp.weixin.qq.com/s/5hsrCfAdO7gBOJcT6fLpbg)

     [Cloud Native Application Scaffolding](https://github.com/alibaba/cloud-native-app-initializer) is built based on the Spring open source Initializr project.
     Not only can it help users manage dependencies, but it can also help users generate tests or code snippets that can be used directly. Users can test after creating a project, and develop projects based on sample code after testing.
     Therefore, building a project based on cloud-native application scaffolding only needs to be completed: create a new project and run the test.

- [Cluster API declarative cluster lifecycle management tool v1.5.0 released (CNCF project)](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.5.0)

     Release features: support for microservice pre-checks to improve cluster stability, support for concurrent MachineDeployment upgrades in classy clusters, support for additional providers in clusterctl, improved performance when deploying at scale, and improved observability of MachinePools through MachinePool Machine, The clusterctl plugin allows custom code to be called from clusterctl, and more metrics can be collected through custom Kube State Metrics configurations.

- [Cluster API Declarative Cluster Lifecycle Management Tool v1.3.0 released (CNCF project)](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.3.0)

     The main new features of this version: support for automatic renewal of machine certificates provided by the Kubeadm control plane provider, the ability to publish and consume cluster API images from the new container container registry registry.k8s.io, allowing the creation of clusters without taints on control plane nodes, clusterctl can now manage IPAM and RuntimeExtension providers.

- [Clusternet Multi-Cloud Multi-Cluster Management Project v0.16.0 Released (CNCF Project)](https://github.com/clusternet/clusternet/releases/tag/v0.16.0)

    Updates: support for migrating workloads from non-ready clusters to healthy standby clusters, support for adding taint to non-ready clusters, configurable cluster score percentages for scheduling, add license scan reports and status, support for logging metrics data for health checks.

- [Clusternet multicloud Multicluster Management Project v0.15.0 Released (CNCF Project)](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.4.0)

    Release features: move all controllers out of clusternet-hub into a new component called "clusternet-controller-manager"; add functional gate for multicluster service discovery; add unit tests for scheduler migration validation.

- [Clusternet Distributed Cloud Native Multicluster Management Project Selected for CNCF Sandbox Project](https://www.51cto.com/article/748691.html)

    On March 8, [Clusternet](https://github.com/clusternet/clusternet) was selected by the CNCF Foundation TOC Committee as a CNCF Sandbox project.
    Clusternet extends the powerful single-cluster capability of Kubernetes to multiple clusters in a component-based, non-intrusive and lightweight way, and is well compatible with the cloud-native ecosystem.
    In the future, Clusternet will explore richer multicluster use cases and promote a fully functional and standardized multicluster framework.

- [Clusternet multicloud multicluster management project v0.13.0 released](https://github.com/clusternet/clusternet/releases/tag/v0.13.0)

     The main new features of this version: increase the routing feature from the parent cluster to the sub-cluster pod, add scheduler configuration and support custom scheduler plug-ins, support discovery v1beta1, only provide support for discovering endpointslices for k8s v1.21.0 and later versions, Aggregate worker node labels using thresholds, support scheduling by cluster subgroup, update RBAC rules for clusternet-agent running in capi.

- [Constellation: Edgeless Systems Open Sources First Confidential Computing Kubernetes](https://blog.edgeless.systems/hi-open-source-community-confidential-kubernetes-is-now-on-github-2347dedd8b0c)

     [Constellation](https://github.com/edgelesssys/constellation) aims to provide an end-to-end confidential K8s framework.
     It wraps the K8s cluster in a confidential context, shielding it from the underlying cloud infrastructure.
     It supports running and scaling all containers; provides Sigstore-based node and artifact proof; provides Cilium-based network solutions, etc.

- [Consul Service Discovery Framework v1.13.0 release (CNCF project)](https://github.com/hashicorp/consul/releases/tag/v1.13.0)

     The main new features of this version: Remove support for Envoy 1.19; Cluster Peering supports federated Consul clusters for service mesh and traditional service discovery; allows routing egress traffic through terminal gateways in transparent proxy mode without modifying the directory.

- [containerd container runtime v1.7.0 released (CNCF project)](https://github.com/containerd/containerd/releases/tag/v1.7.0)

     Release features: New Sandbox API to simplify management of higher-level pods and provide new extension points for shim implementations and clients; New Transfer Service for transferring artifact objects between sources and targets; Support for extending the scope of the Node Resource Interface NRI to enable common pluggable runtime extensions; Added support for CDI device injection; Added support for cgroups blockio for enhanced restart manager; Added restart policy for enhanced restart manager; Added support for cgroups blockio for enhanced restart manager. support; support for cgroups blockio; add reboot policies for enhanced reboot manager; initial support for gRPC shim.

- [containerd completes fuzzy test audit](https://mp.weixin.qq.com/s/IUgdPaT6OAhPW5uCPlteEA)

    This [containerd audit](https://containerd.io/img/ADA-fuzzing-audit-21-22.pdf) adds a total of 28 fuzzer testers (fuzzer), covering a wide range of container runtime features.
    During this audit, a [vulnerability](https://github.com/containerd/containerd/security/advisories/GHSA-259w-8hf6-59c2) was found in the OCI image import process: importing a malicious image could lead to a DoS attack on the node .
    This issue has been fixed in containerd 1.5.18 and 1.6.18.

- [Contour Kubernetes ingress controller v1.26.0 released (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.26.0)

    Release features: support for gateway listeners on more than two ports, support for outputting stateful update load metrics, support for limiting the namespace of resources monitored by Contour instances, introduction of a new critical access logging level, and support for defining a default global rate-limiting policy.

- [Contour Kubernetes ingress controller v1.25.0 released (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.25.0)

    Version features: HTTPProxy support for configuring IP filters, support for exporting trace data to OpenTelemetry, support for external authorization for all hosts, support for internal redirection.

- [Contour Kubernetes ingress controller v1.22.0 release (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.22.0)

     The main new features of this version: support for Gateway API v0.5.0, allow configuring a direct response for a set of conditions in a single route, enable revocation checking for user certificate verification, merge access records and TLS cipher suite verification.

- [Contour Kubernetes ingress controller v1.21.0 release (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.21.0)

     The main new features of this version: Contour's RBAC access to leader election resources has been transferred to the namespace role; container images are now only published on the GitHub Container Registry (GHCR); new `contour gateway-provisioner` command and deployment list for dynamic Configure Gateways.

- [CoreDNS DNS Server v1.11.0 Released (CNCF Project)](https://github.com/coredns/coredns/releases/tag/v1.11.0)

    Release features: support for accepting DNS connections via QUIC protocol (doq), support for rewriting the target of CNAME records, removal of support for Endpoint and Endpointslice v1beta in kubernetes plugin.

- [Cortex Prometheus long-term storage solution v1.14 released](https://github.com/cortexproject/cortex/releases/tag/v1.14.0)

     Major new features in this version: Removed support for block storage, experimental support for vertical query sharding, enabled PromQL @modifier, can use OTel collector to send trace information to multiple destinations, multiple performance improvements and issues repair.

- [Cortex Distributed Prometheus Service v1.13.0 Release (CNCF Project)](https://github.com/cortexproject/cortex/releases/tag/v1.13.0)

     The main new features of this version: Add the streaming feature of the metadata API queryer, provide experimental shuffle sharding support for compactor, fix the memory leak of Distributor and Ruler, add a jitter to reset the initial value of each pod when distributing requests time.

- [Crane cost optimization tool launches an open source cloud native application carbon emission calculation optimizer](https://mp.weixin.qq.com/s/D46-7S20kaMF4CH_H5oTuA)

     The carbon emission calculation optimizer calculates the corresponding server power consumption based on the actual resource consumption of the application running on the Kubernetes platform, and then calculates the carbon emission generated by the application operation.
     In addition, it also supports providing Pod resource configuration, wOptimization suggestions for the number of orkload copies, HPA parameter configuration, etc., as well as the optimized power consumption and carbon emission calculation results.

- [CRI-O Container Runtime v1.28.0 Released (CNCF Project)](https://github.com/cri-o/cri-o/releases/tag/v1.28.0)

    Release features: allow users to disable host port mapping for Pods, new metrics to show when Pods and Containers are stuck at different stages of creation, support for specifying that a kubelet should not perform garbage collection on certain images, addition of version upgrade automation scripts, support for configurable metrics exporter namespaces, and support for error validation via CRI's mirror policy.

- [CRI-O: CNCF Announces Graduation of Container Runtime Program CRI-O](https://mp.weixin.qq.com/s/p7ogT3pAtbj17qrDh7acHQ)

    CRI-O provides a secure, efficient, and stable container runtime interface implementation for Kubelet to orchestrate Open Container Initiative (OCI) containers in production Kubernetes environments. In the future, CRI-O plans to improve upstream documentation, automate the publishing process, increase Pod density on nodes, and more. The project is also working on moving some parts to the Rust language.

- [CRI-O Container Runtime v1.26.0 Released (CNCF Project)](https://github.com/cri-o/cri-o/releases/tag/v1.26.0)

     Major new features in this release: Removal of support for CRI v1alpha2 (v1 support), added support for OTLP tracing, added logging and GRPC error code support for OTel tracing, support for Evented PLEG, added seccomp notifier functionality, added checkpointing for containers without infrastructure and recovery container support, allowing full runtime configuration updates, allowing additional runtimes to be added when reloading configurations, and changing the default runtime.

- [CRI-O Container Runtime v1.25.0 Release (CNCF project)](https://github.com/cri-o/cri-o/releases/tag/v1.25.0)

     The main new features of this version: support for setting the maximum log file size of pod at runtime, user namespace configuration capable of executing Kubelet, new annotations for configuring container power management, added minimum checkpoint/restore support, and signing statics through sigstore signatures binary package.

- [CRI-O Container Runtime v1.24.0 Release (CNCF project)](https://github.com/cri-o/cri-o/releases/tag/v1.24.0)

     Major new features in this release: block `unshare` syscall for containers without CAP_SYS_ADMIN by default, use task sets to generate new cri-o run commands, add pause and unpause functionality to CRI-O HTTP API.

- [Crossplane cloud-native control plane build framework completes fuzz testing security audit](https://mp.weixin.qq.com/s/BJXg8CCjaHFK29hxWe9W-g)

    The fuzzing test found 4 issues. One of the issues was that allowing a partially untrusted user to control the amount of memory allocated by crossplane-runtime in a certain state could lead to a DoS attack due to resource exhaustion. The fixes for this vulnerability are [crossplane-runtime 0.19.2](https://github.com/crossplane/crossplane-runtime/releases/tag/v0.19.2) and [Crossplane 1.11.2](https://github.com/crossplane/crossplane/releases/tag/v1.11.2) have been released.

- [CubeFS Distributed Storage System v3.3.0 Released (CNCF Project)](https://github.com/cubefs/cubefs/releases/tag/v3.3.0)

    Features: add support for ObjectNode storage bucket policies, add support for cross-domain resource sharing (CORS) for ObjectNode, support for atomicity in rename, delete, create, etc., support for configuring and dynamically adjusting MP (Multiplexing) step size, add support for UID space limit, support for autofs mounting. autofs mount feature.

- [CubeFS distributed storage system v3.1.0 release (CNCF project)](https://github.com/cubefs/cubefs/releases/tag/v3.1.0)

     The main new features of this version: provide QoS service to improve the multi-tenant isolation function, optimize the hybrid cloud multi-level read cache function, support two copies of data storage, support the configuration of posixAcl for volume management, and add a limit on the total number of data partitions for datanodes.

- [CubeFS distributed storage system upgraded from CNCF sandbox to incubation project](https://mp.weixin.qq.com/s/sAVaCa-yGEsJk3bUaJizmA)
  
     [CubeFS](https://github.com/cubefs) is the first cloud-native storage product in China with complete object and file storage capabilities.
     CubeFS supports multiple copies and erasure code engines, and provides features such as multi-tenant, multi-AZ deployment, and cross-region replication; it is suitable for a wide range of Cases such as big data, AI, container platforms, databases, and middleware separation of storage and computing.

### D

- [Dapr Distributed Application Runtime v1.11.0 Released (CNCF Project)](https://github.com/dapr/dapr/releases/tag/v1.11.0)

    Release features: configuration artifacts are now a v1 stable API; service calls support calling non-Dapr endpoints; support for suspending, restarting, and clearing workflows in the management API; introduction of cryptography building blocks; two build versions now available (with all components and with only stable components); Dapr dashboards are no longer installed with the control plane; container images are available for Windows Server 2022 container images; application health checks upgraded to stable.

- [Dapr Distributed Application Runtime v1.10.0 Released (CNCF Project)](https://github.com/dapr/dapr/releases/tag/v1.10.0)

    Release features: New Dapr Workflows for building long-running processes or data streams across multiple applications, support for bulk publishing and subscription information, allows creation of pluggable component SDKs written in any language, new Multi-App Run feature to improve local development, elasticity policy upgraded to stable, new service call metrics.

- [Dapr Distributed Application Runtime v1.9.0 Release (CNCF project)](https://github.com/dapr/dapr/releases/tag/v1.9.0)

     The main new features of this version: allow custom pluggable components, support OTel protocol, add elastic observation metrics, support application health checks, support setting default elastic policies, allow service calls using any middleware components, add pub/sub Namespace consumer groups, support for Podman container runtime.

- [The first open source version of the DeepFlow automated cloud-native observability platform is officially released](https://mp.weixin.qq.com/s/79wZ00RKoei_boZfiUmqgg)

     [DeepFlow](https://github.com/deepflowys/deepflow) is an observability platform developed by Yunshan Network. Based on technologies such as eBPF, it realizes automatic synchronization of resources, services, and K8s custom labels and injects them into observations as labels data.
     It can automatically collect application performance metrics and track data without interpolation, and the innovative mechanism of SmartEncoding reduces the resource consumption of tag storage by 10 times.
     In addition, it can integrate a wide range of data sources and provide a northbound interface based on SQL.

- [Devspace becomes a CNCF sandbox project](https://mp.weixin.qq.com/s/7ySQLtyYBX1ZDLvpeVObvQ)

     On December 15, CNCF announced that [DevSpace](https://github.com/loft-sh/devspace) officially became a CNCF sandbox project. With Devspace, applications can be built, tested, and debugged directly in Kubernetes; development can be performed using hot reloads; deployment workflows within teams and across development, staging, and production can be unified; and repetitive tasks of image builds and deployments can be automated.

- [DevSpace K8s development tools v6.0 released](https://github.com/loft-sh/devspace/releases/tag/v6.0.0)

     The main new features of this version: the introduction of pipeline to manage tasks in devspace.yaml, the new import feature to merge different devspace.yaml files together, and the new proxy command to run commands executed in the container on the local computer.

- [Dragonfly Mirror and File Distribution System v2.1.0 Released (CNCF Project)](https://github.com/dragonflyoss/Dragonfly2/releases/tag/v2.1.0)

    Release features: Visualization Console v1.0 released, new Virtual Network Topology Exploration feature, support for Dragonfly as a JuiceFS backend storage, support for Scheduler control in Manager, new Personal Access Token feature, new Cluster Resource Unit (Cluster represents a P2P cluster).

### E

- [Envoy v1.27.0 released (CNCF project)](https://github.com/envoyproxy/envoy/releases/tag/v1.27.0)

    Release features: Introduced new golang network filter, added Load shed point for rejecting requests when resources are insufficient, support for CONNECT-UDP, introduced Open Telemetry-compatible stats collector, added access log formatter for printing CEL expressions.

- [Envoy v1.26.0 released (CNCF project)](https://www.envoyproxy.io/docs/envoy/v1.26.0/version_history/v1.26/v1.26.0)

    Version features: added support for tracking generic proxies, support for modifying request and response headers anywhere in the http filter chain, support for setting JWT authentication failure status codes and messages in dynamic metadata, added filter status input, support for enabling rate limiting before TLS handshake and filter matching, support for routing information in upstream access logs, support for dynamically disabling TCP tunnels, add load balancer Maglev extensions and ring hash extensions.

- [Envoy v1.23.0 released (CNCF project)](https://www.envoyproxy.io/docs/envoy/v1.23.0/version_history/v1.23/v1.23.0)

     The main new features of this version: send SDS resources of multiple clusters or listeners in one SDS request, obtain filter configuration through the configuration name of HTTP filter, update listener filter statistics, dns_resolver adds support for multiple addresses, Add dynamic listener filter configuration for listener filters, etc.

- [Envoy Gateway API Gateway v0.5 released](https://gateway.envoyproxy.io/v0.5.0/releases/v0.5.html)

    Release features: add data plane proxy telemetry, support direct configuration of xDS, support different rate limiting based on IP address, support configuration of EnvoyProxy Pod labels, support configuration of EnvoyProxy deployment policy settings, volume and volume mounts, support configuration of EnvoyProxy as a NodePort type service, add Pprof debugging support.

- [Envoy Gateway Envoy-based Gateway v0.4 Released](https://gateway.envoyproxy.io/v0.4.0/releases/v0.4.html)

    Release features: support for installing Envoy Gateway via Helm; new initial framework for extending Envoy Gateway; support for IP-based subnet rate limiting; support for custom Envoy proxy boot configuration, Envoy proxy image and service configuration annotations, resource and security context settings, etc.; support for EDS (Endpoint Discovery Service).

- [Envoy Gateway v0.3 released](https://gateway.envoyproxy.io/v0.3.0/releases/v0.3.html)

    Release features: Support extended Gateway API fields; Support TCP routing API, UDP routing API and GRPC routing API; Support global rate limit; Support request authentication.

- [Envoy Gateway API Gateway v0.2 release](https://github.com/envoyproxy/gateway/releases/tag/v0.2.0)

     The main new features of this version: support for Kubernetes, support for Gateway API resources.

- [Envoy Gateway Open Source](https://blog.envoyproxy.io/introducing-envoy-gateway-ad385cc59532)

     [Envoy Gateway](https://github.com/envoyproxy/gateway) is officially a new member of the Envoy proxy family, a project aimed at lowering the barriers to using Envoy as an API gateway.
     Envoy Gateway can be thought of as a wrapper around the core of Envoy Proxy.
     The features it provides include: providing simplified API for gateway use cases, out-of-the-box controller resources, control plane resources, lifecycle management capabilities of proxy instances, etc., and an extensible API plane.

- [Emissary Ingress Cloud Native Ingress Controller and API Gateway v2.3.0 Release (CNCF Project)](https://github.com/emissary-ingress/emissary/releases/tag/v2.3.0)

     Main new features of this version: When using lightstep as the driver, `propagation_modes` can be set in `TracingService` configuration; support `crl_secret` can be set in `Host` and `TLSContext` resources to compare certificate revocation list checks and other certificates; optimize communication with external log services, etc.

- [eunomia-bpf: eBPF lightweight development framework officially open source](https://mp.weixin.qq.com/s/fewVoIKbLn5fYbXUaDyTpQ)

     [eunomia-bpf](https://gitee.com/anolis/eunomia) is jointly developed by universities and the Eunomia community, aiming to simplify the development, distribution and operation of eBPF programs. In eunomia-bpf, you only need to write the kernel mode code to run correctly, and do not need to recompile when deploying, and provide a standardized distribution method of JSON/WASM.

### F, G

- [Falco Runtime Security Project v0.35.0 released (CNCF project)](https://github.com/falcosecurity/falco/releases/tag/0.35.0)

    Release features: introduces metrics snapshot option and new metrics configuration, supports signing of published container images with cosign, allows custom CA certificates and storage, supports managing Talos pre-build drivers, Mesos no longer supports metadata enhancements.

- [Falco 2023 Security Audit Results Released](https://mp.weixin.qq.com/s/Uae58tOQpqOfV0vCoXBsqw)

    The [Audit Report](https://github.com/falcosecurity/falco/blob/master/audits/SECURITY_AUDIT_2023_01_23-01-1097-LIV.pdf) found one medium severity vulnerability and several low severity and information severity vulnerabilities, with no high severity vulnerabilities. All issues have been fixed in the Falco 0.34.0 and 0.34.1 patch releases.

- [Falco Runtime Security Project v0.34.0 Released (CNCF Project)](https://github.com/falcosecurity/falco/releases/tag/0.34.0)

    Release features: support for manual download and application-related rules [`application_rules.yaml`](https://github.com/falcosecurity/rules/tree/main/rules), new detection rules using PTRACE to inject code into processes, rule results adding compile condition context, allow modern bpf probes to allocate more than one CPU to a ring buffer, add webserver endpoint to retrieve internal version number, support multiple drivers in systemd unit.

- [Falco Runtime Security Project v0.32.0 Release (CNCF Project)](https://github.com/falcosecurity/falco/releases/tag/0.32.0)

     The main new features of this version: new ConfigMaps, when a rule or configuration file change is detected, Falco will be restarted; support for detecting containers with excessive permissions; support for detecting shared host pids and pods in the IPC namespace, etc.

- [Finch: AWS Open Source Container Development Client Command Line Tool](https://aws.amazon.com/cn/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/)

     [Finch](https://github.com/runfinch/finch) can be used to build, run and distribute Linux containers. It provides native, extensible macOS client installers for open source tools such as Lima, nerdctl, containerd, and BuildKit, simplifying the use of Containerd on macOS. users can use Finch to create and run containers on the local side, and to publish OCI container image files.

- [Flagger Progressive Delivery Project v1.31.0 Released (CNCF Project)](https://github.com/fluxcd/flagger/blob/main/CHANGELOG.md#1310)

    Version features: Support for Service Mesh Linkerd 2.12 and higher, removal of OSM e2e testing.

- [Flagger Progressive Delivery Project v1.22.0 released (CNCF project)](https://github.com/fluxcd/flagger/blob/main/CHANGELOG.md#1220)

     The main new features of this version: support for replacing HPA with KEDA ScaledObjects, adding namespace parameters in the parameter table, and adding an optional `appProtocol` field for Canary.Service.

- [Fluent Operator Cloud Native Log Collection Solution 2.5.0 Released](https://github.com/fluent/fluent-operator/releases/tag/v2.5.0)

    Version features: add support for 7 plugins, including Prometheus Exporter, Forward, OpenTelemetry, HTTP, MQTT, etc.; add support for Fluentd running as DaemonSet.

- [Fluent Bit log processing tool v2.0.0 release (CNCF project)](https://github.com/fluent/fluent-bit/releases/tag/v2.0.0)

     The main new features of this version: Add support for Traces (fully integrated with Prometheus and OpenTelemetry), allow the input plug-in to run in a separate thread, all network transport layers that need to be enabled will use OpenSSL, and the input plug-in will add native TLS functionality, support for integrating more plugin types with Golang and WebAssembly, support for inspecting data flowing through pipelines, and introduction of new input plugins that collect and process internal metrics.

- [Fluentd log collection tool v1.15.0 released (CNCF project)](https://github.com/fluent/fluentd/releases/tag/v1.15.0)

     The main new features of this version: support for setting rate limit rules for log collection, support for processing YAML configuration formats, and allow setting the time interval for restarting workers.

- [Flux Continuous Delivery Tool v2.0 Released (CNCF Project)](https://github.com/fluxcd/flux2/releases/tag/v2.0.0)

    Release features: GitOps-related API upgraded to v1; Flux controller adds horizontal scaling and sharding features; Git bootstrap feature upgraded to stable; build, release and proof parts of Flux project supply chain temporarily conform to SLSA Build Level 3; with Kubernetes Workload Identity Full integration with Kubernetes Workload Identity for AWS, Azure, and Google Cloud; Alerts feature optimization.

- [Flux continuous delivery tool becomes CNCF graduation project](https://mp.weixin.qq.com/s/3F3DHuKEZqqd7M6-im6B-A)

     [Flux](https://github.com/fluxcd/flux2) is a continuous progressive delivery solution for Kubernetes that supports GitOps and progressive delivery for developers and infrastructure teams. Since becoming a CNCF incubation project in March 2021, Flux and its sub-project Flagger have grown 200-500% in terms of user base, integrations, software usage, user engagement, contributions, etc.

- [Flux continuous delivery tool v0.34.0 released (CNCF project)](https://github.com/fluxcd/flux2/releases/tag/v0.34.0)

     Major new features in this version: Flux controller logs are consistent with Kubernetes structured logs, allow OCI sources to be defined for non-TLS container registries, and static credentials are preferred over OIDC providers when pulling OCI artifacts from container registries in multi-tenant clusters By.

- [Gatekeeper Policy Engine v3.13.0 Released (CNCF Project)](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.13.0)

    Release features: support for publishing audit information to PubSub systems, upgraded ExpansionTemplates for validating workload resources to beta, added experimental VAP driver for validating and reviewing resource object compliance, added support for external data provider audit caching, support for obtaining observability statistics on access, auditing, and gator CLI. Observability statistics for access, auditing, and the gator CLI.

- [Gatekeeper Policy Engine v3.10.0 release (CNCF project)](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.10.0)

     The main new features of this version are: removing Pod security policy and migrating to Pod security admission, upgrading Mutation feature to stable, introducing workload resource verification (alpha), and performance improvement.

- [Gatekeeper policy engine v3.9.0 release (CNCF project)](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.9.0)

     The main new features of this version: add constraint mode verification tests, add TLS support for external data providers, add pod security context variables, support verification sub-resources, allow skipping tests in gator verification, add dockerfile for gator, add opencensus and stackdriver exporter.

### H

- [Harvester Hyperconverged Infrastructure v1.2.0 released](https://github.com/harvester/harvester/releases/tag/v1.2.0)

    Release features: Reduced system footprint (better suited for edge scenarios), support for automatic resource limit adjustment, support for adding analog Trusted Platform Modules (TPMs) to VMs, support for SR-IOV network virtualization, new rancher-vcluster plug-in and bare-metal container support, support for installing third-party Container Storage Interfaces (CSIs) in Harvester clusters, support for per-node Pods, and more, and an increase in the per-node pod limit to 200.

- [HoloInsight: an intelligent observable platform open sourced by Ant Group](https://mp.weixin.qq.com/s/Tx7EKr0P_rhO-kltlW-wuQ)

    [HoloInsight](https://github.com/traas-stack/holoinsight) is an open source version of AntMonitor, an observation platform by Ant Group, which focuses on real-time log-based observation capabilities, business metrics monitoring, and timing intelligence and AIOps.
    It also incorporates other data types that have consensus in the observable domain, such as Trace, Event, etc.

- [HAProxy Kubernetes Ingress Controller v1.8 released](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-8/)

     The main new features of this version: reduce the permissions of all processes in the container, and no longer run the privileged container by default; expose an endpoint for viewing pprof diagnostic data; support the collection of Prometheus metrics inside the controller, such as the amount of memory allocated and spent CPU time; if the ingress rules do not match, it supports custom setting of the backend port.

- [Harbor Container Image Repository v2.9.0 released (CNCF project)](https://github.com/goharbor/harbor/releases/tag/v2.9.0)

    Release features: Administrators can access security information including the number of scanned and unscanned artifacts, dangerous artifacts, and CVEs; provides more detailed information to track garbage collection operations and supports enabling parallel deletion to accelerate the triggering and execution process of garbage collection; supports the OCI Distribution Specification v1.1.0-rc2 and adds support for Notation signatures and Nydus conversions; Introduces a new mechanism that uses Redis for optimistic locking to update quotas when pushing mirrors.

- [Harbor Container Container Registry v2.8.0 Released (CNCF Project)](https://github.com/goharbor/harbor/releases/tag/v2.8.0)

    Version features: support for OCI distribution spec v1.1.0-rc1, support for sending Webhook loads via CloudEvents format, support for skipping automatic update pull times for task scanners, removal of helm chart repository server ChartMuseum.

- [Harbor Container Container Registry v2.7.0 Released (CNCF Project)](https://github.com/goharbor/harbor/releases/tag/v2.7.0)

     Major new features in this release: adds Jobservice dashboard to monitor and control job queues, schedulers, and workers; supports per-block replication of mirror blob; adds WASM filter to artifact list.

- [Harbor Container Registry v2.6.0 release (CNCF project)](https://github.com/goharbor/harbor/releases/tag/v2.6.0)

     The main new features of this version: introduce a cache layer to improve the performance of fetching artifacts under high concurrency conditions; add CVE export function, allowing project owners and members to export CBR data generated by scanners; support regular cleaning of audit logs or run on demand, Support for forwarding audit logs to remote syslog endpoints; support for WebAssembly artifacts.

- [HashiCorp Vault private information management tool 1.11 adds Kubernetes Secret engine](https://github.com/hashicorp/vault/blob/main/website/content/docs/secrets/kubernetes.mdx)

     The Kubernetes Secret engine can dynamically generate Kubernetes service account tokens, service accounts, role bindings, and roles. The created service account token has a configurable TTL value (Time To Live), when the lease expires, Vault will automatically delete the created object. For each lease, Vault creates a token connected to the defined service account, and the service account token is returned to the caller.

- [Helm completes fuzzing test security audit](https://mp.weixin.qq.com/s/sMPjsKC6gy9VkhXzI2bvzw)

    A total of 38 fuzzers were written for [this audit](https://github.com/helm/community/tree/main/security-audit/FUZZING_AUDIT_2022.pdf), covering key parts of chart processing, version storage, and repository discovery.
    A total of 9 issues were found (8 fixed so far), including 4 null pointer reference issues, 4 out-of-memory issues, and 1 stack overflow issue.

- [Helm Package Manager v3.10.0 release (CNCF project)](https://github.com/helm/helm/releases/tag/v3.10.0)

     The main new features of this version: support to set json value through the command line, allow not to output the header when executing helm list, add parameters to configure client throttling limit, support to control whether to skip the certificate verification of kube-apiserver .

- [Helm Dashboard: Komodor open source Helm GUI](https://github.com/komodorio/helm-dashboard)

     The Helm Dashboard runs locally and opens in a browser, and can be used to view installed Helm Charts, view their revision history and corresponding k8s resources. In addition, it is possible to perform simple operations such as rolling back to a version or upgrading to a newer version.

- [Helm v3.9.0 release (CNCF project)](https://github.com/helm/helm/releases/tag/v3.9.0)

     The main new features of this version: new fields to support passing parameters to post renderer, more checks in the signing process, updated support for Kubernetes 1.24.

- [Higress: Alibaba Cloud Open Source Cloud Native Gateway](https://mp.weixin.qq.com/s/dgvd9TslzhX1ZuUNIH2ZXg)

     [Higress](https://github.com/alibaba/higress) follows the Ingress/Gateway API standard, combining traffic gateway, microservice gateway and security gateway, and extending the service management plug-in and security class on this basis Plug-ins and custom plug-ins are highly integrated with K8s and microservice ecology, including Nacos registration and configuration, Sentinel current limit and downgrade capabilities, and support hot update capabilities such as rule changes taking effect in milliseconds.

- [Horizon: a cloud-native application deployment platform open sourced by NetEase](https://mp.weixin.qq.com/s/hRuHQ5egP_vzLD4IdKiOvA)

    [Horizon](https://github.com/horizoncd/horizon) is a cloud-native continuous deployment platform based on Kubernetes and fully practices GitOps.
    Platform teams can customize and create versioned service templates to define uniform standards-compliant deployment and operations for business applications and middleware.
    Development teams can select pre-defined templates to automate service deployments and ensure uniform Kubernetes-based best practices. Ensure that any change (code, configuration, environment) is persistent, rollbackable, and auditable through Horizon GitOps mechanism.

- [HwameiStor Cloud Native Local Storage Becomes CNCF Sandbox Project](https://mp.weixin.qq.com/s/KvoQq24M8Pv4hDloVLtYVQ)

    On June 23, [HwameiStor](https://github.com/hwameistor/hwameistor), a cloud-native local storage open-sourced by "DaoCloud", was selected as a CNCF sandbox project with high votes. HwameiStor unifies the management of all local disks on system nodes to form a pool of different types of local storage resources and provides local data volume services through CSI standard interface to provide data persistence capability for stateful cloud-native applications or components.

### I

- [iLogtail: all codes of iLogtail observable data collector open source](https://mp.weixin.qq.com/s/Cam_OjPWhcEj77kqC0Q1SA)

     Recently, Alibaba Cloud officially released the community version of [iLogtail](https://github.com/alibaba/ilogtail) with full features.
     This update open-sources all C++ core codes, and this version aligns with the enterprise version for the first time in terms of core capabilities. Added many important features such as log file collection, container file collection, lock-free event processing, multi-tenant isolation, and new configuration methods based on Pipeline.

- [Ingress-NGINX Controller v1.7.0 Released](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.7.0)

    Version features: support for golang 1.20, removal of support for Kubernetes 1.23, integration with OpenTelemetry module.

- [Istio Service Mesh 1.19 released (CNCF project)](https://istio.io/latest/news/releases/1.19.x/announcing-1.19/)

    Release features: Gateway API v0.8.0 adds support for Service Mesh; Ambient Mesh adds support for `ServiceEntry`, `WorkloadEntry`, `PeerAuthentication`, and DNS proxies; support for optional client-side certificate validation; support for configuring non-Istio mTLS traffic cipher suites.

- [Istio Community Releases Istio 1.18 Performance Test Results](https://istio.io/latest/docs/ops/deployment/performance-and-scalability/)

    The Istio load test grid consists of 1000 services and 2000 sidecars with 70,000 grid-wide requests per second. The control plane supports thousands of services distributed across thousands of Pods. Data plane performance is affected by a variety of factors such as the number of client connections, request size and response size, the number of agent worker threads, protocols, CPU cores, and so on. each of the features injected by Istio may increase the internal path length of the agent, as well as affecting latency.

- [Istio Project Officially Graduates from CNCF](https://mp.weixin.qq.com/s/QaHU3OtLVFKPCz69z8176Q)

    Less than a year after entering the CNCF as an incubator project, Istio has become a CNCF graduate, the fastest project to graduate in CNCF history. Graduation from the CNCF means that Istio has become a key component of the modern application network, demonstrating that it is a proven, mature project that can be used to scale critical applications in production.

- [Istio Service Mesh v1.18 Released (CNCF Project)](https://istio.io/latest/news/releases/1.18.x/announcing-1.18/)

    Release features: release of Ambient Mesh, a data plane schema; several Kubernetes Gateway API improvements, including support for v1beta1 release, automatic deployment logic no longer relies on pod injection; concurrent configuration consistency across deployment types; Istioctl enhancements.

- [Istio Service Mesh v1.17 Released (CNCF Project)](https://istio.io/latest/news/releases/1.17.x/announcing-1.17/)

    Release features: Revision tag for Canary upgrade upgraded to Beta, Helm-based installation of Istio upgraded to Beta, full compatibility with the latest version of Kubernetes Gateway API (0.6.1), optimized IPv4/IPv6 dual-stack support, added support for listener filter patches, support for using the encryption and decryption technology QuickAssist Technology (QAT) PrivateKeyProvider.

- [Istio Announces 2022 Security Audit Results](https://istio.io/latest/blog/2023/ada-logics-security-assessment/)

     The audit found no critical issues, and a total of 11 security issues were identified, all of which have now been fixed. Of these, the only CVE vulnerability found was [Request Smuggling Vulnerability in Go](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721), the most common issue related to Istio getting files over the network.

- [Istio v1.16 Announcement (CNCF project)](https://istio.io/latest/news/releases/1.16.x/announcing-1.16/)

     The main new features of this version: Three features are upgraded to beta: external authorization function, Kubernetes Gateway API implementation, route-based JWT statement; add experimental support for HBONE protocol of sidecar and ingress gateway, support MAGLEV load balancing algorithm, and pass Telemetry The API supports the OpenTelemetry tracing provider.

- [Istio officially became a CNCF incubation project](https://istio.io/latest/blog/2022/istio-accepted-into-cncf/)

     The [Istio](https://github.com/istio/istio) Steering Committee submitted an application to hand over the project to CNCF in April this year. After nearly 5 months of review, it is now an incubating project.

- [Istio community launches Istio data plane mode Ambient Mesh without sidecar proxy](https://mp.weixin.qq.com/s/JpLPuqbPggXsQzFR5pii8A)

     [Ambient Mesh](https://github.com/istio/istio/tree/experimental-ambient) separates the data plane agent from the application pod and deploys it independently, completely solving the coupling problem between mesh infrastructure and application deployment.
     Through the introduction of zero trust tunnel (ztunnel) and Waypoint proxy (waypoint proxy) to achieve zero trust and reduce the resource occupation of the mesh, it can also seamlessly interoperate with the sidecar mode, reducing the user's operation and maintenance costs.

- [Istio v1.14 release](https://istio.io/latest/news/releases/1.14.x/announcing-1.14/change-notes/)

     Main new features of this version:

     - Traffic governance: support sending unready endpoints to Envoy; optimize egress traffic interception; relax the restrictions on setting SNI; support filter to replace virtual hosts; add API `runtimeValues` in Proxy Config for Envoy runtime configuration.
     - Security: Support for CA integration via Envoy SDS API, support for `PrivateKeyProvider` in SDS, support for TLS provisioning API for workloads.
     - Telemetry: Added OpenTelemetry access log, added `WorkloadMode` option to log.
     - Extension: Support WasmPlugin to pull images from private repositories via `imagePullSecret`.

### J

- [Jaeger Distributed Tracking System v1.46.0 Released (CNCF Project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.46.0)

    Version features: OTLP receivers enabled by default, added support for OpenTelemetry SpanMetrics connector.

- [Jaeger Distributed Tracing System v1.36.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.36.0)

     The main new features of this version: support for reporting span size metrics, and increase multi-tenant support.

- [Jaeger v1.35.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.35.0)

     The main new features of this version: introduce the ability to receive OpenTelemetry tracking data through the OpenTelemetry Protocol (OTLP), define health servers for GRPC servers, add flags for enabling/disabling dependencies during rollover, and add TLS configuration for Admin Servers.

- [Jaeger Distributed Tracing System v1.34.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.34.0)

     The main new features of this version: add kubernetes instances for hotrod applications, add streamingSpanWriterPlugin to improve the writing performance of grpc plugins, add metrics to MetricsReader, etc.

- [Jakarta EE 10 Java-based framework released, opening the era of cloud-native Java](https://mp.weixin.qq.com/s/BQBy5AWFOc7kS55JBtBjiQ)

     [Jakarta EE 10](https://github.com/jakartaee/jakarta.ee) introduces features for building modern and lightweight cloud-native Java applications.
     These include: a new configuration file specification that defines a multi-vendor platform for lightweight Java applications and microservices; a subset of the specification for smaller runtimes suitable for microservice development, including the New CDI-Lite specification; supports polymorphic types; standardizes UUID as a primitive type and extends the query language and query API.

### K

- [k0smotron: Mirantis open source Kubernetes control plane project k0smotron](https://www.mirantis.com/blog/introducing-k0smotron)

    [k0smotron](https://github.com/k0sproject/k0smotron) Essentially a set of Kubernetes controllers that enable you to run and manage multiple Kubernetes cluster control planes as pods in a single Kubernetes cluster. Enables true control plane and work plane separation, where the control plane running on an existing cluster has no direct network connection to the work plane. In addition, there is support for connecting worker nodes from any infrastructure to the cluster control plane.

- [k8gb Kubernetes Global Load Balancer v0.10.0 release (CNCF project)](https://github.com/k8gb-io/k8gb/releases/tag/v0.10.0)

     The main new features of this version: can access LeaderElection through environment variables, support the OpenTelemetry tracing scheme, support the creation of Grafana dashboard samples of K8GB metrics, and implement a consistent polling load balancing strategy.

- [KapacityStack: Cloud-native intelligent capacity technology open sourced by Ant Group](https://mp.weixin.qq.com/s/Wm4wj1OTANLYZaziRH2sDw)

    [KapacityStack](https://github.com/traas-stack/kapacity) provides IHPA (Intelligent Horizontal Pod Autoscaler) capabilities: supports scaling up and down using different algorithms for different scenarios; supports fine-grained control of each Pod's state throughout the The entire IHPA capability is split into three modules: control, decision, and execution, any of which can be replaced or extended.

- [Karmada Multi-Cloud Multi-Cluster Container Orchestration Platform v1.7.0 Released (CNCF Project)](https://github.com/karmada-io/karmada/blob/master/docs/CHANGELOG/CHANGELOG-1.7.md)

    Features: Introduces the CronFederatedHPA API for automatically adjusting the number of replicas of a workload at regular intervals; introduces the MultiClusterService API for controlling the exposure of a service to multiple external clusters and realizing service discovery between clusters; supports the preemption of resources according to the priority declaration reservation policy; supports the batch migration of resources without the need to terminate or restart a container; supports the batch migration of resources without the need to terminate or restart a container; supports the batch migration of resources without the need to terminate or restart a container; supports the batch migration of resources without the need to terminate or restart a container. support for batch migration of resources without container termination or restart; FederatedHPA support for adjusting the number of replicas based on customized metrics other than CPU and memory.

- [Karmada Multi-Cloud Multi-Cluster Container Orchestration Platform v1.6.0 Released (CNCF Project)](https://github.com/karmada-io/karmada/releases/tag/v1.6.0)

    Release features: Introduces FederatedHPA API to address the requirement of scaling workloads across clusters; supports automatic migration of unhealthy applications to other available clusters; introduces new declarative deployment method Karmada operator; supports third-party resource interpreters.

- [Karmada multicloud Multicluster Container Orchestration Platform v1.5.0 Released (CNCF Project)](https://github.com/karmada-io/karmada/releases/tag/v1.5.0)

    Release features: multiple scheduling groups support, default scheduler compatible with any third-party scheduler, built-in interpreter support for StatefulSet, default interpreter support for CronJob aggregation state, and PodDisruptionBudget.

- [Karmada multicloud multicluster container orchestration platform v1.4.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.4.0)

     The main new features of this version: new declarative resource interpreter, support for priority of declarative distribution strategy/cluster distribution strategy, enhanced observability through metrics and events, failover/elegant eviction FeatureGate is upgraded to Beta and enabled by default.

- [Karmada multicloud multicluster container orchestration platform v1.3.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.3.0)

     The main new features of this version: support taint-based elegant workload eviction, introduce global proxy for multicluster resource access, support cluster resource modeling, add Bootstrap token-based cluster registration method, optimize system scalability, etc.

- [Karmada cross-cloud multicluster container orchestration platform v1.2.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.2.0)

     The main new features of this version: optimize the scheduling strategy that changes over time; support cross-region deployment of workloads; `karmadactl` and `kubectl-karmada` support richer commands; add a distributed search and analysis engine for Kubernetes resources (alpha ); implement custom resource state collection.

- [Karpenter automatic scaling tool v0.19.0 released](https://github.com/aws/karpenter/releases/tag/v0.19.0)

     Major new features in this version: Evicting pods without a controller by default, migrating AWS settings from CLI Args to ConfigMap, supporting IPv6 auto-discovery, merging webhooks and controllers into one binary.

- [Kata Container Container Security Project v3.1.0 Released](https://github.com/kata-containers/kata-containers/releases/tag/3.1.0)

    Release features: support for AMD SEV-SNP confidential VMs; support for EROFS file system; improved Docker/Moby network support for improved runtime (runtime-rs), including adding support for large pages (hugepages); added QEMU logging capabilities; CRI-O and containerd 1.6.8 compatible; Support for Kubernetes 1.23.1-00.

- [Kata Containers Secure Container Runtime v3.0.0 released](https://github.com/kata-containers/kata-containers/releases/tag/3.0.0)

     The main new features of this version: a new Rust language rewritten container runtime component and an optional integrated virtual machine management component, support for mainstream cloud-native ecological components (including Kubernetes,CRI-O, Containerd, and OCI container runtime standards, etc.), supports cgroupv2, and supports the latest stable version of the Linux kernel.

- [Kata Container Container Security Project v2.5.0 release](https://github.com/kata-containers/kata-containers/releases/tag/2.5.0)

     The main new features of this version: support containerd shimv2 log plugin, support virtio-block multi-queue, support QEMU sandbox function, support containerd core scheduling, kata-runtime iptables subcommand can operate iptables in guest, and support directly allocated volumes.

- [Katalyst Cloud Native Resource Management System v0.3.0 released](https://github.com/kubewharf/katalyst-core/releases/tag/v0.3.0)

    Version features: KCNR API increases the ability to request, schedule, and allocate network bandwidth resources, and provides network bandwidth isolation capability in combination with EDT/TC and other speed-limiting schemes; new task execution framework; new asynchronous execution framework; algorithm realizes multi-CPU Region mode; mixed-sections capability enhancement.

- [Katalyst: byte-hopping open source cloud-native resource control system](https://mp.weixin.qq.com/s/A5_1h3RLmDNazmAddbhYaA)

    The main features of [Katalyst](https://github.com/kubewharf/katalyst-core) include: fully incubated in the mega-mixed-part practice and synchronously take over the resource control link in the byte service cloud-native process; equipped with ByteBeat's internal Kubernetes distribution Enhanced Kubernetes is synchronized with open source; the system is built based on plug-in model, and users can customize various scheduling, control, policy, data and other module plug-ins on Katalyst Framework.

- [KCL: Configuration Language KCL Becomes CNCF Sandbox Project](https://mp.weixin.qq.com/s/VbIIHj28DZZea3R4tYT66A)

    [KCL](https://github.com/kcl-lang/kcl) is an open source constraint-based record and function language that expects to improve the writing of a large number of complex configurations such as cloud-native Kubernetes configuration scenarios through mature programming language techniques and practices, and is committed to building a simpler logic authoring experience around the modularity, extensibility, and stability of configurations. We are committed to creating a simpler logic authoring experience and building simpler automation and eco-integration paths around configuration modularity, scalability, and stability.

- [KEDA: CNCF Announces KEDA Graduation for K8s Auto Scaler](https://mp.weixin.qq.com/s/Jkl8bGreQPk77VADOB-MOw)

    KEDA is an event-driven autoscaler designed specifically for Kubernetes. As a graduation project, the KEDA team plans to improve the project's performance, multi-tenant installation, monitoring, and observability features. It also plans to add the ability to configure scaling behavior and metrics evaluation, factor carbon and energy consumption into scaling evaluation, and predictive auto-scaling.

- [KEDA Event Driven Auto Scaler v2.11.0 Released (CNCF Project)](https://github.com/kedacore/keda/releases/tag/v2.11.0)

    Updates: New Solr Scaler; support for pause autoscaling; improved and extended Promethean metrics; ability to scale multiple scalers with CPU and memory scalers to zero if they are available.

- [KEDA Announces Security Audit Results Based on Kubernetes Event-Driven Autoscaling Project](https://mp.weixin.qq.com/s/ZwCg-qCeC2CMm7EbxJbi9w)

    The audit identified a significant flaw in Redis Scalers that could affect the confidentiality, integrity, or availability of the system.
    The issue was related to encryption and bypassing TLS, thus allowing for potential MitM (man-in-the-middle) attacks.
    The issue has now been fixed. In addition, based on the audit results, KEDA has updated the existing security toolchain to introduce the semgrep tool and TLS certificate management.

- [KEDA Event-Driven Autoscaler v2.9.0 Release (CNCF Project)](https://github.com/kedacore/keda/releases/tag/v2.9.0)

     The main new features of this version: add CouchDB, Etcd and Loki extensions, introduce Grafana dashboard for monitoring application auto-scaling, integrate all exposed Prometheus metrics in KEDA Operator, experimental support for extensions during polling intervals Cache metric values.

- [KEDA Kubernetes-based event-driven automatic scaling tool v2.8.0 released (CNCF project)](https://github.com/kedacore/keda/releases/tag/v2.8.0)

     The main new features of this version: support for NATS streaming, support for custom HPA names, support for specifying the minimum number of pod replicas in ScaledJob, and allow the cpu/memory scaler to scale only one container in the pod.

- [KEDA Kubernetes event-driven scaling tool v2.7.0 release (CNCF project)](https://github.com/kedacore/keda/releases/tag/v2.7.0)

     Major new features in this release: support for pausing autoscaling via ScaledObject annotations, new ARM-based container images, support for non-root KEDA default security mode, CPU, memory, Datadog extenders use global `metricType` instead of `metadata. type` etc.

- [Kelemetry: ByteBeat's open source global tracking system for Kubernetes control plane](https://mp.weixin.qq.com/s/qgiladzN-l6jGaSwiWZ-_Q)

    [Kelemetry](https://github.com/kubewharf/kelemetry) ties together the behavior of multiple Kubernetes components from a global perspective, tracing the complete lifecycle of a single Kubernetes object and the interactions between different objects. By visualizing event chains within a K8s system, it makes Kubernetes systems easier to observe, easier to understand, and easier to debug.

- [Keptn Cloud Native Application Lifecycle Orchestration Project v0.19.0 release (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.19.0)

     The main new features of this version: Helm-service and Jmeter-service moved to the keptn contribution repository, support for verifying inbound events, introduction of signed Keptn Helm charts, and support for signing all released/pre-released container images through sigstore/cosign.

- [Keptn Cloud Native Application Lifecycle Orchestration Project v0.18.0 release (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.18.0)

     The main new features of this version: install/uninstall/upgrade commands are not available, use Helm to operate Keptn instead; in the resource API, tail `/` will return 404; configuration service is deprecated, all core services of Keptn depend on resource service .

- [Keptn Cloud Native Application Lifecycle Orchestration Engine Upgraded to CNCF Incubation Project](https://mp.weixin.qq.com/s/gkv_fSnrRv0ao1AHUzBB5A)

     [Keptn](https://github.com/keptn/keptn) is an event-based control plane that uses declarative programming methods to achieve continuous delivery and automatic repair of applications. Keptn will support GitOps and control registry management methods, RBAC, remote management of execution planes, etc. in the future.

- [Keptn Cloud Native Application Continuous Delivery and Automated Operation Tool v0.16.0 released (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.16.0)

     Main new features of this version: `resource-service` replaces `configuration-service` to speed up response time and support Keptn upgrades without downtime; in v0.17, the CLI will remove install/uninstall/upgrade commands; support direct Sends events to Nats; service is considered ready only when connected to the control plane; allows running approval service without distributor sideCar.

- [Keycloak Identity and Access Management Project becomes a CNCF Incubation Project](https://www.cncf.io/blog/2023/04/11/keycloak-joins-cncf-as-an-incubating-project/)

    [Keycloak](https://github.com/keycloak/keycloak) provides centralized authentication and authorization of applications and APIs. Keycloak integrates well with cloud-native ecosystems.
    It supports running on Kubernetes and can be installed using Operator Framework built operators. It also provides Prometheus metrics and integrates with the standard Kubernetes stack.
    Many CNCF projects integrate directly with Keycloak for authentication and access, including Argo, Envoy, and Jaeger, among others.

- [Kindling Cloud-native observable tool v0.7.0 Released](https://github.com/KindlingProject/kindling/releases/tag/v0.7.0)

    Release features: provides a simple version of the view to display Trace Profiling data, adds tracing functionality to cpuevents, supports NoAPM Java applications with dependent agents.

- [Kindling Cloud-native observable tool v0.6.0 released](https://github.com/KindlingProject/kindling/releases/tag/v0.6.0)

     Main new features in this release: add tracing span data in cpu events, add debugging tool for Trace Profiling, support RocketMQ protocol.

- [Knative serverless architecture solution based on Kubernetes v1.11.0 released (CNCF project)](https://github.com/knative/serving/releases/tag/knative-v1.11.0)

    Release features: Domain Mapping Controller logic has been merged with Serving Controller, new fields for resource requests and limits when Queue Proxy is enabled (CPU and Memory only), Activator now has a separate service account, and support for configuring Queue Proxy resources via service level annotations.

- [Knative fuzz testing audit results announced](https://mp.weixin.qq.com/s/CeGpRJCwYkhrrfwgMR7AFw)

    As disclosed in [Knative fuzzing test report](https://github.com/knative/docs/blob/main/reports/ADA-knative-fuzzing-audit-22-23.pdf), this fuzzing test security audit for 3 Knative sub-projects 29 fuzz testers were written. These fuzz testers identified an issue in a third-party dependency that has now been fixed.

- [Knative Kubernetes-based serverless architecture solution v1.8.0 release (CNCF project)](https://github.com/knative/serving/releases/tag/knative-v1.8.0)

     The main new features of this version: modify the default domain, upgrade HPA to version v2, allow setting seccompProfile to enable the use of restricted security profiles, the minimum k8s support version is upgraded to v1.23, the reconciliation timeout is increased to 30 seconds, and EmptyDir is enabled by default Volume feature parameters.

- [Koordinator cloud-native hybrid system v1.0 released](https://github.com/koordinator-sh/koordinator/releases/tag/v1.0.0)

     The main new features of this version are: optimized task scheduling, optimized ElasticQuota scheduling, support for fine-grained device scheduling management mechanism, support for adjusting the CPU resource quota of BestEffort type Pod according to the load level of the node, support for using CPU Burst to improve the performance of delay-sensitive applications, Realize the eviction mechanism based on memory safety threshold and resource satisfaction, fine-grained CPU scheduling, support resource reservation without intruding Kubernetes' existing mechanisms and codes, and simplify the operation of custom rescheduling strategies.

- [Koordinator cloud-native hybrid system v0.6.0 released](https://github.com/koordinator-sh/koordinator/releases/tag/v0.6.0)

     The main new features of this version: improve the CPU fine-grained orchestration strategy, support resource reservation without intruding on the existing mechanisms and codes of Kubernetes, support Pod MigrationJob, and release a new Descheduler framework.

- [Kruise Rollout Progressive Delivery Framework v0.2.0 released](https://openkruise.io/docs/)

     The main new features of this version are: support for Gateway API, support for batch release of stateful applications, new "Pod batch marking" capability, integration into KubeVela to realize Helm Charts canary release capability.

- [KSOC Labs Releases First Kubernetes Bill of Materials (KBOM)](https://www.infoq.com/news/2023/06/kubernetes-bill-of-materials/?topicPageSponsorship=6dafd62c-9925-4408-bfda-e96bc971c941)

    [KBOM](https://github.com/ksoclabs/kbom) is an open source standard and command line tool that helps security teams quickly analyze cluster configurations and respond to CVEs. The project includes an initial specification and implementation plan that can be used across cloud providers, on-premise, and custom environments. Security and specification teams can gain greater visibility into their Kubernetes clusters (especially the three-party plug-in) using KBOM to quickly identify vulnerabilities and maintain them.

- [Kuasar: a multi-sandbox container runtime officially open-sourced by Huawei Cloud in association with several units](https://mp.weixin.qq.com/s/pXBZ-U1KF0_bNU8u6MOv8A)

    [Kuasar](https://github.com/kuasar-io/kuasar) further reduces management overhead, simplifies invocation traces, and extends support for mainstream sandbox technologies by retaining traditional container runtime functionality through comprehensive Rustification and optimizing management models and frameworks. In addition, by supporting multi-security sandbox co-node deployment, Kuasar can fully utilize node resources to achieve cost reduction and efficiency.

- [KubeAdmiral byte-jumping open source K8s-based next-generation multi-cluster orchestration scheduling engine](https://mp.weixin.qq.com/s/aS18urPF8UB4K2I_9ECbHg)

    [KubeAdmiral](https://github.com/kubewharf/kubeadmiral) is based on the Kubernetes Federation v2 iterative evolution, designed to provide cloud-native multi-cloud multi-cluster management and application distribution capabilities. KubeAdmiral builds on its enhancements KubeAdmiral: compatible with native Kubernetes API; provides a more flexible scheduling framework and supports rich scheduling distribution policies; differentiated policies; dependent scheduling/following scheduling; provides a framework for state collection and provides more flexible state collection.

- [KubeClipper K8S Cluster Lifecycle Management Service Becomes CNCF Sandbox Project](https://mp.weixin.qq.com/s/UEFtUZR8BZX9pK_PYsAWlA)

    [KubeClipper](https://github.com/kubeclipper/kubeclipper) is based on the Kubeadm package, which allows users to manage host nodes through a web interface, API, or command line tool (kcctl), to quickly create and delete K8S clusters, and to perform nano-management of existing K8S clusters can be quickly created and deleted, and existing K8S clusters can be managed, upgraded, configured, deployed, and scaled up or down.

- [KubeClipper: K8s multicluster lifecycle management tool open sourced by Kyushu Cloud](https://mp.weixin.qq.com/s/RVUB5Pw6-A5zZAQktl8AcQ)

     [KubeClipper](https://github.com/KubeClipper-labs) is based on the kubeadm tool for secondary packaging, providing rapid deployment of K8S clusters and continuous full lifecycle management (installation, uninstallation, upgrade, scaling, remote access, etc.) capabilities,
     It supports multiple deployment methods such as online, proxy, and offline, and also provides rich and scalable management services for CRI, CNI, CSI, and various CRD components.

- [KubeEdge Sedna v0.6 & Ianvs SideCloud Collaborative Lifelong Learning Program v0.2 Released](https://mp.weixin.qq.com/s/OQdNmmzRl4GC_ZssU4vatQ)

    Release features: supports open-world edge cloud collaborative lifelong learning in unstructured data scenarios; provides a complete test suite of open-source datasets, baseline algorithms, and evaluation metrics; develops new unknown task identification and processing capabilities for robot inspection, autonomous driving, and other scenarios, including new sample identification, training data generation, and multi-model joint inference.

- [KubeEdge Reaches Software Supply Chain SLSA L3 Level](https://mp.weixin.qq.com/s/5kpbnE-F__HqlF0JAwCOSg)

    In the recent v1.13.0 release, the KubeEdge project has reached [SLSA](https://slsa.dev/) L3 level (including binary and container image artifacts), making it the first project in the CNCF community to reach SLSA L3 level.
    This means that KubeEdge can be securely hardened from end-to-end from the source build to the release process to protect the binary or container image products obtained by users from malicious tampering.

- [KubeEdge cloud-native edge computing platform v1.12 release (CNCF project)](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.12.md)

     The main new features of this version: the introduction of the next generation of cloud-native device management interface (DMI), the new version of the lightweight engine Edged upgraded to GA, EdgeMesh new high-availability mode, support for edge nodes to upgrade from the cloud, support for edge Kube-API endpoints Authorization, support GigE Device Mapper.

- [KubeEdge Audit Report Release](https://github.com/kubeedge/community/blob/master/sig-security/sig-security-audit/KubeEdge-security-audit-2022.pdf)

     OSTIF (Open Source Technology Improvement Fund, Open Source Technology Improvement Foundation) completed a security audit of KubeEdge. The audit found 12 medium-severity issues, a threat model was built, and integrated into OSS Fuzz. The KubeEdge security team has fixed all issues in the newly released v1.11.1, v1.10.2 and v1.9.4.

- [KubeEdge cloud-native edge computing platform v1.11.0 release (CNCF project)](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.11.md)

     The main new features of this version: new node group management function; edge device Mapper SDK is provided to reduce the workload of developing Mapper; Keadm subcommands such as containerized deployment and offline security are officially supported; edge node agent Edged is applicable to more use cases.

- [KubeKey Cluster Deployment Tool v3.0 released](https://github.com/kubesphere/kubekey/releases/tag/v3.0.0)

     Main new features of this version: Add GitHub workflow for docker build and push, support for executing custom setup scripts, add k3s control plane controller and startup controller, add k3s container runtime configuration, add k3s e2e test support, customize OpenEBS Base path, refactor KubeKey project, support more Kubernetes and k3s versions.

- [Kubeflow: Kubeflow, the Machine Learning Platform for Kubernetes, upgraded to become a CNCF Incubation Project](https://mp.weixin.qq.com/s/8bZr2Edmyh-unE5ghIBhJg)

    Kubeflow is an open source, community-driven project for deploying and managing Machine Learning (ML) stacks on Kubernetes.The Kubeflow community actively develops and supports MLOps for Kubernetes, developing and deploying popular frameworks for its users, including TensorFlow, PyTorch, XGBoost, Apache MXNet, and other distributed machine learning (ML).

- [KubeKey cluster deployment tool v2.3.0 released](https://github.com/kubesphere/kubekey/releases/tag/v2.3.0)

     The main new features of this version: add kubelet pod pid restrictions, use Jenkins Pipeline instead of GitHub Actions, add security enhancement commands when creating clusters or adding nodes, clear vip when deleting clusters or nodes, support kube-vip BGP mode, support cleaning CRI, Support kube-vip, support the latest patch version released by k8s.

- [KubeKey cluster deployment tool v2.1.0 released (KubeSphere community open source)](https://github.com/kubesphere/kubekey/releases/tag/v2.1.0)

     The main new features of this version: According to the OCI standard, the image pulling, uploading, archiving and saving features are realized, so that it does not rely on additional container runtimes when making and using KubeKey products; it supports the initialization of the operating system command (kk init os) Use products to install operating system dependencies from offline local sources; support both ARM64 nodes and AMD64 nodes in the same K8s cluster.

- [Kube-OVN CNI plugin v1.12.0 released (CNCF project)](https://github.com/kubeovn/kube-ovn/releases/tag/v1.12.0)

    Features: optimize the way of calling OVN interfaces from the bottom layer; support remote mirroring of traffic; support IPSec encryption of traffic across nodes in the cluster; support one-click collection of all Kube-OVN-related component logs, dmesg information, iptables rules, and other network-related details through the kubectl-ko plug-in; realize the interoperability between Overlay and Underlay networks. Overlay and Underlay network interoperability; add CRD resources for IPPool; add policy NAT function; add OVN native gateway types.

- [Kube-OVN CNI Plugin v1.11.0 Released (CNCF Project)](https://github.com/kubeovn/kube-ovn/releases/tag/v1.11.0)

    The main new features of this version: Underlay and Overlay subnet interoperability, new SR-IOV Network Operator for automated NIC configuration, support for custom VPC internal load balancing, new vpc-dns CRD, support for Load Balancer type service under default VPC.

- [Kube-OVN v1.10.0 release (CNCF project)](https://mp.weixin.qq.com/s/e1TW_s3r9__qSgZz6aWmAA)

     The main new features of this version: ACL field is added in the subnet, and users can write ACL rules that conform to the OVN flow table specification according to their own needs; in the KubeVirt scenario, the address allocation strategy of VM instance adopts a strategy similar to that of StatefulSet, and supports DPDK, DHCP; Integrated SubMariner is used for the interconnection of multiple clusters; for large-scale environments, the performance of the control plane is optimized.

- [Kubernetes Gateway API v0.8.0 released](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v0.8.0)

    Release features: Introduction of Service Grid support, support for CEL authentication (fully supported in Kubernetes 1.25+ only).

- [Kubernetes Cluster API v1.4.0 Released](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.4.0)

    Release features: support for automatic failback in case of KCP control plane deployment failure, support for synchronizing certain tags from Machine to Node, propagation of tags, annotations, etc. from ClusterClass to KubeadmControlPlane/MachineDeployment and Machine, support for Variable discovery in ClusterClass and Managed Topologies.

- [Kubernetes v1.28 release](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md)

    Release features: support for deviation changes between control plane and node versions, non-graceful shutdown of nodes GA, CRD Common Expression Language (CEL)-based validation rules Beta, Kube APIServer Hybrid Version Interoperability Proxy Alpha, new Common Control Plane Repository Alpha, Device Plugin APIs add support for CDI-standard devices Alpha, native support for Sidecar containers Alpha, node Swap memory support Beta, new support for Windows nodes Beta. Alpha, Native Support for Sidecar Containers Alpha, Node Swap Memory Support Beta, Added Support for Windows Nodes Beta.

- [Kubernetes v1.27.0 released](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#changelog-since-v1260)

    Release features: freeze k8s.gcr.io container registry, upgrade SeccompDefault to GA, upgrade Job variable scheduling directive to GA, upgrade Pod scheduling Readiness to beta, allow access to node logs via Kubernetes API, introduce new access mode ReadWriteOncePod to limit volume Access is restricted to a single Pod in the cluster, and VolumeManager rebuild is upgraded to beta.

- [Kubernetes third-party audit based on the 1.24 release](https://www.cncf.io/blog/2023/04/19/new-kubernetes-security-audit-complete-and-open-sourced/)

    [This audit](https://github.com/kubernetes/sig-security/blob/main/sig-security-external-audit/security-audit-2021-2022/findings/Kubernetes%20v1.24%20Final%20Report.pdf) found the following issues: problems in restricting user or network privileges, which could lead to administrators obfuscating the privileges available to specific components; vulnerabilities in inter-component authentication, where a malicious user could gain cluster administrator privileges; flaws in logging and auditing, which could be exploited by an attacker after taking control of the The flaws in logging and auditing could be exploited by attackers to potentially conduct activities after taking control of the cluster; and vulnerabilities in user input filtering could allow authentication to be bypassed by modifying requests to the etcd datastore.

- [Kubernetes v1.26 released](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md)

     The main new features of this version: allow users to configure volumes from volume snapshots across namespaces, allow admission control using CEL, improve multi-numa alignment in topology manager, add a scheduling-ready mechanism for Pod scheduling, remove CRI v1alpha2, Auth API allows to fetch User properties, reducing Kubelet's CPU consumption in PLEG.

- [Kubernetes 1.26 First Look](https://sysdig.com/blog/kubernetes-1-26-whats-new/)

     Kubernetes 1.26 is about to be released and includes 37 enhancements, 11 will be upgraded to stable, 10 will be improvements to existing features, 16 will be new features, and one will be deprecated.
     Among them, there is a new feature that is very noteworthy and may change the way users interact with Kubernetes-provisioning volumes with snapshots of other namespaces.
     There are also new features for high-performance workloads like machine learning, and features to simplify operations for cluster administrators (support for OpenAPIv3).

- [Kubernetes Publishes Kubernetes CVE Feed List](https://kubernetes.io/blog/2022/09/12/k8s-cve-feed-alpha/)

     Kubernetes now supports tracking Kubernetes security issues (also known as "CVE", a database of common security issues from various products and vendors).

- [Kubernetes v1.25 release (CNCF project)](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md)

     Main new features of this version: upgrade to Stable: Pod Security Admission, temporary container, cgroups v2 support, endPort in network policy, local temporary storage capacity isolation, core CSI Migration, CSI temporary volume upgrade; upgrade to Beta: SeccompDefault, CRD verification Expression language; introduction of KMS v2 API, etc.

- [Kubernetes v1.24.0 release (CNCF project)](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md)

     The main new features of this version: dockershim components are removed from kubelet; the new beta API is turned off by default; published artifacts are signed with cosign, and experimental support for verifying image signatures is provided; storage capacity tracking is supported to show currently available storage Capacity and volume scaling; gRPC probe and kubelet credential provider upgrades to Beta; allowing soft-reserved allocation of a range of static IP addresses for services; and more.

- [Kubernetes Gateway API v0.5.0 released](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v0.5.0)

     The main new features of this version: three APIs have been upgraded to beta: `GatewayClass`, `Gateway` and `HTTPRoute`; the introduction of experimental and standard version channels; routing can be connected to the gateway by specifying the port number; URL rewriting and routing are supported redirect.

- [kube-rs Rust client for Kubernetes v0.79.0 released (CNCF project)](https://github.com/kube-rs/kube/releases/tag/0.79.0)

    Release features: add support for metadata api to reduce network load, expose default namespace for clients, allow event subscription from watcher without consuming raw watcher stream, support for persistent metadata watch.

- [KubeSkoop: Kubernetes network monitoring tool open sourced by Alicloud](https://mp.weixin.qq.com/s/zbAcZCNT5vyzGvp7uTDB1w)

     [KubeSkoop](https://github.com/alibaba/kubeskoop) supports features including: Pod-level network monitoring, including traffic, application-level connection information, socket memory allocation status, etc.; Pod-level monitoring of metrics for abnormal network status, such as the wait time for a Pod process to perform a socket Pod-level network abnormal state metrics monitoring, such as the number of times a process within a Pod waits more than 100ms for a read or write operation, etc.; Pod-level network abnormal events on site, providing detailed observation of the events that occur.

- [KubeSphere Multi-Tenant Container Platform v3.4.0 released (CNCF project)](https://github.com/kubesphere/kubesphere/releases/tag/v3.4.0)

    Release features: add golangci-lint workflow for node checking, integrate opensearch v1/v2, add admission webhook for rulegroup, add alerting v2beta1 api, support for filtering workspace roles using tag selector, add dynamic options for caching, add helm executor generic package, generate helm executor generic package, generating CRDs to support multiple versions, support for gitlab identity providers, support for node- and workload-wide global rules, and support for pluggable notification features.

- [KubeSphere v3.3.0 release (CNCF project)](https://github.com/kubesphere/kubesphere/blob/master/CHANGELOG/CHANGELOG-3.3.md)

     Main new features of this version:

     - DevOps: The backend supports independent deployment, provides a GitOps-based continuous deployment solution, introduces Argo CD as the backend of CD, and can count the status of continuous deployment in real time.
     - Network: The integrated load balancer OpenELB can expose the LoadBalancer service even under the K8s cluster in a non-public cloud environment.
     - Multi-tenancy and multicluster: Cluster applications can obtain the name of the cluster through a ConfigMap, and support setting cluster members and cluster roles for the cluster.
     - Observability: Add container process/thread metrics, optimize disk usage metrics, and support importing Grafana templates in namespace custom monitoring.
     - Storage: Support PVC automatic expansion policy, support management of volume snapshot content and type, and support setting authorization rules for storage types.
     - Edge: KubeEdge integrated.

- [Kubespray Kubernetes Cluster Deployment Tool v2.22.0 released](https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.22.0)

    Release features: support for multi-architecture mirroring under the same mirror name, add DNS configuration for cert-manager, add kube-profile configuration to kube-scheduler configuration, allow configuration of mirror garbage collection, support for custom ssh ports, support for control plane load balancing with kube-vip enabled.

- [Kubespray Kubernetes cluster deployment tool v2.20.0 released](https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.20.0)

     Main new features of this version: Support Rocky Linux 8 and Kylin Linux, add "flush ip6tables" task in reset role, support NTP configuration, add kubelet systemd service hardening option, add rewrite plugin for CoreDNS/NodelocalDNS, add SeccompDefault for kubelet admission plugin, add extra_groups parameter for k8s_nodes, add ingress nginx webhook, add support for node and pod pid restrictions, and enable default Pod security configuration.

- [KubeVela Hybrid multicloud App delivery Platform v1.8.0 Released (CNCF Project)](https://github.com/kubevela/kubevela/releases/tag/v1.8.0)

    Release features: support for horizontal scaling of the control plane through multiple slices, support for language-aware SDK generation from existing KubeVela definitions, new workflow-based trigger kube-trigger, allows application developers to orchestrate the app delivery process in the style of a canary release.

- [KubeVela Upgrades to CNCF Incubation Program](https://mp.weixin.qq.com/s/mhH9u4aXJT2-qVwf06xn5Q)

    [KubeVela](https://github.com/kubevela/kubevela) is built with the Kubernetes control plane, making it easier, faster, and more reliable to deploy and operate applications across hybrid and multicloud environments.
    Going forward, the KubeVela community plans to improve the user experience of cloud resource creation and consumption through delivery workflows that enhance the security of the entire CI/CD delivery process in hybrid/multicluster use cases.
    Support for the KubeVela Dynamic API that allows users to easily integrate with third-party APIs, and more.

- [KubeVela hybrid multicloud environment app delivery platform v1.6.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.6.0)

     The main new features of this version: support resource delivery visualization, provide observable infrastructure construction, application-oriented observability, observability as code capabilities, support unified management of multi-environment pipelines, support configuration sharing between applications and third-party external systems Do configuration integration.

- [KubeVela hybrid multicloud environment app delivery platform v1.5.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.5.0)

     Main new features of this version: Plug-in framework optimization, providing management of the entire plug-in lifecycle such as creating scaffolding, packaging, and pushing to the plug-in registry; supporting defining plug-ins in CUE format, and using CUE parameters to render some plug-ins; adding a large number of vela cli command; VelaUX supports managing applications created by the CLI.

- [KubeVela v1.4.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.4.0)

     The main new features of this version: support multicluster authentication, automatic login of controllers using kubeconfig, support for more authorization methods; allow resources to be selected by resource type in GC policies, and new policy controllers to generate OpenAPI patterns for VelaUX and CLI parameters ; CLI supports displaying resource topology, etc.

- [KubeVirt Virtual Machine Operations Project v1.0 Released (CNCF Project)](https://github.com/kubevirt/kubevirt/releases/tag/v1.0.0)

    Release features: removes hot-plugging VMI API, introduces CPU hot-plugging, experimental support for AMD's Secure Encryption Virtualization (SEV), supports setting minimum resource requirements for CPU and memory in preferences, supports hot-plugging of network interfaces on VirtualMachine objects, supports specifying cluster-level VM behavior, adds multi-architecture support, allows specifying the memory of created VMs, allows specifying the memory of created VMs, allows specifying the memory of created VMs, and allows specifying the memory of created VMs when creating VMs. The support for cloning and exporting virtual machines supports RBAC configuration.

- [KubeVirt Virtual Machine Management Plugin v0.58.0 released (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.58.0)

     Major new features in this release: Enable DataVolume garbage collection by default in cluster-deploy, ability to run with restricted Pod security enabled, add tls configuration, fix migration failure for VMs with containerdisks on systems with containerd.

- [KubeVirt Virtual Machine Management Plugin v0.57.0 released (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.57.0)

     The main new features of this version: deprecated SR-IOV live migration feature gate, deprecated virtual machine instance preset resources, added support for virtual machine output resource types, supported DataVolume garbage collection, and allowed support for configuring virtual machine topology distribution constraints .

- [KubeVirt virtual machine running project v0.55.0 release (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)

     The main new features of this version: introduce clone CRD, controller and API, introduce deprecation policy, increase memory overhead of virt-launcher, enable memory dump to VMSnapshot, support monitoring VMI migration objects from creation to a specific stage required time, allowing the VMI to migrate from root to non-root.

- [KubeVirt virtual machine running project v0.55.0 release (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)

     The main new features of this version: introduce clone CRD, controller and API, introduce deprecation policy, increase memory overhead of virt-launcher, enable memory dump to VMSnapshot, support monitoring VMI migration objects from creation to a specific stage required time, allowing the VMI to migrate from root to non-root.

- [Kubewarden Kubernetes Policy Engine v1.0.0 Release (CNCF Project)](https://www.kubewarden.io/blog/2022/06/v1-release/)

     The main new features of this version are: allowing policies to be written in Go, Rust or Swift, supporting the use of Kubewarden policies to replace each Pod Security Policy, integrating OpenTelemetry, and using the Sigstore project to implement software signing and verification.

- [KubeWharf: Bytedance Open Source Cloud Native Project Collection](https://mp.weixin.qq.com/s/uNbT3Ss0rBYc9pqlZe3n8Q)

     [KubeWharf](https://github.com/kubewharf) is a distributed operating system based on Kubernetes, which consists of a set of cloud-native components, focusing on improving system scalability, resource utilization, and scalability. Observability, security, etc., support Cases such as large-scale multi-tenant clusters, offline mixing, and storage.
     The first batch of KubeWharf plans to open source three projects: KubeBrain, a high-performance meta-information storage system, KubeGateway, a seven-layer gateway for kube-apiserver, and KubeZoo, a lightweight multi-tenant solution.

- [Kuma service mesh Project v2.2.0 Released (CNCF Project)](https://github.com/kumahq/kuma/releases/tag/2.2.0)

    Release features: support for OpenTelemetry, support for defining MeshProxyPatch policies using JSONPatch, support for retry directives and priorities, upgrade the underlying Envoy version to 1.25, new policies for more fine-grained control of load balancing between services, support for deploying generic patterns in Kubernetes clusters for global Support for global control plane deployment in Kubernetes clusters (supported by Postgres), and support for providing public keys for offline token signing and verification.

- [Kuma Service Mesh v2.0 release (CNCF project)](https://github.com/kumahq/kuma/releases/tag/2.0.0)

     The main new features of this version: add support for eBPF in CNI and init container configuration, add 3 new "next generation" policies, optimize the user interface, support the configuration of TLS versions and ciphers supported by the control plane/API server, allow configuration Multiple UIDs make it ignored by traffic redirection, allowing logging to be turned on when using iptables for traffic redirection.

- [Kuma Service Mesh Project v1.8.0 release (CNCF project)](https://github.com/kumahq/kuma/releases/tag/1.8.0)

    The main new features of this version: cross-mesh gateway supports multi-region operation, mesh gateway/built-in gateway adds observability function, rewrites CNI, mesh gateway supports path rewriting and header addition/deletion, supports filtering proxy metrics, Simplify the implementation of TCP traffic logs and support Projected Service Account Tokens.

- [Kurator Distributed Cloud Native Platform v0.3.0 Released](https://github.com/kurator-dev/kurator/releases/tag/v0.4.0)

    Update: New module application manager to distribute applications/configurations across Fleet via GitOps; add metrics plugin to support unified monitoring of multiple clusters; new policy manager to provide consistent security policies.

- [Kurator Distributed Cloud Native Platform v0.3.0 Released](https://github.com/kurator-dev/kurator/releases/tag/v0.3.0)

    Release Features: Adds a CRD cluster to the Cluster API, allowing users to manage the lifecycle of a kubernetes cluster by simply declaring an API object; supports kubernetes cluster upgrades; supports kubernetes cluster scaling; supports setting up a highly available kubernetes cluster locally.

- [Kurator Distributed Cloud Native Platform v0.2.0 Released](https://github.com/kurator-dev/kurator/releases/tag/v0.2.0)

    Release features: support for Thanos-based multicluster monitoring and metrics persistence storage; support for Pixie-based real-time K8s application monitoring; new component Cluster Operator to manage the kubernetes cluster lifecycle for various infrastructures, including public clouds, hybrid clouds and local data centers, in a cloud-native way.

- [KusionStack: Ant Group's open source programmable cloud-native protocol stack](https://mp.weixin.qq.com/s/EZrVKdZ_hG5-p_HltaTCMg)

     [KusionStack](https://github.com/KusionStack) deposits the operation and maintenance model ([Kusion Model](http://github.com/KusionStack/konfig)) through the self-developed DSL (KCL), and the infrastructure part The use of capabilities is changed from white screen to code, and combined with the DevOps tool chain (Kusion CLI) to achieve rapid configuration verification and validation, so as to improve the openness and operation and maintenance efficiency of the infrastructure.

- [Kusk Gateway Self Service API Gateway v1.1.0 Release](https://github.com/kubeshop/kusk-gateway/releases/tag/v1.1.0)

     The main new features of this version: support for specifying services or hosts to verify authentication headers, support for rate limiting policies, simplify the complexity of HTTP caching by annotating in the OpenAPI specification, and handle all mocking locally by Envoy.

- [Kyma Cloud Native Application Development Platform and Runtime v2.15.0 Released](https://github.com/kyma-project/kyma/releases/tag/2.15.0)

    Release features: plan to reorganize telemetry components into one module; keep webhook CA bundles stable during Pod restarts and webhook modifications; added default timeout for HTTP requests; simplified Serverless configuration for internal Docker registry; support for otel-collector 0.77.0.

- [Kyverno Cloud Native Policy Engine v1.10.0 Released (CNCF Project)](https://github.com/kyverno/kyverno/releases/tag/v1.10.0)

    Release features: split Kyverno into 3 separate controllers/deployments, support for intra-cluster service calls, support for verifying Notary v2 signatures, update generation and change of existing policies.

- [Kyverno Cloud Native Policy Engine v1.8.0 release (CNCF project)](https://github.com/kyverno/kyverno/releases/tag/v1.8.0)

     The main new features of this version: add podSecurity verification sub-rules, integrate Pod Security Admission library; support YAML manifest signature verification; allow generation rules to generate multiple resources in a single rule; support OpenTelemetry; support test generation policies; support Kubernetes 1.25.

- [Kyverno cloud-native strategy engine upgraded to CNCF incubation project](https://mp.weixin.qq.com/s/GijHJm6-JcqfcLn91vSs6g)

     [Kyverno](https://github.com/kyverno/kyverno) is a policy engine built for Kubernetes that provides automation and security for K8s configuration management.
     Next, the project plans to add features such as YAML signing and verification, OpenTelemetry support, idempotent auto-generated pod controller policies, enhanced pod security standard integration, OCI-based policy bundling, in-cluster API calls, and more.

- [Kyverno Cloud Native Policy Engine v1.7.0 release (CNCF project)](https://github.com/kyverno/kyverno/releases/tag/v1.7.0)

     Main new features of this version: support query `mutate.target` via dynamic client, allow Kyverno jp to work on Yaml files, optimize image verification signatures, mutate existing resources when policies are updated, allow users to define inline variables in context, disable leader election for update request controllers, support apiCall and CLI updates in tests, etc.

### L

- [Lima Linux Virtual Machine v0.14.0 release (CNCF project)](https://github.com/lima-vm/lima/releases/tag/v0.14.0)

     The main new features of this version: support for virtual machine shared file system virtiofs, support for Apple's virtualization framework Virtualization.framework, and support for Containerd command-line tool nerdctl 1.1.0.

- [Linkerd Service Grid v2.14.0 released (CNCF project)](https://github.com/linkerd/linkerd2/releases/tag/stable-2.14.0)

    Release features: New direct Pod-to-Pod multi-cluster service mirroring, support for Gateway API HTTPRoute resources.

- [Linkerd service mesh Project v2.13.0 Released (CNCF Project)](https://github.com/linkerd/linkerd2/releases/tag/stable-2.13.0)

    Release features: Introduces client-side policies, including dynamic routing and fuser mode; supports debugging HTTPRoute-based policies; introduces a new init container -- network-validator -- to ensure that local iptables rules work as expected.

- [Linkerd Service Mesh Project v2.12.0 Release (CNCF Project)](https://github.com/linkerd/linkerd2/releases/tag/stable-2.12.0)

     The main new features of this version: allow users to define and run authorization policies based on HTTP routes in a completely zero-trust manner; support configuration using the Kubernetes Gateway API; add support for `iptables-nft` to the initialization container.

- [Litmus Chaos Engineering Framework v2.14.0 release (CNCF project)](https://github.com/litmuschaos/litmus/releases/tag/2.14.0)

     The main new features of this version: Add support for containerd CRI in DNS experiment, support for http-chaos experiment in service mesh environment, add support for source and destination ports in network experiment, support for providing custom labels for chaos runner pods, Optimizing the description of probe state patterns in chaotic results.

- [Litmus Chaos Engineering Framework v2.10.0 release (CNCF project)](https://github.com/litmuschaos/litmus/releases/tag/2.10.0)

     The main new features of this version: add HTTP chaos experiments for Kubernetes applications; introduce m-agent (machine agent), which can now implement chaos on non-k8s objects; optimize the recovery of node warning line experiments when application status checks fail during chaos; Added support for Envoy proxy when using frontend nginx; optimized logging, etc. Litmusctl updates.

- [Longhorn Cloud Native Distributed Block Storage v1.5.0 Released (CNCF Project)](https://github.com/longhorn/longhorn/releases/tag/v1.5.0)

    Updates: Launched V2 data engine based on SPDK (Storage Performance Development Kit), upgraded Cluster Autoscaler feature to GA, merged Instance Manager engine and Replica, supported different volume backup compression methods, automated volume deletion operations, managed backup images via CSI VolumeSnapshot, added snapshot cleanup and deletion jobs, supported CIFS and CIFS. and delete jobs, support for CIFS backup storage and Azure backup storage protocols, and a new Kubernetes upgrade node exhaustion policy.

- [Longhorn Cloud Native Distributed Block Storage v1.4.0 Released (CNCF Project)](https://github.com/longhorn/longhorn/releases/tag/v1.4.0)

     Main new features in this release: Kubernetes 1.25 support, ARM64 support upgraded to GA, network file system NFS support upgraded to GA, volume snapshot checksum support, volume Bit-rot protection support, improved rebuild speed for volume replication, support for reclaiming space by deleting old snapshots, online volume expansion support, allowing users to Create a replica volume that stays in a consistent location, increase I/O metrics for volumes, and support backup and restore of Longhorn systems.

- [Longhorn Cloud Native Distributed Block Storage v1.3.0 release (CNCF project)](https://github.com/longhorn/longhorn/releases/tag/v1.3.0)

     Main new features of this version: support for multi-network K8s clusters, compatibility with fully managed K8s clusters (EKS, GKE, AKS), new Snapshot CRD, new Mutating & Validating admission webhooks, support for automatic identification and cleaning of unowned/unused volumes, introduce CSI snapshots, and support cluster expansion through Kubernetes Cluster Autoscaler.

### M

- [Merbridge: The service mesh accelerator open sourced by DaoCloud has officially entered the CNCF sandbox](https://mp.weixin.qq.com/s/Ht1HuLxQ2RngrVD92TBl4Q)

     On December 14, the CNCF Foundation announced that Merbridge was officially included in the CNCF sandbox project. [Merbridge](https://github.com/merbridge/merbridge) is currently the only open source project in CNCF focused on using eBPF to accelerate service mesh.
     Through Merbridge, you only need to run a command in the Istio cluster, and you can directly use eBPF instead of iptables to achieve network acceleration and improve service performance.

- [MetalLB Kubernetes Load Balancer v1.3.2 release (CNCF project)](https://metallb.universe.tf/release-notes/#version-0-13-2)

     The main new features of this version: support for configuration through CRD (no longer supports ConfigMap); can broadcast addresses in L2 or BGP mode, or only assign IP without broadcasting addresses; add node selector support for L2 Announcement and BGP Announcement; add BGPPeer selector; support for more flexible deployment using kustomize; add LoadBalancerClass support; support multi-protocol BGP.

- [Microcks API Simulation and Testing Project Becomes CNCF Sandbox Project](https://mp.weixin.qq.com/s/cdbf_1LUVwb4euldblV14w)

    [Microcks](https://github.com/microcks) provides a de facto standard for different API styles and protocols to accelerate and ensure API delivery. Microcks supports testing of new APIs before creating API contracts using the "Backend as a Service " feature to test new APIs before creating an API contract, and supports REST APIs, gRPC, GraphQL, and event-driven APIs, among others, seamlessly integrated with continuous builds or pipelines.

- [MicroK8s lightweight Kubernetes distribution v1.25 released](https://github.com/canonical/microk8s/releases/tag/v1.25)

     Main new features of this version: Added "strict confinement" isolation level to limit host system access and enforce a stricter security posture, 25% reduction in snap size, support for image sideloading (sideloading), new plugins kube-ovn and osm-edge.

- [Mimir Prometheus long-term storage project v2.4.0 released](https://github.com/grafana/mimir/releases/tag/mimir-2.4.0)

     The main new features of this version: introduce query scheduler query-scheduler, and support DNS-based and ring-based two service discovery mechanisms; add API endpoints to expose the limit of each tenant; add new TLS configuration options; allow maximum limit Range query length.

- [Mimir Prometheus long-term storage project v2.3.0 released](https://github.com/grafana/mimir/releases/tag/mimir-2.3.0)

     The main new features of this version: support for ingesting metrics in OpenTelemetry format, new tenant alliance for metadata query, simplified object storage configuration, support for importing historical data, optimized instant query function, and enabled query sharding by default.

- [Mimir new feature: Integrating Graphite, Datadog, Influx and Prometheus metrics into a unified storage backend](https://grafana.com/blog/2022/07/25/new-in-grafana-mimir-ingest-graphite-datadog-influx-and-prometheus-metrics-into-a-single-storage-backend/)

     [Mimir](https://github.com/grafana/mimir) is an open source timing database based on Cortex by Grafana Labs.
     Mimir now open-sources [three proxies](https://github.com/grafana/mimir-proxies) for ingesting metrics from Graphite, Datadog, and InfluxDB and storing them in System uptake metrics lay the groundwork.
     OTLP for native ingestion of OpenTelemetry will be supported in the future.

- [MinIO object storage tools release new features: extended repository and official support for OPA (CNCF project)](https://github.com/minio/minio/releases/tag/RELEASE.2022-05-08T23-50-31Z )

     MinIO has extended the repository to exclude certain prefixes and folders in the repository to improve the performance of applications such as the Spark S3A connector. Additionally, following widespread requests, MinIO officially supports OPA.

### N

- [Nacos Dynamic Service Discovery Platform v2.2.0 released](https://github.com/alibaba/nacos/releases/tag/2.2.0)

     The main new features of this version: support batch registration and batch logout services, support openAPI 2.0, add multi-data source plug-ins, add track tracking plug-ins, support Prometheus http service discovery, and support Ldaps authentication.

- [Nacos Dynamic Service Discovery Platform v2.1.0 release (CNCF project)](https://github.com/alibaba/nacos/releases/tag/2.1.0)

     The main new features of this version: Two new SPI plug-ins are added: respectively used to configure encryption, decryption and authentication, support cluster gRPC client to set thread pool size, support reset raft cluster, etc.

- [Narrows: Cloud-native security detector open-sourced by VMware that adds dynamic scanning for container security on Harbor](https://mp.weixin.qq.com/s/xJ1Sx5pc0rKkJaYopD-vjw)

    [Narrows](https://github.com/vmware-tanzu/cloud-native-security-inspector) enables runtime security posture assessment of Kubernetes clusters and the workloads within them, finds misconfigurations in Kubernetes clusters, and Ability to aggregate, aggregate, and analyze scan reports and provide an openAPI; seamlessly integrate with Harbor and automatically sync images from external public image repositories to Harbor to generate security data.

- [nerdctl Containerd command line tool v1.3.0 released](https://github.com/containerd/nerdctl/releases/tag/v1.3.0)

    Release features: support for image signing and verification using notation projects, support for Port Windows devices, new [project maintainer's guide](https://github.com/containerd/nerdctl/blob/main/MAINTAINERS_GUIDE.md) officially available The new [project maintainer's guide](https://github.com/containerd/nerdctl/blob/main/MAINTAINERS_GUIDE.md) is now available, fixes for rootless mode operations that do not allow systemd-homed.

- [nerdctl Containerd Command Line Tool v1.2.0](https://github.com/containerd/nerdctl/releases/tag/v1.2.0)

     This version features: experimental support for reading Kubernetes container logs, improved compilation error messages, allows running Host Process containers on Windows, adds Windows HyperV container mode.

- [NeuVector Container Security Platform v5.2.0 released](https://github.com/neuvector/neuvector/releases/tag/v5.2.0)

    Release features: adds search SaaS service for CVE queries, supports NeuVector API access tokens, supports image signing for access control, adds support for custom access control criteria such as resource limits, supports calling NeuVector scanners from the Harbor registry via the pluggable scanner interface, allows users to disable network protection, supports scanning of golang dependencies.

- [NeuVector Container Security Platform v5.0Release](https://mp.weixin.qq.com/s/nZ_a7JiryZJskJEPPIEmcw)

     The main new features of this version: integration with SUSE Rancher, and can also be docked with other enterprise-level container management platforms such as Amazon EKS, Google GKE, and Microsoft AKS; support for web application firewall detection; support for automated container protection; support for zero-drift process and file protection And the network, process/file segmentation strategy mode protection, etc.

- [Nightingale Observability Platform Release V6](https://mp.weixin.qq.com/s/ckeaA1JovW43w0jgsj9Y7A)

    Version features: built-in common middleware monitoring dashboard and alarm rules; support for LDAP, CAS, OIDC and other authentication integration; built-in support for alarm self-healing capabilities; support for flexible alarm rules, blocking rules, subscription rules, suppression rules; by default, only a binary can be docked to the market's common collector; integration of ElasticSearch data source.

- [Nightgale v5.10 released](https://github.com/ccfos/nightingale/releases/tag/v5.10.0)

     The main new features of this version: support recording rule management, alert rules support multicluster, dashboard variables support TextBox, alert masking supports more operators, and more flexible custom alert content.

- [Notification Manager multi-tenant notification management system 2.0.0 released](https://mp.weixin.qq.com/s/op79OMTp0nxzfxM8fH-nnA)

     [Notification Manager](https://github.com/kubesphere/notification-manager) can receive alerts, events, and audits from Kubernetes, generate notification messages according to templates set by users, and push them to users.
     Main features of the new version: new routing function, users can send specified notifications to specified users by setting routing rules; new silent function, by configuring silent rules, specific notifications can be blocked in a specific time period; support dynamic update templates Wait.

- [Nydus Container Image Acceleration Service v2.2.0 Released (CNCF Project)](https://github.com/dragonflyoss/image-service/releases/tag/v2.2.0)

    Version features: enable mirror on-demand loading feature erofs over fscache, support v6 mirror conversion, merge subcommand supports merging multiple versions of mirrors, support converting Nydus mirror layer to tar file, add BackendProxy storage backend to emulate registry storage backend.

### O

- [OCM multicluster management platform v0.9 release (CNCF project)](https://www.cncf.io/blog/2022/10/31/open-cluster-management-november-2022-update/)

     The main new features of this version: reduce the permissions of the worker agent on the managed cluster, support access to kube-apiserver and other services in the managed cluster, and support the use of AddOn API to refer to AddOn configuration.

- [OPA Generic Policy Engine v0.50.0 Released (CNCF Project)](https://github.com/open-policy-agent/opa/releases/tag/v0.50.0)

     Release features: New built-in feature to validate JSON Schema; package scoped schema comments can be applied across modules; support for starting OPA with a remote bundle via a simple command; introduction of a new EditTree data structure to improve the performance of json.patch; support for exposing decision logs via the status API errors; all published OPA images now run with a non-root uid/gid.

- [OPA Common Policy Engine v0.44.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.44.0)

     The main new features of this version: fix 3 CVE vulnerabilities, Set Element Addition optimization, built-in Set union optimization, add optimization parameters to OPA evaluation command, allow more bundlers to be compiled into WASM.

- [OPA Common Policy Engine v0.43.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.43.0)

     Major new features in this release: linear scaling optimization for Rego Object inserts, status and log plugins now accept HTTP 2xx status codes, OPA bundle commands now support .yml files, storage system fixes, Rego compiler and runtime environment bug fixes and optimizations.

- [OPA Common Policy Engine v0.41.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.41.0)

     The main new features of this version: a new set of built-in features for validating, parsing, and verifying GraphQL queries and schemas; built-in feature declarations support specifying the names and descriptions of feature parameters and return values ​​through metadata; support skipping based on the summary of OCI artifacts Bundle reload; delete empty list in bundle signature; unit resolution and token update, etc.

- [OpenClusterManagement (OCM) multicluster management platform v0.7 release (CNCF project)](https://mp.weixin.qq.com/s/EQgdnZVOqzfvuxOzg-Q0cQ)

     The main new features of this version: Add the "DefaultClusterSet" function, all managed clusters registered in the OCM environment will be registered in the ClusterSet named "default" by default; support multicluster scheduling based on Taint / Toleration semantics; deployment architecture Adjust to the "Hosted deployment" mode, that is, no other components need to be deployed in the managed cluster, and all proxy controllers are executed remotely.

- [OpenCost supports FinOps Open Cost and Usage Specification (FOCUS)](https://www.opencost.io/blog/focus)

    The FinOps Open Cost and Usage Specification (FOCUS) released the first version of its specification to define an open standard for cloud cost, usage, and billing data.The OpenCost project has announced support for this standard and has already begun using it to support initial patches.

- [OpenEBS Cloud Native Storage v3.4.0 Released (CNCF Project)](https://github.com/openebs/openebs/releases/tag/v3.4.0)

    Release features: support for installing Mayastor via OpenEBS helm chart, support for switching Mayastor nodes on demand during failure detection, support for NVMe virtual path detection using NDM, fix for pull image key error in LVM LocalPV helm chart, add backend volume PVC contexts to NFS server deployments as a label in NFS server deployments.

- [OpenEBS Cloud Native Storage v3.3.0 release (CNCF project)](https://github.com/openebs/openebs/releases/tag/v3.3.0)

     Major new features in this release: deprecated arch-specific container images, enforced hostpath quotas with ext4 filesystems for LocalPV Hostpath, enhanced NDM functionality, added logging in cstor to improve debugging, added rate limiters to reduce LocalPV Log flooding issue in LVM.

- [OpenFunction Function as a Service Project v1.0.0 Released (CNCF Project)](https://github.com/OpenFunction/OpenFunction/releases/tag/v1.0.0)

     Release features: integration with wasmedge, support for building from local source code, multiple features supported in a single Pod, support for detecting changes to source code or images and rebuilding/redeploying newly built images.

- [OpenKruise upgraded to CNCF Incubation Program](https://mp.weixin.qq.com/s/9knMn8eKJBNdXUU-TcmTQg)

    [OpenKruise](https://github.com/openkruise/kruise/) is an extended suite of components focused on application automation such as deployment, upgrades, operations and availability protection. OpenKruise helps organizations with large workloads adopt and automate Kubernetes and cloud-native deployments, opening the door to new use cases in areas such as AI / ML.

- [OpenKruise Cloud Native Application Automation Management Suite v1.4.0 Released (CNCF Project)](https://github.com/openkruise/kruise/releases/tag/v1.4.0)

    Release features: new JobSidecarTerminator feature to terminate sidecar containers after the main container exits; new field to immediately recreate containers; support for attaching metadata to the PullImage CRI interface during ImagePullJob; sidecarSet controller support for namespace selectors ; change Kubernetes image address reference from "k8s.gcr.io" to "registry.k8s.io".

- [OpenKruise Cloud Native Application Automation Management Suite v1.3.0 release (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.3.0)

     The main new features of this version: support custom probes and return the results to Pod yaml, SidecarSet supports injecting pods under the kube-system and kube-public namespaces, adds timezone support for upstream AdvancedCronJob, WorkloadSpread supports StatefulSet.

- [OpenKruise Cloud Native Application Automation Management Suite v1.2.0 released (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.2.0)

     The main new features of this version: Added CRD `PersistentPodState` to persist certain states of Pods, such as "fixed IP scheduling"; CloneSet calculates logic changes for percentage-based partitions; sets Pod not-ready in the lifecycle hook stage; supports protection scale Any custom workload for subresource; new performance optimization methods for large-scale clusters, etc.

- [OSM (Open Service Mesh) Open Service Mesh Project is no longer maintained](https://mp.weixin.qq.com/s/_eqhL999E1ojmTAoaAOuiQ)

    OSM has adopted the Service Mesh Interface (SMI) as its standard API, allowing compatibility with other Service Mesh implementations that support SMI to simplify the Service Mesh operating experience. Recently, the OSM maintenance team announced that there will be no new releases of OSM and that the team will move to work with the Istio community to advance Istio.

- [Open Service Mesh v1.2.0 release (CNCF project)](https://github.com/openservicemesh/osm/releases/tag/v1.2.0)

     The main new features of this version: support for custom trust domains (that is, the common name of certificates), Envoy updated to v1.22, and use envoyproxy/envoy-distroless mirroring, added support for Kubernetes 1.23 and 1.24, support for limiting TCP connections and HTTP requests local per-instance rate, fix Statefulset and headless service.

- [OpenShift Toolkit 1.0, simplifying the development of cloud-native applications](https://cloud.redhat.com/blog/announcing-openshift-toolkit-enhance-cloud-native-application-development-in-ides)

     [OpenShift Toolkit](https://github.com/redhat-developer/vscode-openshift-tools) is a set of extensions for VS Code and IntelliJ. Its features include: support for connecting and configuring OpenShift; providing hybrid cloud support, developers can connect to any running OpenShift instance; develop applications through local workspaces, git repositories, or default devfile templates; allow one-click Strategy, directly deploy registry code to OpenShift; provide Kubernetes resource management, seamless Kube configuration context switching; multi-platform s platform support.

- [OpenTelemetry Observable Project v1.21.0 released (CNCF project)](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.21.0)

    Version features: add experimental histogram suggestion API, clarify parameters used when logging, mark OpenCensus compatibility specification as stable.

- [OpenTelemetry v1.13.0 release (CNCF project)](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.13.0)

     The main new features of this version: Context is immutable when setting span, supports experimental configuration of default histogram aggregation of OTLP metric exporter, allows log processor to modify log records, adds experimental event and log API specifications, in Add network metrics to process semantic conventions, and add semantic conventions to GraphQL.

- [OpenTelemetry Metrics release RC version](https://opentelemetry.io/blog/2022/metrics-announcement/)

     RC versions of OpenTelemetry metrics have been released for Java, .NET, Python (JS coming next week). This means that the specification, API, SDK, and components that interact with metrics in the way of authoring, capturing, processing, etc., now have the full OTel metrics feature set ready to use.

- [OpenTelemetry v1.11.0 release (CNCF project)](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.11.0)

     The main new features of this version: replace the histogram with a more clear bucket histogram, support displaying examples on OpenMetrics counters, increase the semantic specification of database connection pool metrics, allow all metrics specifications to be synchronous or asynchronous, add HTTP/3, etc.

- [Openyurt Cloud Native Edge Computing Project v1.3.0 Released (CNCF Project)](https://github.com/openyurtio/openyurt/releases/tag/v1.3.0)

    Release features: refactoring Openyurt control plane components, new component yurt-manager for managing controllers and webhooks of multiple components; allowing users to define Pod templates and upgrade models for static Pods; NodePort Service supports node pool isolation.

- [Openyurt Cloud Native Edge Computing Project v1.2.0 Released (CNCF Project)](https://github.com/openyurtio/openyurt/releases/tag/v1.2.0)

     New node pool governance component Pool-Coordinator for reducing cloud edge network bandwidth and improving edge autonomy in case of cloud edge network failure; use raven component to replace yurt-tunnel component to solve cross-region network communication problems; improve certificate manager.

- [Openyurt Cloud Native Edge Computing Project v1.1.0 release (CNCF project)](https://github.com/openyurtio/openyurt/releases/tag/v1.1.0)

     The main new features of this version: support OTA/automatic upgrade mode of DaemonSet workload, support autonomous feature verification of e2e test, enable data filtering function, add suggestions for unified cloud computing edge communication solution, and improve health checker.

- [Openyurt Cloud Native Edge Computing Project v1.0.0 release (CNCF project)](https://github.com/openyurtio/openyurt/releases/tag/v1.0.0)

     The main new features of this version: NodePool API version upgrade to v1beta1, use CodeCov to track unit test coverage, and add two new performance test reports for OpenYurt components.

- [OpenKruise Cloud Native Application Automation Management Suite v1.2.0 released (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.2.0)

     The main new features of this version: Added CRD `PersistentPodState` to persist certain states of Pods, such as "fixed IP scheduling"; CloneSet calculates logic changes for percentage-based partitions; sets Pod not-ready in the lifecycle hook stage; supports protection scale Any custom workload for subresource; new performance optimization methods for large-scale clusters, etc.

- [osm-edge: Yiheng Technology Flomesh open source edge service mesh](https://mp.weixin.qq.com/s/tbCxbKFQkvx84Ku5IWg38g)

     [osm-edge](https://github.com/flomesh-io/osm-edge) uses [osm](https://github.com/openservicemesh/osm) as the control plane and Programmable Gateway [Pipy](https://github.com/flomesh-io/pipy) as the data plane.
     Support SMI specification; support [fsm](https://github.com/flomesh-io/fsm) for ingress, gateway API, and cross-cluster service discovery, and provide "east-west + north-south" traffic of "k8s cluster + multicluster" Management and service governance capabilities.
     Its development and testing environment uses k3s, k8e, etc., so users can quickly and cost-effectively deploy low-resource, high-performance service meshs on x86, arm, RISC-V, Loongson and other hardware platforms.

### P

- [Paralus Kubernetes Zero Trust Access Service Becomes CNCF Sandbox Project](https://mp.weixin.qq.com/s/hYmMT0mvMdO6-LW6oHxteg)

     [Paralus](https://github.com/paralus/paralus) is designed for multicluster environments, securing access to resources with instant service account creation and fine-grained user credential management.
     In addition, Paralus incorporates the zero-trust principle, supporting multiple identity providers, custom roles, and more.

- [Paralus: The industry's first open-source zero-trust access service for Kubernetes by Rafay Systems](https://rafay.co/the-kubernetes-current/paralus-industrys-first-open-source-zero-trust-access-service-for-kubernetes/)

     The main features of [Paralus](https://github.com/paralus/paralus) are: it can handle the access management of multiple clusters in a unified way, allows integration with existing RBAC policies and SSO providers, and supports recording of user actions performed by users in the organization. Each kubectl command supports OIDC, supports creating custom roles with specific permissions, and allows dynamic revoking of permissions, etc.

- [Phlare: Grafana open source large-scale continuous profiling database](https://grafana.com/blog/2022/11/02/announcing-grafana-phlare-oss-continuous-profiling-database/)

     [Phlare](https://github.com/grafana/phlare) is a horizontally scalable, highly available, multi-tenant continuous analysis data aggregation system, fully integrated with Grafana, and can be related to observation metrics such as metrics, logs and traces couplet. Installation requires only one binary and no other dependencies.
     Phlare uses object storage for long-term data storage and is compatible with multiple object storage implementations. Its native multi-tenancy and isolation feature set allows multiple independent teams or business units to run a single database.

- [PipeCD becomes a CNCF sandbox project](https://pipecd.dev/blog/2023/05/19/cncf-sandbox-admission/)

    [PipeCD](https://github.com/pipe-cd/pipecd) provides a unified continuous delivery solution for multi-cloud applications, providing a consistent deployment and operational experience for any application.PipeCD is a GitOps tool that enables deployment operations via pr requests on Git.

- [Pisanix: SphereEx Open Source Solution for Database Mesh](https://mp.weixin.qq.com/s/p8bi14s8FWdp7GlqQxKzzw)

     [Pisanix](https://github.com/database-mesh/pisanix) helps users easily implement SQL-aware traffic governance based on the Database Mesh framework, runtime-oriented resource programming, database reliability engineering and other capabilities to help users Database governance on the cloud. Pisanix currently supports the MySQL protocol, mainly including three components: Pisa-Controller, Pisa-Proxy and Pisa-Daemon (coming soon).

- [Pixie Kubernetes observation platform releases Plugin System](https://www.cncf.io/blog/2022/07/06/easy-observability-with-open-standards-introducing-the-pixie-plugin-system/) 

     [Pixie Plugin System](https://github.com/pixie-io/pixie-plugin) allows users to export their Pixie data into any service that supports OpenTelemetry. This means users can leverage external data storage for long-term data retention, seamlessly adopt Pixie in existing workflows and dashboards, and combine Pixie data with other data streams.

- [Podman Container Runtime Project v4.5.0 released](https://github.com/containers/podman/releases/tag/v4.5.0)

    Release features: support for automatic update of containers running inside Pod, support for using SQLite database as backend, added support for container network stack Netavark plugin, support for DHCP with Macvlan and Netavark backend.

- [Podman container engine v4.3.0 released](https://github.com/containers/podman/releases/tag/v4.3.0)

     Command update: support changing container resource limits, delete pods and containers created by K8s YAML, support K8s secret, support reading YAML from URL, support emptyDir volume type, support binary data in ConfigMap; support repeated volume mounts.

- [Podman container runtime project v4.2.0 released](https://github.com/containers/podman/releases/tag/v4.2.0)

     The main new features of this version: support for GitLab Runner, new commands for creating copies of existing pods, new commands for synchronizing state changes between the database and any volume plugins, new exit policies for pods, and automatic cleanup of unused pods Caches Podman virtual machine images, allowing multiple overlay volumes of different containers to reuse the same workdir or upperdir.

- [Prometheus v2.46.0 released (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.46.0)

    Release features: added PromQL format and label matcher set/delete commands, push metrics command, added more labels to Endpointslice and Endpoints Role for K8s service discovery, won't add Pods to a target group if PodIP's status isn't set, support for validating metrics names and labels in the Remote Write Handler, support for storing the native histograms stored in snapshots.

- [Prometheus v2.45.0 Released (CNCF Project)](https://github.com/prometheus/prometheus/releases/tag/v2.45.0)

    Update: Support limit the number of returns per TSDB statistic, add limit in global configuration, support ingesting both classic histogram and native histogram, native histogram support limit the size of storage bucket.

- [Prometheus v2.44.0 released (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.44.0)

    Release features: default number of samples per send increased to 2,000, support for handling native histogram data, added functionality for checking Prometheus server health status and availability at the command line, added metrics for total number of samples loaded for all queries.

- [Prometheus v2.43.0 released (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.43.0)

    Version features: store all tags and corresponding values in a single string to reduce memory footprint (only enabled when compiling with Go tag stringlabels); provide HTTP client configuration in query commands; add option to import grab configuration from different files; add two new HTTP client configuration parameters; allow dynamic setting via API backtracking time of queries.

- [Prometheus v2.42.0 released (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.42.0)

     This release features: support for native histograms, change WAL record format for native histograms, support for selecting TSDB dump time order, support for Float histograms, add container IDs as meta tags for Kubernetes pod objects.

- [Prometheus v2.40.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.40.0)

     The main new features of this version: add experimental support for native histograms, Kubernetes discovery client supports the use of protobuf encoding, improve sorting speed, and increase enterprise management partitions.

- [Prometheus v2.39.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.39.0)

     The main new features of this version: add experimental support for ingesting unordered samples, and optimize memory resource usage.

- [Prometheus v2.37.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)

     Major new features in this release: allow Kubernetes service discovery to add node labels to targets from endpoint roles, TSDB memory optimization, reduce sleep time when reading WAL, optimize signature creation, add timeout and User-Agent header.

- [Prometheus v2.37.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)

     Major new features in this release: Allow Kubernetes service discovery to add node labels to targets from endpoint roles, TSDB memory optimization, reduce sleep time when reading WAL, optimize signature creation, add timeout and User-Agent header.

- [Prometheus v2.36.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.36.0)

     The main new features of this version: Vultr integration, Linode SD failure count metric and `prometheus_ready` metric added, `stripDomain` added to the template function, promtool supports using matchers when querying label values, and proxy pattern identifiers added.

- [Pyroscope Performance Continuous Analysis Platform v1.0 Released](https://github.com/grafana/pyroscope/releases/tag/v1.0.0)

    Pyroscope is a horizontally scalable, highly available, multi-tenant continuous analytics aggregation system with an architecture similar to Grafana Mimir, Loki, and Tempo; installation guides for Helm, Tanka, and docker-compose; and Grafana Explore and dashboards to correlate continuous analytics data with other observable data. Grafana Explore and dashboards can be used to correlate continuous analysis data with other observable data.

### R

- [Rainbond IT innovation version of cloud-native multi-cloud application management platform released](https://mp.weixin.qq.com/s/eelPIhoCQdAfBnQOm_YDAg)

    Rainbond Cintron Edition supports deployment and management of multiple single-architecture clusters. It supports one-click deployment and management of amd64 clusters, arm64 clusters, and amd64 & arm64 hybrid architecture clusters. Compatible with mainstream localized CPUs and adapted to multiple localized operating systems. Supports rapid migration of legacy applications to Cintron environment. Cloud native app store supports publishing and installation of arm64 architecture apps.

- [Rainbond Cloud Native multicloud Application Management Platform v5.14.0 Released](https://github.com/goodrain/rainbond/releases/tag/v5.14.0-release)

    Version features: upgrade the source code builder version of each language; support one-click deletion of applications and related resources under applications; reasonable recycling mechanism for Pods created using cluster command line; add search feature or prioritize matching certificates with the same domain name when configuring https certificates for domain names; support configuration of log storage path.

- [Rainbond Cloud Native multicloud Application Management Platform v5.12.0 Released](https://github.com/goodrain/rainbond/releases/tag/v5.12.0-release)

    Release features: support for platform-level plugins and capability extensions, new pipeline plugins, support for creating components via OpenAPI, and optimized Helm repository installation application logic.

- [Rainbond cloud-native multicloud application management platform v5.9.0 released](https://github.com/goodrain/rainbond/releases/tag/v5.9.0-release)

     The main new features of this version: support for Containerd container runtime, support for using the grctl command to change the cluster API address, support for K8s 1.24 and 1.25, support for MiniKube deployment, and support for custom monitoring rules.

- [Rainbond cloud-native multicloud application management platform v5.8.0 released](https://github.com/goodrain/rainbond/releases/tag/v5.8.0-release)

     The main new features of this version: support for one-click import of existing applications in the Kubernetes cluster, support for deploying components directly through Jar, War packages or Yaml files, support for creating Job/CronJob type tasks, support for extending the properties supported by applications and components, and support for Dockerfile Build using a private image.

- [Rook Cloud Native Storage Project v1.12.0 Released (CNCF Project)](https://github.com/rook/rook/releases/tag/v1.12.0)

    Release features: support for Kubernetes v1.22+, use of Ceph CSI v3.9 by default, support for Ceph Reef (v18), addition of Ceph COSI driver for configuring storage buckets (experimental), automatic recovery of RBD (RWO) volumes after node loss, introduction of Multus network authentication tool, improvements in security by dropping container privileges, support for RGW as a CSP, and support for RGW as a CSP. security, and support for RGW as a CephNFS backend (experimental).

- [Rook Cloud Native Storage Project v1.11.0 Released (CNCF Project)](https://github.com/rook/rook/releases/tag/v1.11.0)

    Release features: Support for K8s v1.21 and above, Ceph-CSI v3.8 becomes the default deployment, MachineDisruptionBudgets support removed, Object Storage Bucket notification and topic functionality brought to stable state, Support for data mirroring across multiple clusters with overlapping CIDRs, Ceph exporter becomes a source of metrics for the Ceph performance counter.

### S

- [Sealer Distributed app delivery tool v0.9.0 released (CNCF project)](https://github.com/sealerio/sealer/releases/tag/v0.9.0)

     The main new features of this release: support for configuring tags, permissions, roles, registry, cluster host aliases via Clusterfile; support for ipv4/ipv6 dual stack; support for high availability mode for local registry; support for buildah-based OCI standard; Kubefile support for Helm packages, k8s yaml files, Kubefile supports Helm packages, k8s yaml files, shell scripts, and other application types.

- [Serverless-cd: Serverless Devs released a lightweight CI/CD framework based on Serverless architecture——](https://mp.weixin.qq.com/s/ps_ZFsv7KGwV2V61SvvWIA)

     Serverless Devs is the industry's first platform that supports cloud-native full lifecycle management of mainstream serverless services/frameworks. [Serverless-cd](https://github.com/Serverless-Devs/serverless-cd) is built based on Serverless Devs, fully follows the best practices of Serverless architecture, and refers to the implementation of Github Action at the specification and ecological level. It adopts the Master Worker model and event-driven architecture, which can be used to quickly build an enterprise internal application management PaaS platform.

- [Serverless Devs entered the CNCF sandbox and became the first serverless tool project selected](https://mp.weixin.qq.com/s/ICVDO3U5Ea1DzP3LFJq8mQ)

     [Serverless Devs](https://github.com/Serverless-Devs/Serverless-Devs) is open sourced by Alibaba Cloud and is committed to providing developers with a powerful tool chain system. In this way, developers can not only experience multicloud serverless products with one click, quickly deploy serverless projects, but also carry out project management in the whole lifecycle of serverless applications, integrate with other tools/platforms, and improve the efficiency of R & D and operation and maintenance.

- [Skywalking Application Performance Monitor v9.6.0 released](https://github.com/apache/skywalking/releases/tag/v9.6.0)

    Release Features: Supports MQE (Metrics Query Expression) and introduces a new notification mechanism; Loki LogQL query language and Grafana Loki Dashboard can now be used to view and analyze logs collected by SkyWalking; Supports OTEL-based implementation of MongoDB server/cluster monitoring; Improved build process. /cluster monitoring; improvements to the build process to make it replicable for automated release CI processes.

- [Skywalking Application Performance Monitoring System v9.5.0 Released](https://github.com/apache/skywalking/releases/tag/v9.5.0)

    Release features: new topology layout, support for Elasticsearch server monitoring, support for continuous analysis, support for collecting process-level related metrics, support for cross-thread trace analysis, support for monitoring the total number of metrics in k8s StatefulSet and DaemonSet, support for Redis and RabbitMQ monitoring.

- [Skywalking application performance monitoring system v9.3.0 released](https://github.com/apache/skywalking/releases/tag/v9.3.0)

     The main new features of this version: increase the metric correlation function, use Sharding MySQL as the database, visualize the performance of virtual cache and message queue, use Skywalking OpenTelemetry receiver instead of prometheus-fetcher plug-in to grab Prometheus metrics.

- [Skywalking application performance monitoring system v9.2.0 released](https://github.com/apache/skywalking/releases/tag/v9.2.0)

     The main new features of this version: Added eBPF network analysis feature of K8s Pod, support for MySQL and PostgreSQL monitoring, correlation event component and tracking, and log component.

- [Skywalking application performance monitoring system v9.1.0 release (CNCF project)](https://github.com/apache/skywalking/releases/tag/v9.1.0)

     Main new features of this version: update the eBPF Profiling task to the service level; add a layer field to the event, and prohibit the reporting of events without a layer; the Zipkin receiver mechanism is changed, and the trace no longer flows to the OAP segment; SQL database related updates; remove InfluxDB 1. x and Apache IoTDB 0.X storage scheme, add BanyanDB storage scheme (still in development).

- [SPIFFE and SPIRE projects officially become CNCF graduate projects](https://www.cncf.io/announcements/2022/09/20/spiffe-and-spire-projects-graduate-from-cloud-native-computing-foundation-incubator/)

     [SPIFFE](https://github.com/spiffe/spiffe) provides secure identities for various workloads in modern production environments, eliminates the need to share confidential information, and is expected to become the foundation for higher-level platform-neutral security controls Realize the basis.
     [SPIRE](https://github.com/spiffe/spire) (SPIFFE Runtime Environment) is responsible for implementing the SPIFFE specification on various platforms and enforcing multi-factor proof of identity.

- [Spring Cloud Tencent: Tencent Open Source One-stop Microservice Solution](https://mp.weixin.qq.com/s/A-DcZJY9sJcTQSEoWEibww)

     [Spring Cloud Tencent](https://github.com/Tencent/spring-cloud-tencent) Relying on Polaris, Tencent's open-source one-stop microservice solution, it mainly provides common service registration, discovery, and configuration in the field of microservices Center, service routing, current limiting and fusing, and metadata link transparent transmission capabilities.

- [K8s operator v0.31.0 release of Strimzi message middleware Kafka (CNCF project)](https://github.com/strimzi/strimzi-kafka-operator/releases/tag/0.31.0)

     Main new features of this version: support for Kafka 3.2.1; pluggable Pod security profile, built-in support for restricted Kubernetes security profile; support for leader election and running multiple operator copies; support for using IPv6 in certificates issued by Strimzi address.

- [SuperEdge edge container management system v0.8.0 release (CNCF project)](https://github.com/superedge/superedge/releases/tag/v0.8.0)

     The main new features of this version: separate edgeadm from the SuperEdge project, tunnel supports http_proxy capability, Lite-apiserver supports caching some key resources (nodes, services, etc.) and ExternalName Service forwarding on edge nodes.

- [Sylva cloud-native infrastructure stack launched by Linux Foundation Europe to lay a cloud-native foundation for telecom services](https://www.prnewswire.com/news-releases/linux-foundation-europe-announces-project-sylva-to-create-open-source-telco-cloud-software-framework-to-complement-open-networking-momentum-301678955.html)

     [Sylva](https://gitlab.com/sylva-projects/sylva) Leverages container network features (CNF) and cloud-native platforms such as Kubernetes to create a telecom cloud technology stack to reduce the fragmentation of cloud infrastructure for telecom and edge services sex.
     The technology stack provided by Sylva consists of 5 components: network performance (SR-IOV, DPDK, designated CNI, etc.), distributed cloud (multicluster Kubernetes, bare metal automation), energy efficiency, security (hardening and compliance), and openness and standardized API.

### T

- [TDengine Cloud Native Time Series Database v3.0 released](https://github.com/taosdata/TDengine/releases/tag/ver-3.0.0.0)

     The main new features of this version: support data collected by 1 billion devices, 100 nodes; support separation of storage and computing, introduce computing nodes, and restructure the entire computing engine; optimize support for message queues, streaming computing, and caching, introduce event-driven stream computing; support container and Kubernetes deployment.

- [Tekton Cloud Native CI/CD Framework v0.50.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.50.0)

    Release Features: Upgraded CSI and scheduled volume workspace functionality to stable, upgraded standalone workspace functionality to beta, support for restoring PVC creation, added event configuration mapping, introduced coschedule switch, support for automatically deleting PVCs created by their volume declaration templates after a PipelineRun completes.

- [Tekton Cloud-native CI/CD framework v0.43.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.43.0)

     The main new features in this release: support for parsing sidecar logs to extract results into task-running CRD, enable custom tasks in pipeline by default, add support for PipelineRun regulator, allow users to configure public keys for trusted resources, PodTemplate can be used to update global environment variables.

- [Tekton Cloud Native CI/CD Framework v0.42.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.42.0)

     The main new features of this version: support for configuring the Webhook port number, support for setting source values for cluster resources, add a new feature flag related to the status governance field, support for recording the source of remote resources, and add verification features in reconciler.

- [Tekton Cloud Native CI/CD Framework v0.40.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.40.0)

     The main new features of this version: add task running templates, support for propagating workspace in pipelinerun to simplify specification writing, optimize git remote resolution support, add cluster remote resolvers, merge affinity parameters of podtempalte and affinity-assistant.

- [Telepresence K8s Native Development Tool v2.14.0 Released (CNCF Project)](https://www.getambassador.io/docs/telepresence-oss/latest/release-notes#2.14.0)

    Release features: new exclusion fields and mapping fields for DNS configuration, support for excluding environment variables, support for detecting and reporting routing conflicts between other VPN software running on client computers.

- [Telepresence K8s Native Development Tool v2.10.0 Release (CNCF Project)](https://www.getambassador.io/docs/telepresence/latest/release-notes#2.10.0)

    The main new features of this release: Traffic Manager supports team mode and single-user mode, adding the secret of pulling mirrors in Helm Chart, OSS Helm chart will be pushed to telepresence proprietary repository (formerly datawire Helm repository).

- [Tetragon Security Observable and Runtime Enhancement Platform v0.11.0 released](https://github.com/cilium/tetragon/releases/tag/v0.11.0)

    Added Tetragon operator deployment to Helm Chart, IPv6 support, support for monitoring Kubernetes service, added access to K8sResourceWatcher, removed metrics for deleted Pods, added workload labeling to metrics with Pod information, added registration logic to Pod information CRD. Pod Information CRD.

- [Tetragon Security Observable and Runtime Enhancement Platform v0.10.0 released](https://github.com/cilium/tetragon/releases/tag/v0.10.0)

    Release features: support for recreating daemonset Pods on configmap changes, add events for tracking policy metrics, Pod tag filter support for tracking policies, support for loading Linux Security Module LSMs and tracers, enable parallel builds of bpf objects, add rate limiting for events, add socket tracking, add policies for file monitoring.

- [Tetragon Security Observable and Runtime Enhancement Platform v0.9.0 Released](https://github.com/cilium/tetragon/releases/tag/v0.9.0)

    Release features: add logging feature for loading BPF programs, support container image signing with cosign, support basic Cgroups tracing function, support pprof http, gRPC support using unix socket.

- [Tetragon: Isovalent open source eBPF-based security observability and runtime enhancement platform](https://isovalent.com/blog/post/2022-05-16-tetragon)

     [Tetragon](https://github.com/cilium/tetragon) provides fully transparent security observability capabilities based on eBPF and real-time runtime enhancement capabilities.
     Tetragon has smart kernel filtering capabilities and aggregation logic built directly into its eBPF-based kernel-level collector, so deep observability can be achieved with very low overhead without requiring application changes.
     The embedded runtime execution layer can not only perform access control at the system call level,
     It also detects escalation of privileges, Capabilities, and namespaces, and automatically blocks further execution of affected processes in real time.

- [ThreatMapper Cloud Native Security Observation Platform v1.4.0 release](https://github.com/deepfence/ThreatMapper/releases/tag/v1.4.0)

     The main new features of this version: the new feature ThreatGraph can combine the network and other runtime environments to determine the priority of threat scanning results, support agentless cloud security situation management for cloud assets, and integrate cloud-native environment malicious program scanning tools [YaraHunter]( https://github.com/deepfence/YaraHunter).

- [Trivy Container Vulnerability Scanning Tool v0.44.0 Released (CNCF Project)](https://github.com/aquasecurity/trivy/releases/tag/v0.44.0)

    Release features: support scanning local repositories, increase integration test timeout to 15 minutes, support displaying vulnerability status, support custom URLs for policy bundles, support customizing data for Rego policies.

- [Trivy Container Vulnerability Scanning Tool v0.41.0 Released (CNCF Project)](https://github.com/aquasecurity/trivy/discussions/4135)

    Version features: support for using Vulnerability Exploitability Exchange (VEX) to filter detected vulnerabilities, support for SBOM for generating VM images, support for nested JAR paths, support for using custom Docker sockets.

- [Trivy Container Vulnerability Scanning Tool v0.39.0 released (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.39.0)

    Version features: OCI artifact download support authorization function, support SBOM discovery in OCI referrer, support k8s parallel resource scanning, add pipeline for concurrent processing, add node tolerance option.

- [Trivy container vulnerability scanner v0.35.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.35.0)

     The main new features of this version: add a scanner for virtual machine images, support OS wildcards for multi-architecture images, support scanning images by digest, and add slow mode to reduce CPU and memory utilization.

- [Trivy container vulnerability scanner v0.33.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.33.0)

     The main new features of this version: disable containerd integration tests for non-amd64 architectures, refactor k8s custom reports, support non-packaged binary files, and fix golang x/text vulnerabilities.

- [Trivy container vulnerability scanner v0.32.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.32.0)

     The main new features of this version: increase the scanning of SPDX, support the dependency scanning of Rust binary files, and increase the support for gradle.lockfile and conan.lock files.

- [Trivy container vulnerability scanner v0.31.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.31.0)

     The main new features of this version: support for scanning SBOM proofs, adding tests for dockerfile misconf handlers, adding support for Cosign vulnerability proofs, allowing users to define an existing secret for tokens, and adding two new vulnerabilities.

- [Trivy container vulnerability scanner v0.30.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.30.0)

     The main new features of this version: support for scanning licenses, pushing canary build images to the registry, Trivy k8s supports scanning single argument resources, supports scanning Cyclonedx software bill of materials (SBOM), and adds pnpm support.

- [Trivy container vulnerability scanner v0.29.0 release (CNCF project)](https://github.com/aquasecurity/trivy/releases/tag/v0.29.0)

     The main new features of this version: support for RBAC scanning, support for K8s secret scanning, increase support for WASM modules, increase support for containerd, support for displaying slow scan suggestions, add loop checks for variable evaluation in pom files, add go mod tidy check.

- [Trivy Container Vulnerability Scanner Can Now Scan Almost Everything Cloud Native Related (CNCF Project)](https://thenewstack.io/aqua-securitys-trivy-security-scanner-can-scan-anything-now/ )

     According to Aqua, [Trivy](https://github.com/aquasecurity/trivy) is the most comprehensive vulnerability and misconfiguration scanning tool available,
     Can be used to scan cloud-native applications and infrastructure such as source code, repositories, images, artifact registries, Infrastructure-as-Code (IaC) templates, Kubernetes environments, and more.

### V

- [Vcluster Virtual Kubernetes Clustering Implementation Solution v0.15.0 Released](https://github.com/vmware-tanzu/velero/releases/tag/v1.11.0)

    Release features: allows users to access all host cluster services within vcluster, new built-in metrics server, generic synchronization feature supports importing cluster-wide resources from host clusters.

- [Vcluster virtual Kubernetes cluster implementation v0.13.0 released](https://github.com/loft-sh/vcluster/releases/tag/v0.13.0)

     The main new features of this version: adding log and backup features, adding high availability support for k3s with external data storage, and automatically synchronizing CSI resources when the vcluster scheduler is turned on.

- [Velero Backup Disaster Recovery Tool v1.11.0 Released (CNCF Project)](https://github.com/vmware-tanzu/velero/releases/tag/v1.11.0)

    Version features: add plugin progress monitoring feature, support filtering volumes to be skipped during backup, add cluster-wide and namespace-wide resource filters, add parameter for setting timeout connection between Velero server and k8s API server, support backup description command output in JSON format, refactor controller with controller-runtime, CSI The plugin will decide whether to restore data from snapshots by checking the setting of the `restorePVs` parameter.

- [Velero backup disaster recovery tool v1.10.0 release (CNCF project)](https://github.com/vmware-tanzu/velero/releases/tag/v1.10.0)

     The main new features of this version: introduce unified repository architecture, integrate cross-platform backup tool [Kopia](https://github.com/kopia/kopia), refactor file system backup, use Kubebuilder v3 to refactor the controller, Allows adding credentials for volume snapshot locations, enhances the robustness of CSI snapshots, supports pausing backup plans, and renames some modules and parameters.

- [Velero backup disaster recovery tool v1.9.0 release (CNCF project)](https://github.com/vmware-tanzu/velero/releases/tag/v1.9.0)

     The main new features of this version: CSI support improvements, refactoring of the controller using Kubebuilder v3, support for restoring the state of selected resources, and support for updating existing resources during resource restoration.

- [Virtink: A lightweight Kubernetes-native virtualization management engine open sourced by SmartX](https://mp.weixin.qq.com/s/LOZ8RhFE_9SZKwcdV90dPw)

     Unlike KubeVirt, [Virtink](https://github.com/smartxworks/virtink) does not support legacy hardware device simulation and desktop application scenario capabilities, but uses [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor) As the underlying virtualization manager, it only supports modern cloud workloads and can be installed in Kubernetes on any virtualized CPU platform to support virtualized workloads in a safer and lighter way.

- [Vitess Cloud Native Database System v14.0.0 release (CNCF project)](https://github.com/vitessio/vitess/releases/tag/v14.0.0)

     The main new features of this version: officially support online DDL, Gen4 becomes the default planner, add cluster management API and UI - VTAdmin (Beta), add a branch of Orchestrator running as a Vitess component - VTOrc (Beta), support cross Aggregation query of multiple shards and keyspaces.

- [Volcano Cloud Native Bulk Compute Project v1.8.0 released (CNCF project)](https://github.com/volcano-sh/volcano/releases/tag/v1.8.0)

    Release features: add JobFlow support for lightweight workflow orchestration, support for vGPU scheduling and isolation, support for GPU and user-defined resource preemption, support for using ElasticSearch monitoring system for node load-aware scheduling and re-scheduling, add switches to enable and disable Kubernetes default scheduler plug-ins, provide device plug-in exception fault tolerance mechanism for device plug-in exceptions, and adding Helm Chart to Volcano.

- [Volcano Cloud Native Batch Computing Project v1.7.0 Released (CNCF Project)](https://github.com/volcano-sh/volcano/releases/tag/v1.7.0)

    The main new features of this version: add Pytorch job plugin, support batch scheduling for Ray, a distributed high-performance AI computing framework, enrich scheduling policies to support more long-running service use cases, support Kubernetes v1.25, support multi-architecture mirroring, and support real-time view of resource allocation information of queues.

- [Volcano Cloud Native Batch Computing Project v1.6.0 release (CNCF project)](https://github.com/volcano-sh/volcano/releases/tag/v1.6.0)

     The main new features of this version: support dynamic scheduling and rescheduling based on real node load, support elastic job scheduling, add MPI job plug-ins, allow tasks not to retry when they fail, support checking the overhead of pod requests, and support enqueueing in pod groups Resource quotas are considered in the process, and the default privileged container passes the verification of admission webhook.

### W

- [WasmEdge WebAssembly Runtime v0.13.0 Released (CNCF Project)](https://github.com/WasmEdge/WasmEdge/releases/tag/0.13.0)

    Updates: unified wasmedge CLI tools, ported WasmEdge extensions as plugins, introduced wasi_logging plugin, compile-time support for enabling undefined behavior detectors, introduced new API for including data to module instances, support for asynchronous calls to WASM functions, introduced unified tools API.

- [WasmEdge WebAssembly Runtime v0.12.0 Released (CNCF Project)](https://github.com/WasmEdge/WasmEdge/releases/tag/0.12.0)

    Release features: introduced plugin context and related API, introduced multiple WASI socket API implementations, added VM API, added wasm_bpf plugin.

- [Wazero: Tetrate open source WebAssembly runtime for Go language development](https://mp.weixin.qq.com/s/aozmJpuwD69vGWcM525ucg)

    Wazero allows developers to write code in different programming languages and run it in a secure sandbox environment. Wazero features include: pure Go, no dependencies, cross-platform and cross-architecture support; follows the WebAssembly Core Specification 1.0 and 2.0; supports Go features such as concurrency safety and context passing; and provides a rich programming interface and command line tools.

- [werf, CLI tools for CI/CD, become a CNCF sandbox project](https://mp.weixin.qq.com/s/DGA1_k16QAQImFmy8mWcDw)

    [werf](https://github.com/werf/werf) can be integrated with any of your existing CI/CD systems, providing full application lifecycle management for Kubernetes.
    werf relies on Buildah to build container images, is compatible with various container registries to manage images, and uses Helm chart to deploy applications to Kubernetes.
    It also supports automatic build caching, content-based tagging, enhanced resource tracking capabilities in Helm, intelligent cleanup of old/unused container images, and more.

- [Wolfi: Chainguard Releases First Linux Distribution to Secure Software Supply Chain, Designed for Containers and Cloud-Native Environments](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro)

     [Wolfi](https://github.com/wolfi-dev) is a stripped-down Linux distribution designed for cloud-native, but it does not have a Linux kernel, instead relying on the environment (such as a container runtime) to provide the kernel. Main features: Provide high-quality build-time SBOM as a standard for all packages; packages are fine-grained and independent of each other to support lightweight mirroring; use mature and reliable apk package format, fully declarative, repeatable Build system, supports glibc and musl.

### X, Z

- [Xline Cross-Cloud Metadata KV Storage into CNCF Sandbox Project](https://mp.weixin.qq.com/s/Pj8TOStT_oEABZGqFkCVaA)

    [Xline](https://github.com/datenlord/Xline) is an open source distributed KV storage for managing small amounts of critical data and still guaranteeing high performance and strong data consistency in cross-cloud and cross-data center scenarios. Xline is etcd-compatible, providing a KV interface, multi-version concurrency control, while Xline is compatible with K8S for smooth user usage and migration.

- [Xline is open sourced by DatenLord: Achieving data consistency management across data centers](https://mp.weixin.qq.com/s/NqScUOjUA1t4gdNeLEcPwg)

     [Xline](https://github.com/datenlord/Xline) aims to solve the problem that etcd cannot fully meet the needs of cross-cloud and cross-data center use cases. Xline is a distributed KV storage, which is used to manage a small amount of critical data, and still ensure high performance and strong data consistency in cross-cloud and cross-data center use cases. It is compatible with the etcd interface, allowing users to use and migrate more smoothly.

- [Zadig cloud-native continuous delivery tool v1.12.0 released](https://github.com/koderover/zadig/releases/tag/v1.12.0)

     The main new features of this version: support for code scanning, support for service association with multiple builds, K8s YAML project support for importing services from existing K8s, support for synchronizing service configuration from the Gitee code base, support for automatically updating the environment after service configuration changes, and support for global construction Template, K8s Helm Chart environment supports self-test mode, supports integration of multiple Jenkins, etc.
