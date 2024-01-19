---
MTPE: FanLin
Date: 2024-01-04
---

# Manage Multicloud CRDs

You can follow the steps below to create a custom resource definition (CRD) for multicloud.

1. Click __Multicloud CRDs__ in the left navigation bar to access the custom resource page. Then, click the __Create from YAML__ button located in the upper right corner.

    ![Create CRD](../images/crd01.png)

2. Navigate to the __Create from YAML__ page, input the YAML statement, and click __OK__. You also have the option to download and import features.

    ![Create from yaml](../images/crd02.png)

3. After creating the custom resource named `crontabs.stable.example.com`, you can return to the custom resource list page to view it.

    ![Successfully Created](../images/crd03.png)

4. You can click the name to access the custom resource details page, where the YAML information can be edited to update the custom resource.

    ![CRD Details](../images/crd04.png)

**CRD Example:**

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

1. Access the custom resource details and click the __Create from YAML__ button located on the right side of the CR instance.

    ![Create CR](../images/crd05.png)

2. Navigate to the __Create from YAML__ page and begin by filling in the YAML information of the CR. This page also supports download and import features. Note that the propagation policy and override policy are optional.

    ![Create from yaml](../images/crd06.png)

3. After creating the CR instance named __my-new-cron-obiext__, return to the CR instance list page where you can view it.

    ![Successfully Created](../images/crd07.png)

**CR Example:**

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```
