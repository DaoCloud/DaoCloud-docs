---
hide:
  - toc
---

# 管理多云自定义资源

参照以下步骤创建一个多云自定义资源（CRD）。

1. 在左侧导航栏中，点击 __多云自定义资源__ ，进入自定义资源页面，点击右上角的 __YAML 创建__ 按钮。

    ![创建crd](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd01.png)

2. 在 __YAML 创建__ 页面中，填写 YAML 语句后，点击 __确定__ 。还支持下载和导入功能。

    ![yaml创建](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd02.png)

3. 返回自定义资源列表页，即可查看刚刚创建的名为 `crontabs.stable.example.com` 的自定义资源。

    ![crd创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd03.png)

4. 点击名称，进入自定义资源详情页面，在此页面内可以编辑 YAML 信息来更新自定义资源。

    ![crd详情](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd04.png)

**自定义资源示例：**

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

## 通过 YAML 创建 CR 实例

1. 进入自定义资源详情，点击 CR 列表右侧的 __YAML 创建__ 按钮。

    ![创建cr](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd05.png)

2. 在 __YAML 创建__ 页面中，先填写 CR 的 YAML 信息，支持下载和导入功能。

    ![yaml创建cr](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd06.png)

3. 再填写部署策略，用来指定想要分发在哪些集群。注意需要将部署策略的 YAML 信息根据需要传播的资源的信息进行填写：
   __spec__ 的 __resourceSelector__ 中 __apiVersion__ 、 __kind__ 、 __namespace__ 、 __name__ 四个参数需要和所需要传播的资源保持一致。
   若没有差异化需求，差异化策略可不填。

    ![必填pp](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd07.png)

4. 返回 CR 实例列表页，即可查看刚刚创建的名为 __my-new-cron-obiext__ 的 CR 实例。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/crd08.png)

**CR 示例：**

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
