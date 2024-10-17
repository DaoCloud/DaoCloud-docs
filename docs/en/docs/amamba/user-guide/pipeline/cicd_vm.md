---
MTPE: windsonsea
Date: 2024-07-16
---

# Jenkins Delivers Application to Virtual Machine

This document focuses on how Jenkins can deliver applications to a virtual machine.
The process involves pulling code through the pipeline, testing, compiling,
generating a package (such as a jar file), copying the installation package
to the specified location on the corresponding server via scp or other tools,
and replacing the old version of the package by executing commands or scripts remotely.

## Steps

1. Prepare the image for pipeline execution

    Since the pipeline needs to copy the package to the server where the application is located,
    tools such as `scp`, `ansible`, and `sshpass` are required. However, these tools are not
    installed in the default build image provided by the platform, so manual construction is needed.

    Refer to [Using Custom Toolchain in Jenkins](../../quickstart/jenkins-custom.md)
    for installation instructions.

1. Go to **Workbench** -> **Pipelines** -> **Credentials**, and create a credential of
   **Access Token** for the virtual machine

    <!-- add images later -->

1. Go to **Workbench** -> **Pipelines** -> **Pipelines**, and create a pipeline

    The pipeline steps are: pull code -> code build -> deploy application.
    Below is an example that omits the code build step:

    ```groovy
    pipeline {
      agent {
        kubernetes {
          inheritFrom 'base'
          yaml '''
          spec:
            containers:
            - name: ssh
              image: your-custom-tooling-image
              command: 
              - cat
    '''
          defaultContainer 'ssh'
        }
    
      }  
      stages {
        stage('clone') {
          agent none
          steps {
            container('ssh') {
              git(branch: 'main', credentialsId: 'gitsecret1', url: 'https://gitlab.daocloud.cn/***/***.git')
            }
     
          }
        }
      
      stages {
        stage('build') {
          agent none
          steps {
            container('ssh') {
              sh 'build command'
            }
     
          }
        }
        stage('deploy') {
          agent none
          steps {
            container('base') {
              withCredentials([string(credentialsId:'sshpasswd',variable:'sshpasswd')]) {
                sh '''sshpass -p $sshpasswd ssh  -o StrictHostKeyChecking=no root@10.1.5.53 mv -f /usr/share/nginx/html/* /tmp
    sshpass -p $sshpasswd scp  -r -o StrictHostKeyChecking=no ./* root@10.1.5.53:/usr/share/nginx/html/
    sshpass -p $sshpasswd ssh  -o StrictHostKeyChecking=no root@10.1.5.53 nginx -s reload'''
              }
     
            }
     
          }
        }
     
      }
    }
    ```

1. After successful creation, run the pipeline.
