---
hide:
  - toc
---

# Manage multi-cloud custom resources

Follow the steps below to create a multi-cloud custom resource (CRD).

1. In the left navigation bar, click `Multi-Cloud Custom Resources` to enter the custom resource page, and click the `YAML Create` button in the upper right corner.

    <!--screenshot-->

2. On the `YAML Creation` page, fill in the YAML statement and click `OK`. Download and import functions are also supported.

    <!--screenshot-->

3. Return to the custom resource list page, and you can view the custom resource named `crontabs.stable.example.com` just created.

    <!--screenshot-->

4. Click the name to enter the custom resource details page, where you can edit the YAML information to update the custom resource.

    <!--screenshot-->

**Custom resource example:**

**CRD example**

```yaml
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

## Create CR instance via YAML

1. Enter the custom resource details, click the `YAML Create` button on the right side of the CR list.

    <!--screenshot-->

2. On the `YAML Creation` page, first fill in the YAML information of the CR, which supports download and import functions.

    <!--screenshot-->

3. Fill in the deployment strategy again to specify which clusters you want to distribute to. Note that the YAML information of the deployment strategy needs to be filled in according to the information of the resources to be propagated:
   The four parameters `apiVersion`, `kind`, `namespace`, and `name` in `resourceSelector` of `spec` need to be consistent with the resources to be propagated.
   If there is no differentiation requirement, the differentiation strategy can be left blank.

    <!--screenshot-->

4. Return to the CR instance list page, and you can view the newly created CR instance named `my-new-cron-obiext`.

    <!--screenshot-->

**CR Example:**

**CR example**

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```