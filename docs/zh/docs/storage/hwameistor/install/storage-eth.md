# 存储网卡配置

HwameiStor 支持使用单独的网卡进行数据卷同步，可以避免使用通信网卡带来流量阻塞问题。

## 配置步骤

1. 查看 local-storage 的 ENV: **NODE_ANNOTATION_KEY_STORAGE_IPV4** 的值，默认是
    **[localstorage.hwameistor.io/storage-ipv4](http://localstorage.hwameistor.io/storage-ipv4)**

2. 将节点上的**存储网卡地址通过注释的方式标记**

    ```sh
    kubectl annotate node <your_storage_node> localstorage.hwameistor.io``/storage-ipv4``=xxx.xxx.xxx.xxx
    ```

3. **重启**节点上的 local-storage 服务

4. **验证**配置是否生效

    ```sh
    kubectl get lsn <your_storage_node> -o yaml |``grep` `-i storageIP
    ```

!!! note

    - 【🔥提前配置】：存储网卡的配置属于存储系统的前置性配置，建议在 HwameiStor 系统安装前**提前配置**。
    - 【运行中配置】：如果 HwameiStor 已经部署，后面进行上述配置修改，那么**对之前已经创建出来的数据卷不会生效**，也就是还会使用之前的网卡进行数据卷同步。
