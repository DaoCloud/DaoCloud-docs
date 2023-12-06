---
hide:
  - toc
---


# 导入离线 MinIo Operator

本文将介绍在离线环境下如何导入 MinIo Operator。

## 前提条件

- 当前集群已接入容器管理且 Global 集群已经安装 `kolm` 组件（helm 模板搜索 kolm）
- 当前集群已经安装 `olm` 组件且版本 >= 0.2.4 (helm 模板搜索 olm)
- 支持执行 Docker 命令
- 准备一个镜像仓库

## 操作步骤

1. 在执行环境中设置环境变量并在后续步骤使用，执行命令：

    ```bash
    export OPM_IMG=10.5.14.200/quay.m.daocloud.io/operator-framework/opm:v1.29.0 
    export BUNDLE_IMG=10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3 
    ```

    如何获取上述镜像地址：

    前往`容器管理` -> 选择当前集群 -> `helm 应用` -> 查看 `olm` 组件 -> `插件设置`，找到后续步骤所需 opm，minio，minio bundle，minio operator 的镜像。

    ![olm](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/olm.png)

    ```bash
    以上诉截图为例，则四个镜像地址如下

    # opm 镜像 
    10.5.14.200/quay.m.daocloud.io/operator-framework/opm:v1.29.0

    # minio 镜像
    10.5.14.200/quay.m.daocloud.io/minio/minio:RELEASE.2023-03-24T21-41-23Z

    # minio bundle 镜像
    10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3

    # minio operator 镜像 
    10.5.14.200/quay.m.daocloud.io/minio/operator:v5.0.3
    ```

2. 执行 opm 命令获取离线 bundle 镜像包含的 operator。

    ```bash
    # 创建 operator 存放目录
    $ mkdir minio-operator && cd minio-operator 

    # 获取 operator yaml 
    $ docker run --user root  -v $PWD/minio-operator:/minio-operator ${OPM_IMG} alpha bundle unpack --skip-tls-verify -v -d ${BUNDLE_IMG} -o ./minio-operator

    # 预期结果
    .
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    3 directories, 9 files
    ```

3. 替换  minio-operator/manifests/minio-operator.clusterserviceversion.yaml  文件中的所有镜像地址为离线镜像仓库地址镜像。

    替换前：

    ![image1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/csv1.png)

    替换后：

    ![image2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/csv2.png)

4. 生成构建 bundle 镜像的 Dockerfile

    ```bash
    $ docker run --user root  -v $PWD:/minio-operator -w /minio-operator ${OPM_IMG} alpha bundle generate --channels stable,beta -d /minio-operator/minio-operator/manifests -e stable -p minio-operator  

    # 预期结果
    .
    ├── bundle.Dockerfile
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    3 directories, 10 files
    ```

5. 执行构建命令，构建 bundle 镜像且推送到离线 registry。

    ```bash
    # 设置新的 bundle image 
    export OFFLINE_BUNDLE_IMG=10.5.14.200/quay.m.daocloud.io/operatorhubio/minio-operator:v5.0.3-offline 

    $ docker build . -f bundle.Dockerfile -t ${OFFLINE_BUNDLE_IMG}  

    $ docker push ${OFFLINE_BUNDLE_IMG}
    ```

6. 生成构建 catalog 镜像的 Dockerfile。

    ```bash
    $ docker run --user root  -v $PWD:/minio-operator  -w /minio-operator ${OPM_IMG} index add  --bundles ${OFFLINE_BUNDLE_IMG} --generate --binary-image ${OPM_IMG} --skip-tls-verify

    # 预期结果
    .
    ├── bundle.Dockerfile
    ├── database
    │   └── index.db
    ├── index.Dockerfile
    └── minio-operator
        ├── manifests
        │   ├── console-env_v1_configmap.yaml
        │   ├── console-sa-secret_v1_secret.yaml
        │   ├── console_v1_service.yaml
        │   ├── minio.min.io_tenants.yaml
        │   ├── minio-operator.clusterserviceversion.yaml
        │   ├── operator_v1_service.yaml
        │   ├── sts.min.io_policybindings.yaml
        │   └── sts_v1_service.yaml
        └── metadata
            └── annotations.yaml

    4 directories, 12 files
    ```

7. 构建 catalog 镜像

    ```bash
    # 设置新的 catalog image  
    export OFFLINE_CATALOG_IMG=10.5.14.200/release.daocloud.io/operator-framework/system-operator-index:v0.1.0-offline

    $ docker build . -f index.Dockerfile -t ${OFFLINE_CATALOG_IMG}  

    $ docker push ${OFFLINE_CATALOG_IMG}
    ```

8. 前往容器管理，更新 helm 应用 olm 的内置 catsrc 镜像（填写构建 catalog 镜像指定的 ${catalog-image} 即可）

    ![olm1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/olm1.png)

    ![olm2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/olm2.png)

9. 更新成功后，Operator Hub 中会出现 `minio-operator` 组件

    ![olm3](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/olm3.png)
