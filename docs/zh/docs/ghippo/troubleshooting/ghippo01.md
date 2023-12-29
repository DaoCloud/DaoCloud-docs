---
hide:
  - toc
---

# 重启集群（虚拟机）istio-ingressgateway 无法启动？

报错提示如下图：

![](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/bug01.png)

可能原因：RequestAuthentication CR 的 jwtsUri 地址无法访问，
导致 istiod 无法下发配置给 istio-ingressgateway（Istio 1.15 可以规避这个 bug：
[https://github.com/istio/istio/pull/39341/](https://github.com/istio/istio/pull/39341/files)）

解决方法：

1. 备份 RequestAuthentication ghippo CR。

    ```shell
    kubectl get RequestAuthentication ghippo -n istio-system -o yaml > ghippo-ra.yaml 
    ```

2. 删除 RequestAuthentication ghippo CR。

    ```shell
    kubectl delete RequestAuthentication ghippo -n istio-system 
    ```

3. 重启 Istio。

    ```shell
    kubectl rollout restart deploy/istiod -n istio-system
    kubectl rollout restart deploy/istio-ingressgateway -n istio-system 
    ```

4. 重新 apply RequestAuthentication ghippo CR。

    ```sh
    kubectl apply -f ghippo-ra.yaml 
    ```

    !!! note

        apply RequestAuthentication ghippo CR 之前，请确保 ghippo-apiserver 和 ghippo-keycloak 已经正常启动。
