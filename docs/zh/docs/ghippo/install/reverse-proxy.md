# 自定义 DCE 5.0 反向代理服务器地址

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
    # 您的反向代理地址，例如 `export DCE_PROXY="https://demo-alpha.daocloud.io"` 
    export DCE_PROXY="https://domain:port"

    # helm --set 参数备份文件
    export GHIPPO_VALUES_BAK="ghippo-values-bak.yaml"

    # 获取当前 ghippo 的版本号
    export GHIPPO_HELM_VERSION=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')
    ```

4.  备份 --set 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > ${GHIPPO_VALUES_BAK}
    ```

5.  添加您的反向代理地址。

    !!! note

        - 如果可以，您可以使用 __yq__ 命令：

            ```shell
            yq -i ".global.reverseProxy = \"${DCE_PROXY}\"" ${GHIPPO_VALUES_BAK}
            ```

        - 或者您可以使用 __vim__ 命令编辑并保存：

            ```shell
            vim ${GHIPPO_VALUES_BAK}

            USER-SUPPLIED VALUES:
            ...
            global:
              ...
              reverseProxy: ${DCE_PROXY} # 只需要修改这一行
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
    kubectl rollout restart statefulset/ghippo-keycloakx -n ghippo-system
    ```
