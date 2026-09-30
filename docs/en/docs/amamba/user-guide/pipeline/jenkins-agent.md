---
MTPE: windsonsea
Date: 2024-07-16
---

# Custom Jenkins Agent

If you need to use a Jenkins Agent with a specific environment, such as a special version of JDK or specific tools, you can achieve this by creating a custom Jenkins Agent.
This document describes how to customize a Jenkins Agent in DCE. The Workbench supports both global-scope custom Agents and pipeline-level custom Agents, and you can decide which one to use according to your actual scenario.

For how to build a custom image, refer to [Using a custom toolchain in Jenkins](../../quickstart/jenkins-custom.md#create-a-custom-image).

## Customize a Global-scope Agent

When many pipelines in the current environment all need a specific tool, you can define an Agent at the global scope so that all pipelines can use it.

### Configure Jenkins

1. Go to __Container Management__ -> __Clusters__, and select the cluster and namespace where you installed Jenkins
   (the default cluster name is kpanda-global-cluster, and the namespace is amamba-system).
2. Select __ConfigMaps and Secrets__ -> __ConfigMaps__, select the namespace where Jenkins is installed, and search for the ConfigMap `global-jenkins-casc-config`.
3. Select __Edit YAML__, search for `jenkins.clouds.kubernetes.templates`, and add the following content (taking the addition of maven-jdk11 as an example):

    ```yaml
    - name: "maven-jdk11" # (1)!
      label: "maven-jdk11" # (2)!
      inheritFrom: "maven" # (3)!
      containers:
      - name: "maven" # (4)!
        image: "my-maven-image" # (5)!
    ```

    1. The name of the custom Jenkins Agent
    2. The label of the custom Jenkins Agent. To specify multiple labels, separate them with spaces.
    3. The name of the existing pod template that this custom Jenkins Agent inherits from
    4. The name of the container specified in the existing pod template that this custom Jenkins Agent inherits from. If the name is different, a new container will be added according to the original template
    5. Use the custom image

    !!! note

        You can also add other podTemplate-related configuration items in containers. Jenkins uses YAML merge, so fields that are not filled in are inherited from the parent template.

5. Save the ConfigMap. Wait for about a minute, and Jenkins will automatically reload the configuration. You can also choose to restart the Jenkins instance to load it quickly.

### Usage

1. Orchestrate the pipeline through the DAG page

    On the DAG orchestration page, click __Global Settings__, select **node** as the type, and select your custom label.

2. Orchestrate the pipeline through Jenkinsfile

    Reference the custom label in the agent section of the Jenkinsfile:

    ```groovy
    pipeline {
      agent {
        node {
          label 'maven-jdk11'  # Specify the custom label
        }
      }
      stages {
        stage('print jdk version') {
          steps {
            container('maven') {
              sh '''
              java -version
              '''
            }
          }
        }
      }
    }
    ```

## Customize a Pipeline-level Agent

If only one pipeline in the current environment needs a specific tool, you only need to customize the Agent in that pipeline.

### Use in a Pipeline

1. Select a pipeline, and enter the __Edit Jenkinsfile__ page.

2. Edit it by referring to the following file:

    ```groovy
    pipeline {
      agent {
        kubernetes {
          inheritFrom 'base' # Specify the label of the inherited pod template
          yaml '''
          spec:
            containers:
            - name: mavenjdk11 # Declare the container name
              image: maven:3.8.1-jdk-11 # Define the container image
    '''
        …
        }
    }
      stages {
        stage('print jdk version') {
          steps {
            container('mavenjdk11') { 
              sh '''
              java -version # Check the jdk version of the current environment
              '''
            }
          }
        }
      }
    }
    ```

## FAQ

### When customizing a pipeline-level Agent in a pipeline, how do I inherit the YAML information declared in the parent template by default?

The `yamlMergeStrategy` parameter supports merge() or override(), which is used to control whether the YAML information in the template is overridden or merged with the inherited pod template. The default is override() .

```groovy
pipeline {
  agent {
    kubernetes {
      yamlMergeStrategy merge() // After this strategy is defined, the YAML defined in the base template will be merged
      inheritFrom 'base' // Specify the label of the inherited pod template
      yaml '''
      spec:
        containers:
        - name: mavenjdk11 // Declare the container name
          image: maven:3.8.1-jdk-11 // Define the container image
      '''
    }
  }
  // Other parts of the pipeline can be added here
}
```

### When using the inheritFrom syntax, will the volumeMounts information in the parent template be inherited?

When using the inheritFrom syntax, there are the following two cases:

- If the new container matches a container with the same name in the parent template, all configurations of that container under the parent template will be inherited, including volumeMounts, command, arguments, and so on

- If it does not match a container in the parent template, the volumeMounts information of the parent template will not be inherited, and the container will be added to the pod according to the current definition

### When a pipeline fails, the pod that runs the task is also deleted. How can I extend its lifetime so that I can view the logs of the failed pod?

You can configure the `activeDeadlineSeconds` and `podRetention` parameters of the pipeline so that the pod is deleted only after the specified time.

1. Go to __Container Management__ -> __Clusters__, and select the cluster and namespace where you installed Jenkins (the default cluster name is kpanda-global-cluster, and the namespace is amamba-system).
2. Select __ConfigMaps and Secrets__ -> __ConfigMaps__, select the namespace where Jenkins is installed, and search for the ConfigMap `global-jenkins-casc-config`.
3. Select __Edit YAML__, search for `jenkins.clouds.kubernetes.templates`, and add the above two parameters under each container template:

    ```yaml
    - name: "maven"
      label: "maven" 
      # When it is set to podRetention: onFailure(), the pod will be deleted after the time defined by activeDeadlineSeconds is exceeded
      podRetention: onFailure() 
      activeDeadlineSeconds: 100  # the unit is seconds
      containers:
      - name: "maven" 
        image: "my-maven-image" 
    ```

4. Save the ConfigMap. Wait for about a minute, and Jenkins will automatically reload the configuration. You can also choose to restart the Jenkins instance to load it quickly.
