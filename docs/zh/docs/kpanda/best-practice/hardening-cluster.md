# 如何加固自建工作集群

在 DCE 5.0 中，使用 cisbenchmark (CIS) 扫描使用界面创建的工作集群，有一些扫描项并没有通过扫描。
本文将基于不同的 cisbenchmark 版本进行加固说明。

## cisbenchmark 1.27

扫描环境说明：

- kubernetes version: 1.25.4
- containerd: 1.7.0
- kubean version: 0.4.9
- kubespary version: v2.22

#### 未通过扫描项

1. [FAIL] 1.2.5 Ensure that the --kubelet-certificate-authority argument is set as appropriate (Automated)
2. [FAIL] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)
3. [FAIL] 1.4.1 Ensure that the --profiling argument is set to false (Automated)
4. [FAIL] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

#### 扫描失败原因分析

1. [FAIL] 1.2.5 Ensure that the --kubelet-certificate-authority argument is set as appropriate (Automated)

    **原因：**CIS 要求 kube-apiserver 必须指定 kubelet 的 CA 证书路径：

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening01.png)

2. [FAIL] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

    **原因：**CIS 要求 kube-controller-manager 的 --bing-address=127.0.0.1

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening02.png)

3. [FAIL] 1.4.1 Ensure that the --profiling argument is set to false (Automated)

    **原因：** CIS 要求 kube-scheduler 设置 --profiling=false

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening03.png)

4. [FAIL] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

    **原因：** CIS 要求 设置 kube-scheduler 的 --bind-address=127.0.0.1

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening04.png)

#### 加固配置以通过 CIS 扫描

kubespray 官方为了解决这些安全扫描问题，在 v2.22 中添加默认值解决了一部分问题，
更多细节请参考 [kubespray 加固文档](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/hardening.md)。

- 通过修改 kubean var-config 配置文件来添加参数：

    ```yaml
    kubernetes_audit: true
    kube_controller_manager_bind_address: 127.0.0.1
    kube_scheduler_bind_address: 127.0.0.1
    kube_kubeadm_scheduler_extra_args:
      profiling: false
    kubelet_rotate_server_certificates: true
    ```

- 在 DCE 5.0 中，也提供了通过 UI 来配置高级参数的功能，在创建集群最后一步添加自定义参数：

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening05.png)

- 设置自定义参数后，在 kubean 的 var-config 的 configmap 中添加了如下参数：

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening06.png)

- 安装集群后进行扫描：

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening07.png)

扫描后所有的扫描项都通过了扫描（WARN 和 INFO 计算为 PASS），
由于 cibenchmark 会不断更新，此文档的内容只适用于 cibenchmark 1.27。
