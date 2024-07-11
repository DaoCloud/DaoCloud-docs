# 启用昇腾虚拟化

昇腾虚拟化分为动态虚拟化和静态虚拟化，本文介绍如何开启并使用昇腾静态虚拟化能力。

## 前提条件

- 昇腾相关固件与驱动安装成功
- Kubernetes 集群环境搭建
- ascend-docker-runtime 已安装
- ascend-mindxdl 组件已安装

请参考[昇腾 NPU 组件安装文档](./ascend_driver_install.md)安装基础环境。

## 开启虚拟化能力

开启虚拟化能力需要手动修改 ascend-device-plugin-daemonset 组件的启动参数，参考下述命令：

```init
- device-plugin -useAscendDocker=true -volcanoType=true -presetVirtualDevice=false
- logFile=/var/log/mindx-dl/devicePlugin/devicePlugin.log -logLevel=0
```

### 切分 VNPU 实例

静态虚拟化需要手动对 VNPU 实例的切分，请参考下述命令：

``` bash
npu-smi set -t create-vnpu -i 13 -c 0 -f vir02
```

- `i` 指的是 card id
- `c` 指的是 chip id
- `vir02` 指的是切分规格模板

关于 card id 和 chip id，可以通过 npu-smi info 查询，切分规格可通过
[ascend 官方模板](https://www.hiascend.com/document/detail/zh/mindx-dl/500/AVI/cpaug/cpaug_006.html)进行查询。

切分实例过后可通过下述命令查询切分结果：

```bash
npu-smi info -t info-vnpu -i 13 -c 0
```

查询结果如下：

![vnpu1](../images/vnpu1.png)

### 重启 ascend-device-plugin-daemonset

切分实例过后 手动重启 device-plugin pod，然后使用 `kubectl describe` 命令查看已注册 node 的资源：

```bash
kubectl describe node {{nodename}}
```

![vnpu2](../images/vnpu2.png)

## 如何使用设备

在创建应用时，指定资源 key，参考下述 YAML：

```yaml
......
resources:
  requests:
    huawei.com/Ascend310P-2c: 1
  limits:
    huawei.com/Ascend310P-2c: 1
......
```
