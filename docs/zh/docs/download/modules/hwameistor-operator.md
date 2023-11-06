# hwameistor-operator

本页可下载hwameistor-operator的离线安装包。

## 下载

| 版本  | 架构 | 文件大小 | 安装包      | 校验文件 | 更新日期   |
| ----------- | ----- |-------- | ---------- | ---------- | ---------- |
| [v0.13.1] | AMD 64 | 1.62GB | [:arrow_down: hwameistor-operator_v0.13.1_amd64.tar](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64.tar) | [:arrow_down: hwameistor-operator_v0.13.1_amd64_checksum.sha512sum](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/hwameistor-operator_v0.13.1_amd64_checksum.sha512sum) | 2023-11-06 |

## 校验

在下载离线安装包和校验文件的目录，以 `v0.13.1_amd64` 为例，执行以下命令校验完整性：

```sh
echo "$(cat hwameistor-operator_v0.13.1_amd64_checksum.sha512sum)" | sha512sum -c
```

校验成功后打印结果类似于：

```none
hwameistor-operator_v0.13.1_amd64.tar: ok
```
