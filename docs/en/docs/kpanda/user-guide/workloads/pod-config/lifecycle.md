# Configure the container lifecycle

Pods follow a predefined lifecycle, starting in the __Pending__ phase and entering the __Running__ state if at least one container in the Pod starts normally. If any container in the Pod ends in a failed state, the state becomes __Failed__ . The following __phase__ field values ​​indicate which phase of the lifecycle a Pod is in.

value | description
:-----|:----------
 __Pending__ <br /> | The Pod has been accepted by the system, but one or more containers have not yet been created or run. This phase includes waiting for the pod to be scheduled and downloading the image over the network.
 __Running__ <br /> (Running) | The Pod has been bound to a node, and all containers in the Pod have been created. At least one container is still running, or in the process of starting or restarting.
 __Succeeded__ <br /> (Success) | All containers in the Pod were successfully terminated and will not be restarted.
 __Failed__ <br /> | All containers in the Pod have terminated, and at least one container terminated due to failure. That is, the container exited with a non-zero status or was terminated by the system.
 __Unknown__ <br /> (Unknown) | The status of the Pod cannot be obtained for some reason, usually due to a communication failure with the host where the Pod resides.

When creating a workload in DCE container management, images are usually used to specify the running environment in the container. By default, when building an image, the __Entrypoint__ and __CMD__ fields can be used to define the commands and parameters to be executed when the container is running. If you need to change the commands and parameters of the container image before starting, after starting, and before stopping, you can override the default commands and parameters in the image by setting the life cycle event commands and parameters of the container.

## Life cycle configuration

Configure the startup command, post-start command, and pre-stop command of the container according to business needs.

| parameter | description | example value |
| :-------- | :------------------------------------- --------------------- | :--------------------------- --------------------- |
| Start command | [Type] Optional<br /> [Meaning] The container will be started according to the start command. | |
| Command after startup | [Type] optional<br />[Meaning] command after container startup<br /> | |
| Command before stopping | [Type] Optional<br /> [Meaning] The command executed by the container after receiving the stop command. Ensure that the services running in the instance can be drained in advance when the instance is upgraded or deleted. | -- |

### start command

Configure the startup command according to the table below.

| parameter | description | example value |
| :------- | :--------------------------------------- -------------------- | :---------- |
| Run command | [Type] Required<br />[Meaning] Enter an executable command, and separate multiple commands with spaces. If the command itself has spaces, you need to add (""). <br />[Meaning] When there are multiple commands, it is recommended to use /bin/sh or other shells to run the command, and pass in all other commands as parameters. | /run/server |
| Running parameters | [Type] Optional<br />[Meaning] Enter the parameters of the control container running command. <br /> | port=8080 |

### Post-start commands

DCE provides two processing types, command line script and HTTP request, to configure post-start commands. You can choose the configuration method that suits you according to the table below.

**Command line script configuration**

| parameter | description | example value |
| :------- | :--------------------------------------- -------------------- | :---------- |
| Run Command | [Type] Optional<br /> [Meaning] Enter an executable command, and separate multiple commands with spaces. If the command itself contains spaces, you need to add (""). <br />[Meaning] When there are multiple commands, it is recommended to use /bin/sh or other shells to run the command, and pass in all other commands as parameters. | /run/server |
| Running parameters | [Type] Optional<br />[Meaning] Enter the parameters of the control container running command. <br /> | port=8080 |

### stop pre-command

DCE provides two processing types, command line script and HTTP request, to configure the pre-stop command. You can choose the configuration method that suits you according to the table below.

**HTTP request configuration**

| parameter | description | example value |
| :------- | :--------------------------------------- -------------------- | :---------- |
| URL Path | [Type] Optional<br /> [Meaning] Requested URL path. <br />[Meaning] When there are multiple commands, it is recommended to use /bin/sh or other shells to run the command, and pass in all other commands as parameters. | /run/server |
| Port | [Type] Required<br />[Meaning] Requested port. <br /> | port=8080 |
| Node Address | [Type] Optional<br /> [Meaning] The requested IP address, the default is the node IP where the container is located. <br /> | -- |