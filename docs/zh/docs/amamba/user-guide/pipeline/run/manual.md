# 手动执行流水线

本页介绍在图形界面上手动执行流水线，包括立即执行、重新运行和取消运行。

## 立即执行流水线

1. 在流水线列表页选择某一个流水线，点击 **︙** ，在弹出的菜单中点击 **立即执行** 。

   ![handrun01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun01.jpeg)

2. 根据流水线是否配置了 **构建参数** ，执行后会出现一下两种情况：

   - 如果配置了 **构建参数** ，则会出现对话框并展示相关内容进行参数配置。

     ![handrun02](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun02.jpeg)

   - 如果未配置 **构建参数** ，则流水线会立即执行。

3. 流水线开始执行。

   ![handrun03](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun03.jpeg)

## 重新运行流水线

在流水线详情页面，根据流水线运行记录中的执行 ID 可以 **重新运行** 已运行过的流水线。

1. 在流水线列表中，点击某一个流水线的名称，进入流水线详情页面。

2. 在 **运行记录** 区域，找到需要重新运行的 **执行 ID** 。

3. 点击右侧的 **︙** ，在弹出的菜单中点击 **重新运行** 。

   ![handrun04](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun04.jpeg)

4. 流水线重新运行成功。

   ![handrun05](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun05.jpeg)

## 取消运行流水线

在流水线详情页面，根据流水线运行记录中的 **执行 ID** 可以 **取消** 正在执行的流水线。

1. 在流水线列表中，点击某一个流水线的名称，进入流水线详情页面。

2. 在 **运行记录** 区域，找到需要取消的 **执行 ID** 。

3. 点击右侧的 **︙** ，在弹出的菜单中点击 **取消** （适用于状态为 **执行中** 的流水线）。

   ![handrun06](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun06.jpeg)

4. 流水线取消运行成功。

   ![handrun07](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/handrun07.jpeg)
