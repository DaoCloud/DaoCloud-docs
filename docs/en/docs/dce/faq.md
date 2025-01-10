# Frequently Asked Questions

This is an index page for FAQs and troubleshooting for DCE 5.0.

## Installation

- UI Login Issues
    - [Cannot open DCE 5.0 interface after installation is complete; you can execute the diag.sh script for quick troubleshooting](../install/faq.md#troubleshoot-dce-50-ui-issues-with-diagsh)
    - [DCE 5.0 login interface cannot be opened due to VIP access issues when installing with Metallb](../install/faq.md#vip-access-issues-when-using-metallb-preventing-the-dce-login-page-from-opening)
- bootstrap node Issues
    - [After shutting down and restarting the bootstrap node, the kind cluster cannot restart properly](../install/faq.md#after-shutting-down-and-restarting-the-bootstrap-node-the-kind-cluster-cannot-restart-properly)
    - [Missing ip6tables when deploying Ubuntu 20.04 as a seed machine](../install/faq.md#missing-ip6tables-when-deploying-ubuntu-2004-as-a-bootstrap-node)
    - [After disabling IPv6 during installation, Podman on the bootstrap node cannot create containers](../install/faq.md#after-disabling-ipv6-during-installation-podman-on-the-bootstrap-node-cannot-create-containers)
    - [After restarting the bootstrap node's kind container, the kubelet service cannot start](../install/faq.md/#after-restarting-the-kind-container-on-the-bootstrap-node-the-kubelet-service-cannot-start)
    - [How to uninstall data from the bootstrap node](../install/faq.md#how-to-uninstall-data-from-the-bootstrap-node)
- Certificate Issues
    - [The kubeconfig for the global service cluster needs to be updated on the seed's replica](../install/faq.md#the-kubeconfig-of-the-global-cluster-needs-to-be-updated-on-the-bootstraps-replica)
    - [Certificate updates and kubeconfig for the kind cluster on the bootstrap node](../install/faq.md#updating-the-certificates-and-kubeconfig-of-the-kind-cluster-on-the-bootstrap-node-itself)
    - [After installing Contour, the default certificate validity period is only one year and does not auto-renew, causing the contour-envoy component to restart continuously after expiration](../install/faq.md#after-installing-contour-the-default-certificate-validity-period-is-only-one-year-and-will-not-auto-renew-leading-to-continuous-restarts-of-the-contour-envoy-component)
- Operating System Related Issues
    - [Error during installation on CentOS 7.6](../install/faq.md#error-during-installation-on-centos-76)
    - [CentOS environment preparation issues](../install/faq.md#centos-environment-preparation-issues)
- Community Edition Installation Issues
    - [Redis gets stuck during DCE 5.0 reinstallation in kind cluster](../install/faq.md#redis-hanging-during-dce-50-reinstallation-of-the-kind-cluster)
    - [Failed to install fluent-bit in the community edition](../install/faq.md#community-version-fluent-bit-installation-failure)

## Workbench

- Pipeline Related Issues
    - [Error when executing the pipeline](../amamba/faq/faq-jenkins.md#error-when-running-a-pipeline)
    - [How to update the podTemplate image for built-in Label?](../amamba/faq/faq-jenkins.md#update-podtemplate-image-of-built-in-labels)
    - [When the pipeline build environment is Maven, how to modify the dependency package source in settings.xml?](../amamba/faq/faq-jenkins.md#modify-dependency-source-in-settingsxml-in-maven)
    - [When building images through Jenkins, containers cannot access private registry](../amamba/faq/faq-jenkins.md#unable-to-access-private-container-registries-when-building-images-through-jenkins)
    - [How to modify the concurrency execution count of Jenkins pipelines](../amamba/faq/faq-jenkins.md#how-to-modify-the-number-of-concurrent-running-of-jenkins-pipelines)
    - [What to do if the pipeline running status does not update in time?](../amamba/faq/faq-jenkins.md#unable-to-update-pipeline-running-status-in-time)
- GitOps Related Issues
    - [Error when adding a GitHub repository under the GitOps module](../amamba/faq/faq-gitops.md#error-when-adding-a-github-repo)
    - [When adding a repository in the GitOps module under a certain workspace, it prompts that the repository already exists](../amamba/faq/faq-gitops.md#repo-exists-when-adding-it-in-a-certain-workspace)
- Toolchain Related Issues
    - [When the pipeline runs with Maven as the agent and uses integrated SonarQube for Java code scanning, it reports an error](../amamba/faq/faq-toochain.md#error-when-the-pipeline-runs-with-maven-as-the-agent-and-uses-integrated-sonarqube-for-java-code-scanning)
    - [What are the precautions when deploying GitLab](../amamba/faq/faq-toochain.md#what-are-the-precautions-when-deploying-gitlab)

## Container Management

- [Permission issues in container management and global management modules](../kpanda/intro/faq.md#permissions)
- Helm Installation:
    - [Helm application installation fails with “OOMKilled” error](../kpanda/intro/faq.md#oomkilled)
    - [Unable to pull kpanda-shell image when installing application with Helm](../kpanda/intro/faq.md#kpanda-shell)
    - [Helm Chart interface does not display the latest Chart uploaded to Helm Repo](../kpanda/intro/faq.md#no-chart)
    - [When Helm application installation fails, it gets stuck during installation and cannot delete the application to reinstall](../kpanda/intro/faq.md#cannot-remove-app)
- [Workload -> After deleting node affinity and other scheduling policies, scheduling exceptions occur](../kpanda/intro/faq.md#scheduling-exception)
- Application Backup:
    - [What is the logic for Kcoral application backup to detect Velero status in the working cluster](../kpanda/intro/faq.md#kcoral-logic-for-velero)
    - [When backing up and restoring across clusters, how does Kcoral obtain available clusters](../kpanda/intro/faq.md#kcoral-get-cluster)
    - [Kcoral backed up Pods and Deployments with the same label, but after restoring the backup, two Pods appear](../kpanda/intro/faq.md#2pod-with-same-label)
- [Why do the corresponding scaling records still exist after uninstalling VPA, HPA, and CronHPA](../kpanda/intro/faq.md#autoscaling-log)
- [Why does the console open abnormally in lower version clusters](../kpanda/intro/faq.md#console-error)
- Creating and Integrating Clusters:
    - [How to reset a created cluster](#reset-cluster)
    - [Failed to install plugins when integrating the cluster](#failed-plugin)
    - [When creating a cluster, enabling **Kernel tuning for new clusters** in advanced settings fails the cluster creation](../kpanda/intro/faq.md#conntrack)
    - [After the cluster is disconnected, the `kpanda-system` namespace remains in Terminating state](../kpanda/intro/faq.md#ns-terminating)

## MultiCloud Management

- [The kernel for multicloud management is Karmada; what is the currently supported version of Karmada? Can a specific version be specified? Can it be upgraded?](../kairship/intro/faq.md#no1)
- [How to seamlessly migrate single-cluster applications to multicloud management?](../kairship/intro/faq.md#no2)
- [Does multicloud management support cross-cluster application log collection?](../kairship/intro/faq.md#no3)
- [For workloads distributed to multiple clusters in multicloud management, can monitoring information be presented in one view?](../kairship/intro/faq.md#no4)
- [Can multicloud management workloads communicate across clusters?](../kairship/intro/faq.md#no5)
- [Can multicloud management services achieve cross-cluster service discovery?](../kairship/intro/faq.md#no6)
- [Is there production-level support for multicloud management?](../kairship/intro/faq.md#no7)
- [How does multicloud management achieve failover?](../kairship/intro/faq.md#no8)
- [Multi-cluster permission issues](../kairship/intro/faq.md#no9)
- [How to query events from multiple clusters in multicloud management?](../kairship/intro/faq.md#no10)
- [After creating a multicloud application through multicloud management, how can relevant resource information be obtained through container management?](../kairship/intro/faq.md#no11)
- [How to customize the Karmada image source repository address in multicloud management?](../kairship/intro/faq.md#no12)
- [How to connect to multicloud clusters?](../kairship/intro/faq.md#no13)
- [Is it possible to delete only multicloud instances without deleting the components of multicloud management?](../kairship/intro/faq.md#no14)
- [How to achieve network intercommunication among multiple working clusters within a multicloud instance?](../kairship/intro/faq.md#no15)

## Cloud Native Networking

- kube-proxy Issues
    - [IPVS Mode](../network/intro/issues.md#ipvs-mode)
    - [iptables Mode](../network/intro/issues.md#iptables-mode)
    - [externalIPs not working under `externalTrafficPolicy: Local`](../network/intro/issues.md#externalips-does-not-work-under-externaltrafficpolicy-local)
    - [New endpoint rules for Service take a long time to take effect when updating endpoints](../network/intro/issues.md#when-endpoint-in-service-is-updated-the-rules-of-new-endpoint-dont-take-effect-until-much-later)
    - [LoadBalancerSourceRanges not working properly under nftables mode](../network/intro/issues.md#loadbalancersourceranges-does-not-work-properly-in-nftables-mode)
    - [iptables nft and legacy mode selection issues](../network/intro/issues.md#iptables-nft-and-legacy-mode-selection-issue)
- Calico Issues
    - [Offloading VXLAN causes latency](../network/intro/issues.md#offload-vxlan-causes-a-delay-during-access)
    - [VXLAN parent device changed but routing not updated](../network/intro/issues.md#the-parent-device-of-vxlan-is-modified-but-the-route-is-not-updated)
    - [Cluster calico-kube-controllers cache desynchronization causing memory leaks](../network/intro/issues.md#caches-of-cluster-calico-kube-controllers-are-out-of-sync-causing-memory-leaks)
    - [Inter-node pod networking not working in IPIP mode](../network/intro/issues.md#inter-node-networking-is-not-functioning-properly-for-pods-in-the-ipip-mode)
    - [iptables nft and legacy mode selection issues](../network/intro/issues.md#iptables-nft-and-legacy-mode-selection-issue-1)
- Known Issues in Spiderpool v0.9
    - [Error when SpiderCoordinator synchronizes status, but status remains running](../network/intro/issues.md#spidercoordinator-status-running)
    - [`Values.multus.multusCNI.uninstall` setting ineffective, causing multus resources not to be deleted correctly](../network/intro/issues.md#valuesmultusmultuscniuninstall-multus)
    - [Unable to obtain serviceCIDR from kubeControllerManager Pod when kubeadm-config is missing](../network/intro/issues.md#kubeadm-config-kubecontrollermanager-pod-servicecidr)
    - [Upgrading from v0.7.0 to v0.9.0 causes panic due to new TxQueueLen property in SpiderCoordinator CRD](../network/intro/issues.md#v070-v090-spidercoordinator-crd-txqueuelen-panic)
    - [Due to different cluster deployment methods, SpiderCoordinator returns empty serviceCIDR, preventing Pod creation](../network/intro/issues.md#spidercoordinator-has-an-error-synchronizing-status-but-the-status-is-still-running)
- Known Issues in Spiderpool v0.8
    - [ifacer cannot create bond using vlan 0](../network/intro/issues.md#ifacer-cannot-create-bond-using-vlan-0)
    - [Disabling multus functionality still creates multus CR resources](../network/intro/issues.md#the-multus-feature-is-disabled-but-multus-cr-resource-still-is-created)
    - [SpiderCoordinator cannot detect gateway connections in Pod's netns](../network/intro/issues.md#spidercoordinator-fails-to-detect-gateway-connections-in-netns-of-pods)
    - [spiderpool-agent Pod crashes when kubevirt fixed IP feature is turned off](../network/intro/issues.md#the-spiderpool-agent-pod-crashes-when-kubevirt-fixed-ip-feature-is-turned-off)
    - [SpiderIPPool resources do not inherit gateway and route properties from SpiderSubnet](../network/intro/issues.md#spiderippool-resource-does-not-inherit-attributes-of-spidersubnet-such-as-gateway-and-route)
- Known Issues in Spiderpool v0.7
    - [StatefulSet type Pods report IP conflict when obtaining IP allocation after restart](../network/intro/issues.md#ip-conflicts-will-be-notified-when-the-statefulset-type-pod-receives-the-ip-allocation-after-restarting)
    - [Spiderpool cannot recognize certain third-party controllers, causing Pods in StatefulSet to be unable to use fixed IP](../network/intro/issues.md#spiderpool-cannot-recognize-third-party-controllers-preventing-statefulset-pod-from-having-fixed-ip-addresses)
    - [Empty `spidermultusconfig.spec` causes spiderpool-controller Pod to crash](../network/intro/issues.md#empty-spidermultusconfigspec-will-cause-the-spiderpool-controller-pod-to-crash)
    - [Cilium mode obtains incorrect overlayPodCIDR](../network/intro/issues.md#cilium-gets-wrong-overlaypodcidr)
    - [In scenarios with a 1:1 Pod to IP ratio, IPAM allocation blockage occurs, preventing some Pods from running and affecting IP allocation performance](../network/intro/issues.md#in-a-11-pod-to-ip-scenario-ipam-allocation-can-be-blocked-preventing-some-pods-from-running-and-affecting-ip-allocation-performance)
    - [Disabling IP GC feature causes spiderpool-controller component to fail to start correctly due to readiness health check failure](../network/intro/issues.md#after-disabling-the-ip-gc-feature-the-spiderpool-controller-component-will-not-start-correctly-due-to-a-readiness-health-check-failure)
    - [`IPPool.Spec.MultusName` namespace/multusName resolution error causes associated multusName to be unfindable](../network/intro/issues.md#ippoolspecmultusname-specifies-namespacemultusname-but-the-associated-multusname-cannot-be-found-due-to-a-namespace-parsing-error)

## Cloud Native Storage

- [How does HwameiStor scheduler work in Kubernetes platform?](../storage/hwameistor/faqs.md#how-does-the-hwameistor-scheduler-work-in-the-kubernetes-platform)
- [How does HwameiStor handle scheduling for multi-replica workloads? How is it different from traditional general-purpose shared storage?](../storage/hwameistor/faqs.md#how-does-hwameistor-handle-scheduling-for-applications-with-multiple-replicas)
- [How to operate and maintain a data volume on a Kubernetes node?](../storage/hwameistor/faqs.md#how-is-a-volume-on-a-kubernetes-node-maintained)
- [How to handle errors when viewing LocalStorageNode?](../storage/hwameistor/faqs.md#how-to-handle-the-error-when-viewing-localstoragenode)
- [Why is StorageClass not automatically created after installing hwameistor-operator?](../storage/hwameistor/faqs.md#why-were-no-storageclasses-automatically-created-after-installing-hwameistor-operator)

## Virtual Machine

- [API error on the virtual machine page](../virtnest/intro/faq.md#page-api-errors)
- [Virtual machine creation failed](../virtnest/intro/faq.md#vm-creation-failure)
- [Virtual machine created successfully but cannot be used](../virtnest/intro/faq.md#vm-creation-failure)
- [VNC can start but network is inaccessible](../virtnest/intro/faq.md#vnc-can-start-but-network-is-unreachable)

## Insight

- [Clock skew in trace data](../insight/faq/traceclockskew.md)
- [Log collection troubleshooting guide](../insight/best-practice/debug-log.md)
- [Trace collection troubleshooting guide](../insight/best-practice/debug-trace.md)
- [Using Insight to locate application anomalies](../insight/best-practice/find_root_cause.md)
- [What to do when ElasticSearch data is full?](../insight/faq/expand-once-es-full.md)
- [How to configure container log blacklist](../insight/faq/ignore-pod-log-collect.md)

## Microservices Engine

- [x-kubernets-validations error issue with skoala-init](../skoala/troubleshoot/auth-server.md)
- [Nacos version downgrade issue](../skoala/troubleshoot/nacos.md)

## Service Mesh

- [Cannot find the associated cluster when creating a mesh](../mspider/troubleshoot/cannot-find-cluster.md)
- [Mesh creation is stuck in "Creating" and ultimately fails](../mspider/troubleshoot/always-in-creating.md)
- [Created mesh is abnormal but cannot be deleted](../mspider/troubleshoot/failed-to-delete.md)
- [Managed mesh management cluster failed](../mspider/troubleshoot/failed-to-add-cluster.md)
- [Anomalies with istio-ingressgateway when managing mesh management cluster](../mspider/troubleshoot/hosted-mesh-errors.md)
- [Mesh space cannot unbind properly](../mspider/troubleshoot/mesh-space-cannot-unbind.md)
- [Tracking issues to integrate DCE 4.0](../mspider/troubleshoot/dce4.0-issues.md)
- [Sidecar configuration conflicts with workload sidecar](../mspider/troubleshoot/sidecar.md)
- [Multi-cloud interconnect anomalies in managed mesh](../mspider/troubleshoot/cluster-interconnect.md)
- [Sidecar occupies a lot of memory](../mspider/troubleshoot/sidecar-memory-err.md)
- [When creating a mesh, the cluster list contains unknown clusters](../mspider/troubleshoot/cluster-already-exist.md)
- [Managed mesh APIServer certificate expiration handling methods](../mspider/troubleshoot/hosted-apiserver-cert-expiration.md)
- [Common 503 errors in service mesh](../mspider/troubleshoot/503-issue.md)
- [How to allow applications listening on localhost in the cluster to be accessed by other Pods](../mspider/troubleshoot/localhost-by-pod.md)

## Middleware

- MySQL Troubleshooting
    - [MySQL health check](../middleware/mysql/faq/quick-check.md)
    - [MySQL Pod issues](../middleware/mysql/faq/faq-pod.md)
    - [MySQL Operator issues](../middleware/mysql/faq/faq-operator.md)
    - [MySQL master-slave relationship issues](../middleware/mysql/faq/faq-master-slave.md)
    - [MySQL MGR parameter configuration issues](../middleware/mysql/faq/faq-mgr-parameter.md)
    - [MySQL MGR troubleshooting manual](../middleware/mysql/faq/mgr-troubleshooting.md)
    - [Other MySQL failure cases](../middleware/mysql/faq/faq-others.md)
    - [MySQL master-slave mode response to network interruptions](../middleware/mysql/faq/faq-mtsql-net.md)
- Elasticsearch Troubleshooting
    - [Elasticsearch PVC disk capacity full](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch-pvc)
    - [Elasticsearch business index alias is occupied](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch_1)
    - [Error setting GoMAXPROCS for operator](../middleware/elasticsearch/faq/common-question-es.md#error-setting-gomaxprocs-for-operator)
    - [Error terminating due to java.lang.OutOfMemoryError: Java heap space](../middleware/elasticsearch/faq/common-question-es.md#terminating-due-to-javalangoutofmemoryerror-java-heap-space)
    - [Error during Elasticsearch installation in OCP environment: Operation not permitted](../middleware/elasticsearch/faq/common-question-es.md#ocp-elasticsearch-operation-not-permitted)
    - [One node has abnormal disk read throughput and high CPU workload](../middleware/elasticsearch/faq/common-question-es.md#cpu-workload)
    - [Error status:429 when writing data to Elasticsearch](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch-status429)

## AI Lab

- [Cluster not found in AI Lab dropdown list](../baize/troubleshoot/cluster-not-found.md)
- [AI Lab Notebook not controlled by queue quotas](../baize/troubleshoot/notebook-not-controlled-by-quotas.md)
- [AI Lab queue initialization failed](../baize/troubleshoot/local-queue-initialization-failed.md)

## Global Management

- [Why can't istio-ingressgateway start after restarting the cluster (virtual machine)?](../ghippo/troubleshooting/ghippo01.md)
- [Login infinite loop, error 401 or 403](../ghippo/troubleshooting/ghippo02.md)
- [Keycloak cannot start](../ghippo/troubleshooting/ghippo03.md)
- [Upgrade fails when upgrading global management alone](../ghippo/troubleshooting/ghippo04.md)

## Permission Issues

- [Container management permission description](../ghippo/permissions//kpanda.md)
- [Microservices engine permission description](../ghippo/permissions/skoala.md)
- [Application workbench permission description](../ghippo/permissions/amamba.md)
- [Service mesh permission description](../ghippo/permissions/mspider.md)
- [Middleware permission description](../ghippo/permissions/mcamel.md)
- [AI Lab permission description](../ghippo/permissions/baize.md)
