# 对接导航栏

以容器管理（开发代号 `kpanda`）为例，对接到导航栏。

对接后的预期效果如图：

[对接效果](../images/gproduct01.png)

## 对接方法

通过 GProductNavigator CR 将容器管理的各功能项注册到导航栏菜单。

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GProductNavigator
metadata:
  name: kpanda
spec:
  gproduct: kpanda
  name: 容器管理
  localizedName:
    zh-CN: 容器管理
    en-US: Container Management
  url: /kpanda
  category: 容器   # 当前只支持概览、工作台、容器、微服务、中间件、管理，六选一
  iconUrl: /kpanda/nav-icon.png
  order: 10 # 数字越大排在越上面
  menus:
  - name: 备份管理
    localizedName:
      zh-CN: 备份管理
      en-US: Backup Management
    iconUrl: /kpanda/bkup-icon.png
    url: /kpanda/backup
```

全局管理的导航栏 `category` 配置在 ConfigMap，暂时不能以注册方式增加，需要联系全局管理团队来添加。

## 临时增加导航 `category`（仅供参考）

若想在某个环境下临时增加 `category`，可采用以下方法。

以 DOP 在 demo-dev.daocloud.io 站点对接为例。

1. 进入 demo-dev 集群。

    ```shell
    ssh root@10.6.229.191 / dangerous
    ```

2. 备份全局管理上一次安装的参数。

    ```shell
    helm get values ghippo -n ghippo-system > ghippo-values.yaml
    ```

3. 编辑 `ghippo-values.yaml` 文件，为 DOP 添加左侧菜单。

    ```yaml
    apiserver:
    ...
    navigatorCategories:
        - name: Example
        localizedName:
            zhCN: example_zh-CN
            enUS: example_en-US
    ```

4. 确认当前部署的全局管理版本。例如当前版本为 0.10.6-dev-3-7-g25505d99（注意，helm 版本不带 v）。

    ```shell
    $ helm list -n ghippo-system
    NAME    NAMESPACE       REVISION    UPDATED                                 STATUS      CHART                           APP VERSION
    ghippo  ghippo-system   2           2022-10-13 16:37:32.100921894 +0800 CST deployed    ghippo-0.10.6-dev-3-7-g25505d99 v0.10.6-dev-3-7-g25505d99
    ```

5. 更新全局管理的配置文件，使 DOP 左侧菜单的配置生效（注意替换全局管理的版本号）。

    ```shell
    helm upgrade ghippo -n ghippo-system ghippo-release/ghippo -f ./ghippo-values.yaml --version 0.10.6-dev-3-7-g25505d99
    ```

6. 重启 ghippo-apiserver，使配置文件生效，成功添加了 `category`。

    ```shell
    kubectl rollout restart deploy/ghippo-apiserver -n ghippo-system
    ```
