# Jenkins **Pipeline Syntax**

Jenkins supports **Declarative Pipeline** and **Scripted Pipeline**, with the workspace mainly using **Declarative Pipeline syntax**. Therefore, this article will focus on introducing Jenkins Declarative syntax.

## Overview

Pipeline scripts are based on the Groovy language, but even if you are not familiar with Groovy, you can write basic Pipeline scripts through simple learning. Below is a simplified example of Declarative Pipeline:

```groovy
pipeline {
    agent any // Defines where the Pipeline runs,
              // `any` means it can run on any available agent

    parameters {
        // Set build parameters
    }

    environment { 
        // Set environment variables
    }

    stages { // Define the stages to execute
        stage('Build') { // Build stage
            steps {
                // Define the steps to execute in the build stage
            }
        }
        stage('Test') { // Test stage
            steps {
                // Define the steps to execute in the test stage
            }
        }
        stage('Deploy') { // Deploy stage
            steps {
                // Define the steps to execute in the deploy stage
            }
        }
    }
    
}
```

## Modules

### Agent

The `agent` section specifies where the entire pipeline or specific parts should execute within the Jenkins environment, based on the location in the `agent` section. This section must be defined at the top level of the `pipeline` block, but its usage at the stage level is optional.

Currently, the workspace interface already supports:

- **any**

    Runs the pipeline or stage on any available agent. For example `agent any`

- **none**

    When there is no global agent at the top of the `pipeline` block, this parameter will be assigned to the entire pipeline run, and each `stage` section must include its own `agent` section. For example `agent none`

- **node**

    `agent { node { label 'labelName' } }`, for information about the built-in node in Workbench,
    refer to the document [Using Built-in Labels](../pipeline/config/agent.md)

- **kubernetes**

    Define the Pod template within the `kubernetes { }` block. For example, if you want a Pod containing a podman container internally, you can define it as follows.
    Note: Be sure to define the jnlp container to communicate with the Jenkins service.

    ```groovy
    agent {
        kubernetes {
            defaultContainer 'kaniko'
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                jenkins-pipeline: pipeline-amamba-pod
            spec: 
              containers:
                - name: podman
                  image: release-ci.daocloud.io/amamba/jenkins-agent/builder-base:v0.2.1-podman
                  resources:
                    limits:
                      cpu: 500m
                      memory: 1024Mi
                    requests:
                      cpu: 100m
                      memory: 100Mi
                  securityContext:
                    privileged: true
                  command:
                    - cat
                  tty: true
                - name: jnlp
                  image: release-ci.daocloud.io/amamba/jenkins-agent/inbound-agent:4.10-2
                  resources:
                    limits:
                      cpu: 100m
                      memory: 256Mi
                    requests:
                      cpu: 100m
                      memory: 128Mi
    '''
      }
    ```

### `environment`

The `environment` directive specifies a sequence of key-value pairs that will be defined as environment variables for all steps or specific to stage steps, depending on the location of the `environment` directive within the pipeline. For detailed information, refer to the [Jenkins official documentation](https://www.jenkins.io/doc/book/pipeline/syntax/#environment). Here is a simple example:

```groovy
pipeline {
    agent any
    environment { 
        CC = 'clang'
        // The `environment` directive used in the top-level pipeline block will apply
        // to all steps in the pipeline.
    }
    stages {
        stage('Example') {
            environment {  // The `environment` directive defined in a stage will only apply
                          // the given environment variables to the steps in that stage.
                AN_ACCESS_KEY = credentials('my-prefined-secret-text') 
                // The `environment` block has a helper method `credentials()` defined, which can
                // be used in the Jenkins environment to access pre-defined credentials by identifier.
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
```

#### Using Credentials in the `environment` Section

For credentials of types secret text, username and password, and secret file, you can directly
use them in the pipeline by utilizing the `environment` section. For other types of credentials,
refer to [Handling Credentials](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#handling-credentials).

Usage examples:

- [Using Secret text credentials via `environment`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#secret-text)
- [Using Usernames and passwords credentials via `environment`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#usernames-and-passwords)
- [Using Secret files credentials via `environment`](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#secret-files)

### `parameters`

The `parameters` directive provides a list of parameters that a user should provide when triggering the pipeline. The values of these user-specified parameters can be provided to pipeline steps through the `params` object. For detailed information, refer to the [Jenkins official documentation](https://www.jenkins.io/doc/book/pipeline/syntax/#parameters). Here is a simple example:

```groovy
pipeline {
    agent any
    parameters { 
        
       // Supported parameter types
        
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"

                echo "Biography: ${params.BIOGRAPHY}"

                echo "Toggle: ${params.TOGGLE}"

                echo "Choice: ${params.CHOICE}"

                echo "Password: ${params.PASSWORD}"
            }
        }
    }
}
```

### `stages`

Contains a series of one or more stage directives. The `stages` section is the location where most of the "work" of the pipeline description is performed. It is recommended to include at least one stage directive in the `stages` section for each discrete part of the continuous delivery process, such as build, test, and deploy.

```groovy
pipeline {
    agent any
    stages { 
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

### `steps`

The `steps` section defines a series of one or more steps to be executed within the given `stage` directive.

```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps { // The `steps` section must include one or more steps.
                echo 'Hello World'
            }
        }
    }
}
```

The above only describes some aspects of Declarative Pipeline. For more details, refer to the official [Jenkins syntax introduction](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline).
