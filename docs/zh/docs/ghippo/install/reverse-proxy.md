# 自定义 DCE 5.0 反向代理服务器地址

## 设置步骤

1.  设置环境变量，方便在下文中使用。

    ```shell
    # 您的反向代理地址，例如： `export DCE_PROXY="https://demo-alpha.daocloud.io"` 
    export DCE_PROXY="https://domain:port"

    # helm --set 参数备份文件
    export GHIPPO_VALUES_BAK="ghippo-values-bak.yaml"

    # 获取当前 ghippo 的版本号
    export GHIPPO_HELM_VERSION=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')
    ```

2.  更新全局管理 Helm 仓库。

    ```shell
    helm repo update ghippo
    ```

3.  备份 --set 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > ${GHIPPO_VALUES_BAK}
    ```

4.  添加您的反向代理地址。

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

5.  执行 `helm upgrade` 使配置生效。

    ```shell
    helm upgrade ghippo ghippo/ghippo \
      -n ghippo-system \
      -f ${GHIPPO_VALUES_BAK} \
      --version ${GHIPPO_HELM_VERSION}
    ```

6.  使用 __kubectl__ 重启全局管理 Pod，使配置生效。

    ```shell
    kubectl rollout restart deploy/ghippo-apiserver -n ghippo-system
    kubectl rollout restart statefulset/ghippo-keycloakx -n ghippo-system
    ```
