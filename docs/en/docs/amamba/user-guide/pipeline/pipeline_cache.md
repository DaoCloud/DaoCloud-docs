---
hide:
  - toc
---

# Pipeline Buffer

Workbench v0.32.0 supports the cache feature of Jenkins pipelines. Since resources such as SC and PVC
need to be configured for the pipeline, the Workbench administrator must enable the pipeline before it
can be used.

## Administrator Enables Pipeline Buffer

1. Go to Workbench -> Workbench Management -> Pipeline Settings -> Pipeline Configuration.

2. Click `Go to Configure` to enable the pipeline buffer.

    ![cache1](../../images/cache1.jpg)

3. Fill in the relevant parameters. The purpose is to configure the backend storage class for the platform
   pipeline so that PVC resources can be created later.

    - Jenkins Name: reads the name of the Jenkins instance currently integrated with the platform by default
    - Jenkins Address: reads the address of the Jenkins instance currently integrated with the platform by default
    - Jenkins Deployment Location: reads the deployment location of the Jenkins instance currently integrated with the platform by default. If no deployment location is set, the pipeline buffer cannot be enabled
    - Storage Pool: select the storage class provided by the cluster where Jenkins is located
    - Default Capacity: the default capacity value when configuring the cache in the pipeline
    - Capacity Limit: the maximum capacity value that can be set when configuring the cache in the pipeline
    - Access Mode: supports ReadWriteOnce, ReadWriteMany, ReadOnlyMany, ReadWriteOncePod
    - Default Mount Path: the default value of the directory to which the data volume is mounted when configuring the cache in the pipeline

    ![cache2](../../images/cache2.jpg)

4. After the configuration is complete, go to the pipeline to enable the cache for a single pipeline.

    ![cache3](../../images/cache3.jpg)

## Enable Buffer for a Pipeline

1. On the Workbench -> Pipelines page, select a pipeline and click the name of the pipeline.

2. On the pipeline details page, click `Edit Pipeline` in the upper right corner to enter the graphical
   editing page, and click `Cache Configuration`.

    ![cache4](../../images/cache4.jpg)

3. Enable the cache capability for the current pipeline, and configure the relevant parameters.

    - Access Mode: supports ReadWriteOnce, ReadWriteMany, ReadOnlyMany, ReadWriteOncePod
    - Capacity: must not be higher than the maximum value set by the administrator
    - Cache Directory: the mount path. Mount the data volume in a directory of the container for caching data

    ![cache4](../../images/cache5.jpg)

4. After the configuration is successful, a PVC resource will be created for the current pipeline. Note that
   a second update is not supported for now.

## Use Buffer in a Pipeline

!!! note

    Note: after the pipeline buffer is enabled, you need to set the Agent type to Kubernetes. Other types are not supported for now!

1. On the pipeline details page, click `Edit Pipeline` in the upper right corner to enter the graphical
   editing page, and click `Agent Settings`.

    ![cache5](../../images/cache6.jpg)

2. Select `Kubernetes` as the type, and enable `Enable Cache`.

    ![cache6](../../images/cache7.jpg)

3. After configuring the container image of the Agent, you can use the cache capability in the pipeline.

    ![cache8](../../images/cache8.jpg)

## Cache Example

The following example shows that after the cache is enabled, when a pipeline is triggered to build with the
Go language for a non-first time, the cache in the cache directory mounted in the container will be used:

```groovy

pipeline {
  agent {
    kubernetes {
      defaultContainer 'base'
      yaml '''apiVersion: v1
kind: Pod
spec:
  containers:
    - name: builder
      image: docker.m.daocloud.io/library/golang:1.22.3
      resources:
        requests:
          cpu: \'0.5\'
          memory: 512Mi
        limits:
          cpu: \'1\'
          memory: 1Gi
      volumeMounts:
        - name: agent-cache-1730346511327
          mountPath: /var/lib/containers
          subPath: container
        - name: agent-cache-1730346511327
          mountPath: /go/pkg
          subPath: gocache
      tty: true
      env:
        - name: GOPROXY
          value: https://goproxy.cn,direct
        - name: GO111MODULE
          value: on
  volumes:
    - name: agent-cache-1730346511327
      persistentVolumeClaim:
        claimName: agent-cache
metadata:
  annotations:
    amamba.io/enable-cache: \'true\'
'''
      inheritFrom 'base'
    }
  }
  stages {
    stage('clone') {
      steps {
        container('base') {
          git(branch: 'main', url: 'https://github.com/amamba-io/amamba-examples.git', credentialsId: '', changelog: true, poll: true)
        }
      }
    }
    stage('build') {
      steps {
        container('builder') {
          sh '''cd guestbook-go/pkg
go mod vendor
CGO_ENABLED=0 GOOS=linux go build -buildvcs=false -o main .'''
        }
      }
    }
  }
}

```
