# 批量检测中英同步问题

本文基于 [./scripts/lsync.sh](https://github.com/DaoCloud/DaoCloud-docs/blob/main/scripts/lsync.sh)
这个脚本批量检测中英文字的不同步问题。

## MacOS

在仓库的根目录中，

1. 赋予 lsync.sh 脚本可执行权限（主要是解决 `permission denied` 问题）

    ```sh
    sudo chmod +x ./scripts/lsync.sh
    ```

1. 查看某个文件夹的中英文档同步情况

    ```sh
    ./scripts/lsync.sh docs/en/docs/kpanda
    ```

    输出类似于：

    ```diff
    1	1	docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md
    7	7	docs/zh/docs/kpanda/user-guide/clusters/access-cluster.md
    7	5	docs/zh/docs/kpanda/user-guide/clusters/runtime.md
    ```

    第一个数字表示新增的行数，第二个数字表示删除的行数

1. 查看某个文档的中英同步情况

    ```sh
    ./scripts/lsync.sh docs/en/docs/kpanda/intro/concepts.md
    ```

    输出类似于：

    ```diff
    diff --git a/docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md b/docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md
    index 8cf6b8a8e..e7fcce06b 100644
    --- a/docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md
    +++ b/docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md
    @@ -19,4 +19,4 @@ Kubernetes 版本发布说明
    | ----------------------- | -------------------------- | -------------------------- | ---------- | ---------- |
    | 1.25</br>1.26</br>1.27        | 1.24</br>1.25</br>1.26           | **1.26.5**                 | V0.7.0     | 2023.05.09 |
    
    -![版本支持机制](../../images/cluster-version.png)
    +![版本支持机制](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/cluster-version.png)
    ```

    其中红色文字表示删除，绿色文字表示新增

1. 参照以上 diff 比较结果，修改对应的英文文件后提交 PR。

!!! tip

    上述命令建议在 `main` 分支中运行。

## Windows

可以在 [Git for Windows](https://gitforwindows.org/) 中直接运行上述 diff 命令，无需 `sudo chmod` 赋权操作。

![windows](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/windows.jpg)
