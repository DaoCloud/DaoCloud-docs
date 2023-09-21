# Network Policies

Network policies in Kubernetes allow you to control network traffic at the IP address or port level (OSI layer 3 or layer 4). The container management module currently supports creating network policies based on Pods or namespaces, using label selectors to specify which traffic can enter or leave Pods with specific labels.

For more details on network policies, refer to the official Kubernetes documentation on [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

## Creating Network Policies

Currently, there are two methods available for creating network policies: YAML and form-based creation. Each method has its advantages and disadvantages, catering to different user needs.

YAML creation requires fewer steps and is more efficient, but it has a higher learning curve as it requires familiarity with configuring network policy YAML files.

Form-based creation is more intuitive and straightforward. Users can simply fill in the corresponding values based on the prompts. However, this method involves more steps.

### YAML Creation

1. In the cluster list, click on the name of the target cluster, then navigate to `Container Network` -> `Network Policies` -> `YAML Creation` in the left navigation bar.


2. In the pop-up dialog, enter or paste the pre-prepared YAML file, then click `OK` at the bottom of the dialog.


### Form-Based Creation

1. In the cluster list, click on the name of the target cluster, then navigate to `Container Network` -> `Network Policies` -> `Create Policy` in the left navigation bar.


2. Fill in the basic information.

    The name and namespace cannot be changed after creation.


3. Fill in the policy configuration.

    The policy configuration includes ingress and egress policies. To establish a successful connection from a source Pod to a target Pod, both the egress policy of the source Pod and the ingress policy of the target Pod need to allow the connection. If either side does not allow the connection, the connection will fail.

    - Ingress Policy: Click on `➕` to begin configuring the policy. Multiple policies can be configured. The effects of multiple network policies are cumulative. Only when all network policies are satisfied simultaneously can a connection be successfully established.

    - Egress Policy

## Viewing Network Policies

1. In the cluster list, click on the name of the target cluster, then navigate to `Container Network` -> `Network Policies`. Click on the name of the network policy.


2. View the basic configuration, associated instances, ingress policies, and egress policies of the policy.


!!! info

    Under the "Associated Instances" tab, you can view instance monitoring, logs, container lists, YAML files, events, and more.


## Updating Network Policies

There are two ways to update network policies. You can either update them through the form or by using a YAML file.

- On the network policy list page, find the policy you want to update, and choose `Update` in the action column on the right to update it via the form. Choose `Edit YAML` to update it using a YAML file.


- Click on the name of the network policy, then choose `Update` in the top right corner of the policy details page to update it via the form. Choose `Edit YAML` to update it using a YAML file.

## Deleting Network Policies

There are two ways to delete network policies. You can delete network policies either through the form or by using a YAML file.

- On the network policy list page, find the policy you want to delete, and choose `Delete` in the action column on the right to delete it via the form. Choose `Edit YAML` to delete it using a YAML file.


- Click on the name of the network policy, then choose `Delete` in the top right corner of the policy details page to delete it via the form. Choose `Edit YAML` to delete it using a YAML file.
