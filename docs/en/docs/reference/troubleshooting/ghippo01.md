# Restart the cluster (virtual machine) istio-ingressgateway cannot start?

The error message is as follows:

![](../images/bug01.png)

Possible cause: The jwtsUri address of the RequestAuthentication CR cannot be accessed,
As a result, istiod cannot deliver configuration to istio-ingressgateway (Istio 1.15 can avoid this bug:
[https://github.com/istio/istio/pull/39341/](https://github.com/istio/istio/pull/39341/files))

Solution:

1. Back up the RequestAuthentication ghippo CR.

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

4. Re-apply RequestAuthentication ghippo CR.

    ```sh
    kubectl apply -f ghippo-ra.yaml
    ```

    !!! note

        Before applying RequestAuthentication ghippo CR, please make sure that ghippo-apiserver and ghippo-keycloak have been started normally.