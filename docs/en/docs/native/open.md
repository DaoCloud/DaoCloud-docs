# open source project

This page lists activity in cloud native open source projects in alphabetical order.

### A, B

- [Acorn: Acorn Labs open source K8s application packaging and deployment framework](https://acorn.io/introducing-acorn/)

     [Acorn](https://github.com/acorn-io/acorn) can package all application's Docker image, configuration and deployment specification into an Acorn image artifact, which can be pushed to any OCI registry.
     As a result, developers can move locally developed applications to production without switching tools or technology stacks.
     Acorn images are created by describing the application's configuration in an Acornfile, eliminating the boilerplate of Kubernetes YAML.

- [Aeraki Mesh service mesh project v1.1.0 released (CNCF project)](https://www.aeraki.net/zh/blog/2022/announcing-1.1.0/)

     The main new features of this version: support Istio 1.12.x version; support bRPC (better RPC) protocol, bRPC is Baidu's open source industrial-grade RPC framework; Pass the real IP of the server, etc.

- [Antrea CNI plugin v1.9.0 release (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.9.0)

     Added multiple multi-cluster functions, including inter-cluster Pod connections, node controllers supporting Gateway high availability, and allowing Pod IPs to serve as endpoints for multi-cluster services;
     Add service health check similar to kube-proxy; add rule name to audit log; a service supports 800+ endpoints.

- [Antrea CNI Plugin v1.8.0 released (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.8.0)

     The main new features of this version: add ExternalNode function, K8s network policy adds audit log support, supports the use of Antrea ClusterNetworkPolicy to control external access to NodePort services, allows logical grouping of different network endpoints, and generates a new Helm Chart version every time Antrea releases , Support topology awareness TopologyAwareHints, add status field in IPPool CRD.

- [Antrea CNI plugin v1.7.0 release (CNCF project)](https://github.com/antrea-io/antrea/releases/tag/v1.7.0)
  
     The main new features of this version: increase the TrafficControl function to control the transmission of Pod traffic; support IPsec certificate authentication; enrich Antrea-native policies; enrich multicast functions; increase multi-cluster gateway functions; enrich secondary network IPAM functions.
  
- [APISIX Cloud Native API Gateway v3.0 released](https://github.com/apache/apisix/blob/release/3.0/CHANGELOG.md#300)

     v3.0 adds Consumer Group to manage multiple consumers, supports configuring the order of DNS resolution domain name types, adds AI plane for intelligent analysis and visualization of configuration and traffic, fully supports ARM64, adds gRPC client, and implements data Complete separation of control plane and control plane, service discovery support for control plane, new xRPC framework, support for more four-layer observability, integration of OpenAPI specification, and full support for Gateway API.

- [APISIX Cloud Native API Gateway v2.15.0 released](https://github.com/apache/apisix/blob/release/2.15/CHANGELOG.md#2150)

     The main new features of this version: support for user-defined priority of plug-ins, support for determining whether plug-ins need to be executed through expressions, custom error responses, and allow collection of metrics on Stream Route.

- [Apollo Distributed Configuration Management System v2.0.0 release (CNCF project)](https://github.com/apolloconfig/apollo/releases/tag/v2.0.0)

     The main new features of this version: Add public namespace list view on the home page, grayscale rules support label matching when IP is not fixed, enable namespace export/import function, most lists have added `DeletedAt` column support Unique constraint index.

- [Arbiter: Speed Cloud Open Source Scalable Scheduling and Elasticity Tool Based on K8s](https://mp.weixin.qq.com/s/xF6Zij2FB2dq3QsZO6ch1g)

     [Arbiter](https://github.com/kube-arbiter/arbiter) aggregates various types of data based on which users can manage, schedule, or scale applications in a cluster. It can help Kubernetes users understand and manage the resources deployed in the cluster, thereby improving the resource utilization and operational efficiency of enterprise applications.

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

### C

- [Calico CNI plugin v3.24.0 release (CNCF project)](https://github.com/projectcalico/calico/blob/release-v3.24/calico/_includes/release-notes/v3.24.0-release-notes.md)

     The main new features of this version: support IPv6 network wireguard encryption, expose IPAM configuration and IPAM block affinity through API, add new fields to operator API, support split IP pool, and transition from pod security policy to pod security standard.

- [Carina cloud-native local storage project v0.11.0 released](https://github.com/carina-io/carina/releases/tag/v0.11.0)

     Main new features of this version: support Cgroup v2, remove HTTP Server, upgrade CSI official image version, remove ConfigMap synchronization controller, move carina image to a separate namespace, add carina e2e test to replace the original e2e test code ( In development and testing), optimize the pvc scheduling logic of Storageclass parameters.

- [Carina Local Storage Project v0.10.0 Release (CNCF Project)](https://github.com/carina-io/carina/releases/tag/v0.10.0)

     The main new features of this version: support for mounting bare disks into containers for direct use, support for velero backup storage volumes, new CRD resource NodeStorageResource to replace the original method of registering disk devices to Node nodes, and use job to generate webhook certificates to replace the original How the script generates the certificate, etc.

- [cdk8s+: AWS open source Kubernetes development framework officially available](https://aws.amazon.com/blogs/containers/announcing-general-availablecity-of-cdk8s-plus-and-support-for-manifest-validation/)

     [cdk8s+](https://github.com/cdk8s-team/cdk8s) allows users to define Kubernetes applications and reusable abstractions using familiar programming languages and object-oriented APIs.
     Compared with the beta version released last year, the new features of the official version include: isolate the pod network and only allow specified communication; improve the configuration mechanism for running multiple pods on the same node; integrate [Datree](https://github. com/datreeio/datree-cdk8s) plugin to check for misconfigurations in Kubernetes using third-party policy enforcement tools.

- [Cert-manager cloud native certificate management project v1.10.0 release (CNCF project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.10.0)

     The main new features of this version: use trivy to scan locally built containers; if the target Secret is misconfigured or created after the request, resynchronize the signing request; add the option to load the Vault CA Bundle from the Kubernetes Secret; support adding on all resources deployed by the chart same label.

- [Cert-manager cloud native certificate management project upgraded to CNCF incubation project](https://www.cncf.io/blog/2022/10/19/cert-manager-becomes-a-cncf-incubating-project/)

     Cert-manager is a plugin for Kubernetes that automates the management and issuance of TLS certificates from various sources, providing cryptographic protection for cloud-native workloads. Recently, the CNCF Technical Oversight Committee has voted to accept cert-manager as a CNCF incubation project.

- [Cert-manager cloud native certificate management project v1.9.0 release (CNCF project)](https://github.com/cert-manager/cert-manager/releases/tag/v1.9.0)

     The main new features of this version: support for using cert-manager certificate (alpha), and support for configuring ingress-shim certificates through annotations on Ingress resources.

- [Chaosblade Chaos Engineering Project v1.7.0 Release (CNCF Project)](https://github.com/rook/rook/releases/tag/v1.10.0)

     The main new features of this version: add time travel experiment, add plugins zookeeper and clickhouse, jvm performance optimization, support for mTLS authentication of blade server.

- [Chaos Mesh Chaos Engineering Platform v2.5.0 release (CNCF project)](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.5.0)

     The main new features of this version: support for multi-cluster chaos experiments, HTTPChaos adds TLS support, allows configuring Pod security contexts for controller manager and dashboards in Helm templates, and StressChaos supports cgroups v2.

- [Chaos Mesh Chaos Engineering Test Platform v2.2.0 Release (CNCF Project)](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.2.0)

     The main new features of this version: Add the StatusCheck function to check the health of the application, and stop the chaos experiment when the application is unhealthy; support the use of `Chaosctl` for outbound forced recovery, and add workflows based on flow charts in the dashboard interface etc.

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

- [Cluster API Declarative Cluster Lifecycle Management Tool v1.3.0 released (CNCF project)](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.3.0)

     The main new features of this version: support for automatic renewal of machine certificates provided by the Kubeadm control plane provider, the ability to publish and consume cluster API images from the new container image registry registry.k8s.io, allowing the creation of clusters without taints on control plane nodes , clusterctl can now manage IPAM and RuntimeExtension providers.

- [Clusternet multi-cloud multi-cluster management project v0.13.0 released](https://github.com/clusternet/clusternet/releases/tag/v0.13.0)

     The main new features of this version: increase the routing function from the parent cluster to the sub-cluster pod, add scheduler configuration and support custom scheduler plug-ins, support discovery v1beta1, only provide support for discovering endpointslices for k8s v1.21.0 and later versions, Aggregate worker node labels using thresholds, support scheduling by cluster subgroup, update RBAC rules for clusternet-agent running in capi.

- [Constellation: Edgeless Systems Open Sources First Confidential Computing Kubernetes](https://blog.edgeless.systems/hi-open-source-community-confidential-kubernetes-is-now-on-github-2347dedd8b0c)

     [Constellation](https://github.com/edgelesssys/constellation) aims to provide an end-to-end confidential K8s framework.
     It wraps the K8s cluster in a confidential context, shielding it from the underlying cloud infrastructure.
     It supports running and scaling all containers; provides Sigstore-based node and artifact proof; provides Cilium-based network solutions, etc.

- [Consul Service Discovery Framework v1.13.0 release (CNCF project)](https://github.com/hashicorp/consul/releases/tag/v1.13.0)

     The main new features of this version: Remove support for Envoy 1.19; Cluster Peering supports federated Consul clusters for service grid and traditional service discovery; allows routing egress traffic through terminal gateways in transparent proxy mode without modifying the directory.

- [Contour Kubernetes ingress controller v1.22.0 release (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.22.0)

     The main new features of this version: support for Gateway API v0.5.0, allow configuring a direct response for a set of conditions in a single route, enable revocation checking for user certificate verification, merge access records and TLS cipher suite verification.

- [Contour Kubernetes ingress controller v1.21.0 release (CNCF project)](https://github.com/projectcontour/contour/releases/tag/v1.21.0)

     The main new features of this version: Contour's RBAC access to leader election resources has been transferred to the namespace role; container images are now only published on the GitHub Container Registry (GHCR); new `contour gateway-provisioner` command and deployment list for dynamic Configure Gateways.

- [Cortex Prometheus long-term storage solution v1.14 released](https://github.com/cortexproject/cortex/releases/tag/v1.14.0)

     Major new features in this version: Removed support for block storage, experimental support for vertical query sharding, enabled PromQL @modifier, can use OTel collector to send trace information to multiple destinations, multiple performance improvements and issues repair.

- [Cortex Distributed Prometheus Service v1.13.0 Release (CNCF Project)](https://github.com/cortexproject/cortex/releases/tag/v1.13.0)

     The main new features of this version: Add the streaming function of the metadata API queryer, provide experimental shuffle sharding support for compactor, fix the memory leak of Distributor and Ruler, add a jitter to reset the initial value of each pod when distributing requests time.

- [Crane cost optimization tool launches an open source cloud native application carbon emission calculation optimizer](https://mp.weixin.qq.com/s/D46-7S20kaMF4CH_H5oTuA)

     The carbon emission calculation optimizer calculates the corresponding server power consumption based on the actual resource consumption of the application running on the Kubernetes platform, and then calculates the carbon emission generated by the application operation.
     In addition, it also supports providing Pod resource configuration, wOptimization suggestions for the number of orkload copies, HPA parameter configuration, etc., as well as the optimized power consumption and carbon emission calculation results.

- [CRI-O Container Runtime v1.25.0 Release (CNCF project)](https://github.com/cri-o/cri-o/releases/tag/v1.25.0)

     The main new features of this version: support for setting the maximum log file size of pod at runtime, user namespace configuration capable of executing Kubelet, new annotations for configuring container power management, added minimum checkpoint/restore support, and signing statics through sigstore signatures binary package.

- [CRI-O Container Runtime v1.24.0 Release (CNCF project)](https://github.com/cri-o/cri-o/releases/tag/v1.24.0)

     Major new features in this release: block `unshare` syscall for containers without CAP_SYS_ADMIN by default, use task sets to generate new cri-o run commands, add pause and unpause functionality to CRI-O HTTP API.

- [CubeFS distributed storage system v3.1.0 release (CNCF project)](https://github.com/cubefs/cubefs/releases/tag/v3.1.0)

     The main new features of this version: provide QoS service to improve the multi-tenant isolation function, optimize the hybrid cloud multi-level read cache function, support two copies of data storage, support the configuration of posixAcl for volume management, and add a limit on the total number of data partitions for datanodes.

- [CubeFS distributed storage system upgraded from CNCF sandbox to incubation project](https://mp.weixin.qq.com/s/sAVaCa-yGEsJk3bUaJizmA)
  
     [CubeFS](https://github.com/cubefs) is the first cloud-native storage product in China with complete object and file storage capabilities.
     CubeFS supports multiple copies and erasure code engines, and provides features such as multi-tenant, multi-AZ deployment, and cross-region replication; it is suitable for a wide range of scenarios such as big data, AI, container platforms, databases, and middleware separation of storage and computing.

###D

- [Dapr Distributed Application Runtime v1.9.0 Release (CNCF project)](https://github.com/dapr/dapr/releases/tag/v1.9.0)

     The main new features of this version: allow custom pluggable components, support OTel protocol, add elastic observation indicators, support application health checks, support setting default elastic policies, allow service calls using any middleware components, add pub/sub Namespace consumer groups, support for Podman container runtime.

- [The first open source version of the DeepFlow automated cloud-native observability platform is officially released](https://mp.weixin.qq.com/s/79wZ00RKoei_boZfiUmqgg)

     [DeepFlow](https://github.com/deepflowys/deepflow) is an observability platform developed by Yunshan Network. Based on technologies such as eBPF, it realizes automatic synchronization of resources, services, and K8s custom labels and injects them into observations as labels data.
     It can automatically collect application performance indicators and track data without interpolation, and the innovative mechanism of SmartEncoding reduces the resource consumption of tag storage by 10 times.
     In addition, it can integrate a wide range of data sources and provide a northbound interface based on SQL.

- [DevSpace K8s development tools v6.0 released](https://github.com/loft-sh/devspace/releases/tag/v6.0.0)

     The main new features of this version: the introduction of pipeline to manage tasks in devspace.yaml, the new import function to merge different devspace.yaml files together, and the new proxy command to run commands executed in the container on the local computer.

###E

- [Envoy Gateway API Gateway v0.2 release](https://github.com/envoyproxy/gateway/releases/tag/v0.2.0)

     The main new features of this version: support for Kubernetes, support for Gateway API resources.

- [Envoy v1.23.0 released (CNCF project)](https://www.envoyproxy.io/docs/envoy/v1.23.0/version_history/v1.23/v1.23.0)

     The main new features of this version: send SDS resources of multiple clusters or listeners in one SDS request, obtain filter configuration through the configuration name of HTTP filter, update listener filter statistics, dns_resolver adds support for multiple addresses , Add dynamic listener filter configuration for listener filters, etc.

- [Envoy Gateway Open Source](https://blog.envoyproxy.io/introducing-envoy-gateway-ad385cc59532)

     [Envoy Gateway](https://github.com/envoyproxy/gateway) is officially a new member of the Envoy proxy family, a project aimed at lowering the barriers to using Envoy as an API gateway.
     Envoy Gateway can be thought of as a wrapper around the core of Envoy Proxy.
     The features it provides include: providing simplified API for gateway use cases, out-of-the-box controller resources, control plane resources, lifecycle management capabilities of proxy instances, etc., and an extensible API plane.

- [Emissary Ingress Cloud Native Ingress Controller and API Gateway v2.3.0 Release (CNCF Project)](https://github.com/emissary-ingress/emissary/releases/tag/v2.3.0)

     Main new features of this version: When using lightstep as the driver, `propagation_modes` can be set in `TracingService` configuration; support `crl_secret` can be set in `Host` and `TLSContext` resources to compare certificate revocation list checks and other certificates; optimize communication with external log services, etc.

- [eunomia-bpf: eBPF lightweight development framework officially open source](https://mp.weixin.qq.com/s/fewVoIKbLn5fYbXUaDyTpQ)

     [eunomia-bpf](https://gitee.com/anolis/eunomia) is jointly developed by universities and the Eunomia community, aiming to simplify the development, distribution and operation of eBPF programs. In eunomia-bpf, you only need to write the kernel mode code to run correctly, and do not need to recompile when deploying, and provide a standardized distribution method of JSON/WASM.

### F, G

- [Falco Runtime Security Project v0.32.0 Release (CNCF Project)](https://github.com/falcosecurity/falco/releases/tag/0.32.0)

     The main new features of this version: new ConfigMaps, when a rule or configuration file change is detected, Falco will be restarted; support for detecting containers with excessive permissions; support for detecting shared host pids and pods in the IPC namespace, etc.

- [Flagger Progressive Delivery Attack v1.22.0 released (CNCF project)](https://github.com/fluxcd/flagger/blob/main/CHANGELOG.md#1220)

     The main new features of this version: support for replacing HPA with KEDA ScaledObjects, adding namespace parameters in the parameter table, and adding an optional `appProtocol` field for Canary.Service.

- [Fluent Bit log processing tool v2.0.0 release (CNCF project)](https://github.com/fluent/fluent-bit/releases/tag/v2.0.0)

     The main new features of this version: Add support for Traces (fully integrated with Prometheus and OpenTelemetry), allow the input plug-in to run in a separate thread, all network transport layers that need to be enabled will use OpenSSL, and the input plug-in will add native TLS functionality , support for integrating more plugin types with Golang and WebAssembly, support for inspecting data flowing through pipelines, and introduction of new input plugins that collect and process internal metrics.

- [Fluentd log collection tool v1.15.0 released (CNCF project)](https://github.com/fluent/fluentd/releases/tag/v1.15.0)

     The main new features of this version: support for setting rate limit rules for log collection, support for processing YAML configuration formats, and allow setting the time interval for restarting workers.

- [Flux continuous delivery tool becomes CNCF graduation project](https://mp.weixin.qq.com/s/3F3DHuKEZqqd7M6-im6B-A)

     [Flux](https://github.com/fluxcd/flux2) is a continuous progressive delivery solution for Kubernetes that supports GitOps and progressive delivery for developers and infrastructure teams. Since becoming a CNCF incubation project in March 2021, Flux and its sub-project Flagger have grown 200-500% in terms of user base, integrations, software usage, user engagement, contributions, etc.

- [Flux continuous delivery tool v0.34.0 released (CNCF project)](https://github.com/fluxcd/flux2/releases/tag/v0.34.0)

     Major new features in this version: Flux controller logs are consistent with Kubernetes structured logs, allow OCI sources to be defined for non-TLS container registries, and static credentials are preferred over OIDC providers when pulling OCI artifacts from container registries in multi-tenant clusters By.

- [Gatekeeper Policy Engine v3.10.0 release (CNCF project)](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.10.0)

     The main new features of this version are: removing Pod security policy and migrating to Pod security admission, upgrading Mutation function to stable, introducing workload resource verification (alpha), and performance improvement.

- [Gatekeeper policy engine v3.9.0 release (CNCF project)](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.9.0)

     The main new features of this version: add constraint mode verification tests, add TLS support for external data providers, add pod security context variables, support verification sub-resources, allow skipping tests in gator verification, add dockerfile for gator, add opencensus and stackdriver exporter.

###H

- [HAProxy Kubernetes Ingress Controller v1.8 released](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-8/)

     The main new features of this version: reduce the permissions of all processes in the container, and no longer run the privileged container by default; expose an endpoint for viewing pprof diagnostic data; support the collection of Prometheus indicators inside the controller, such as the amount of memory allocated and spent CPU time; if the ingress rules do not match, it supports custom setting of the backend port.

- [Harbor Container Registry v2.6.0 release (CNCF project)](https://github.com/goharbor/harbor/releases/tag/v2.6.0)

     The main new features of this version: introduce a cache layer to improve the performance of fetching artifacts under high concurrency conditions; add CVE export function, allowing project owners and members to export CBR data generated by scanners; support regular cleaning of audit logs or run on demand, Support for forwarding audit logs to remote syslog endpoints; support for WebAssembly artifacts.

- [HashiCorp Vault private information management tool 1.11 adds Kubernetes Secret engine](https://github.com/hashicorp/vault/blob/main/website/content/docs/secrets/kubernetes.mdx)

     The Kubernetes Secret engine can dynamically generate Kubernetes service account tokens, service accounts, role bindings, and roles. The created service account token has a configurable TTL value (Time To Live), when the lease expires, Vault will automatically delete the created object. For each lease, Vault creates a token connected to the defined service account, and the service account token is returned to the caller.

- [Helm Package Manager v3.10.0 release (CNCF project)](https://github.com/helm/helm/releases/tag/v3.10.0)

     The main new features of this version: support to set json value through the command line, allow not to output the header when executing helm list, add parameters to configure client throttling limit, support to control whether to skip the certificate verification of kube-apiserver .

- [Helm Dashboard: Komodor open source Helm GUI](https://github.com/komodorio/helm-dashboard)

     The Helm Dashboard runs locally and opens in a browser, and can be used to view installed Helm Charts, view their revision history and corresponding k8s resources. In addition, it is possible to perform simple operations such as rolling back to a version or upgrading to a newer version.

- [Helm v3.9.0 release (CNCF project)](https://github.com/helm/helm/releases/tag/v3.9.0)

     The main new features of this version: new fields to support passing parameters to post renderer, more checks in the signing process, updated support for Kubernetes 1.24.

- [Higress: Alibaba Cloud Open Source Cloud Native Gateway](https://mp.weixin.qq.com/s/dgvd9TslzhX1ZuUNIH2ZXg)

     [Higress](https://github.com/alibaba/higress) follows the Ingress/Gateway API standard, combining traffic gateway, microservice gateway and security gateway, and extending the service management plug-in and security class on this basis Plug-ins and custom plug-ins are highly integrated with K8s and microservice ecology, including Nacos registration and configuration, Sentinel current limit and downgrade capabilities, and support hot update capabilities such as rule changes taking effect in milliseconds.

### I, J

- [All codes of iLogtail observable data collector open source](https://mp.weixin.qq.com/s/Cam_OjPWhcEj77kqC0Q1SA)

     Recently, Alibaba Cloud officially released the community version of [iLogtail](https://github.com/alibaba/ilogtail) with full functions.
     This update open-sources all C++ core codes, and this version aligns with the enterprise version for the first time in terms of core capabilities. Added many important features such as log file collection, container file collection, lock-free event processing, multi-tenant isolation, and new configuration methods based on Pipeline.

- [Istio v1.16 Announcement (CNCF project)](https://istio.io/latest/news/releases/1.16.x/announcing-1.16/)

     The main new features of this version: Three functions are upgraded to beta: external authorization function, Kubernetes Gateway API implementation, route-based JWT statement; add experimental support for HBONE protocol of sidecar and ingress gateway, support MAGLEV load balancing algorithm, and pass Telemetry The API supports the OpenTelemetry tracing provider.

- [Istio officially became a CNCF incubation project](https://istio.io/latest/blog/2022/istio-accepted-into-cncf/)

     The [Istio](https://github.com/istio/istio) Steering Committee submitted an application to hand over the project to CNCF in April this year. After nearly 5 months of review, it is now an incubating project.

- [Istio community launches Istio data plane mode Ambient Mesh without sidecar proxy](https://mp.weixin.qq.com/s/JpLPuqbPggXsQzFR5pii8A)

     [Ambient Mesh](https://github.com/istio/istio/tree/experimental-ambient) separates the data plane agent from the application pod and deploys it independently, completely solving the coupling problem between mesh infrastructure and application deployment.
     Through the introduction of zero trust tunnel (ztunnel) and Waypoint proxy (waypoint proxy) to achieve zero trust and reduce the resource occupation of the grid, it can also seamlessly interoperate with the sidecar mode, reducing the user's operation and maintenance costs.

- [Istio v1.14 release](https://istio.io/latest/news/releases/1.14.x/announcing-1.14/change-notes/)

     Main new features of this version:

     - Traffic governance: support sending unready endpoints to Envoy; optimize egress traffic interception; relax the restrictions on setting SNI; support filter to replace virtual hosts; add API `runtimeValues` in Proxy Config for Envoy runtime configuration.
     - Security: Support for CA integration via Envoy SDS API, support for `PrivateKeyProvider` in SDS, support for TLS provisioning API for workloads.
     - Telemetry: Added OpenTelemetry access log, added `WorkloadMode` option to log.
     - Extension: Support WasmPlugin to pull images from private repositories via `imagePullSecret`.

- [Jaeger Distributed Tracing System v1.36.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.36.0)

     The main new features of this version: support for reporting span size indicators, and increase multi-tenant support.

- [Jaeger v1.35.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.35.0)

     The main new features of this version: introduce the ability to receive OpenTelemetry tracking data through the OpenTelemetry Protocol (OTLP), define health servers for GRPC servers, add flags for enabling/disabling dependencies during rollover, and add TLS configuration for Admin Servers.

- [Jaeger Distributed Tracing System v1.34.0 release (CNCF project)](https://github.com/jaegertracing/jaeger/releases/tag/v1.34.0)

     The main new features of this version: add kubernetes instances for hotrod applications, add streamingSpanWriterPlugin to improve the writing performance of grpc plugins, add metrics to MetricsReader, etc.

- [Jakarta EE 10 Java-based framework released, opening the era of cloud-native Java](https://mp.weixin.qq.com/s/BQBy5AWFOc7kS55JBtBjiQ)

     [Jakarta EE 10](https://github.com/jakartaee/jakarta.ee) introduces features for building modern and lightweight cloud-native Java applications.
     These include: a new configuration file specification that defines a multi-vendor platform for lightweight Java applications and microservices; a subset of the specification for smaller runtimes suitable for microservice development, including the New CDI-Lite specification; supports polymorphic types; standardizes UUID as a primitive type and extends the query language and query API.

### K

- [k8gb Kubernetes Global Load Balancer v0.10.0 release (CNCF project)](https://github.com/k8gb-io/k8gb/releases/tag/v0.10.0)

     The main new features of this version: can access LeaderElection through environment variables, support the OpenTelemetry tracing scheme, support the creation of Grafana dashboard samples of K8GB indicators, and implement a consistent polling load balancing strategy.

- [Karmada multi-cloud multi-cluster container orchestration platform v1.4.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.4.0)

     The main new features of this version: new declarative resource interpreter, support for priority of declarative distribution strategy/cluster distribution strategy, enhanced observability through indicators and events, failover/elegant eviction FeatureGate is upgraded to Beta and enabled by default.

- [Karmada multi-cloud multi-cluster container orchestration platform v1.3.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.3.0)

     The main new features of this version: support taint-based elegant workload eviction, introduce global proxy for multi-cluster resource access, support cluster resource modeling, add Bootstrap token-based cluster registration method, optimize system scalability, etc.

- [Karmada cross-cloud multi-cluster container orchestration platform v1.2.0 release (CNCF project)](https://github.com/karmada-io/karmada/releases/tag/v1.2.0)

     The main new features of this version: optimize the scheduling strategy that changes over time; support cross-region deployment of workloads; `karmadactl` and `kubectl-karmada` support richer commands; add a distributed search and analysis engine for Kubernetes resources (alpha ); implement custom resource state collection.

- [Karpenter automatic scaling tool v0.19.0 released](https://github.com/aws/karpenter/releases/tag/v0.19.0)

     Major new features in this version: Evicting pods without a controller by default, migrating AWS settings from CLI Args to ConfigMap, supporting IPv6 auto-discovery, merging webhooks and controllers into one binary.

- [Kata Containers Secure Container Runtime v3.0.0 released](https://github.com/kata-containers/kata-containers/releases/tag/3.0.0)

     The main new features of this version: a new Rust language rewritten container runtime component and an optional integrated virtual machine management component, support for mainstream cloud-native ecological components (including Kubernetes,CRI-O, Containerd, and OCI container runtime standards, etc.), supports cgroupv2, and supports the latest stable version of the Linux kernel.

- [Kata Container Container Security Project v2.5.0 release](https://github.com/kata-containers/kata-containers/releases/tag/2.5.0)

     The main new features of this version: support containerd shimv2 log plugin, support virtio-block multi-queue, support QEMU sandbox function, support containerd core scheduling, kata-runtime iptables subcommand can operate iptables in guest, and support directly allocated volumes.

- [KEDA Event-Driven Autoscaler v2.9.0 Release (CNCF Project)](https://github.com/kedacore/keda/releases/tag/v2.9.0)

     The main new features of this version: add CouchDB, Etcd and Loki extensions, introduce Grafana dashboard for monitoring application auto-scaling, integrate all exposed Prometheus indicators in KEDA Operator, experimental support for extensions during polling intervals Cache metric values.

- [KEDA Kubernetes-based event-driven automatic scaling tool v2.8.0 released (CNCF project)](https://github.com/kedacore/keda/releases/tag/v2.8.0)

     The main new features of this version: support for NATS streaming, support for custom HPA names, support for specifying the minimum number of pod replicas in ScaledJob, and allow the cpu/memory scaler to scale only one container in the pod.

- [KEDA Kubernetes event-driven scaling tool v2.7.0 release (CNCF project)](https://github.com/kedacore/keda/releases/tag/v2.7.0)

     Major new features in this release: support for pausing autoscaling via ScaledObject annotations, new ARM-based container images, support for non-root KEDA default security mode, CPU, memory, Datadog extenders use global `metricType` instead of `metadata. type` etc.

- [Keptn Cloud Native Application Lifecycle Orchestration Project v0.19.0 release (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.19.0)

     The main new features of this version: Helm-service and Jmeter-service moved to the keptn contribution repository, support for verifying inbound events, introduction of signed Keptn Helm charts, and support for signing all released/pre-released container images through sigstore/cosign.

- [Keptn Cloud Native Application Lifecycle Orchestration Project v0.18.0 release (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.18.0)

     The main new features of this version: install/uninstall/upgrade commands are not available, use Helm to operate Keptn instead; in the resource API, tail `/` will return 404; configuration service is deprecated, all core services of Keptn depend on resource service .

- [Keptn Cloud Native Application Lifecycle Orchestration Engine Upgraded to CNCF Incubation Project](https://mp.weixin.qq.com/s/gkv_fSnrRv0ao1AHUzBB5A)

     [Keptn](https://github.com/keptn/keptn) is an event-based control plane that uses declarative programming methods to achieve continuous delivery and automatic repair of applications. Keptn will support GitOps and control warehouse management methods, RBAC, remote management of execution planes, etc. in the future.

- [Keptn Cloud Native Application Continuous Delivery and Automated Operation Tool v0.16.0 released (CNCF project)](https://github.com/keptn/keptn/releases/tag/0.16.0)

     Main new features of this version: `resource-service` replaces `configuration-service` to speed up response time and support Keptn upgrades without downtime; in v0.17, the CLI will remove install/uninstall/upgrade commands; support direct Sends events to Nats; service is considered ready only when connected to the control plane; allows running approval service without distributor sideCar.

- [Knative Kubernetes-based serverless architecture solution v1.8.0 release (CNCF project)](https://github.com/knative/serving/releases/tag/knative-v1.8.0)

     The main new features of this version: modify the default domain, upgrade HPA to version v2, allow setting seccompProfile to enable the use of restricted security profiles, the minimum k8s support version is upgraded to v1.23, the reconciliation timeout is increased to 30 seconds, and EmptyDir is enabled by default Volume function parameters.

- [Koordinator cloud-native hybrid system v1.0 released](https://github.com/koordinator-sh/koordinator/releases/tag/v1.0.0)

     The main new features of this version are: optimized task scheduling, optimized ElasticQuota scheduling, support for fine-grained device scheduling management mechanism, support for adjusting the CPU resource quota of BestEffort type Pod according to the load level of the node, support for using CPU Burst to improve the performance of delay-sensitive applications, Realize the eviction mechanism based on memory safety threshold and resource satisfaction, fine-grained CPU scheduling, support resource reservation without intruding Kubernetes' existing mechanisms and codes, and simplify the operation of custom rescheduling strategies.

- [Koordinator cloud-native hybrid system v0.6.0 released](https://github.com/koordinator-sh/koordinator/releases/tag/v0.6.0)

     The main new features of this version: improve the CPU fine-grained orchestration strategy, support resource reservation without intruding on the existing mechanisms and codes of Kubernetes, support Pod MigrationJob, and release a new Descheduler framework.

- [Kruise Rollout Progressive Delivery Framework v0.2.0 released](https://openkruise.io/docs/)

     The main new features of this version are: support for Gateway API, support for batch release of stateful applications, new "Pod batch marking" capability, integration into KubeVela to realize Helm Charts canary release capability.

- [KubeClipper: K8s multi-cluster lifecycle management tool open sourced by Kyushu Cloud](https://mp.weixin.qq.com/s/RVUB5Pw6-A5zZAQktl8AcQ)

     [KubeClipper](https://github.com/KubeClipper-labs) is based on the kubeadm tool for secondary packaging, providing rapid deployment of K8S clusters and continuous full lifecycle management (installation, uninstallation, upgrade, scaling, remote access, etc.) capabilities,
     It supports multiple deployment methods such as online, proxy, and offline, and also provides rich and scalable management services for CRI, CNI, CSI, and various CRD components.

- [KubeEdge cloud-native edge computing platform v1.12 release (CNCF project)](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.12.md)

     The main new features of this version: the introduction of the next generation of cloud-native device management interface (DMI), the new version of the lightweight engine Edged upgraded to GA, EdgeMesh new high-availability mode, support for edge nodes to upgrade from the cloud, support for edge Kube-API endpoints Authorization, support GigE Device Mapper.

- [KubeEdge Audit Report Release](https://github.com/kubeedge/community/blob/master/sig-security/sig-security-audit/KubeEdge-security-audit-2022.pdf)

     OSTIF (Open Source Technology Improvement Fund, Open Source Technology Improvement Foundation) completed a security audit of KubeEdge. The audit found 12 medium-severity issues, a threat model was built, and integrated into OSS Fuzz. The KubeEdge security team has fixed all issues in the newly released v1.11.1, v1.10.2 and v1.9.4.

- [KubeEdge cloud-native edge computing platform v1.11.0 release (CNCF project)](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.11.md)

     The main new features of this version: new node group management function; edge device Mapper SDK is provided to reduce the workload of developing Mapper; Keadm subcommands such as containerized deployment and offline security are officially supported; edge node agent Edged is applicable to more scenarios.

- [KubeKey Cluster Deployment Tool v3.0 released](https://github.com/kubesphere/kubekey/releases/tag/v3.0.0)

     Main new features of this version: Add GitHub workflow for docker build and push, support for executing custom setup scripts, add k3s control plane controller and startup controller, add k3s container runtime configuration, add k3s e2e test support, customize OpenEBS Base path, refactor KubeKey project, support more Kubernetes and k3s versions.

- [KubeKey cluster deployment tool v2.3.0 released](https://github.com/kubesphere/kubekey/releases/tag/v2.3.0)

     The main new features of this version: add kubelet pod pid restrictions, use Jenkins Pipeline instead of GitHub Actions, add security enhancement commands when creating clusters or adding nodes, clear vip when deleting clusters or nodes, support kube-vip BGP mode, support cleaning CRI, Support kube-vip, support the latest patch version released by k8s.

- [KubeKey cluster deployment tool v2.1.0 released (KubeSphere community open source)](https://github.com/kubesphere/kubekey/releases/tag/v2.1.0)

     The main new features of this version: According to the OCI standard, the image pulling, uploading, archiving and saving functions are realized, so that it does not rely on additional container runtimes when making and using KubeKey products; it supports the initialization of the operating system command (kk init os) Use products to install operating system dependencies from offline local sources; support both ARM64 nodes and AMD64 nodes in the same K8s cluster.

- [Kube-OVN v1.10.0 release (CNCF project)](https://mp.weixin.qq.com/s/e1TW_s3r9__qSgZz6aWmAA)

     The main new features of this version: ACL field is added in the subnet, and users can write ACL rules that conform to the OVN flow table specification according to their own needs; in the KubeVirt scenario, the address allocation strategy of VM instance adopts a strategy similar to that of StatefulSet, and supports DPDK, DHCP; Integrated SubMariner is used for the interconnection of multiple clusters; for large-scale environments, the performance of the control plane is optimized.

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

- [KubeSphere v3.3.0 release (CNCF project)](https://github.com/kubesphere/kubesphere/blob/master/CHANGELOG/CHANGELOG-3.3.md)

     Main new features of this version:

     - DevOps: The backend supports independent deployment, provides a GitOps-based continuous deployment solution, introduces Argo CD as the backend of CD, and can count the status of continuous deployment in real time.
     - Network: The integrated load balancer OpenELB can expose the LoadBalancer service even under the K8s cluster in a non-public cloud environment.
     - Multi-tenancy and multi-cluster: Cluster applications can obtain the name of the cluster through a ConfigMap, and support setting cluster members and cluster roles for the cluster.
     - Observability: Add container process/thread indicators, optimize disk usage indicators, and support importing Grafana templates in namespace custom monitoring.
     - Storage: Support PVC automatic expansion policy, support management of volume snapshot content and type, and support setting authorization rules for storage types.
     - Edge: KubeEdge integrated.

- [Kubespray Kubernetes cluster deployment tool v2.20.0 released](https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.20.0)

     Main new features of this version: Support Rocky Linux 8 and Kylin Linux, add "flush ip6tables" task in reset role, support NTP configuration, add kubelet systemd service hardening option, add rewrite plugin for CoreDNS/NodelocalDNS, add SeccompDefault for kubelet admission plugin, add extra_groups parameter for k8s_nodes, add ingress nginx webhook, add support for node and pod pid restrictions, and enable default Pod security configuration.

- [KubeVela hybrid multi-cloud environment application delivery platform v1.6.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.6.0)

     The main new features of this version: support resource delivery visualization, provide observable infrastructure construction, application-oriented observability, observability as code capabilities, support unified management of multi-environment pipelines, support configuration sharing between applications and third-party external systems Do configuration integration.

- [KubeVela hybrid multi-cloud environment application delivery platform v1.5.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.5.0)

     Main new features of this version: Plug-in framework optimization, providing management of the entire plug-in lifecycle such as creating scaffolding, packaging, and pushing to the plug-in registry; supporting defining plug-ins in CUE format, and using CUE parameters to render some plug-ins; adding a large number of vela cli command; VelaUX supports managing applications created by the CLI.

- [KubeVela v1.4.0 release (CNCF project)](https://github.com/kubevela/kubevela/releases/tag/v1.4.0)

     The main new features of this version: support multi-cluster authentication, automatic login of controllers using kubeconfig, support for more authorization methods; allow resources to be selected by resource type in GC policies, and new policy controllers to generate OpenAPI patterns for VelaUX and CLI parameters ; CLI supports displaying resource topology, etc.

- [KubeVirt Virtual Machine Management Plugin v0.58.0 released (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.58.0)

     Major new features in this release: Enable DataVolume garbage collection by default in cluster-deploy, ability to run with restricted Pod security enabled, add tls configuration, fix migration failure for VMs with containerdisks on systems with containerd.

- [KubeVirt Virtual Machine Management Plugin v0.57.0 released (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.57.0)

     The main new features of this version: deprecated SR-IOV live migration function gate, deprecated virtual machine instance preset resources, added support for virtual machine output resource types, supported DataVolume garbage collection, and allowed support for configuring virtual machine topology distribution constraints .

- [KubeVirt virtual machine running project v0.55.0 release (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)

     The main new features of this version: introduce clone CRD, controller and API, introduce deprecation policy, increase memory overhead of virt-launcher, enable memory dump to VMSnapshot, support monitoring VMI migration objects from creation to a specific stage required time, allowing the VMI to migrate from root to non-root.

- [KubeVirt virtual machine running project v0.55.0 release (CNCF project)](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)

     The main new features of this version: introduce clone CRD, controller and API, introduce deprecation policy, increase memory overhead of virt-launcher, enable memory dump to VMSnapshot, support monitoring VMI migration objects from creation to a specific stage required time, allowing the VMI to migrate from root to non-root.

- [Kubewarden Kubernetes Policy Engine v1.0.0 Release (CNCF Project)](https://www.kubewarden.io/blog/2022/06/v1-release/)

     The main new features of this version are: allowing policies to be written in Go, Rust or Swift, supporting the use of Kubewarden policies to replace each Pod Security Policy, integrating OpenTelemetry, and using the Sigstore project to implement software signing and verification.

- [KubeWharf: Bytedance Open Source Cloud Native Project Collection](https://mp.weixin.qq.com/s/uNbT3Ss0rBYc9pqlZe3n8Q)

     [KubeWharf](https://github.com/kubewharf) is a distributed operating system based on Kubernetes, which consists of a set of cloud-native components, focusing on improving system scalability, resource utilization, and scalability. Observability, security, etc., support scenarios such as large-scale multi-tenant clusters, offline mixing, and storage.
     The first batch of KubeWharf plans to open source three projects: KubeBrain, a high-performance meta-information storage system, KubeGateway, a seven-layer gateway for kube-apiserver, and KubeZoo, a lightweight multi-tenant solution.

- [Kuma Service Mesh v2.0 release (CNCF project)](https://github.com/kumahq/kuma/releases/tag/2.0.0)

     The main new features of this version: add support for eBPF in CNI and init container configuration, add 3 new "next generation" policies, optimize the user interface, support the configuration of TLS versions and ciphers supported by the control plane/API server, allow configuration Multiple UIDs make it ignored by traffic redirection, allowing logging to be turned on when using iptables for traffic redirection.

- [Kuma Service Mesh Project v1.8.0 release (CNCF project)](https://github.com/kumahq/kuma/releases/tag/1.8.0)The main new features of this version: cross-grid gateway supports multi-region operation, grid gateway/built-in gateway adds observability function, rewrites CNI, grid gateway supports path rewriting and header addition/deletion, supports filtering proxy indicators, Simplify the implementation of TCP traffic logs and support Projected Service Account Tokens.

- [KusionStack: Ant Group's open source programmable cloud-native protocol stack](https://mp.weixin.qq.com/s/EZrVKdZ_hG5-p_HltaTCMg)

     [KusionStack](https://github.com/KusionStack) deposits the operation and maintenance model ([Kusion Model](http://github.com/KusionStack/konfig)) through the self-developed DSL (KCL), and the infrastructure part The use of capabilities is changed from white screen to code, and combined with the DevOps tool chain (Kusion CLI) to achieve rapid configuration verification and validation, so as to improve the openness and operation and maintenance efficiency of the infrastructure.

- [Kusk Gateway Self Service API Gateway v1.1.0 Release](https://github.com/kubeshop/kusk-gateway/releases/tag/v1.1.0)

     The main new features of this version: support for specifying services or hosts to verify authentication headers, support for rate limiting policies, simplify the complexity of HTTP caching by annotating in the OpenAPI specification, and handle all mocking locally by Envoy.

- [Kyverno Cloud Native Policy Engine v1.8.0 release (CNCF project)](https://github.com/kyverno/kyverno/releases/tag/v1.8.0)

     The main new features of this version: add podSecurity verification sub-rules, integrate Pod Security Admission library; support YAML manifest signature verification; allow generation rules to generate multiple resources in a single rule; support OpenTelemetry; support test generation policies; support Kubernetes 1.25.

- [Kyverno cloud-native strategy engine upgraded to CNCF incubation project](https://mp.weixin.qq.com/s/GijHJm6-JcqfcLn91vSs6g)

     [Kyverno](https://github.com/kyverno/kyverno) is a policy engine built for Kubernetes that provides automation and security for K8s configuration management.
     Next, the project plans to add features such as YAML signing and verification, OpenTelemetry support, idempotent auto-generated pod controller policies, enhanced pod security standard integration, OCI-based policy bundling, in-cluster API calls, and more.

- [Kyverno Cloud Native Policy Engine v1.7.0 release (CNCF project)](https://github.com/kyverno/kyverno/releases/tag/v1.7.0)

     Main new features of this version: support query `mutate.target` via dynamic client, allow Kyverno jp to work on Yaml files, optimize image verification signatures, mutate existing resources when policies are updated, allow users to define inline variables in context , disable leader election for update request controllers, support apiCall and CLI updates in tests, etc.

### L

- [Lima Linux Virtual Machine v0.14.0 release (CNCF project)](https://github.com/lima-vm/lima/releases/tag/v0.14.0)

     The main new features of this version: support for virtual machine shared file system virtiofs, support for Apple's virtualization framework Virtualization.framework, and support for Containerd command-line tool nerdctl 1.1.0.

- [Linkerd Service Mesh Project v2.12.0 Release (CNCF Project)](https://github.com/linkerd/linkerd2/releases/tag/stable-2.12.0)

     The main new features of this version: allow users to define and execute authorization policies based on HTTP routes in a completely zero-trust manner; support configuration using the Kubernetes Gateway API; add support for `iptables-nft` to the initialization container.

- [Litmus Chaos Engineering Framework v2.14.0 release (CNCF project)](https://github.com/litmuschaos/litmus/releases/tag/2.14.0)

     The main new features of this version: Add support for containerd CRI in DNS experiment, support for http-chaos experiment in service mesh environment, add support for source and destination ports in network experiment, support for providing custom labels for chaos runner pods , Optimizing the description of probe state patterns in chaotic results.

- [Litmus Chaos Engineering Framework v2.10.0 release (CNCF project)](https://github.com/litmuschaos/litmus/releases/tag/2.10.0)

     The main new features of this version: add HTTP chaos experiments for Kubernetes applications; introduce m-agent (machine agent), which can now implement chaos on non-k8s objects; optimize the recovery of node warning line experiments when application status checks fail during chaos; Added support for Envoy proxy when using frontend nginx; optimized logging, etc. Litmusctl updates.

- [Longhorn Cloud Native Distributed Block Storage v1.3.0 release (CNCF project)](https://github.com/longhorn/longhorn/releases/tag/v1.3.0)

     Main new features of this version: support for multi-network K8s clusters, compatibility with fully managed K8s clusters (EKS, GKE, AKS), new Snapshot CRD, new Mutating & Validating admission webhooks, support for automatic identification and cleaning of unowned/unused volumes , introduce CSI snapshots, and support cluster expansion through Kubernetes Cluster Autoscaler.

### M

- [Merbridge: The service grid accelerator open sourced by DaoCloud has officially entered the CNCF sandbox](https://mp.weixin.qq.com/s/Ht1HuLxQ2RngrVD92TBl4Q)

     On December 14, the CNCF Foundation announced that Merbridge was officially included in the CNCF sandbox project. [Merbridge](https://github.com/merbridge/merbridge) is currently the only open source project in CNCF focused on using eBPF to accelerate service mesh.
     Through Merbridge, you only need to execute a command in the Istio cluster, and you can directly use eBPF instead of iptables to achieve network acceleration and improve service performance.

- [MetalLB Kubernetes Load Balancer v1.3.2 release (CNCF project)](https://metallb.universe.tf/release-notes/#version-0-13-2)

     The main new features of this version: support for configuration through CRD (no longer supports ConfigMap); can broadcast addresses in L2 or BGP mode, or only assign IP without broadcasting addresses; add node selector support for L2 Announcement and BGP Announcement; add BGPPeer selector; support for more flexible deployment using kustomize; add LoadBalancerClass support; support multi-protocol BGP.

- [MicroK8s lightweight Kubernetes distribution v1.25 released](https://github.com/canonical/microk8s/releases/tag/v1.25)

     Main new features of this version: Added "strict confinement" isolation level to limit host system access and enforce a stricter security posture, 25% reduction in snap size, support for mirror sideloading (sideloading), new plugins kube-ovn and osm-edge.

- [Mimir Prometheus long-term storage project v2.4.0 released](https://github.com/grafana/mimir/releases/tag/mimir-2.4.0)

     The main new features of this version: introduce query scheduler query-scheduler, and support DNS-based and ring-based two service discovery mechanisms; add API endpoints to expose the limit of each tenant; add new TLS configuration options; allow maximum limit Range query length.

- [Mimir Prometheus long-term storage project v2.3.0 released](https://github.com/grafana/mimir/releases/tag/mimir-2.3.0)

     The main new features of this version: support for ingesting indicators in OpenTelemetry format, new tenant alliance for metadata query, simplified object storage configuration, support for importing historical data, optimized instant query function, and enabled query sharding by default.

- [Mimir new feature: Integrating Graphite, Datadog, Influx and Prometheus metrics into a unified storage backend](https://grafana.com/blog/2022/07/25/new-in-grafana-mimir-ingest- graphite-datadog-influx-and-prometheus-metrics-into-a-single-storage-backend/)

     [Mimir](https://github.com/grafana/mimir) is an open source timing database based on Cortex by Grafana Labs.
     Mimir now open-sources [three proxies](https://github.com/grafana/mimir-proxies) for ingesting metrics from Graphite, Datadog, and InfluxDB and storing them in System uptake metrics lay the groundwork.
     OTLP for native ingestion of OpenTelemetry will be supported in the future.

- [MinIO object storage tools release new features: extended repository and official support for OPA (CNCF project)](https://github.com/minio/minio/releases/tag/RELEASE.2022-05-08T23-50-31Z )

     MinIO has extended the repository to exclude certain prefixes and folders in the repository to improve the performance of applications such as the Spark S3A connector. Additionally, following widespread requests, MinIO officially supports OPA.

###N

- [Nacos Dynamic Service Discovery Platform v2.2.0 released](https://github.com/alibaba/nacos/releases/tag/2.2.0)

     The main new features of this version: support batch registration and batch logout services, support openAPI 2.0, add multi-data source plug-ins, add track tracking plug-ins, support Prometheus http service discovery, and support Ldaps authentication.

- [Nacos Dynamic Service Discovery Platform v2.1.0 release (CNCF project)](https://github.com/alibaba/nacos/releases/tag/2.1.0)

     The main new features of this version: Two new SPI plug-ins are added: respectively used to configure encryption, decryption and authentication, support cluster gRPC client to set thread pool size, support reset raft cluster, etc.

- [NeuVector Container Security Platform v5.0Release](https://mp.weixin.qq.com/s/nZ_a7JiryZJskJEPPIEmcw)

     The main new features of this version: integration with SUSE Rancher, and can also be docked with other enterprise-level container management platforms such as Amazon EKS, Google GKE, and Microsoft AKS; support for web application firewall detection; support for automated container protection; support for zero-drift process and file protection And the network, process/file segmentation strategy mode protection, etc.

- [Nightgale v5.10 released](https://github.com/ccfos/nightingale/releases/tag/v5.10.0)

     The main new features of this version: support recording rule management, alarm rules support multi-cluster, dashboard variables support TextBox, alarm masking supports more operators, and more flexible custom alarm content.

- [Notification Manager multi-tenant notification management system 2.0.0 released](https://mp.weixin.qq.com/s/op79OMTp0nxzfxM8fH-nnA)

     [Notification Manager](https://github.com/kubesphere/notification-manager) can receive alarms, events, and audits from Kubernetes, generate notification messages according to templates set by users, and push them to users.
     Main functions of the new version: new routing function, users can send specified notifications to specified users by setting routing rules; new silent function, by configuring silent rules, specific notifications can be blocked in a specific time period; support dynamic update templates Wait.

### O

- [OCM multi-cluster management platform v0.9 release (CNCF project)](https://www.cncf.io/blog/2022/10/31/open-cluster-management-november-2022-update/)

     The main new features of this version: reduce the permissions of the worker agent on the managed cluster, support access to kube-apiserver and other services in the managed cluster, and support the use of AddOn API to refer to AddOn configuration.

- [OPA Common Policy Engine v0.44.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.44.0)

     The main new features of this version: fix 3 CVE vulnerabilities, Set Element Addition optimization, built-in Set union optimization, add optimization parameters to OPA evaluation command, allow more bundlers to be compiled into WASM.

- [OPA Common Policy Engine v0.43.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.43.0)

     Major new features in this release: linear scaling optimization for Rego Object inserts, status and log plugins now accept HTTP 2xx status codes, OPA bundle commands now support .yml files, storage system fixes, Rego compiler and runtime environment bug fixes and optimizations.

- [OPA Common Policy Engine v0.41.0 release (CNCF project)](https://github.com/open-policy-agent/opa/releases/tag/v0.41.0)

     The main new features of this version: a new set of built-in functions for validating, parsing, and verifying GraphQL queries and schemas; built-in function declarations support specifying the names and descriptions of function parameters and return values ​​through metadata; support skipping based on the summary of OCI artifacts Bundle reload; delete empty list in bundle signature; unit resolution and token update, etc.

- [OpenClusterManagement (OCM) multi-cluster management platform v0.7 release (CNCF project)](https://mp.weixin.qq.com/s/EQgdnZVOqzfvuxOzg-Q0cQ)

     The main new features of this version: Add the "DefaultClusterSet" function, all managed clusters registered in the OCM environment will be registered in the ClusterSet named "default" by default; support multi-cluster scheduling based on Taint / Toleration semantics; deployment architecture Adjust to the "Hosted deployment" mode, that is, no other components need to be deployed in the managed cluster, and all proxy controllers are executed remotely.

- [OpenEBS Cloud Native Storage v3.3.0 release (CNCF project)](https://github.com/openebs/openebs/releases/tag/v3.3.0)

     Major new features in this release: deprecated arch-specific container images, enforced hostpath quotas with ext4 filesystems for LocalPV Hostpath, enhanced NDM functionality, added logging in cstor to improve debugging, added rate limiters to reduce LocalPV Log flooding issue in LVM.

- [OpenKruise Cloud Native Application Automation Management Suite v1.3.0 release (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.3.0)

     The main new features of this version: support custom probes and return the results to Pod yaml, SidecarSet supports injecting pods under the kube-system and kube-public namespaces, adds timezone support for upstream AdvancedCronJob, WorkloadSpread supports StatefulSet.

- [OpenKruise Cloud Native Application Automation Management Suite v1.2.0 released (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.2.0)

     The main new features of this version: Added CRD `PersistentPodState` to persist certain states of Pods, such as "fixed IP scheduling"; CloneSet calculates logic changes for percentage-based partitions; sets Pod not-ready in the lifecycle hook stage; supports protection scale Any custom workload for subresource; new performance optimization methods for large-scale clusters, etc.

- [Open Service Mesh v1.2.0 release (CNCF project)](https://github.com/openservicemesh/osm/releases/tag/v1.2.0)

     The main new features of this version: support for custom trust domains (that is, the common name of certificates), Envoy updated to v1.22, and use envoyproxy/envoy-distroless mirroring, added support for Kubernetes 1.23 and 1.24, support for limiting TCP connections and HTTP requests local per-instance rate, fix Statefulset and headless service.

- [OpenShift Toolkit 1.0, simplifying the development of cloud-native applications](https://cloud.redhat.com/blog/announcing-openshift-toolkit-enhance-cloud-native-application-development-in-ides)

     [OpenShift Toolkit](https://github.com/redhat-developer/vscode-openshift-tools) is a set of extensions for VS Code and IntelliJ. Its features include: support for connecting and configuring OpenShift; providing hybrid cloud support, developers can connect to any running OpenShift instance; develop applications through local workspaces, git repositories, or default devfile templates; allow one-click Strategy, directly deploy warehouse code to OpenShift; provide Kubernetes resource management, seamless Kube configuration context switching; multi-platform s platform support.

- [OpenTelemetry v1.13.0 release (CNCF project)](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.13.0)

     The main new features of this version: Context is immutable when setting span, supports experimental configuration of default histogram aggregation of OTLP indicator exporter, allows log processor to modify log records, adds experimental event and log API specifications, in Add network indicators to process semantic conventions, and add semantic conventions to GraphQL.

- [OpenTelemetry Metrics release RC version](https://opentelemetry.io/blog/2022/metrics-announcement/)

     RC versions of OpenTelemetry metrics have been released for Java, .NET, Python (JS coming next week). This means that the specification, API, SDK, and components that interact with metrics in the way of authoring, capturing, processing, etc., now have the full OTel metrics feature set ready to use.

- [OpenTelemetry v1.11.0 release (CNCF project)](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.11.0)

     The main new features of this version: replace the histogram with a more clear bucket histogram, support displaying examples on OpenMetrics counters, increase the semantic specification of database connection pool indicators, allow all metrics specifications to be synchronous or asynchronous, add HTTP/3, etc.

- [Openyurt Cloud Native Edge Computing Project v1.1.0 release (CNCF project)](https://github.com/openyurtio/openyurt/releases/tag/v1.1.0)

     The main new features of this version: support OTA/automatic upgrade mode of DaemonSet workload, support autonomous function verification of e2e test, enable data filtering function, add suggestions for unified cloud computing edge communication solution, and improve health checker.

- [Openyurt Cloud Native Edge Computing Project v1.0.0 release (CNCF project)](https://github.com/openyurtio/openyurt/releases/tag/v1.0.0)

     The main new features of this version: NodePool API version upgrade to v1beta1, use CodeCov to track unit test coverage, and add two new performance test reports for OpenYurt components.

- [OpenKruise Cloud Native Application Automation Management Suite v1.2.0 released (CNCF project)](https://github.com/openkruise/kruise/releases/tag/v1.2.0)

     The main new features of this version: Added CRD `PersistentPodState` to persist certain states of Pods, such as "fixed IP scheduling"; CloneSet calculates logic changes for percentage-based partitions; sets Pod not-ready in the lifecycle hook stage; supports protection scale Any custom workload for subresource; new performance optimization methods for large-scale clusters, etc.

- [osm-edge: Yiheng Technology Flomesh open source edge service grid](https://mp.weixin.qq.com/s/tbCxbKFQkvx84Ku5IWg38g)

     [osm-edge](https://github.com/flomesh-io/osm-edge) uses [osm](https://github.com/openservicemesh/osm) as the control plane and Programmable Gateway [Pipy](https://github.com/flomesh-io/pipy) as the data plane.
     Support SMI specification; support [fsm](https://github.com/flomesh-io/fsm) for ingress, gateway API, and cross-cluster service discovery, and provide "east-west + north-south" traffic of "k8s cluster + multi-cluster" Management and service governance capabilities.
     Its development and testing environment uses k3s, k8e, etc., so users can quickly and cost-effectively deploy low-resource, high-performance service grids on x86, arm, RISC-V, Loongson and other hardware platforms.

### P

- [Paralus: The industry's first open-source zero-trust access service for Kubernetes by Rafay Systems](https://rafay.co/the-kubernetes-current/paralus-industrys-first-open-source-zero-trust-access-service- for-kubernetes/)

     The main functions of [Paralus](https://github.com/paralus/paralus) are: it can handle the access management of multiple clusters in a unified way, allows integration with existing RBAC policies and SSO providers, and supports recording of user actions performed by users in the organization. Each kubectl command supports OIDC, supports creating custom roles with specific permissions, and allows dynamic revoking of permissions, etc.

- [Phlare: Grafana open source large-scale continuous profiling database] (https://grafana.com/blog/2022/11/02/announcing-grafana-phlare-oss-continuous-profiling-database/)

     [Phlare](https://github.com/grafana/phlare) is a horizontally scalable, highly available, multi-tenant continuous analysis data aggregation system, fully integrated with Grafana, and can be related to observation indicators such as indicators, logs and traces couplet. Installation requires only one binary and no other dependencies.
     Phlare uses object storage for long-term data storage and is compatible with multiple object storage implementations. Its native multi-tenancy and isolation feature set allows multiple independent teams or business units to run a single database.

- [Pisanix: SphereEx Open Source Solution for Database Mesh](https://mp.weixin.qq.com/s/p8bi14s8FWdp7GlqQxKzzw)

     [Pisanix](https://github.com/database-mesh/pisanix) helps users easily implement SQL-aware traffic governance based on the Database Mesh framework, runtime-oriented resource programming, database reliability engineering and other capabilities to help users Database governance on the cloud. Pisanix currently supports the MySQL protocol, mainly including three components: Pisa-Controller, Pisa-Proxy and Pisa-Daemon (coming soon).

- [Pixie Kubernetes observation platform releases Plugin System](https://www.cncf.io/blog/2022/07/06/easy-observability-with-open-standards-introducing-the-pixie-plugin-system/) 

     [Pixie Plugin System](https://github.com/pixie-io/pixie-plugin) allows users to export their Pixie data into any service that supports OpenTelemetry. This means users can leverage external data storage for long-term data retention, seamlessly adopt Pixie in existing workflows and dashboards, and combine Pixie data with other data streams.

- [Podman container engine v4.3.0 released](https://github.com/containers/podman/releases/tag/v4.3.0)

     Command update: support changing container resource limits, delete pods and containers created by K8s YAML, support K8s secret, support reading YAML from URL, support emptyDir volume type, support binary data in ConfigMap; support repeated volume mounts.

- [Podman container runtime project v4.2.0 released](https://github.com/containers/podman/releases/tag/v4.2.0)

     The main new features of this version: support for GitLab Runner, new commands for creating copies of existing pods, new commands for synchronizing state changes between the database and any volume plugins, new exit policies for pods, and automatic cleanup of unused pods Caches Podman virtual machine images, allowing multiple overlay volumes of different containers to reuse the same workdir or upperdir.

- [Prometheus v2.40.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.40.0)

     The main new features of this version: add experimental support for native histograms, Kubernetes discovery client supports the use of protobuf encoding, improve sorting speed, and increase enterprise management partitions.

- [Prometheus v2.39.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.39.0)

     The main new features of this version: add experimental support for ingesting unordered samples, and optimize memory resource usage.

- [Prometheus v2.37.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)

     Major new features in this release: allow Kubernetes service discovery to add node labels to targets from endpoint roles, TSDB memory optimization, reduce sleep time when reading WAL, optimize signature creation, add timeout and User-Agent header.

- [Prometheus v2.37.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)

     Major new features in this release: Allow Kubernetes service discovery to add node labels to targets from endpoint roles, TSDB memory optimization, reduce sleep time when reading WAL, optimize signature creation, add timeout and User-Agent header.

- [Prometheus v2.36.0 release (CNCF project)](https://github.com/prometheus/prometheus/releases/tag/v2.36.0)

     The main new features of this version: Vultr integration, Linode SD failure count indicator and `prometheus_ready` indicator added, `stripDomain` added to the template function, promtool supports using matchers when querying label values, and proxy pattern identifiers added.

### R, S

- [Rainbond cloud-native multi-cloud application management platform v5.9.0 released](https://github.com/goodrain/rainbond/releases/tag/v5.9.0-release)

     The main new features of this version: support for Containerd container runtime, support for using the grctl command to change the cluster API address, support for K8s 1.24 and 1.25, support for MiniKube deployment, and support for custom monitoring rules.

- [Rainbond cloud-native multi-cloud application management platform v5.8.0 released](https://github.com/goodrain/rainbond/releases/tag/v5.8.0-release)

     The main new features of this version: support for one-click import of existing applications in the Kubernetes cluster, support for deploying components directly through Jar, War packages or Yaml files, support for creating Job/CronJob type tasks, support for extending the properties supported by applications and components, and support for Dockerfile Build using a private image.

- [Serverless-cd: Serverless Devs released a lightweight CI/CD framework based on Serverless architecture——](https://mp.weixin.qq.com/s/ps_ZFsv7KGwV2V61SvvWIA)

     Serverless Devs is the industry's first platform that supports cloud-native full lifecycle management of mainstream serverless services/frameworks. [Serverless-cd](https://github.com/Serverless-Devs/serverless-cd) is built based on Serverless Devs, fully follows the best practices of Serverless architecture, and refers to the implementation of Github Action at the specification and ecological level. It adopts the Master Worker model and event-driven architecture, which can be used to quickly build an enterprise internal application management PaaS platform.

- [Serverless Devs entered the CNCF sandbox and became the first serverless tool project selected](https://mp.weixin.qq.com/s/ICVDO3U5Ea1DzP3LFJq8mQ)

     [Serverless Devs](https://github.com/Serverless-Devs/Serverless-Devs) is open sourced by Alibaba Cloud and is committed to providing developers with a powerful tool chain system. In this way, developers can not only experience multi-cloud serverless products with one click, quickly deploy serverless projects, but also carry out project management in the whole lifecycle of serverless applications, integrate with other tools/platforms, and improve the efficiency of R & D and operation and maintenance.

- [Skywalking application performance monitoring system v9.3.0 released](https://github.com/apache/skywalking/releases/tag/v9.3.0)

     The main new features of this version: increase the indicator correlation function, use Sharding MySQL as the database, visualize the performance of virtual cache and message queue, use Skywalking OpenTelemetry receiver instead of prometheus-fetcher plug-in to grab Prometheus indicators.

- [Skywalking application performance monitoring system v9.2.0 released](https://github.com/apache/skywalking/releases/tag/v9.2.0)

     The main new features of this version: Added eBPF network analysis function of K8s Pod, support for MySQL and PostgreSQL monitoring, correlation event component and tracking, and log component.

- [Skywalking application performance monitoring system v9.1.0 release (CNCF project)](https://github.com/apache/skywalking/releases/tag/v9.1.0)

     Main new features of this version: update the eBPF Profiling task to the service level; add a layer field to the event, and prohibit the reporting of events without a layer; the Zipkin receiver mechanism is changed, and the trace no longer flows to the OAP segment; SQL database related updates; remove InfluxDB 1. x and Apache IoTDB 0.X storage scheme, add BanyanDB storage scheme (still in development).

- [SPIFFE and SPIRE projects officially become CNCF graduate projects](https://www.cncf.io/announcements/2022/09/20/spiffe-and-spire-projects-graduate-from-cloud-native-computing-foundation-incubator/)

     [SPIFFE](https://github.com/spiffe/spiffe) provides secure identities for various workloads in modern production environments, eliminates the need to share confidential information, and is expected to become the foundation for higher-level platform-neutral security controls Realize the basis.
     [SPIRE](https://github.com/spiffe/spire) (SPIFFE Runtime Environment) is responsible for implementing the SPIFFE specification on various platforms and enforcing multi-factor proof of identity.

- [Spring Cloud Tencent: Tencent Open Source One-Stop Microservice Solution](https://mp.weixin.qq.com/s/A-DcZJY9sJcTQSEoWEibww)

     [Spring Cloud Tencent](https://github.com/Tencent/spring-cloud-tencent) Relying on Polaris, Tencent's open-source one-stop microservice solution, it mainly provides common service registration, discovery, and configuration in the field of microservices Center, service routing, current limiting and fusing, and metadata link transparent transmission capabilities.

- [K8s operator v0.31.0 release of Strimzi message middleware Kafka (CNCF project)](https://github.com/strimzi/strimzi-kafka-operator/releases/tag/0.31.0)

     Main new features of this version: support for Kafka 3.2.1; pluggable Pod security profile, built-in support for restricted Kubernetes security profile; support for leader election and running multiple operator copies; support for using IPv6 in certificates issued by Strimzi address.

- [SuperEdge edge container management system v0.8.0 release (CNCF project)](https://github.com/superedge/superedge/releases/tag/v0.8.0)

     The main new features of this version: separate edgeadm from the SuperEdge project, tunnel supports http_proxy capability, Lite-apiserver supports caching some key resources (nodes, services, etc.) and ExternalName Service forwarding on edge nodes.

- [Sylva cloud-native infrastructure stack launched by Linux Foundation Europe to lay a cloud-native foundation for telecom services](https://www.prnewswire.com/news-releases/linux-foundation-europe-announces-project -sylva-to-create-open-source-telco-cloud-software-framework-to-complement-open-networking-momentum-301678955.html)

     [Sylva](https://gitlab.com/sylva-projects/sylva) Leverages container network functions (CNF) and cloud-native platforms such as Kubernetes to create a telecom cloud technology stack to reduce the fragmentation of cloud infrastructure for telecom and edge services sex.
     The technology stack provided by Sylva consists of 5 components: network performance (SRIOV, DPDK, designated CNI, etc.), distributed cloud (multi-cluster Kubernetes, bare metal automation), energy efficiency, security (hardening and compliance), and openness and standardized API.

### T

- [TDengine Cloud Native Time Series Database v3.0 released](https://github.com/taosdata/TDengine/releases/tag/ver-3.0.0.0)

     The main new features of this version: support data collected by 1 billion devices, 100 nodes; support separation of storage and computing, introduce computing nodes, and restructure the entire computing engine; optimize support for message queues, streaming computing, and caching , introduce event-driven stream computing; support container and Kubernetes deployment.

- [Tekton Cloud Native CI/CD Framework v0.42.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.42.0)

     The main new features of this version: support for configuring the Webhook port number, support for setting source values for cluster resources, add a new feature flag related to the status governance field, support for recording the source of remote resources, and add verification functions in reconciler.

- [Tekton Cloud Native CI/CD Framework v0.40.0 released](https://github.com/tektoncd/pipeline/releases/tag/v0.40.0)

     The main new features of this version: add task running templates, support for propagating workspace in pipelinerun to simplify specification writing, optimize git remote resolution support, add cluster remote resolvers, merge affinity parameters of podtempalte and affinity-assistant.

- [Tetragon: Isovalent open source eBPF-based security observability and runtime enhancement platform](https://isovalent.com/blog/post/2022-05-16-tetragon)

     [Tetragon](https://github.com/cilium/tetragon) provides fully transparent security observability capabilities based on eBPF and real-time runtime enhancement capabilities.
     Tetragon has smart kernel filtering capabilities and aggregation logic built directly into its eBPF-based kernel-level collector, so deep observability can be achieved with very low overhead without requiring application changes.
     The embedded runtime execution layer can not only perform access control at the system call level,
     It also detects escalation of privileges, Capabilities, and namespaces, and automatically blocks further execution of affected processes in real time.

- [ThreatMapper Cloud Native Security Observation Platform v1.4.0 released](https://github.com/deepfence/ThreatMapper/releases/tag/v1.4.0)

     The main new features of this version: the new function ThreatGraph can combine the network and other runtime environments to determine the priority of threat scanning results, support agentless cloud security situation management for cloud assets, and integrate cloud-native environment malicious program scanning tools [YaraHunter] ( https://github.com/deepfence/YaraHunter).

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

     According to Aqua, [Trivy]((https://github.com/aquasecurity/trivy)) is the most comprehensive vulnerability and misconfiguration scanning tool available,
     Can be used to scan cloud-native applications and infrastructure such as source code, repositories, images, artifact registries, Infrastructure-as-Code (IaC) templates, Kubernetes environments, and more.

### V

- [Vcluster virtual Kubernetes cluster implementation v0.13.0 released](https://github.com/loft-sh/vcluster/releases/tag/v0.13.0)

     The main new features of this version: adding log and backup functions, adding high availability support for k3s with external data storage, and automatically synchronizing CSI resources when the vcluster scheduler is turned on.

- [Velero backup disaster recovery tool v1.10.0 release (CNCF project)](https://github.com/vmware-tanzu/velero/releases/tag/v1.10.0)

     The main new features of this version: introduce unified repository architecture, integrate cross-platform backup tool [Kopia](https://github.com/kopia/kopia), refactor file system backup, use Kubebuilder v3 to refactor the controller, Allows adding credentials for volume snapshot locations, enhances the robustness of CSI snapshots, supports pausing backup plans, and renames some modules and parameters.

- [Velero backup disaster recovery tool v1.9.0 release (CNCF project)](https://github.com/vmware-tanzu/velero/releases/tag/v1.9.0)

     The main new features of this version: CSI support improvements, refactoring of the controller using Kubebuilder v3, support for restoring the state of selected resources, and support for updating existing resources during resource restoration.

- [Virtink: A lightweight Kubernetes-native virtualization management engine open sourced by SmartX](https://mp.weixin.qq.com/s/LOZ8RhFE_9SZKwcdV90dPw)

     Unlike KubeVirt, [Virtink](https://github.com/smartxworks/virtink) does not support legacy hardware device simulation and desktop application scenario capabilities, but uses [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor) As the underlying virtualization manager, it only supports modern cloud workloads and can be installed in Kubernetes on any virtualized CPU platform to support virtualized workloads in a safer and lighter way.

- [Vitess Cloud Native Database System v14.0.0 release (CNCF project)](https://github.com/vitessio/vitess/releases/tag/v14.0.0)

     The main new features of this version: officially support online DDL, Gen4 becomes the default planner, add cluster management API and UI - VTAdmin (Beta), add a branch of Orchestrator running as a Vitess component - VTOrc (Beta), support cross Aggregation query of multiple shards and keyspaces.

- [Volcano Cloud Native Batch Computing Project v1.6.0 release (CNCF project)](https://github.com/volcano-sh/volcano/releases/tag/v1.6.0)

     The main new features of this version: support dynamic scheduling and rescheduling based on real node load, support elastic job scheduling, add MPI job plug-ins, allow tasks not to retry when they fail, support checking the overhead of pod requests, and support enqueueing in pod groups Resource quotas are considered in the process, and the default privileged container passes the verification of admission webhook.

### W, X, Z

- [Wolfi: Chainguard Releases First Linux Distribution to Secure Software Supply Chain, Designed for Containers and Cloud-Native Environments](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux- un-distro)

     [Wolfi](https://github.com/wolfi-dev) is a stripped-down Linux distribution designed for cloud-native, but it does not have a Linux kernel, instead relying on the environment (such as a container runtime) to provide the kernel. Main features: Provide high-quality build-time SBOM as a standard for all packages; packages are fine-grained and independent of each other to support lightweight mirroring; use mature and reliable apk package format, fully declarative, repeatable Build system, supports glibc and musl.

- [Xline is open sourced by DatenLord: Achieving data consistency management across data centers](https://mp.weixin.qq.com/s/NqScUOjUA1t4gdNeLEcPwg)

     [Xline](https://github.com/datenlord/Xline) aims to solve the problem that etcd cannot fully meet the needs of cross-cloud and cross-data center scenarios. Xline is a distributed KV storage, which is used to manage a small amount of critical data, and still ensure high performance and strong data consistency in cross-cloud and cross-data center scenarios. It is compatible with the etcd interface, allowing users to use and migrate more smoothly.

- [Zadig cloud-native continuous delivery tool v1.12.0 released](https://github.com/koderover/zadig/releases/tag/v1.12.0)

     The main new features of this version: support for code scanning, support for service association with multiple builds, K8s YAML project support for importing services from existing K8s, support for synchronizing service configuration from the Gitee code base, support for automatically updating the environment after service configuration changes, and support for global construction Template, K8s Helm Chart environment supports self-test mode, supports integration of multiple Jenkins, etc.
