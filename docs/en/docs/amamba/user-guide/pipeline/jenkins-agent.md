---
MTPE: windsonsea
Date: 2024-07-16
---

# Custom Jenkins Agent

If you need to use a Jenkins Agent with a specific environment, such as a special version of JDK or specific tools, you can achieve this by creating a custom Jenkins Agent. This document describes how to customize a Jenkins Agent in DCE 5.0. The added Agent will be global, meaning all pipelines can use this Agent.

## Configure Jenkins

1. Navigate to __Container Management__ -> __Clusters__ , select the cluster and namespace
   where Jenkins is installed (the default cluster name is kpanda-global-cluster, and the namespace is amamba-system).
2. Select __ConfigMaps and Secrets__ -> __ConfigMaps__, choose the namespace where Jenkins is installed,
    and search for `jenkins-casc-config`.
3. Select __Edit YAML__ , search for `jenkins.clouds.kubernetes.templates`,
   and add the following content (using the addition of maven-jdk11 as an example):

    ```yaml
    - name: "maven-jdk11" # (1)!
      label: "maven-jdk11" # (2)!
      inheritFrom: "maven" # (3)!
      containers:
      - name: "maven" # (4)!
        image: "my-maven-image" # (5)!
    ```

    1. Name of the custom Jenkins Agent
    2. Label for the custom Jenkins Agent. To specify multiple labels, separate them with spaces.
    3. Name of the existing pod template that this custom Jenkins Agent inherits from.
    4. Name of the container specified in the existing pod template that this custom Jenkins Agent inherits from.
    5. Use the custom image.

    !!! note

        You can also add other ConfigMaps related to podTemplate in the containers section.
        Jenkins uses YAML merge, so fields that are not filled in will inherit from the parent template.

4. Save the ConfigMaps. Wait for about a minute, and Jenkins will automatically reload the profile.

## Usage

1. Orchestrate the pipeline through the DAG page

    On the DAG orchestration page, click __Global Settings__, choose **node** as the type,
    and select your custom label.

2. Orchestrate the pipeline through JenkinsFile

    Reference the custom label in the agent section of the JenkinsFile:

    ```groovy
    pipeline {
      agent {
        node {
          label 'maven-jdk11'  // Specify the custom label
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
