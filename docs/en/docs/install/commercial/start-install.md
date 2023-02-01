---
hide:
  - toc
---

# Install DCE 5.0 commercial offline

Please do the following preparations before installation:

- [Deployment planning and environment preparation](deploy-plan.md)
- [install dependencies](../install-tools.md) for bootstrapping node
- Make sure that the time of all nodes is synchronized, otherwise, after the installation is complete, kube.conf will report an error `Unable to connect to the server: x509: certificate has expired or is not yet`
- Make sure that `/etc/resolv.conf` of all nodes has at least one nameserver, otherwise coredns will report `plugin/forward: no nameservers found`

The specific offline installation steps are as follows:

1. Add executable permissions to the `dce5-installer` binary file on the bootstrapping node:

    ```bash
    chmod +x dce5-installer
    ```

2. Set the cluster configuration file [clusterConfig.yaml](clusterconfig.md), which can be obtained under the offline package `offline/sample`, and be modified according to the actual deployment mode needs.

3. Start the installation of DCE 5.0.

    ```shell
    ./dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml -p ./offline/
    ```

    !!! note

        The command needs to specify the `-m` parameter, and the `manifest.yaml` file is under the offline package `offline/sample`.

4. After the installation is complete, the command line will prompt that the installation is successful. congratulations! :smile: Now you can use the default account and password (admin/changeme) to explore the new DCE 5.0 through the URL prompted on the screen!

    ![success](../images/success.png)

    !!! success

        Please record the prompted URL for your next visit.

5. After successfully installing the commercial version of DCE 5.0, please proceed to [Genuine Authorization](https://qingflow.com/f/e3291647).