# 开启并使用昇腾虚拟化

昇腾虚拟化分为动态虚拟化和静态虚拟化，本文介绍如何开启并使用昇腾静态虚拟化能力。

##   前提条件

1. 昇腾相关固件与驱动安装成功
2. kubernetes 集群环境搭建
3. ascend-docker-runtime安装
4. ascend-mindxdl 组件的安装

请参考[昇腾NPU组件安装文档](https://docs.daocloud.io/kpanda/user-guide/gpu/ascend/ascend_driver_install.html)安装基础环境

## 开启虚拟化能力

开启虚拟化能力需要手动修改 ascend-device-plugin-daemonset 组件的启动参数，参考下述命令：
```
- device-plugin -useAscendDocker=true -volcanoType=true -presetVirtualDevice=false
- logFile=/var/log/mindx-dl/devicePlugin/devicePlugin.log -logLevel=0
```
### 切分 VNPU 实例
静态虚拟化需要手动对 VNPU 实例的切分，请参考下述命令：
``` 
npu-smi set -t create-vnpu -i 13 -c 0 -f vir02
``` 
- i 指的是 card id
- c指的是 chip id
- vir02 指的是切分规格模板
关于 card id 和 chip id，可以通过npu-smi info 查询，切分规格可通过[ascend 官方模版]([https://www.hiascend.com/document/detail/zh/mindx-dl/500/AVI/cpaug/cpaug_006.html](https://www.hiascend.com/document/detail/zh/mindx-dl/500/AVI/cpaug/cpaug_006.html))进行查询。

切分实例过后可通过下述命令查询切分结果：

```
npu-smi info -t info-vnpu -i 13 -c 0
```
查询结果如下：

![vnpu1](../images/vnpu1.png)

### 重启 ascend-device-plugin-daemonset
切分实例过后 手动重启device-plugin 容器组，然后使用describe 查看注册上 node 的资源：

```
kubectl describe node {{nodename}}
```
![vnpu2](../images/vnpu2.png)

## 如何使用设备

在创建应用时，指定资源key，参考下述 yaml：


```
......

resources:
  requests:
    huawei.com/Ascend310P-2c: 1
  limits:
    huawei.com/Ascend310P-2c: 1

......
```
