# 基于 Spiderpool 的外部访问

## 配置目标

由于 Redis 本身并未提供集群外部访问的能力，因此需要通过其他网络功能，实现该访问需求。本例中采用了 calico/cilium + macvlan standalone + spiderpool 的支持方式。


## 前提

DCE 5.0 集群内已部署 `multus-underlay` 和 `spiderpool`。

![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool09.png)

## 步骤

### 环境准备

1. 确认macvlan部署情况。执行命令，查看部署状态，可见类似如下图中的返回信息

    ```shell
        kubectl get network-attachment-definitions -A
    ```

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool01.png)

    存在 `macvlan-vlan0(standalone)`和 `macvlan-overlay-vlan0(overlay)` 则表示集群内已部署 macvlan。

    !!! note

        Redis 仅支持通过 `macvlan standalone` 模式实现外部访问

2. 创建子网及 IP 池，具体操作可参见：[创建子网及 IP 池¶](https://docs.daocloud.io/network/modules/spiderpool/createpool.html)

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool02.png)

    !!! note

        Redis 仅可以使用现有子网及 IP 池，请务必先执行手工创建操作。

### Redis 实例配置

#### 集群模式

1. 修改 redis 实例的 `CR`（rediscluster），在 metadata 字段下添加以下内容：

    ```yaml
        annotations:
          v1.multus-cni.io/default-network: kube-system/macvlan-vlan0
          ipam.spidernet.io/ippools: '[{"interface":"eth0","ipv4":["ippool-redis"]}]'
    ```

2. 更新 `CR` 后，查看实例节点信息，可见类似下图的 IP 地址变化，则表示配置成功：

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool03.png)

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool04.png)


3. 完成配置后可从集群外部访问节点，访问成功

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool05.png)


#### 哨兵模式

1. 更新 redis 实例 `CR`（redisfailover），分别在 `spec.redis` 和 `spec.sentinel` 字段添加以下内容：

    ```yaml
        podAnnotations:
          v1.multus-cni.io/default-network: kube-system/macvlan-vlan0
          ipam.spidernet.io/ippools: '[{"interface":"eth0","ipv4":["ippool-redis"]}]'
    ```

    !!! note

        cilium：需要为 `redis-operator` 的 `deployment` 添加 `annotations`，字段位置为 `spec.template.metadata.annotations`

        calico：无需更新 `redis-operator`

2. 更新 `CR` 后，查看实例节点信息，可见类似下图的 IP 地址变化，则表示配置成功：

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool06.png)

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool07.png)

3. 完成配置后可从集群外部访问节点验证配置有效性。访问成功

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/spiderpool08.png)


