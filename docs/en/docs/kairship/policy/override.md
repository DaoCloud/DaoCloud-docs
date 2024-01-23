# Override Policies

The role of Override Policy is to define the configurations delivered to different clusters, which can be different. For example, the addresses of the mirror warehouses corresponding to different clusters are different, so they need to be set in different clusters. The mirroring addresses of the workloads in the server are different. For example, in different environments, different environment variables need to be set. The timing of Override Policy is after the Propagation Policy and before it is actually delivered to the cluster.

Multicloud Management supports Override Policy, supports viewing the list of override policies of the current instance and its associated multicloud resources on the interface, and can create and update the information of override policies through forms and YAML. Override Policy is divided into Namespace Scope and Cluster Scope.

## Create from YAML

Follow the steps below to create an override policy using YAML.


1. After entering a multicloud instance, in the left navigation bar, click __Policy Management__ -> __Override Policies__ , and click the __Create from YAML__ button.

     ![Namespace Scope](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op001.png)

2. On the __Create from YAML__ page, after entering the correct YAML statement, click __OK__ .

     ![Create from YAML](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op002.png)

3. Return to the override policy list, and the newly created one is the first one by default. Click __⋮__ on the right side of the list to edit YAML and perform delete operations.

     !!! note

         If you want to delete an override policy, you need to remove the workload related to the policy first. After the deletion, all the information related to the policy will be deleted. Please operate with caution.

### YAML example

Here is an example YAML for an override policy that you can use with a little modification.

```yaml
kind: OverridePolicy
apiVersion: policy.karmada.io/v1alpha1
metadata:
   name: nginx-op
   namespace: default
   uid: 09f89bc4-c6bf-47b3-81bf-9e494b831aac
   resourceVersion: '856977'
   generation: 1
   creationTimestamp: '2022-09-21T10:30:40Z'
   labels:
     a:b
   annotations:
     shadow.clusterpedia.io/cluster-name:k-kairshiptest
spec:
   resourceSelectors:
     - apiVersion: apps/v1
       kind: Deployment
       namespace: default
       name: nginx
   overriders: {}
```

## Create Override Policy

Follow the steps below to create an override policy.

1. Go to the Namespace Scope menu and click the __Create Override Policy__ button.

2. Enter the form creation page. To create a complete override policy, you need to configure three parts: Basic Settings, Resource Quotas, and Override Policy.

     - Basic Settings: including name, multicloud namespace, labels and annotations. Where Name and Multicloud Namespace are required.

     - Resource Quotas: supports the selection of multicloud resources under the selected multicloud namespace for override configuration, and multicloud resources also support multiple selections.

     - Override Policy: support for adding Image/Command/Args/Plaintext and other Override configurations.

     ![Create OP](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op003.png)

3. After completing the filling, click __OK__ to create successfully. It supports YAML update, form update, and delete operations for an override policy.

### Detailed Override Policy

Next, we will introduce the override policies in detail, which are divided into six types and support adding multiple override configurations:

1. Select ImageOverrider: Override configuration of image.

     1. Select a cluster

         Support Specify Clustes, Specify Regions, and Specify Labels to select the cluster.

         === Specify Clusters: Directly select the specified cluster name

         ![Specify Clusters](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op004.png)

         === Specify Regions: Select clusters by regions, including:

         - provider (a service provider that provides cluster infrastructure)
         - region (area: a collection of availability zones, referring to a specific geographic location where resources can be hosted, such as Beijing, Shanghai, Shenzhen, Chengdu, etc.)
         - zone (Availability zone: is the deployment area within the region, such as Shanghai Availability Zone 1, Shanghai Availability Zone 2·······)
         - Also supports excluding a specified cluster from the selected clusters.

         ![Specify Regions](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op005.png)

         === Specify Labels: Select clusters by labels, support custom labels, and also support exclusion of specified clusters.

         ![Specify Labels](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op006.png)

     2. Override configuration for mirroring the selected clusters

         | Field | Required | Description | Example |
         | :-------- | :--- | :--------------------------------- -------------------------- | :---------------------- -- |
         | Component | is | Image component | Registry, Repository, Tag |
         | Operator | is | the operation on the image | add, remove, replace |
         | Value | No | When the Operator is __add__ or __replace__ , it cannot be empty, and it is empty by default; when the operator is __remove__ , leave it blank. | |

2. When ArgsOverrider is selected: Override configuration of args.

     1. Select a cluster

     2. Override configuration of args for the selected clusters

         | Field | Required | Description | Example |
         | :------------ | :--- | :---------------------------- ------------------------------ | :---------- |
         | ContainerName | is | container name | |
         | Operator | is | the operation to apply on args | add, remove |
         | Value | No | The value to apply to args. When the operator is __add__ , the value is appended to args; when the operator is __remove__ , the value is removed from args; if the value is empty, args remains as it is. | |

3. When CommandOverrider is selected: Run the override configuration of the command.

     1. Select a cluster

     2. Perform override configuration of running commands on selected clusters

         | Field | Required | Description | Example |
         | :------------ | :--- | :---------------------------- ------------------------------ | :------------------ ------------------ |
         | ContainerName | is | container name | |
         | Operator | is | the operation applied to the command | add, remove |
         | Value | No | The value applied to the command. When the operator is __add__ , the value is appended to the command; when the operator is __remove__ , the value is removed from the command; if the value is empty, the command remains as it is. | You can add single or multiple values, use __;__ to divide multiple values |

4. When PlainText is selected: Plaintext override configuration.

     1. Select a cluster

     2. Perform override configuration of running commands on selected clusters

         | Field | Required | Description | Example |
         | :------- | :--- | :---------------------------------- ------------------------- | :------------------- |
         | Path | is | the path to the target field | |
         | Operator | is | the type of operation on the target field | add, remove, replace || Value | No | The value to apply to the target field, when Operator is __remove__ , this field must be empty | |

5. When LabelsOverrider is selected: Label override configuration.

     ![LabelsOverrider](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op007.png)

     1. Select a cluster

     2. Perform override configuration of running labels for the selected clusters

        | Field | Required | Description | Example |
        | :------- | :--- | :----------------- | :--------------- ---- |
        | Key | is | the key of the label | |
        | Operator | is | the type of operation on the target field | add, remove, replace |
        | Value | No | The value of the tag | |

6. When selecting AnnotationsOverrider: Override configuration of annotations.

     ![AnnotationsOverrider](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/op008.png)

     1. Select a cluster

     2. Override configuration of running annotations for selected clusters

        | Field | Required | Description | Example |
        | :------- | :--- | :----------------- | :--------------- ---- |
        | Key | is | the key of the annotation | |
        | Operator | is | the type of operation on the target field | add, remove, replace |
        | Value | No | The value of the annotation | |
