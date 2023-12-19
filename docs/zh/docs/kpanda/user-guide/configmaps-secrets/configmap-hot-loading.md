# configmap/secret 热加载

configmap/secret 热加载是指将 configmap/secret 作为数据卷挂载在容器中挂载时，当配置发生改变时，容器将自动读取 configmap/secret 更新后的配置，而无需重启 Pod。

## 操作步骤

1. 参考创建工作负载 - [【容器配置】](../workloads/create-deployment.md#容器配置)，配置容器【数据存储】，选择 __Configmap__ 、 __Configmap Key__ 、 __Secret__ 、 __Secret Key__ 作为数据卷挂载至容器。

    ![使用 config 作为数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/user_configmap_to_volume.jpg)

    !!! note

        使用子路径（SubPath）方式挂载的配置文件不支持热加载。

2. 进入【配置与密钥】页面，进入配置项详情页面，在【关联资源】中找到对应的 __container__ 资源，点击 __立即加载__ 按钮，进入配置热加载页面。

    ![使用 config 作为数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading03.png)

    !!! note

        如果您的应用支持自动读取 configmap/secret 更新后的配置，则无需手动执行热加载操作。

3. 在热加载配置弹窗中，输入进入容器内的 __执行命令__ 并点击 __确定__ 按钮，以重载配置。例如，在 nginx 容器中，以 root 用户权限，执行 __nginx -s reload__ 命令来重载配置。

    ![使用 config 作为数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading02.png)

4. 在界面弹出的 web 终端中查看应用重载情况。

    ![使用 config 作为数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/configmap-hot-loading.jpg)


