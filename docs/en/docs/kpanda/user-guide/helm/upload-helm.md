---
MTPE: windsonsea
Date: 2024-04-23
hide:
  - toc
---

# Upload Helm Charts

This article explains how to upload Helm charts. See the steps below.

1. Add a Helm repository, refer to [Adding a Third-Party Helm Repository](./helm-repo.md) for the procedure.

2. Upload the Helm Chart to the Helm repository.

    === "Upload with Client"

        !!! note

            This method is suitable for Harbor, ChartMuseum, JFrog type repositories.

        1. Log in to a node that can access the Helm repository, upload the Helm binary to the node, and install the cm-push plugin.

            Refer to the [plugin installation process](https://github.com/chartmuseum/helm-push).

        2. Push the Helm Chart to the Helm repository by executing the following command:

            ```shell
            helm cm-push ${charts-dir} ${HELM_REPO_URL} --username ${username} --password ${password}
            ```

            Parameter descriptions:

            - `charts-dir`: The directory of the Helm Chart, you can also directly push a packaged chart (i.e., a .tgz file).
            - `HELM_REPO_URL`: URL of the Helm repository.
            - `username`/`password`: Username and password with push permissions for the Helm repository.
            - If using https access, add the parameter `--insecure`

    === "Upload with Web Page"

        !!! note

            This method is only applicable to Harbor repositories.

        1. Log into the Harbor repository, ensuring the logged-in user has permissions to push;

        2. Go to the relevant project, select the __Helm Charts__ tab, click the __Upload__ button on the page to upload the Helm Chart.

3. Synchronize remote repository data

    If the cluster settings do not enable __Automatic Helm Repository Refresh__ , manual synchronization is required. The general steps are:

    Go to __Helm Apps__ -> __Helm Charts__ , click the __Sync Repository__
    action button on the right side of the corresponding repository list to complete the repository data synchronization.

