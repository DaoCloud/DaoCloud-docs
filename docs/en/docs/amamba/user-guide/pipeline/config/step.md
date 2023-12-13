# Graphical task template parameter description

The following is a description of the parameters of the graphical pipeline task template.

## Git Clone

| parameter | description |
| -------- | ----------------------------------------- ---------------- |
| Code Warehouse | Fill in the address of the remote code warehouse |
| Branch | Fill in which branch you want to build the pipeline based on, the default is __master__ |
| Credentials | For private warehouses, you need to [create credentials](../credential.md) in advance and select the corresponding credentials when using |

## Shell

Choose this template if you want to run shell commands, multiple lines are supported.

## print message

Choose this template if you want to output some messages in the terminal.

## Preserve Artifacts

| parameter | description |
| -------------- | ---------------------------------- ----------------------------- |
| Files for archiving | Use regular expressions to specify the path where the files are expected to be stored, for example: __module/dist/*/.zip__, please separate multiple files with English commas. |

## review

If this step is added, the pipeline runs until the task will be paused, and the creator and @@ can choose to continue or terminate.

| parameter | description |
| ---- | ----------------------------------------------- ---------------- |
| Message | This message will be displayed in the running status of the pipeline, and it is supported to select the person who can be audited by entering @ + user. |

## Use Credentials

Using the credential component is a special step in graphical editing. If enabled, all steps defined in this stage will be nested in the using credential step.

| Type | Description |
| ------------ | ------------------------------------ ------------------------ |
| Username and Password | The following parameters are required:<br /> __Username variable__: The name of the environment variable for username during Pipeline builds. <br />__Password variable__: The name of the environment variable for the password during Pipeline builds. |
|Access Token| The following parameters are required:<br />__Text Variable__: The name of an environment variable that is texted during Pipeline builds. |
| kubeconfig | The following parameters are required:<br /> __kubeconfig variable__: The name of the kubeconfig environment variable during pipeline builds. |

## time out

If the execution time of the current task exceeds the timeout period, the task will be aborted, and the pipeline status will become __failed__.

| parameter | description |
| ---- | ----------------------------------------- |
| time | Set the time for the timeout. |
| Unit | Set the time unit, support seconds, minutes, hours, days |

## SVN

| parameter | description |
| --- | --- |
| Code repository | Fill in the remote svn address, for example __http://svn.apache.org/repos/asf/ant/__ |
| Credentials | For private warehouses, you need to [create credentials](../credential.md) in advance and select the corresponding credentials when using |

## Collect test reports

Collect JUnit test reports, which must be in __xml__ format, and support filling in multiple addresses, separated by commas.

Collect JUnit test reports, which must be in xml format and support multiple addresses, separated by commas.

| parameter | description |
| --- | --- |
| test reports | specify the location of the generated xml report files, eg myproject/target/test-reports/*.xml |