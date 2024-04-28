# 智能设备控制

本文介绍基于自定义协议的终端设备接入边缘计算平台，并与云端交互的方法。以一个手势控制灯开关的场景为例，介绍整体实现流程。

## 准备工作

- 边缘节点，节点接入要求参见[边缘节点接入要求](../user-guide/node/join-rqmt.md)
- LED 灯
- 手势识别模型应用
- LED 灯驱动 mapper，mapper 开发参见[如何开发设备驱动应用 mapper](./develop-device-mapper.md)

## 操作流程

1. 接入边缘节点，接入流程参考[接入边缘节点](../user-guide/node/access-guide.md)

1. 