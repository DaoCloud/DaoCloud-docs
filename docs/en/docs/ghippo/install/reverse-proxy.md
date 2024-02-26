# Custom DCE 5.0 reverse proxy server address

Follow the steps below to customize the reverse proxy server address for DCE 5.0.

1. Set environment variables for convenience in the following.

    ```shell
    # Your reverse proxy address, for example: `export DCE_PROXY="https://demo-alpha.daocloud.io"` 
    export DCE_PROXY="https://domain:port"

    # helm --set parameter backup file
    export GHIPPO_VALUES_BAK="ghippo-values-bak.yaml"

    # Get the version number of the current ghippo
    export GHIPPO_HELM_VERSION=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')
    ```

2. Update the global management Helm repository.

    ```shell
    helm repo update ghippo
    ```

3. Back up the --set parameter.

    ```shell
    helm get values ​​ghippo -n ghippo-system -o yaml > ${GHIPPO_VALUES_BAK}
    ```

4. Add your reverse proxy address.

    !!! note

        - If available, you can use the __yq__ command:

            ```shell
            yq -i ".global.reverseProxy = \"${DCE_PROXY}\"" ${GHIPPO_VALUES_BAK}
            ```

        - Or you can use the __vim__ command to edit and save:

            ```shell
            vim ${GHIPPO_VALUES_BAK}

            USER-SUPPLIED VALUES:
            ...
            global:
              ...
              reverseProxy: ${DCE_PROXY} # only need to modify this line
            ```

5. Run `helm upgrade` to make the configuration take effect.

    ```shell
    helm upgrade ghippo ghippo/ghippo \
    -n ghippo-system\
    -f ${GHIPPO_VALUES_BAK} \
    --version ${GHIPPO_HELM_VERSION}
    ```

6. Use __kubectl__ to restart the global management Pod to make the configuration take effect.

    ```shell
    kubectl rollout restart deploy/ghippo-apiserver -n ghippo-system
    kubectl rollout restart statefulset/ghippo-keycloakx -n ghippo-system
    ```