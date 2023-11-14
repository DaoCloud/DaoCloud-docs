# How to Harden a Self-built Work Cluster

In DCE 5.0, when using the CIS Benchmark (CIS) scan on a work cluster created using the user interface, some scan items did not pass the scan. This article provides hardening instructions based on different versions of CIS Benchmark.

## CIS Benchmark 1.27

Scan Environment:

- Kubernetes version: 1.25.4
- Containerd: 1.7.0
- Kubean version: 0.4.9
- Kubespray version: v2.22

#### Failed Scan Items

1. [FAIL] 1.2.5 Ensure that the --kubelet-certificate-authority argument is set as appropriate (Automated)
2. [FAIL] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)
3. [FAIL] 1.4.1 Ensure that the --profiling argument is set to false (Automated)
4. [FAIL] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

#### Analysis of Scan Failures

1. [FAIL] 1.2.5 Ensure that the --kubelet-certificate-authority argument is set as appropriate (Automated)

    **Reason:** CIS requires that kube-apiserver must specify the CA certificate path for kubelet:

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening01.png)

2. [FAIL] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

    **Reason:** CIS requires that kube-controller-manager's --bind-address=127.0.0.1

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening02.png)

3. [FAIL] 1.4.1 Ensure that the --profiling argument is set to false (Automated)

    **Reason:** CIS requires that kube-scheduler sets --profiling=false

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening03.png)

4. [FAIL] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 (Automated)

    **Reason:** CIS requires setting kube-scheduler's --bind-address=127.0.0.1

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening04.png)

#### Hardening Configuration to Pass CIS Scan

To address these security scan issues, kubespray has added default values in version v2.22 to solve some of the problems. For more details, please refer to the [kubespray hardening documentation](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/hardening.md).

- Add parameters by modifying the kubean var-config configuration file:

    ```yaml
    kubernetes_audit: true
    kube_controller_manager_bind_address: 127.0.0.1
    kube_scheduler_bind_address: 127.0.0.1
    kube_kubeadm_scheduler_extra_args:
      profiling: false
    kubelet_rotate_server_certificates: true
    ```

- In DCE 5.0, there is also a feature to configure advanced parameters through the user interface. Add custom parameters in the last step of cluster creation:

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening05.png)

- After setting the custom parameters, the following parameters are added to the var-config configmap in kubean:

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening06.png)

- Perform a scan after installing the cluster:

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/hardening07.png)

After the scan, all scan items passed the scan (WARN and INFO are counted as PASS).
Note that this document only applies to CIS Benchmark 1.27, as CIS Benchmark is continuously updated.
