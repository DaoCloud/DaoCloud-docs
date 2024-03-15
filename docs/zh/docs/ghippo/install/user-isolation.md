# 开启 Folder/WS 之间的隔离模式

具体设置步骤如下：

1.  检查全局管理 helm 仓库是否存在。

    ```shell
    helm repo list | grep ghippo
    ```

    若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

    ```none
    Error: no repositories to show
    ```

2.  添加并且更新全局管理的 helm 仓库。

    ```shell
    helm repo add ghippo http://{harbor url}/chartrepo/{project}
    helm repo update ghippo
    ```

3.  设置环境变量，方便在下文中使用。

    ```shell
    # helm --set 参数备份文件
    export GHIPPO_VALUES_BAK="ghippo-values-bak.yaml"

    # 获取当前 ghippo 的版本号
    export GHIPPO_HELM_VERSION=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')
    ```

4.  备份 --set 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > ${GHIPPO_VALUES_BAK}
    ```

5.  打开 Folder/WS 之间的隔离模式开关。

    !!! note

        - 如果可以，您可以使用 __yq__ 命令：

            ```shell
            yq -i ".apiserver.userIsolationMode = \"Folder\"" ${GHIPPO_VALUES_BAK}
            ```

        - 或者您可以使用 __vim__ 命令编辑并保存：

            ```shell
            vim ${GHIPPO_VALUES_BAK}

            USER-SUPPLIED VALUES:
            ...
            # 添加下面两行即可
            apiserver:
              userIsolationMode: Folder
            ```

6.  执行 `helm upgrade` 使配置生效。

    ```shell
    helm upgrade ghippo ghippo/ghippo \
      -n ghippo-system \
      -f ${GHIPPO_VALUES_BAK} \
      --version ${GHIPPO_HELM_VERSION}
    ```

7.  使用 __kubectl__ 重启全局管理 Pod，使配置生效。

    ```shell
    kubectl rollout restart deploy/ghippo-apiserver -n ghippo-system
    ```
