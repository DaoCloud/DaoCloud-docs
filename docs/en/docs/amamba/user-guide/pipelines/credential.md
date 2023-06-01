---
hide:
  - toc
---

# Credential management

Credentials can save sensitive information, such as username and password, access token (Secret text), Kubeconfig, etc., making the saved data more secure and flexible and avoiding being exposed to the mirror.
When the pipeline is running, it will interact with third-party websites or applications in most cases, such as Git warehouses, mirror warehouses, etc.
Corresponding credentials need to be provided during this process, so users are required to configure credentials for the pipeline. After users configure credentials, they can use these credentials to interact with third-party websites or applications.

Currently, you can create the following 3 types of credentials in Workbench:

- **Username and Password**: Used to store the authentication information of username and password. If the third-party website or application supports username/password access, you can choose this type, such as those of GitHub, GitLab and Docker Hub account.

- **Access Token (Secret text)**: A token such as an API token (such as a GitHub personal access token).

- **kubeconfig**: Used to configure cross-cluster authentication.

The specific steps to create and manage credentials are as follows:

1. Click `Pipeline`->`Certificate` in the left navigation bar to enter the list of certificates, and click `New Credentials` in the upper right corner.

    <!--![]()screenshots-->

2. On the `Create Credentials` page, configure the relevant parameters and click `OK`.

    <!--![]()screenshots-->

    - Fill in the `credential name`, set the ID that can be used in the pipeline, such as `dockerhub-id`. Note: Once set it cannot be changed.
    - In the `Type` field, select the type of credential to add.
    - Fill in the corresponding fields according to different document types:

        - Username and Password: Specify the `Username` and `Password` for the credentials in the corresponding fields.
        - Access Token (Secret text): Copy the encrypted text into the `Token` field.
        - Kubeconfig: Copy the cluster certificate into the `Kubeconfig` field.

3. The screen prompts that the creation is successful, and the newly created credential is the first one by default.

    <!--![]()screenshots-->

4. Click `︙` on the right side of the list, and you can choose operations such as edit or delete in the pop-up menu.

    !!! warning

        If you delete a credential that is being used by a certain pipeline, it may affect the access of the pipeline, please proceed with caution.