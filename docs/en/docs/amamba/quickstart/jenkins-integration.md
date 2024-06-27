---
MTPE: windsonsea
date: 2024-06-27
---

# Integrate Jenkins on a Physical/Virtual Machine

## Risks

Since Jenkins is deployed on a physical machine or virtual machine, some Kubernetes (K8s) based functionalities may not be available after integration.

- The application workbench places pipelines in a folder named after the WorkspaceID, which may cause existing pipelines to be undiscoverable and not displayed on the workbench interface.
- All configurations based on casc will become invalid, including SonarQube integration and global email settings.
- If Jenkins is not running using KubernetesCloud, related syntax will become invalid, requiring manual adjustments to the Jenkinsfile.

## Plugins

### Required Plugins

The following dependency plugins will be automatically installed when installing Jenkins:

- [Folders Plugin](https://plugins.jenkins.io/cloudbees-folder)
- [Pipeline: REST API Plugin](https://plugins.jenkins.io/pipeline-rest-api/)
- [Pipeline: Declarative](https://plugins.jenkins.io/pipeline-model-definition/)
- [Pipeline: Declarative Extension Points API](https://plugins.jenkins.io/pipeline-model-extensions)
- [Pipeline: Model API](https://plugins.jenkins.io/pipeline-model-api)
- [Git](https://plugins.jenkins.io/git)
- [Blue Ocean](https://plugins.jenkins.io/blueocean)
- [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger)
- [Sonar(SonarQube Scanner for Jenkins)](https://plugins.jenkins.io/sonar)
- [generic-event](https://plugins.jenkins.io/generic-event)

### Optional Plugins

- [Kubernetes Plugin](https://plugins.jenkins.io/kubernetes): If you want the pipeline to run on a K8s cluster, you need to install this plugin.
- [Docker Plugin](https://plugins.jenkins.io/docker-plugin): If you want the pipeline to run in isolation as a container from the physical machine, you need to install this plugin.
- [Chinese Plugin](https://plugins.jenkins.io/localization-zh-cn): This is a localization plugin provided by the Chinese community.

## Configure Nodes

For preparation work related to physical machine nodes, please refer to [Using Jenkins agents](https://www.jenkins.io/doc/book/using/using-agents/).

## Configure Jenkins

### EventDispatcher

First, ensure that the generic-event plugin is properly installed and enabled.  
Check the amamba-devops-server:

```shell
# Get the svc of amamba-devops-server
kubectl get svc amamba-devops-server -n amamba-system

NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)            AGE
amamba-devops-server   ClusterIP   10.233.45.104   <none>        80/TCP,15090/TCP   230d
```

Ensure that Jenkins can communicate properly with the amamba-devops-server, exposed via NodePort or LB, and then fill the corresponding IP in the host field.

!!! note

    This operation is not very secure, and this service is not suitable for direct exposure.

Fill the address of the amamba-devops-server into the Event Receiver input box in Jenkins system management configuration, as per the following format:

```text
http://<hostIP:Port>/apis/internel.amamba.io/devops/pipeline/v1alpha1/webhooks/jenkins
```

### SonarQube

For SonarQube configuration information, refer to [Jenkins Integration with SonarQube](https://docs.daocloud.io/amamba/user-guide/pipeline/install-jenkins.html#jenkins_2).

## Configure Email

Get the email configuration of Ghippo.

```shell
kubectl get ghippoconfig smtp -n ghippo-system -o yaml
```

Below is a simple example:

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GhippoConfig
metadata:
  labels:
    k8slens-edit-resource-version: v1alpha1
  name: smtp
spec:
  from: test@163.com
  host: smtp.163.com
  password: test
  port: 25
  ssl: false
  starttls: false
  user: test@163.com
```

Configure the email service in Jenkins.  
Go to System Management System Configuration, enter the administrator email address `test@163.com`, set the SMTP email server to `smtp.163.com`, select SMTP authentication and fill in the username and password, set the SMTP port, and go to the user settings page to set the email address to `test@163.com`.
