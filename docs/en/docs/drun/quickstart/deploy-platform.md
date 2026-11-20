# Install d.run AI Operating System - Admin

This tutorial walks you through an offline installation of d.run AI Operating System and signing in to the console with the default account.

## Prerequisites {: #prereq }

- A machine that meets the [deployment requirements](../install/commercial/deploy-requirements.md) serves as the seed node, with IPv4 forwarding enabled and the firewall disabled.
- The [offline image package](../install/start-install.md) (e.g. `offline-v0.46.0-amd64.tar`) has been downloaded and uploaded to the seed node.
- The osPackage offline package matching the seed node OS has been downloaded.

## Steps

1. Extract the offline image package on the seed node:

    ```bash
    tar -xvf offline-v0.46.0-amd64.tar
    ```

2. Edit [clusterConfig.yaml](../install/commercial/cluster-config.md) in the extracted `offline/sample` directory
   to configure the deployment mode, cluster nodes, and ISO image path. To adjust the modules to install,
   edit [manifest-cloud.yaml](../install/commercial/manifest.md).

    !!! note

        For d.run AI Operating System, use the manifest `manifest-cloud.yaml`: LLM Studio (`hydra`)
        is enabled by default, while Cockpit (`crane`) is disabled by default.
        This differs from the `manifest-cloud-tokfact.yaml` used by
        [Token Factory](../../tf/install/index.md).

3. Run the following command to start the installation:

    ```bash
    ./offline/dce5-installer cluster-create \
      -c ./offline/sample/clusterConfig.yaml \
      -m ./offline/sample/manifest-cloud.yaml
    ```

    !!! note

        - `-c` specifies the cluster config file (required)
        - `-m` specifies the product manifest; for d.run AI Operating System, use `manifest-cloud.yaml`
        - `-z` performs a minimal installation
        - `-d` enables debug mode

    The installation takes about 30 minutes, depending on the number of nodes and the network environment.

4. When the installation completes, the command line prints a success message. Use the URL shown on the screen
   to access the console and sign in with the default account and password `admin/changeme`.

5. Contact DaoCloud for authorization: email info@daocloud.io or call 400 002 6898. After authorization,
   go to the console home page to confirm that all modules are running normally.

## Verify

Sign in to the console as `admin`. If the left navigation shows entries for Global Management, Container Management, LLM Studio, and other modules, the installation succeeded.

## Next step

After the installation, continue to [Create Users and Workspaces](init-users.md).

For the complete installation workflow and configuration details, see the [Installation Guide](../install/index.md). For troubleshooting, see [Installation FAQs](../install/faq.md).
