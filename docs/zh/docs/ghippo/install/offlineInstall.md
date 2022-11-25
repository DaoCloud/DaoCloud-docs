# GHippo 离线安装包使用文档

## 解压 tar 压缩包

```sh
tar zxvf ghippo.bundle.tar
```

解压成功后会得到 ghippo.bundle 文件，其中包含 hints.yaml、images.tar、original-chart 3个子文件。

## 加载镜像文件

```sh
cd ghippo.bundle

docker load -i images.tar
```

## 开始升级

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
