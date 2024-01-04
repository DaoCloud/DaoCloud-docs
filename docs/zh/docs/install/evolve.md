# 标准版升级到白金版

DCE 5.0 支持多种版本，除社区版以外的其他版本均为商业版，本文演示如何从标准版升级到白金版。

![模块图](https://docs.daocloud.io/daocloud-docs-images/docs/images/dce-modules04.png)

## 前提条件

- 您需要有一个 DCE 5.0 的集群环境，参阅[离线化部署商业版](commercial/start-install.md)
- 请确保您的火种机器还存活，并且当前环境对应的离线包还在，否则需要重新下载。

## 操作步骤

### 第 1 步：配置 manifest.yaml 文件

将 manifest.yaml 文件中所有 `enable: false` 改为 `enable: true`。

```yaml
skoala:
   enable: false
   helmVersion: 0.26.1
   variables:
 mspider:
   enable: false
   helmVersion: v0.18.0-rc2
   variables:
 mcamel-rabbitmq:
   enable: false
   helmVersion: 0.12.2
   variables:
 mcamel-elasticsearch:
   enable: false
   helmVersion: 0.9.2
   variables:
 ...
 mcamel-mysql:
   enable: false
   helmVersion: 0.10.2
   variables:
 mcamel-redis:
   enable: false
   helmVersion: 0.10.0-rc2
   variables:
 mcamel-kafka:
   enable: false
   helmVersion: 0.7.2
   variables:
 mcamel-minio:
   enable: false
   helmVersion: 0.7.2
   variables:
 mcamel-postgresql:
   enable: false
   helmVersion: 0.4.0-rc2
   variables:
 mcamel-mongodb:
   enable: false
   helmVersion: 0.2.0-rc2
   variables:
```

### 第 2 步：执行命令

执行升级命令

```bash
./offline/dce5-installer cluster-create -c ./sample/clusterConfig.yaml -m ./sample/manifest.yaml -j 11,12
```

!!! note

    clusterConfig.yaml 文件需要与安装时使用的参数保持一致。

    -j 11,12 是目前执行标准版升级到白金版的必须参数。

### 第 3 步：安装成功提示

![upgrade](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/commercial/images/succeed01.png)
