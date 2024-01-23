# Configure environment variables

An environment variable refers to a variable set in the container running environment, which is used to add environment flags to Pods or transfer configurations, etc. It supports configuring environment variables for Pods in the form of key-value pairs.

DCE container management adds a graphical interface to configure environment variables for Pods on the basis of native Kubernetes, and supports the following configuration methods:

- **Key-value pair** (Key/Value Pair): Use a custom key-value pair as the environment variable of the container

- **Resource reference** (Resource): Use the fields defined by Container as the value of environment variables, such as the memory limit of the container, the number of copies, etc.

- **Variable/Variable Reference** (Pod Field): Use the Pod field as the value of an environment variable, such as the name of the Pod

- **ConfigMap key value import** (ConfigMap key): Import the value of a key in the ConfigMap as the value of an environment variable

- **Key key value import** (Secret Key): use the data from the Secret to define the value of the environment variable

- **Key Import** (Secret): Import all key values ​​in Secret as environment variables

- **ConfigMap import** (ConfigMap): import all key values ​​in the ConfigMap as environment variables