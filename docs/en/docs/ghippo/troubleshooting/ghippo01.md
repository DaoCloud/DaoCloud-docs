---
hide:
  - toc
---

# Unable to start istio-ingressgateway when restarting the cluster (virtual machine)?

The error message is as shown in the following image:

![](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/bug01.png)

Possible cause: The jwtsUri address of the RequestAuthentication CR cannot be accessed, causing istiod to be unable to push the configuration to istio-ingressgateway (This bug can be avoided in Istio 1.15: [https://github.com/istio/istio/pull/39341/](https://github.com/istio/istio/pull/39341/files)).

Solution:

1. Backup the RequestAuthentication ghippo CR.

    ```shell
    kubectl get RequestAuthentication ghippo -n istio-system -o yaml > ghippo-ra.yaml
    ```

2. Delete the RequestAuthentication ghippo CR.

    ```shell
    kubectl delete RequestAuthentication ghippo -n istio-system
    ```

3. Restart Istio.

    ```shell
    kubectl rollout restart deploy/istiod -n istio-system
    kubectl rollout restart deploy/istio-ingressgateway -n istio-system
    ```

4. Reapply the RequestAuthentication ghippo CR.

    ```sh
    kubectl apply -f ghippo-ra.yaml
    ```

    !!! note

        Before applying the RequestAuthentication ghippo CR, make sure that ghippo-apiserver and ghippo-keycloak are started correctly.
