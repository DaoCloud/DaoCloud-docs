# Create Multicloud Deployment from YAML

You can create multicloud deployments either from an image or a YAML file.

- Image creation involves filling out a form with various configuration options. It is user-friendly and easy-to-perform, but it requires more steps.
- YAML creation involves configuring the necessary information in a YAML file. It requires fewer steps and is more efficient, but it assumes some backend technical knowledge.

This guide explains how to create a multicloud deployment using a YAML file. If you want to learn about the image creation method, refer to [Create Multicloud Deployment from Image](deployment.md).

## Prerequisites

- [Create a Multicloud instance](../instance/add.md)
- Add at least one worker cluster in the multicloud instance. (See [Cluster](../cluster.md#_2) for details)

## Steps

1. Click __Multicloud Workloads__ -> __Deployments__ , and __Create from YAML__ in the top-right corner.

    ![yaml creation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create01.png)

2. Enter or import the YAML file for the Deployment, then click __Next__ .

    > The __Download__ button allows you to download the current YAML file and save it locally for future use.

    ![yaml creation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create02.png)

3. Enter or import the YAML file for the deployment policy, then click __Next__ .

    ![yaml creation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create03.png)

4. Enter or import the YAML file for the override policy, then click __OK__ .

    !!! note

        The override policy is an optional configuration. If you don't need any override configurations, just leave this field empty and click __OK__ .

Then you will be automatically directed to the multicloud deployment list. You can click the __⋮__ icon on the right of the list to edit the YAML, pause, restart, or delete the workload.

![more actions](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-update01.png)

## YAML File Examples

The built-in YAML editor can detect your YAML syntax. If there are any errors, they will be marked with a red squiggly line.

Here are some common YAML file examples that you can modify for your own use.

### Deployment Example

```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-nginx
  labels:
    app: demo-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: demo-nginx
  template:
    metadata:
      labels:
        app: demo-nginx
    spec:
      containers:
      - image: nginx
        name: nginx
```

### Propagation Policy Example

```yaml
# Karmada PropagationPolicy
apiVersion: policy.karmada.io/v1alpha1
kind: PropagationPolicy
metadata:
  name: demo-nginx-pp
  namespace: default    # (1)
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: demo-nginx # (2)
   placement:
    clusterAffinities:
      affinityName: default
      clusterNames:
        - demo-stage
        - demo-dev
```

1. The default namespace is __default__ .
2. If no namespace is specified, the namespace is inherited from the parent object scope.

### Override Policy Example

```yaml
# Karmada OverridePolicy
apiVersion: policy.karmada.io/v1alpha1
kind: OverridePolicy
metadata:
  name: demo-nginx-op
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      name: demo-nginx
  overrideRules:
    - targetCluster:
        clusterNames:
          - demo-dev
      overriders:
        plaintext:
          - path: "/metadata/labels/env"
            operator: add
            value: demo-dev
    - targetCluster:
        clusterNames:
          - demo-stage
      overriders:
        plaintext:
          - path: "/metadata/labels/env"
            operator: add
            value: demo-stage
```
