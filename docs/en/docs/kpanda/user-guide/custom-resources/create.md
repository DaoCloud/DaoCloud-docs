# CustomResourceDefinition (CRD)

In Kubernetes, all objects are abstracted as resources, such as Pod, Deployment, Service, Volume, etc. are the default resources provided by Kubernetes.
This provides important support for our daily operation and maintenance and management work, but in some special cases, the existing preset resources cannot meet the needs of the business.
Therefore, we hope to expand the capabilities of the Kubernetes API, and CustomResourceDefinition (CRD) was born based on this requirement.

The container management module supports interface-based management of custom resources, and its main features are as follows:

- Obtain the list and detailed information of custom resources under the cluster
- Create custom resources based on YAML
- Create a custom resource example CR (Custom Resource) based on YAML
- Delete custom resources

## Prerequisites

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created Kubernetes](../clusters/create-cluster.md), and you can access the cluster UI interface.

- Created a [namespace](../namespaces/createns.md),
  [user](../../../ghippo/user-guide/access-control/user.md),
  and authorized the user as [`Cluster Admin`](../permissions/permission-brief.md#cluster-admin)
  For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

## Create CRD via YAML

1. Click a cluster name to enter __Cluster Details__ .

    

2. In the left navigation bar, click __Custom Resource__ , and click the __YAML Create__ button in the upper right corner.

    

3. On the __Create with YAML__ page, fill in the YAML statement and click __OK__ .

    

4. Return to the custom resource list page, and you can view the custom resource named `crontabs.stable.example.com` just created.

    

**Custom resource example:**

```yaml title="CRD example"
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

## Create a custom resource example via YAML

1. Click a cluster name to enter __Cluster Details__ .

    

2. In the left navigation bar, click __Custom Resource__ , and click the __YAML Create__ button in the upper right corner.

    

3. Click the custom resource named `crontabs.stable.example.com` , enter the details, and click the __YAML Create__ button in the upper right corner.

    

4. On the __Create with YAML__ page, fill in the YAML statement and click __OK__ .

    

5. Return to the details page of `crontabs.stable.example.com` , and you can view the custom resource named __my-new-cron-object__ just created.

**CR Example:**

```yaml title="CR example"
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
  namespace: dev
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```
