# Unknown Clusters Detected When Creating Mesh Instances

There are several potential reasons for this issue:

- **Reason**: The unknown cluster was recently uninstalled, and the cluster synchronization task has not yet been triggered.

    **Analysis**: The mesh instance of the unknown cluster may still be in the process of being uninstalled, waiting for the uninstallation to complete.

    **Solution**: In this case, simply trigger the cluster synchronization automatically.

- **Reason**: There are remnants from the cluster uninstallation.

    **Solution**: Confirm that the unknown cluster no longer exists, and manually delete
    any remained cluster information. To do this, log into the global service cluster
    `kpanda-global-cluster` and run the following commands:

    ```bash
    kubectl -n mspider-system get mc
    kubectl -n mspider-system delete mc jy-test
    ```

    ![Memory Usage Check](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/troubleshoot/images/mc-delete-01.png)
