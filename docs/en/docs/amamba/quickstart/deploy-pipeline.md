# Rapid creation pipeline

This section describes how to create an pipeline by compiling, constructing, and deploying an pipeline.

## prerequisite

- Create a workspace and a user. Add the user to the workspace and assign the role __workspace edit__. See [Create Workspace](../../ghippo/user-guide/workspace/workspace.md), [Users and Roles](../../ghippo/user-guide/access-control/user.md).
- Create two credentials that can access the mirrored warehouse and cluster, and name them __registry__ and __kubeconfig__. For more information on creating credentials, see [Credential Management](../user-guide/pipeline/credential.md).
- Prepare a GitHub repository and a DockerHub repository.

## Create credentials

1. Create two credentials on the __Credential__ page:

    - docker-credential: The username and password used to access the container registry.
    - demo-dev-kubeconfig: Used to access the Kubernetes cluster using this kubeconfig.

2. After the creation is complete, you can see the credential information on the __Credential List__ page.

## Create a custom pipeline

1. On the pipeline list page, click __Create Pipeline__.

    <!--![]()screenshots-->

2. In the dialog box that pops up, select __Create Custom Pipeline__ and click __OK__.

    <!--![]()screenshots-->

3. Enter pipeline name __pipeline-demo__.

    <!--![]()screenshots-->

4. Add three string arguments in __Build Parameters__ that will be used in the command for the mirror build.

    - registry: indicates the address of the mirror repository. Example value: __release.daocloud.io__
    - project: Name of the project in the mirror repository. Example value: __demo__
    - name: indicates the name of the mirror. Example value: __http-hello__

    <!--![]()screenshots-->

5. After adding, click __OK__.

## Editing pipeline

1. Click the name of a pipeline on the Pipeline list page.

    <!--![]()screenshots-->

2. In the upper right corner, click __Edit Pipeline__,

    <!--![]()screenshots-->

3. Click __Global Settings__ in the upper right corner.

    <!--![]()screenshots-->

4. Set type to node and label to go and click __OK__.

    <!--![]()screenshots-->

5. Add Phase – Pull source code.

    - Click __Add Stages__ in the canvas. In the stage Settings on the right, set the name: git clone.
    - Click __Add Steps__, select git clone under step type in the pop-up dialog box, and configure related parameters:
        - Warehouse URL: Enter the GitLab warehouse address.
        - Branch: If this parameter is not specified, the default branch is master.
        - Credential: If you are a private repository, you need to provide a credential.

    <!--![]()screenshots-->

6. Add phase – Build and push the image.

    - Click __Add Stages__ in the canvas. In the stage Settings on the right, set the name: build & push.

    - Select Open __Specify Container__ in the step module, fill in the container name: go in the pop-up dialog box, and then click __OK__.

        <!--![]()screenshots-->

    - Select Enable __Use Credential__ in the step module, fill in relevant parameters in the dialog box that pops up, and then click __OK__.

        - Credentials: Select the Docker hub credentials created for users to access the container registry.
        - Password variable: PASS
        - username variable: USER

        <!--![]()screenshots-->

    - Click __Add Steps__ to build the code, select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click __OK__.

        ```go
        go build -o simple-http-server main.go
        ```

    - Click __Add Steps__ to build the Docker image according to the Dockerfile in the source code. Select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click __OK__.

        ```docker
        docker build -f Dockerfile . -t $registry/$project/$name:latest
        ```

    - Click __Add Steps__ to log in to the mirror warehouse, select shell under step type in the pop-up dialog box, and enter the following command in the command line, then click __OK__.

        ```docker
        docker login $registry -u $USER -p $PASS
        ```

    - Click __Add Steps__ to push the image to the image warehouse, select shell under step type in the pop-up dialog box, and enter the following command in the command line, and then click __OK__.

        ```docker
        docker push $registry/$project/$name:latest
        ```

7. Add Phase – Deploy to cluster

    - Click __Add Stages__ in the canvas. In the stage Settings on the right, set the name: deploy.

    - Select Open __Specify Container__ in the step module, fill in the container name: go in the pop-up dialog box, and then click __OK__.

        <!--![]()screenshots-->

    - Select Enable __Use Credential__ in the step module, fill in relevant parameters in the pop-up dialog box, and then click __OK__.

         - Credentials: Select credentials of type kubeconfig.

         - kubeconfig variable: If you are deploying kubectl apply, the variable value must be KUBECONFIG.

         <!--![]()screenshots-->

    - Click __Add Steps__ to perform cluster deployment. In the dialog box that appears, select shell under Step type, enter the following command in the command line, and click __OK__.

        ```shell
        kubectl apply -f deploy.yaml
        ```

## Save and run the assembly line

1. Click __Save & Run__ after finishing the previous step.

    <!--![]()screenshots-->

2. Enter the example parameters in Step 2 in the dialog box that appears. Click __OK__ to run the pipeline successfully.

    <!--![]()screenshots-->
