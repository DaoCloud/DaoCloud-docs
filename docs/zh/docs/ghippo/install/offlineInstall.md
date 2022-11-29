# GHippo 离线安装包使用文档

## 加载镜像文件
解压 tar 压缩包
```sh
tar zxvf ghippo.bundle.tar
```

解压成功后会得到 ghippo.bundle 文件，其中包含 hints.yaml、images.tar、original-chart 3个子文件。

### 通过chart-syncer同步镜像到指定镜像仓库

- 首先请确认本地是否安装chart-syncer，如果已安装，则跳过当前安装步骤

```shell
tmp_dir=$(mktemp -d)

git clone https://github.com/DaoCloud/charts-syncer.git ${tmp_dir}

cp ${tmp_dir}/charts-syncer /usr/local/bin/charts-syncer

chmod +x /usr/local/bin/charts-syncer

rm -rf ${tmp_dir}
```

- 创建load-image.yaml，完整yaml参考：
https://github.com/DaoCloud/charts-syncer/blob/master/examples/test-load-dao-2048.yaml
⚠️下面参数均为必填，且需要私有harbor修改相关配置
```
source:
  intermediateBundlesPath: dist/offline # the relative path where your do charts-syncer,but not relative path between this yaml and offline-package
target:
  containerRegistry: 10.64.0.156 # need change to your harbor url
  repo:
    kind: HARBOR # or as any other supported Helm Chart repository kinds
    url: http://10.64.0.156/chartrepo/ghippo # need change to your harbor url
    auth:
      username: "admin" # the harbor username
      password: "Harbor12345" # the harbor password
  containers:
    auth:
      username: "admin" # the harbor username
      password: "Harbor12345" # the harbor password
```


- 执行同步镜像命令
```shell
charts-syncer sync --config load-image.yaml
```

### 本地加载镜像到docker

```sh
cd ghippo.bundle

docker load -i images.tar
```

## 开始升级

### 通过harbor升级ghippo

- 配置 ghippo helm 仓库

```shell
heml repo add ghippo https://{harbor url}/chartrepo/ghippo

helm repo update ghippo # helm版本过低会导致失败，若失败，请尝试执行helm update repo
```

- 选择您想安装的 ghippo 版本（🔥建议安装最新版本）

```shell
helm search repo ghippo/ghippo --versions
```

```
[root@master ~]# helm search repo ghippo/ghippo --versions
NAME                   CHART VERSION  APP VERSION  DESCRIPTION
ghippo/ghippo  0.9.0          v0.9.0       A Helm chart for GHippo
...
```

- 备份 --set 参数

在升级 ghippo 版本之前，我们建议您执行如下命令，备份上一个版本的 --set 参数。

```shell
helm get values ghippo -n ghippo-system -o yaml > bak.yaml
```

- 执行 helm upgrade

```
helm upgrade ghippo ghippo/ghippo \
-n ghippo-system \
-f ./bak.yaml \
--version 0.9.0
```

### 通过docker升级ghippo
- 备份 --set 参数

在升级 ghippo 版本之前，我们建议您执行如下命令，备份上一个版本的 --set 参数。

```shell
helm get values ghippo -n ghippo-system -o yaml > bak.yaml
```

- 执行 helm upgrade

```shell
cd original-chart

helm upgrade ghippo . \
-n ghippo-system \
-f ./bak.yaml
```
