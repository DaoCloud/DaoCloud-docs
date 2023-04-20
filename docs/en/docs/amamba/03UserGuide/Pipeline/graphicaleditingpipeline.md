# use the graphical editor pipeline

The application workbench has designed a graphical pipeline editing view, which is compatible with editing most of the custom operations in the Jenkinsfile.
You can intuitively see each [stage (Stage)](https://www.jenkins.io/doc/book/pipeline/#stage) and each [step (Step)] on the pipeline (https://www.jenkins.io/doc/book/pipeline/#steps), so as to realize the pipeline editing experience of what you see is what you get.

## Prerequisites

- You need to create a workspace and a user, who must be invited to the workspace and given the `workspace edit` role. Refer to [Create Workspace](../../../ghippo/user-guide/02Workspace/Workspaces.md), [Users and Roles](../../../ghippo/user-guide/01UserandAccess/User.md).

- Create three credentials that can access the codebase, container registry, and cluster. For more information on creating credentials, please refer to [Credential Management](Credential.md)).

- To create a custom pipeline, please refer to [Create a custom pipeline](createpipelinebyself.md). When creating a custom pipeline, you need to add two string parameters to the build parameters, and these parameters will be used in the image build command. The parameters are described as follows:

| Parameter Type | Parameter Name | Description |
| -------- | -------- | ------------------------------- ------------------ |
| String | registry | container registry address. In this example use `release-ci.daocloud.io` |
| string | project | The project name in the registry. In this example use `demo` |
| string | name | The name of the image. This example uses `http-hello` |

## Canvas description



The graphical editing page includes two areas: **Canvas** and **Stage Settings**.

1. After clicking `+Add Stage`, a serial stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage .

2. After clicking `+ Add Parallel Stage`, a parallel stage will be generated. After clicking, a new stage will be generated, and pipeline steps can be added to this stage. By selecting the step type, you can quickly create the pipeline steps in the current stage .

3. After the stage is created, click `Stage`, and you can use the stage to configure the stage. Support setting the name, agent, trigger condition and steps of the stage.

## Steps

Click on a created custom pipeline. Click `Edit Pipeline` in the upper right corner to enter the graphical editing page.



### Configure global settings

Click on `Global Settings`, select node from the `Type` drop-down list, and select go 16 from the label drop-down list.



### Add stage - pull source code

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: git clone.

2. Click `Add Step`, select `git clone` under the step type in the pop-up dialog box, and refer to the table below to configure the relevant parameters.

     - registry URL: Enter the registry address.
     - Branch: do not fill in, the default is the master branch.
     - Credentials: If your registry is a private registry, you need to provide a credential.

     

### Add Phase - Unit Test

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: unit test.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     

3. Click `Add step to unit test the code and generate a test report`, select shell under the step type in the pop-up dialog box, and enter the following command in the command line, and then click `OK`.

     ```go
     go test -coverprofile=coverage.out
     ```

     

### Add stage - build and push image

1. Click `Add Stage` in the canvas. Set the name in the stage settings on the right: build & push.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     

3. Select to enable `Use Credentials` in the step module, fill in the relevant parameters in the pop-up dialog box, and then click `OK`.

     - Credentials: Select the created docker hub credentials to allow users to access the container registry. Select the created "docker-credential" credential.
     - Password variable: PASS
     - Username variable: USER

     

4. Click `Add Step` to build the code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```go
     go build -o simple-http-server main.go
     ```

5. Click `Add Step` to build a Docker image according to the Dockerfile in the source code, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```docker
     docker build -f Dockerfile . -t $REGISTRY/$PROJECT/$NAME:latest
     ```

6. Click `Add Step` to log in to the container registry and push the image to the container registry. In the pop-up dialog box, select shell under the step type, enter the following command in the command line, and click `OK`.

     ```docker
     docker login $REGISTRY -u $USER -p $PASS
     ```

     

6. Click `Add Step` to push the image to the container registry, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and click `OK`.

     ```docker
     docker push $REGISTRY/$PROJECT/$NAME:latest
     ```

     

!!! note
    
     After the image is updated, the trigger pipeline can also be implemented. For details, please refer to [Trigger Pipeline](./PipelineTrigger.md).

### Add stage - review

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: review.

2. Click `Add Step`, select `Audit` under the step type in the pop-up dialog box, fill in `@admin` in the message field, that is, the `admin` account will be audited when the pipeline runs to this stage, and then Click `OK`.

     

### Add stage - deploy to cluster

1. Click `Add Stage` in the canvas. In the stage settings on the right set the name: deploy.

2. In the step module, select to open `specify container`, fill in the container name: go in the pop-up dialog box, and then click `OK`.

     

3. Select to enable `Use Credentials` in the step module, fill in the relevant parameters in the pop-up dialog box, and then click `OK`.

     - Credentials: Choose a credential of type kubeconfig.

     - kubeconfig variable: If you are using the kubectl apply deployment method, the variable value must be KUBECONFIG.

     

4. Click `Add Step` to perform the cluster deployment operation, select shell under the step type in the pop-up dialog box, enter the following command in the command line, and then click `OK`.

     ```shell
     kubectl apply -f deploy.yaml
     ```

### Run the pipeline

1. Click `Execute Now` on the transaction details page. In the pop-up dialog box, set the three string parameters defined in the prerequisites, and click `OK` to run the pipeline.

     

2. After the operation is successfully started, the page will automatically switch to the pipeline details page, click the record of the currently running pipeline.

3. After entering the pipeline record details page, you can view the running process of the current pipeline. The admin or platform administrator is required to review the pipeline. After the audit is successful, the resources will be deployed to the cluster.

    

### Verify cluster resources

1. If each stage of the pipeline runs successfully, a Docker image is automatically built and pushed to your Docker Hub repository. Eventually, the pipeline will automatically create a stateless load in the project you set up beforehand.

2. Go to the container management platform, click `Workload` under the cluster, and you can see the stateless workload displayed in the list.

     