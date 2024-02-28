# Support for Custom Workload Types

DCE 5.0 provides an enhanced service mesh module that can be deployed in a Kubernetes cluster and automatically manages services within the cluster, enabling features like traffic control, service discovery, traffic monitoring, and fault tolerance.

By default, DCE 5.0 service mesh supports injecting sidecars into Deployment, DaemonSet, and StatefulSet workload types, allowing services to be added to the mesh directly from the workload page.

However, in real production scenarios, there may be special workload types that cannot be governed by the capabilities of traditional service meshes due to cluster distribution versions.

The Istio version provided by DCE 5.0 service mesh has enhanced this capability, allowing users to easily configure governance for special workload types.

## Enabling Custom Workload Capability in the Mesh Control Plane

To add support for corresponding special workload types in the mesh control plane module using the standard `helm upgrade` method, follow these steps:

### Back up Parameters

```shell
# First, back up the existing Helm parameter configuration for the mesh
helm -n mspider-system get values mspider > mspider.yaml
```

### Update Configuration

Edit the backup file __mspider.yaml__ and append the configuration for the custom workload type(s). If there are multiple configurations, you can add them accordingly:

```yaml
global:
  # Example with DeploymentConfig
  # --- add start ---
  custom_workloads:
    - localized_name: 
        en-US: DeploymentConfig
        zh-CN: 自定义工作负载类型 (Custom Workload Type)
      name: deploymentconfigs
      path:
        pod_template: .spec.template
        replicas: .spec.replicas
        status_ready_replicas: .status.availableReplicas
      resource_schema:
        group: apps.openshift.io
        kind: DeploymentConfig
        resource: deploymentconfigs
        version: v1
  # --- add end ---
  debug: true
  # ...
```

Update __mspider__ using Helm:

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

Update the mesh control plane's workload:

```shell
# Run the update command in kpanda-global-cluster
kubectl -n mspider-system rollout restart deployment mspider-api-service mspider-ckube-remote mspider-gsc-controller mspider-ckube mspider-work-api
```

## Adding Custom Workload Types to a Specific Mesh Instance

After enabling the custom workload capability for the mesh's global control plane, you only need to enable the corresponding custom workload type for the specific instance of the mesh control plane.

```shell
# Still performing operations in kpanda-global-cluster
[root@ globalcluster]# kubectl -n mspider-system get globalmesh
NAME      MODE       OWNERCLUSTER            DEPLOYNAMESPACE   PHASE       MESHVERSION
local     EXTERNAL   kpanda-global-cluster   istio-system      SUCCEEDED   1.16.1
test-ce   HOSTED     dsm01                   istio-system      SUCCEEDED   1.17.1-mspider

# Edit the CR configuration for the mesh instance to be enabled
[root@ globalcluster]# kubectl -n mspider-system edit globalmesh test-ce

apiVersion: discovery.mspider.io/v3alpha1
kind: GlobalMesh
metadata:
  finalizers:
  - gsc-controller
  generation: 31
  name: test-ce
  ...
spec:
  clusters:
  - dsm01
  hub: release.daocloud.io/mspider
  mode: HOSTED
  ownerCluster: dsm01
  ownerConfig:
    controlPlaneParams:
      global.high_available: "true"
      global.istio_version: 1.17.1-mspider
      ...
    controlPlaneParamsStruct:
      # --- add start ---
      global:
        custom_workloads:
        - localized_name:
            en-US: DeploymentConfig
            zh-CN: DeploymentConfig
          name: deploymentconfigs
          path:
            pod_template: .spec.template
            replicas: .spec.replicas
            status_ready_replicas: .status.availableReplicas
          resource_schema:
            group: apps.openshift.io
        kind: DeploymentConfig
        resource: deploymentconfigs
        version: v1 # Custom CRD version for workloads
  # --- add end ---
  debug: true
  # ...
```

Updating __mspider__ using Helm:

```shell
# Add repo if it doesn't exist
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

Updating the workload of the mesh control plane:

```shell
# Run update command in kpanda-global-cluster
kubectl -n mspider-system rollout restart deployment mspider-api-service mspider-ckube-remote mspider-gsc-controller mspider-ckube mspider-work-api
```

## Adding custom workload types for a specific mesh instance

Once we have enabled custom workload capabilities for the mesh global control plane, we only need to enable the corresponding custom workload type in the corresponding mesh instance.

```shell
# This is still an operation in the kpanda-global-cluster
[root@ globalcluster]# kubectl -n mspider-system get globalmesh
NAME      MODE       OWNERCLUSTER            DEPLOYNAMESPACE   PHASE       MESHVERSION
local     EXTERNAL   kpanda-global-cluster   istio-system      SUCCEEDED   1.16.1
test-ce   HOSTED     dsm01                   istio-system      SUCCEEDED   1.17.1-mspider

# Edit the CR configuration of the mesh instance to be enabled
[root@ globalcluster]# kubectl -n mspider-system edit globalmesh test-ce

apiVersion: discovery.mspider.io/v3alpha1
kind: GlobalMesh
metadata:
  finalizers:
  - gsc-controller
  generation: 31
  name: test-ce
  ...
spec:
  clusters:
  - dsm01
  hub: release.daocloud.io/mspider
  mode: HOSTED
  ownerCluster: dsm01
  ownerConfig:
    controlPlaneParams:
      global.high_available: "true"
      global.istio_version: 1.17.1-mspider
      ...
    controlPlaneParamsStruct:  # <<< Pay attention to find this line
      # --- add start ---
      global:
        custom_workloads:
        - localized_name:
            en-US: DeploymentConfig
            zh-CN: DeploymentConfig
          name: deploymentconfigs
          path:
            pod_template: .spec.template
            replicas: .spec.replicas
            status_ready_replicas: .status.availableReplicas
          resource_schema:
            group: apps.openshift.io
            kind: DeploymentConfig
            resource: deploymentconfigs
            version: v1
      # --- end ---
      istio:
        custom_params:
          values:
            sidecarInjectorWebhook:
              injectedAnnotations:
                k8s.v1.cni.cncf.io/networks: default/istio-cni
    deployNamespace: istio-system
```

Successful modification of the mesh instance's CR. Note the control plane services in the cluster where the mesh control plane is located.

```shell
# This needs to be done in the cluster where the mesh control plane is located
[root@ meshcontorlcluster]#kubectl -n istio-system rollout restart deployment mspider-mcpc-ckube-remote mspider-mcpc-mcpc-controller mspider-mcpc-reg-proxy test-ce-hosted-apiserver
```

Example Application

In OCP, there is support for a new workload called __DeploymentConfig__ . This example demonstrates how to successfully manage this workload.

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

Create an application named __nginx-deployment-samzong__ using the provided YAML, and then create an associated Service (svc):

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
  - port: 80
    protocol: TCP
    targetPort: 80
```

This is a standard Kubernetes service that is bound to a previously created __DeploymentConfig__ using the label __app: nginx-app-samzong__ .

```bash
kubectl -n NS_NAME apply -f dc-nginx.yaml dc-nginx-svc.yaml
```

### Result

After successfully starting the workload, you can view the workload in the "Sidecar Management" section. By default, it is not injected with sidecar, but you can manually inject it.


In the service list, you can see the corresponding service. At this point, the service's workload is running normally. You can add corresponding policies to provide access to the service.



## Conclusion

Through the above steps, we can see that by simple configuration, we can support custom workload types. This enables support for more types of workloads, allowing users to utilize the DCE 5.0 service mesh more flexibly.
