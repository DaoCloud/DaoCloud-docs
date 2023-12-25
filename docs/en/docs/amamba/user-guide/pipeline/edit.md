# edit pipeline

After creating a custom pipeline, the pipeline stages need to be defined manually. Currently supports defining execution stages for pipelines by editing the Jenkinsfile or via GUI forms. In addition, if you need to change the configuration of each stage of the pipeline, you can also refer to this article to adjust the configuration.

!!! note

     - For the concepts involved in editing pipelines, please refer to [Concepts in pipelines](config/concept.md)
     - For the parameters involved in editing the pipeline, please refer to [Graphic Task Template Parameter Description](config/step.md)

## prerequisites

- [Create Workspace](../../../ghippo/user-guide/workspace/workspace.md), [Create User](../../../ghippo/user-guide/access-control/user.md).
- Add the user to the workspace with __workspace editor__ or higher privileges.
- Create three credentials that can access the code warehouse, mirror warehouse, and cluster, please refer to [credential management] (credential.md).
- [Create a custom pipeline](create/custom.md), and need to add two string parameters in the build parameters. These parameters will be used in the image build command. The parameters are described as follows:

     | Parameter Type | Parameter Name | Description |
     | -------- | -------- | ------------------------------- ------------------ |
     | String | registry | Mirror registry address. In this example use __release-ci.daocloud.io__ |
     | string | project | The project name in the registry. In this example use __demo__ |
     | string | name | The name of the image. This example uses __http-hello__ |

## Edit the pipeline through the interface form

Workbench has designed a graphical pipeline editing view, which is compatible with editing most of the custom operations in the Jenkinsfile, making it easy to view or define each [stage (Stage)] of the pipeline (https://www.jenkins.io/ doc/book/pipeline/#stage) and each [Step (Step)](https://www.jenkins.io/doc/book/pipeline/#step), to achieve a WYSIWYG pipeline editing experience .

### Interface layout description

1. Click a created custom pipeline. Click __Edit Pipeline__ in the upper right corner to enter the graphical editing page.

     <!--![]()screenshots-->

2. The graphical editing page includes two areas: **Canvas (left)** and **Stage Settings (right)**.

     <!--![]()screenshots-->

     - After clicking __+Add Stage__, a serial stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage.

     - After clicking __+ Add Parallel Stage__, a parallel stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage.

     - After the stage is created, click __Stage__, you can use the stage to configure the stage. Support setting the name, agent, trigger condition and steps of the stage.

### Configure global settings

Click __Global Settings__, select node from the __Type__ drop-down list, and select go 16 from the label drop-down list.

<!--![]()screenshots-->

### Add stage - pull source code

1. Click __Add Stage__ in the canvas. In the stage settings on the right set the name: git clone.

2. Click __Add Step__, select __git clone__ under the step type in the pop-up dialog box, and refer to the table below to configure the relevant parameters.

     - Warehouse URL: Enter the warehouse address.
     - Branch: do not fill in, the default is the master branch.
     - Credentials: If your warehouse is a private warehouse, you need to provide a credential.

     <!--![]()screenshots-->

### Add Phase - Unit Test

1. Click __Add Stage__ in the canvas. In the stage settings on the right set the name: unit test.

2. In the step module, select to open __specify container__, fill in the container name: go in the pop-up dialog box, and then click __OK__.

     <!--![]()screenshots-->

3. Click __Add step to unit test the code and generate a test report__, select shell under the step type in the pop-up dialog box, and enter the following command in the command line, and then click __OK__.

     ```go
     go test -coverprofile=coverage.out
     ```

     <!--![]()screenshots-->

### Add stage - build and push image

1. Click __Add Stage__ in the canvas. Set the name in the stage settings on the right: build & push.

2. In the step module, select to open __specify container__, fill in the container name: go in the pop-up dialog box, and then click __OK__.

     <!--![]()screenshots-->

3. Select to enable __Use Credentials__ in the step module, fill in the relevant parameters in the pop-up dialog box, and then click __OK__.

     - Credentials: Select the created docker hub credentials to allow users to access the mirror warehouse. Select the created "docker-credential" credential.
     - Password variable: PASS
     - Username variable: USER

     <!--![]()screenshots-->

4. Click __Add Step__ to build the code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click __OK__.

     ```go
     go build -o simple-http-server main.go
     ```

5. Click __Add Step__ to build a Docker image according to the Dockerfile in the source code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click __OK__.

     ```docker
     docker build -f Dockerfile . -t $REGISTRY/$PROJECT/$NAME:latest
     ```

6. Click __Add Step__ to log in to the mirror warehouse and push the image to the mirror warehouse. In the pop-up dialog box, select shell under the step type, enter the following command in the command line, and click __OK__.

     ```docker
     docker login $REGISTRY -u $USER -p $PASS
     ```

     <!--![]()screenshots-->

6. Click __Add Step__ to push the image to the mirror warehouse, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click __OK__.

     ```docker
     docker push $REGISTRY/$PROJECT/$NAME:latest
     ```

     <!--![]()screenshots-->

!!! note
    
     After the image is updated, the trigger pipeline can also be implemented. For specific operations, please refer to [Trigger Pipeline](run/trigger.md)

### Add stage - review

1. Click __Add Stage__ in the canvas. In the stage settings on the right set the name: review.

2. Click __Add Step__, select __Audit__ under the step type in the pop-up dialog box, fill in __@admin__ in the message field, that is, the __admin__ account will be audited when the pipeline runs to this stage, and then Click __OK__.

     <!--![]()screenshots-->

### Add stage - deploy to cluster

1. Click __Add Stage__ in the canvas. In the stage settings on the right set the name: deploy.

2. In the step module, select to open __specify container__, fill in the container name: go in the pop-up dialog box, and then click __OK__.

     <!--![]()screenshots-->

3. Select to enable __Use Credentials__ in the step module, fill in the relevant parameters in the pop-up dialog box, and then click __OK__.

     - Credentials: Choose a credential of type kubeconfig.

     - kubeconfig variable: If you are using the kubectl apply deployment method, the variable value must be KUBECONFIG.

     <!--![]()screenshots-->

4. Click __Add Step__ to perform the cluster deployment operation, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and then click __OK__.

     ```shell
     kubectl apply -f deploy.yaml
     ```

### Run the pipeline

1. Click __Run Now__ on the transaction details page. In the pop-up dialog box, set the three string parameters defined in the prerequisites, and click __OK__ to run the pipeline.

     <!--![]()screenshots-->

2. After the operation is successfully started, the page will automatically switch to the pipeline details page, click the record of the currently running pipeline.

3. After entering the pipeline record details page, you can view the running process of the current pipeline. The admin or platform administrator is required to review the pipeline. After the audit is successful, the resources will be deployed to the cluster.

     <!--![]()screenshots-->

### Verify cluster resources

1. If each stage of the pipeline runs successfully, a Docker image is automatically built and pushed to your Docker Hub repository. Eventually, the pipeline will automatically create a stateless load in the project you set up beforehand.

2. Go to the container management platform, click __Workload__ under the cluster, and you can see the stateless workload displayed in the list.

     <!--![]()screenshots-->

## Edit pipeline via Jenkinsfile

The various stages of the pipeline can be quickly defined through the Jenkinsfile.

1. On the pipeline list page, find the pipeline to be created, and click __Edit Jenkinsfile__ on the right.

     <!--![]()screenshots-->

     > You can also click the name of the pipeline and click __Edit Jenkinsfile__ in the upper right corner of the page.

2. Enter or paste the Jenkinsfile prepared in advance, and click __OK__.

     <!--![]()screenshots-->