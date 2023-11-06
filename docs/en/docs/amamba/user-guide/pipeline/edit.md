# edit pipeline

After creating a custom pipeline, the pipeline stages need to be defined manually. Currently supports defining execution stages for pipelines by editing the Jenkinsfile or via GUI forms. In addition, if you need to change the configuration of each stage of the pipeline, you can also refer to this article to adjust the configuration.

!!! note

     - For the concepts involved in editing pipelines, please refer to [Concepts in pipelines](config/concept.md)
     - For the parameters involved in editing the pipeline, please refer to [Graphic Task Template Parameter Description](config/step.md)

## prerequisites

- [Create Workspace](../../../ghippo/user-guide/workspace/workspace.md), [Create User](../../../ghippo/user-guide/access-control/user.md).
- Add the user to the workspace with `workspace editor` or higher privileges.
- Create three credentials that can access the code warehouse, mirror warehouse, and cluster, please refer to [credential management] (credential.md).
- [Create a custom pipeline](create/custom.md), and need to add two string parameters in the build parameters. These parameters will be used in the image build command. The parameters are described as follows:

     | Parameter Type | Parameter Name | Description |
     | -------- | -------- | ------------------------------- ------------------ |
     | String | registry | Mirror registry address. In this example use `release-ci.daocloud.io` |
     | string | project | The project name in the registry. In this example use `demo` |
     | string | name | The name of the image. This example uses `http-hello` |

## Edit the pipeline through the interface form

Workbench has designed a graphical pipeline editing view, which is compatible with editing most of the custom operations in the Jenkinsfile, making it easy to view or define each [stage (Stage)] of the pipeline (https://www.jenkins.io/ doc/book/pipeline/#stage) and each [Step (Step)](https://www.jenkins.io/doc/book/pipeline/#step), to achieve a WYSIWYG pipeline editing experience .

### Interface layout description

1. Click a created custom pipeline. Click `Edit Pipeline` in the upper right corner to enter the graphical editing page.

     <!--![]()screenshots-->

2. The graphical editing page includes two areas: **Canvas (left)** and **Stage Settings (right)**.

     <!--![]()screenshots-->

     - After clicking `+Add Stage`, a serial stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage.

     - After clicking `+ Add Parallel Stage`, a parallel stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage.

     - After the stage is created, click `Stage`, you can use the stage to configure the stage. Support setting the name, agent, trigger condition and steps of the stage.

### Configure global settings

Click `Global Settings`, select node from the `Type` drop-down list, and select go 16 from the label drop-down list.

<!--![]()screenshots-->

### Add stage - pull source code

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: git clone.

2. Click `Add Step`, select `git clone` under the step type in the pop-up dialog box, and refer to the table below to configure the relevant parameters.

     - Warehouse URL: Enter the warehouse address.
     - Branch: do not fill in, the default is the master branch.
     - Credentials: If your warehouse is a private warehouse, you need to provide a credential.

     <!--![]()screenshots-->

### Add Phase - Unit Test

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: unit test.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     <!--![]()screenshots-->

3. Click `Add step to unit test the code and generate a test report`, select shell under the step type in the pop-up dialog box, and enter the following command in the command line, and then click `OK`.

     ```go
     go test -coverprofile=coverage.out
     ```

     <!--![]()screenshots-->

### Add stage - build and push image

1. Click `Add Stage` in the canvas. Set the name in the stage settings on the right: build & push.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     <!--![]()screenshots-->

3. Select to enable `Use Credentials` in the step module, fill in the relevant parameters in the pop-up dialog box, and then click `OK`.

     - Credentials: Select the created docker hub credentials to allow users to access the mirror warehouse. Select the created "docker-credential" credential.
     - Password variable: PASS
     - Username variable: USER

     <!--![]()screenshots-->

4. Click `Add Step` to build the code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```go
     go build -o simple-http-server main.go
     ```

5. Click `Add Step` to build a Docker image according to the Dockerfile in the source code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```docker
     docker build -f Dockerfile . -t $REGISTRY/$PROJECT/$NAME:latest
     ```

6. Click `Add Step` to log in to the mirror warehouse and push the image to the mirror warehouse. In the pop-up dialog box, select shell under the step type, enter the following command in the command line, and click `OK`.

     ```docker
     docker login $REGISTRY -u $USER -p $PASS
     ```

     <!--![]()screenshots-->

6. Click `Add Step` to push the image to the mirror warehouse, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```docker
     docker push $REGISTRY/$PROJECT/$NAME:latest
     ```

     <!--![]()screenshots-->

!!! note
    
     After the image is updated, the trigger pipeline can also be implemented. For specific operations, please refer to [Trigger Pipeline](run/trigger.md)

### Add stage - review

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: review.

2. Click `Add Step`, select `Audit` under the step type in the pop-up dialog box, fill in `@admin` in the message field, that is, the `admin` account will be audited when the pipeline runs to this stage, and then Click `OK`.

     <!--![]()screenshots-->

### Add stage - deploy to cluster

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: deploy.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     <!--![]()screenshots-->

3. Select to enable `Use Credentials` in the step module, fill in the relevant parameters in the pop-up dialog box, and then click `OK`.

     - Credentials: Choose a credential of type kubeconfig.

     - kubeconfig variable: If you are using the kubectl apply deployment method, the variable value must be KUBECONFIG.

     <!--![]()screenshots-->

4. Click `Add Step` to perform the cluster deployment operation, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and then click `OK`.

     ```shell
     kubectl apply -f deploy.yaml
     ```

### Run the pipeline

1. Click `Run Now` on the transaction details page. In the pop-up dialog box, set the three string parameters defined in the prerequisites, and click `OK` to run the pipeline.

     <!--![]()screenshots-->

2. After the operation is successfully started, the page will automatically switch to the pipeline details page, click the record of the currently running pipeline.

3. After entering the pipeline record details page, you can view the running process of the current pipeline. The admin or platform administrator is required to review the pipeline. After the audit is successful, the resources will be deployed to the cluster.

     <!--![]()screenshots-->

### Verify cluster resources

1. If each stage of the pipeline runs successfully, a Docker image is automatically built and pushed to your Docker Hub repository. Eventually, the pipeline will automatically create a stateless load in the project you set up beforehand.

2. Go to the container management platform, click `Workload` under the cluster, and you can see the stateless workload displayed in the list.

     <!--![]()screenshots-->

## Edit pipeline via Jenkinsfile

The various stages of the pipeline can be quickly defined through the Jenkinsfile.

1. On the pipeline list page, find the pipeline to be created, and click `Edit Jenkinsfile` on the right.

     <!--![]()screenshots-->

     > You can also click the name of the pipeline and click `Edit Jenkinsfile` in the upper right corner of the page.

2. Enter or paste the Jenkinsfile prepared in advance, and click `OK`.

     <!--![]()screenshots-->