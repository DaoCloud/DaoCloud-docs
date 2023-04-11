# network strategy

Network Policy (NetworkPolicy) can control network traffic at the IP address or port level (OSI layer 3 or 4). The container management module currently supports the creation of network policies based on Pods or namespaces, and supports label selectors to set which traffic can enter or leave Pods with specific labels.

For more details about network policies, please refer to the official Kubernetes document [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

## Create network policy

Currently, it supports the creation of network policies through YAML and forms. These two methods have their own advantages and disadvantages, and can meet the needs of different users.

There are fewer steps and more efficient creation through YAML, but the threshold requirement is high, and you need to be familiar with the YAML file configuration of network policies.

It is more intuitive and easier to create through the form, just fill in the corresponding values ​​according to the prompts, but the steps are more cumbersome.

### Create with YAML

1. Click the name of the target cluster in the cluster list, and then click `Container Network`->`Network Policy`->`Create with YAML` in the left navigation bar.

    

2. Enter or paste the prepared YAML file in the pop-up box, and click `OK` at the bottom of the pop-up box.

    

### Form Creation

1. Click the name of the target cluster in the cluster list, and then click `Container Network`->`Network Policy`->`Create Policy` in the left navigation bar.

    

2. Fill in the basic information.

    Names and namespaces cannot be changed after creation.

    

3. Fill in the policy configuration.

    Policy configuration is divided into inbound traffic policy and outbound traffic policy. For the source Pod to successfully connect to the target Pod, both the source Pod's outbound policy and the target Pod's inbound policy need to allow the connection. If either side does not allow the connection, it will cause the connection to fail.

    - Incoming traffic policy: Click `➕` to start configuring policies, and multiple policies are supported. The effects of multiple network policies are superimposed on each other. Only when all network policies are satisfied at the same time can a connection be successfully established.

        

    - outbound traffic policy

        

## View network policy

1. Click the name of the target cluster in the cluster list, then click `Container Network`->`Network Policy` in the left navigation bar, and click the name of the network policy.

    

2. View the basic configuration, associated instance information, inbound traffic policy, and outbound traffic policy of the policy.

    

!!! info

    Under the associated instance tab, you can view instance monitoring, logs, container lists, YAML files, events, etc.

    

## Update network policy

There are two ways to update network policies. Supports updating network policies via form or YAML file.

- On the network policy list page, find the policy that needs to be updated, select `Update` under the operation bar on the right to update it through the form, and select `Edit YAML` to update it through YAML.

    

- Click the name of the network policy to enter the details page of the network policy, select `Update` in the upper right corner of the page to update it through the form, and select `Edit YAML` to update it through YAML.

    

## Delete network policy

There are two ways to delete a network policy. Supports updating network policies via form or YAML file.

- On the network policy list page, find the policy that needs to be updated, select `Update` under the operation bar on the right to update it through the form, and select `Edit YAML` to delete it through YAML.

    

- Click on the name of the network policy to enter the details page of the network policy, select `Update` in the upper right corner of the page to update it through the form, and select `Edit YAML` to delete it through YAML.

    