# Support for Custom Workload Types

DCE 5.0 provides an enhanced service mesh module that can be deployed in Kubernetes clusters
and automatically manages services within the cluster. It enables features such as traffic control,
service discovery, traffic monitoring, and fault tolerance.

The DCE 5.0 service mesh supports injecting sidecars into Deployment, DaemonSet, and StatefulSet
workload types by default. Users can directly perform sidecar injection actions on the workload
page to include services in the mesh.

However, in actual production scenarios, there may be special workload types due to issues with
cluster distribution versions. Traditional service mesh capabilities cannot support governance
for such special workload types.

The Istio version provided by the DCE 5.0 service mesh has enhanced this capability.
Users can easily configure governance for special workload types.

## Enabling Specific Workloads

The standard approach is to upgrade the mesh module using `helm upgrade` to add support
for specific workload types.

### Backup Parameters

```shell
# First, back up the existing Helm parameter configuration for the mesh
helm -n mspider-system get values mspider > mspider.yaml
```

### Update Configuration

Edit the configuration file and append the configuration for the custom workload type.
If there are multiple configuration types, you can add them accordingly:

```yaml
global:
  # Use DeploymentConfig as an example
  # --- add start ---
  custom_workloads:
    - localized_name: # The name must be written in both English and Chinese
        en-US: DeploymentConfig
        zh-CN: 自定义工作负载类型
      name: deploymentconfigs
      path:
        pod_template: .spec.template # Define the workload Pod content
        replicas: .spec.replicas # Define the number of workload replicas
        status_ready_replicas: .status.availableReplicas # Define the healthy replicas count
      resource_schema:
        group: apps.openshift.io # The API group of the custom workload CRD
        kind: DeploymentConfig
        resource: deploymentconfigs
        version: v1 # The version of the custom workload CRD
  # --- add end ---
  debug: true
  # ...
```

Use Helm to update `mspider`:

```shell
# Add the repo if it doesn't exist
helm repo add mspider https://release.daocloud.io/chartrepo/mspider
helm repo update mspider

# Perform the update
export VERSION=$(helm list -n mspider-system | grep "mspider" | awk '{print $NF}')
helm upgrade --install --create-namespace \
-n mspider-system mspider mspider/mspider \
--cleanup-on-fail \
--version=$VERSION \
--set global.imageRegistry=release.daocloud.io/mspider \
-f mspider.yaml
```

## Example Application

In OpenShift Container Platform (OCP), a new workload type called `DeploymentConfig`
is supported. This example demonstrates how to successfully manage this workload.

### DeploymentConfig

```yaml
# filename dc-nginx.yaml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: nginx-deployment-samzong
spec:
  replicas: 1
  selector:
    app: nginx-app-samzong
  template:
    metadata:
      labels:
        app: nginx-app-samzong
    spec:
      containers:
        - image: nginx:latest
          imagePullPolicy: Always
          name: nginx-samzong
          ports:
            - containerPort: 80
              protocol: TCP
```

Create an application named `nginx-deployment-samzong` using the above YAML,
and then create the associated service:

```yaml
# filename dc-nginx-svc.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: nginx-app-samzong
  ports:
    port: 80
    protocol: TCP
    targetPort: 80
```

This is a standard Kubernetes service, and we bind it to the pre-existing `DeploymentConfig`
using `app: nginx-app-samzong`.

```bash
kubectl -n NS_NAME apply -f dc-nginx.yaml dc-nginx-svc.yaml
```

### Effect

After the workload is successfully started, you can view it in the `Mesh Sidecar` section.
By default, it is not injected and can be manually injected.

![image](../images/custom-workloads-01.png)

In the service list, you can see the corresponding service. At this point, the service's workload
is also running normally, and you can add corresponding policies to enable access to the service.

![image](../images/custom-workloads-02.png)

## Conclusion

Through the above steps, you can see that by simple configuration, it is possible to support
custom workload types. This enables support for a wider range of workload types, allowing users
to use the DCE 5.0 service mesh more flexibly.
