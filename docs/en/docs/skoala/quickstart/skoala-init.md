# Microservice Engine Cluster Init Components

Deployment structure of the microservice engine cluster init components:

![image](../images/skoala-init-cn.png)

The chart inside the blue box, namely the `skoala-init` component, needs to be installed in the working cluster. After installing the `skoala-init` component, you can use various features of the microservice engine, such as creating a registry center, gateway instances, etc. Additionally, please note that the `skoala-init` component depends on the `insight-agent` component of the DCE 5.0 observability module to provide metric monitoring and distributed tracing functionalities. If you need to use these features, you need to install the `insight-agent` component beforehand. For specific steps, refer to [Install the insight-agent component](../../insight/quickstart/install/install-agent.md).

!!! note

    - If the `insight-agent` is not installed before installing `skoala-init`, the `service-monitor` will not be installed.
    - If you need to install `service-monitor`, please install `insight-agent` first, and then install `skoala-init`.

## Online Installation

`skoala-init` is the Operator for all components of the microservice engine:

- Only needs to be installed in the working cluster
- Includes components such as skoala-agent, nacos-operator, sentinel-operator, seata-operator, contour-provisioner, gateway-api-adminssion-server
- When not installed, creating a registry center and gateway will prompt for missing components

Since Skoala involves multiple components, we package these components into a single Chart, which is the `skoala-init`. Therefore, you should install `skoala-init` in the working cluster where you use the microservice engine. This installation command can also be used to update the component.

Configure the Skoala repository to view and obtain the application chart for `skoala-init`.

```bash
helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
helm repo update
```

```bash
$ helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init	0.28.1       	0.28.1     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.28.0       	0.28.0     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.2       	0.27.2     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.1       	0.27.1     	A Helm Chart for Skoala init, it includes Skoal...
......
```

Run the following command. Note that you shall change the version to a proper nubmer.

```bash
helm upgrade --install skoala-init --create-namespace -n skoala-system --cleanup-on-fail \
    skoala-release/skoala-init \
    --version 0.28.1
```

Check if Pod is started successfully:

```bash
$ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
contour-provisioner-54b55958b7-5ltng                  1/1     Running     0          2d6h
gateway-api-admission-patch-bk7c8                     0/1     Completed   0          2d6h
gateway-api-admission-pwhdh                           0/1     Completed   0          2d6h
gateway-api-admission-server-77545d74c4-v6fpr         1/1     Running     0          2d6h
nacos-operator-6d94bdccc8-wx4w5                       1/1     Running     0          2d6h
seata-operator-f556d989d-8qrf8                        1/1     Running     0          2d6h
sentinel-operator-6fb9dc98f4-d44k5                    1/1     Running     0          2d6h
skoala-agent-54d4df7897-7p4pz                         1/1     Running     0          2d6h
```

## Online Upgrade

Since the `skoala-init` component is installed in the working cluster, you need to perform the following steps in each working cluster. <!--If an upgrade is required, it will be emphasized in the release notes.-->

1. Backup the original parameters.

    ```bash
    helm -n skoala-system get values skoala-init > skoala-init.yaml
    ```

2. Add the Helm repository for the microservice engine.

    ```bash
    helm repo add skoala https://release.daocloud.io/chartrepo/skoala
    ```

3. Update the Helm repository for the microservice engine.

    ```bash
    helm repo update
    ```

4. Delete the `gateway-api-admission` and `gateway-api-admission-patch` jobs.

    ```bash
    kubectl -n skoala-system delete jobs gateway-api-admission gateway-api-admission-patch
    ```

5. Run the `helm upgrade` command.

    ```bash
    helm --kubeconfig /tmp/deploy-kube-config upgrade --install --create-namespace -n skoala-system skoala-init skoala/skoala-init --version=0.28.1 --set nacos-operator.image.tag=v0.28.1 --set skoala-agent.image.tag=v0.28.1 --set sentinel-operator.image.tag=v0.28.1 --set seata-operator.image.tag=v0.28.1 -f skoala-init.yaml
    ```

    !!! note

        Adjust the values of the `version`, `nacos-operator.image.tag`, `skoala-agent.image.tag`, `sentinel-operator.image.tag`, and `seata-operator.image.tag` parameters to the version number of the microservice engine you want to upgrade to.

6. Manually update the CRD files that need to be upgraded based on your needs.

    ```bash
    # projectcontour crd
    kubectl apply -f skoala-init/charts/contour-provisioner/crds/contour.yaml
    # gateway-api crd
    kubectl apply -f skoala-init/charts/contour-provisioner-prereq/crds/gateway-api.yaml
    ```

## Offline Upgrade

Refer to the offline upgrade method for the microservice engine management components in
[Offline Upgrade](./skoala.md#offline-upgrade).

## Uninstalling the Microservice Engine Cluster Init Component

```bash
helm uninstall skoala-init -n skoala-system
```
