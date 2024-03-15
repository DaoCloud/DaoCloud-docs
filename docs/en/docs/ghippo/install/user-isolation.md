# Customize DCE 5.0 Reverse Proxy Server Address

The specific setup steps are as follows:

1. Check if the global management Helm repository exists.

    ```shell
    helm repo list | grep ghippo
    ```

   If the result is empty or shows the following error, proceed to the next step;
   otherwise, skip the next step.

    ```none
    Error: no repositories to show
    ```

2. Add and update the global management Helm repository.

    ```shell
    helm repo add ghippo http://{harbor url}/chartrepo/{project}
    helm repo update ghippo
    ```

3. Set environment variables for easier use in the following steps.

    ```shell
    # Your reverse proxy address, for example `export DCE_PROXY="https://demo-alpha.daocloud.io"` 
    export DCE_PROXY="https://domain:port"

    # Helm --set parameter backup file
    export GHIPPO_VALUES_BAK="ghippo-values-bak.yaml"

    # Get the current version of ghippo
    export GHIPPO_HELM_VERSION=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')
    ```

4. Backup the --set parameters.

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > ${GHIPPO_VALUES_BAK}
    ```

5. Add your reverse proxy address.

   !!! note

        - If possible, you can use the __yq__ command:

            ```shell
            yq -i ".apiserver.userIsolationMode = \"Folder\"" ${GHIPPO_VALUES_BAK}
            ```

        - Or you can use the __vim__ command to edit and save:

            ```shell
            vim ${GHIPPO_VALUES_BAK}

            USER-SUPPLIED VALUES:
            ...
            # Just add the following two lines
            apiserver:
              userIsolationMode: Folder
            ```

6. Run `helm upgrade` to apply the configuration.

    ```shell
    helm upgrade ghippo ghippo/ghippo \
      -n ghippo-system \
      -f ${GHIPPO_VALUES_BAK} \
      --version ${GHIPPO_HELM_VERSION}
    ```

7. Use __kubectl__ to restart the global management Pod to apply the configuration.

    ```shell
    kubectl rollout restart deploy/ghippo-apiserver -n ghippo-system
    ```
