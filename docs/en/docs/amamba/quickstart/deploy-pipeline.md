# Rapid creation pipeline

This section describes how to create an pipeline by compiling, constructing, and deploying an pipeline.

## prerequisite

- Create a workspace and a user. Add the user to the workspace and assign the role `workspace edit`. See [Create Workspace](../../ghippo/user-guide/workspace/workspace.md), [Users and Roles](../../ghippo/user-guide/access-control/user.md).
- Create two credentials that can access the mirrored warehouse and cluster, and name them `registry` and `kubeconfig`. For more information on creating credentials, see [Credential Management](../user-guide/pipelines/credential.md).
- Prepare a GitHub repository and a DockerHub repository.

## Create credentials

1. Create two credentials on the `Credential` page:

    - docker-credential: The username and password used to access the container registry.
    - demo-dev-kubeconfig: Used to access the Kubernetes cluster using this kubeconfig.

2. After the creation is complete, you can see the credential information on the `Credential List` page.

## Create a custom pipeline

1. On the pipeline list page, click `Create Pipeline`.

    <!--![]()screenshots-->

2. In the dialog box that pops up, select `Create Custom Pipeline` and click `OK`.

    <!--![]()screenshots-->

3. Enter pipeline name `pipeline-demo`.

    <!--![]()screenshots-->

4. Add three string arguments in `Build Parameters` that will be used in the command for the mirror build.

    - registry: indicates the address of the mirror repository. Example value: `release.daocloud.io`
    - project: Name of the project in the mirror repository. Example value: `demo`
    - name: indicates the name of the mirror. Example value: `http-hello`

    <!--![]()screenshots-->

5. After adding, click `OK`.

## Editing pipeline

1. Click the name of a pipeline on the Pipeline list page.

    <!--![]()screenshots-->

2. In the upper right corner, click `Edit Pipeline`,

    <!--![]()screenshots-->

3. Click `Global Settings` in the upper right corner.

    <!--![]()screenshots-->

4. Set type to node and label to go and click `OK`.

    <!--![]()screenshots-->

5. Add Phase – Pull source code.

    - Click `Add Stages` in the canvas. In the stage Settings on the right, set the name: git clone.
    - Click `Add Steps`, select git clone under step type in the pop-up dialog box, and configure related parameters:
        - Warehouse URL: Enter the GitLab warehouse address.
        - Branch: If this parameter is not specified, the default branch is master.
        - Credential: If you are a private repository, you need to provide a credential.

    <!--![]()screenshots-->

6. Add phase – Build and push the image.

    - Click `Add Stages` in the canvas. In the stage Settings on the right, set the name: build & push.

    - Select Open `Specify Container` in the step module, fill in the container name: go in the pop-up dialog box, and then click `OK`.

        <!--![]()screenshots-->

    - Select Enable `Use Credential` in the step module, fill in relevant parameters in the dialog box that pops up, and then click `OK`.

        - Credentials: Select the Docker hub credentials created for users to access the container registry.
        - Password variable: PASS
        - username variable: USER

        <!--![]()screenshots-->

    - Click `Add Steps` to build the code, select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click `OK`.

        ```go
        go build -o simple-http-server main.go
        ```

    - Click `Add Steps` to build the Docker image according to the Dockerfile in the source code. Select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click `OK`.

        ```docker
        docker build -f Dockerfile . -t $registry/$project/$name:latest
        ```

    - Click `Add Steps` to log in to the mirror warehouse, select shell under step type in the pop-up dialog box, and enter the following command in the command line, then click `OK`.

        ```docker
        docker login $registry -u $USER -p $PASS
        ```

    - Click `Add Steps` to push the image to the image warehouse, select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click `OK`.

        ```docker
        docker push $registry/$project/$name:latest
        ```

7. Add Phase – Deploy to cluster

    - Click `Add Stages` in the canvas. In the stage Settings on the right, set the name: deploy.

    - Select Open `Specify Container` in the step module, fill in the container name: go in the pop-up dialog box, and then click `OK`.

        <!--![]()screenshots-->

    - Select Enable `Use Credential` in the step module, fill in relevant parameters in the pop-up dialog box, and then click `OK`.

         - Credentials: Select credentials of type kubeconfig.

         - kubeconfig variable: If you are deploying kubectl apply, the variable value must be KUBECONFIG.

         <!--![]()screenshots-->

    - Click `Add Steps` to perform cluster deployment. In the dialog box that appears, select shell under Step type, enter the following command in the command line, and click `OK`.

        ```shell
        kubectl apply -f deploy.yaml
        ```

## Save and run the assembly line

1. Click `Save & Run` after finishing the previous step.

    <!--![]()screenshots-->

2. Enter the example parameters in Step 2 in the dialog box that appears. Click `OK` to run the pipeline successfully.

    <!--![]()screenshots-->
