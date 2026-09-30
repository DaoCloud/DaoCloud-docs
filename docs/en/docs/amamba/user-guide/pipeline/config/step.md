# Graphical Task Template Parameters

The following is a description of the parameters of the graphical pipeline task templates.

## Git Clone

| Parameter | Description |
| -------- | -------------------------------------------------------- |
| Code Repository | Fill in the address of the remote code repository |
| Branch | Fill in which branch you want to build the pipeline based on, the default is __master__ |
| Credentials | For a private repository, you need to [create credentials](../credential.md) in advance and select the corresponding credentials when using |

## Shell

If you want to run shell commands, select this template. Multiple lines are supported.

## Print Message

If you want to output some messages in the terminal, select this template.

## Preserve Artifacts

| Parameter | Description |
| -------------- | ------------------------------------------------------------ |
| Files for Archiving | Use regular expressions to specify the path where the files are expected to be stored, for example: __module/dist/*/.zip__. Please separate multiple files with English commas. |

## Review

If this step is added, the pipeline will be paused when it runs to this task, and the creator and the users who are @ mentioned can choose to continue or terminate.

| Parameter | Description |
| ---- | ------------------------------------------------------------ |
| Message | This message will be displayed in the running status of the pipeline. It is supported to select the people who can approve by entering @ + user. |

## Notify

Using the notification step during pipeline execution allows you to send emails to specified people. You need to make sure that a mail server has been configured in __Global Management__ and that the current Jenkins can access it.

| Type | Description |
| ------------ | ------------------------------------------------------------ |
| Recipient Address | The recipient address. Multiple email addresses are separated by commas or spaces |
| Subject | The title of the email |
| Content | The content of the email |

## Use Credentials

Using the credential component is a special step in graphical editing. If it is enabled, all steps defined in this stage will be nested in the using credential step.

| Type | Description |
| ------------ | ------------------------------------------------------------ |
| Username and Password | The following parameters are required:<br /> __Username variable__: The name of the environment variable for the username during pipeline builds.<br /> __Password variable__: The name of the environment variable for the password during pipeline builds. |
| Access Token | The following parameters are required:<br /> __Text Variable__: The name of the text environment variable during pipeline builds. |
| kubeconfig | The following parameters are required:<br /> __kubeconfig variable__: The name of the kubeconfig environment variable during pipeline builds. |

## Timeout

If the execution time of the current task exceeds the timeout period, the task will be aborted, and the pipeline status will become __failed__ .

| Parameter | Description |
| ---- | -------------------------------------- |
| Time | Set the time for the timeout. |
| Unit | Set the time unit. Supports seconds, minutes, hours, and days |

## SVN

| Parameter | Description |
| --- | --- |
| Code Repository | Fill in the remote svn address, for example `http://svn.apache.org/repos/asf/ant/` |
| Credentials | For a private repository, you need to [create credentials](../credential.md) in advance and select the corresponding credentials when using |

## Collect Test Reports

Collect JUnit test reports, which must be in __xml__ format. You can fill in multiple addresses, separated by commas.

| Parameter | Description |
| --- | --- |
| Test Reports | Specify the location of the generated xml report files, for example myproject/target/test-reports/*.xml |

## SonarQube Configuration

If you need to use SonarQube to scan the code in the code repository, select this step. Before using it, make sure you have integrated a SonarQube instance and bound it to the current workspace.

| Parameter | Description |
| -------------- | ------------------------------------------------------------ |
| SonarQube Instance | Select the SonarQube instance bound to the current workspace from the drop-down options |
| Code Language | Since the SonarQube scan commands for different code languages are different, for the Java language, select __maven__; for other languages, select __Other__ |
| Project | The project name corresponding to this scan in SonarQube |
| Scanned Files | The file directory address in the code repository to be scanned |

## Code Quality Gate

This step needs to be used together with the __SonarQube Configuration__ step. After this step is defined, the pipeline execution will be paused, waiting for the SonarQube code scanning analysis to complete and return the quality gate status, so as to determine whether to terminate the current pipeline run.

In addition, in actual use, it needs to be used together with the __Timeout__ step to wait for the return result of the SonarQube code scan, as follows:

```groovy
steps {
    timeout(time: 1, unit: 'HOURS') {
        waitForQualityGate abortPipeline: true
    }
}
```

| Parameter | Description |
| -------------------------- | ------------------------------------------------------------ |
| Wait for the check result to pause the pipeline | Two options are supported: true/false. If it is set to true, the pipeline will be terminated when the quality gate status returned after the SonarQube code scanning analysis is completed is unhealthy |

## update-application (System Built-in Custom Step)

Through the custom step capability, updating the image of a workload under the current tenant is supported.

Note: currently this step requires creating a credential for the target cluster in advance, using that credential in the `Add Credentials` step, and setting the environment variable to `KUBECONFIG` before it can be used.

| Parameter | Description |
| -------------- | ------------------------------------------------------------ |
| Cluster | Select the cluster where the application to be updated is located |
| Namespace | Select the namespace where the application to be updated is located |
| Cluster Credentials | You need to create a kubeconfig-type credential in advance to connect to the cluster |
| Workload Type | Supports Deployment, StatefulSet, and DaemonSet |
| Workload Name | Select the workload to be updated |
| Container Name | Select the container information of the current workload |
| Image Address/Version | Select or enter the image address/version |

## deploy-application (System Built-in Custom Step)

Through the custom step capability, deploying an application is supported. The prerequisite is that you need to prepare a git repository, and the repository contains the manifest file of the application.

Note: currently this step requires creating a credential for the target cluster in advance, using that credential in the `Add Credentials` step, and setting the environment variable to `KUBECONFIG` before it can be used.

| Parameter | Description |
| -------------- | ------------------------------------------------------------ |
| Cluster | Select the cluster where the application to be updated is located |
| Namespace | Select the namespace where the application to be updated is located |
| Cluster Credentials | You need to create a kubeconfig-type credential in advance to connect to the cluster |
| Manifest File Path | The absolute path of the code repository where the manifest file of the application is located |

## docker-build (System Built-in Custom Step)

Through the custom step capability, building and pushing images is supported.

| Parameter | Description |
| ----------------- | ------------------------------------------------------------ |
| image | The image repository address |
| tag | The image tag |
| tags | Also build images of more tags synchronously |
| working directory | The directory where the build task is located |
| dockerfile | The directory where the Dockerfile is located in the source code repository |
| build arguments | Define the build arguments to pass |
| platform | Specify the target platform for building the container image. The default is ` linux/amd64`, and `linux/arm` is also supported |
| no cache | Whether to use the cache. By default, no cache is used |
| disable push | Whether to push after a successful build. By default, the image is pushed |

### Usage

When pushing an image, this step requires a username/password to log in to the image repository, so there are currently the following two ways to use it:

- Credentials + docker build
- Environment variables + docker build

#### Credentials + docker build

1. Create the credential in advance, and use it in the `Add Credentials` step of the pipeline. Set the username variable to `DOCKER_USERNAME` and the password variable to `DOCKER_PASSWORD`.

    ![docker0](../../../images/docker0.jpg)

2. Create the sub-step `docker build` and fill in the relevant parameters.

#### Environment Variables + docker build

Note: this way is not recommended, because the password will be exposed in the pipeline.

1. Add the variables `DOCKER_USERNAME` and `DOCKER_PASSWORD` in the environment variables module of the pipeline and set the corresponding information.

    ![docker1](../../../images/docker1.jpg)

2. Create the step `docker build` and fill in the relevant parameters.
