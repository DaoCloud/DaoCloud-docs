# Graphical task template parameter description

The following is a description of the parameters of the graphical pipeline task template.

## Git Clone

| parameter | description |
| -------- | ----------------------------------------- ---------------- |
| codebase | Fill in the address of the remote codebase. |
| Branch | Fill in the code branch you want to be built, the default is master. |
| Credentials | If your remote registry is private, please create credentials in advance and select them when using them. |

## Shell

Choose this template if you want to execute shell commands, multiple lines are supported.

## print message

Choose this template if you need to output some messages in the terminal.

## Preserve Artifacts

| parameter | description |
| -------------- | ---------------------------------- ----------------------------- |
| Files for archiving | Please fill in the regular expression of the expected archive file path, for example: `module/dist/*/.zip`, please separate multiple files with English commas. |

## review

If this step is added, the pipeline runs until the task will be paused, and the creator and @@ can choose to continue or terminate.

| parameter | description |
| ---- | ----------------------------------------------- ---------------- |
| Message | This message will be displayed in the running status of the pipeline, and it is supported to select the person who can be audited by entering @ + user. |

## Use Credentials

Using the credential component is a special step in graphical editing. If enabled, all steps defined in this stage will be nested in the using credential step.

| Type | Description |
| ------------ | ------------------------------------ ------------------------ |
| Username and Password | After selecting the username and password type, you need to fill in the following parameters:<br />Username variable: The name of the environment variable for username during pipeline build. <br />Password variable: The name of the environment variable for the password during Pipeline builds. |
| Access Token | After selecting the type of access token to use, you need to fill in the following parameters:<br />Text variable: The name of the environment variable that is texted during the pipeline build. |
| kubeconfig | After selecting the kubeconfig type, you need to fill in the following parameters:<br />kubeconfig variable: The name of the kubeconfig environment variable during pipeline construction. |

## time out

If the execution time of the current task exceeds the timeout period, the task will be aborted and the pipeline will fail.

| parameter | description |
| ---- | ----------------------------------------- |
| time | Set the time for the timeout. |
| Unit | Set the time unit, support seconds, minutes, hours, days. |