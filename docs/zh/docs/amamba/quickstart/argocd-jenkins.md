# 基于流水线和 GitOps 实现 CI/CD

本文介绍如何基于应用工作台的流水线与 GitOps 功能实现 CI/CD。

## 整体流程

![cd:ci01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci01.png)

## 前提条件

基于整体流程，我们需要准备如下信息：

1. 准备两个代码仓库，其中一个作为存业务代码的仓库，一个作为应用的配置文件（yaml）仓库。

    ```console
    可以参考 GitHub 中的配置：
   
    业务代码：<https://github.com/jzhupup/dao-2048.git>
    应用配置：<https://github.com/jzhupup/argocd-example-apps.git>
    ```

2. 准备一个 Harbor 镜像仓库

3. 准备访问上述三个仓库的凭证。此教程中使用的三个凭证分别命为 git-credentials、git-app-credentials、harbor-credentials

## 创建流水线

此教程主要包含的步骤有：拉取业务代码 -> 构建镜像 -> 更新应用配置文件

当 **更新应用配置文件** 步骤执行成功后，Argo CD 会监测变化，并会触发更新同步最新的配置文件部署到集群中。

1. 创建流水线的步骤可以参考[创建流水线](../user-guide/pipeline/create/custom.md)。

2. 创建成功后，选择该流水线操作： **编辑 Jenkinsfile** 

    ??? note "点击查看流水线 Jenkinsfile 文件，可根据实际需要参数"

        ```groovy
        pipeline {
          agent {
            node {
              label 'maven'
            }
          }
          parameters {
            string(name: 'DOCKER_REPO', defaultValue: 'release-ci.daocloud.io/test-jzh/dao-2048', description: '镜像名称')
            string(name: 'DOCKER_IMAGE_VERSION', defaultValue: 'v2.0', description: '镜像版本')
          }
          stages {
            stage('git clone') {
              agent none
              steps {
                git(branch: 'main', credentialsId: ' git-credentials', url: '<http://172.30.40.32:9980/gitlab-instance-facdd89d/dao-2048.git>')
              }
            }
            stage('docker build & push') {
              agent none
              steps {
                container('maven') {
                  withCredentials([usernamePassword(passwordVariable:'PASS',usernameVariable:'USER',credentialsId:'harbor-credentials')]) {
                    sh 'docker login ${DOCKER_REPO} -u $USER -p $PASS'
                    sh 'docker build -f Dockerfile -t ${DOCKER_REPO}:${DOCKER_IMAGE_VERSION} .'
                    sh 'docker push ${DOCKER_REPO}:${DOCKER_IMAGE_VERSION}'
                  }
                }
              }
            }
            stage('update config') {
              agent none
              steps {
                withCredentials([usernamePassword(passwordVariable:'password',usernameVariable:'username',credentialsId:'git-app-credentials')]) {
                  sh """
                    git config --global user.name "root"
                    git config --global user.email "test@gmail.com"
                    git clone <http://${username}:${password}@172.30.40.32:9980/gitlab-instance-facdd89d/argocd-example-apps.git>                                         
                    cd  ./argocd-example-apps
                    sed -i "s#${DOCKER_REPO}.*#${DOCKER_REPO}:${DOCKER_IMAGE_VERSION}#g" guestbook/dao-2048.yaml
                    git add . && git commit -m "update image"
                    git push <http://${username}:${password}@172.30.40.32:9980/gitlab-instance-facdd89d/argocd-example-apps.git>
                    """
                }
              }
            }
          }
        }
        ```

## 创建持续部署应用

1. 用 Https 方式导入 argocd-example-apps 仓库，[参考步骤](../user-guide/gitops/import-repo.md)。

2. 创建一个 GitOps 应用。

    ![cd:ci02](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci02.png)

3. 创建完成后，会自动生成一条记录，同步状态显示 **未同步** 。

    ![cd:ci03](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci03.png)

4. 点击 **同步** ，完成应用部署。

    ![cd:ci04](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci04.png)

## 运行流水线触发 CI/CD

1. 选择上述创建的流水线，点击 **立即运行** 。

    ![cd:ci05](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci05.png)

2. 查看运行日志。

    ![cd:ci06](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci06.png)

3. 流水线运行成功后，验证镜像是否上传到 Harbor，Jenkinsfile 中定义的 tag 为 v2.0。

    ![cd:ci07](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci07.png)

4. 继续验证持续部署应用，发现处于 **未同步** 状态。看到 Deployment 资源未同步，并跳转到 **容器管理** 模块确认目前镜像版本。

    ![cd:ci08](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci08.png)

    ![cd:ci09](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci09.png)

5. 点击 **同步** ，等待同步成功后，查看 Deployment 资源，确认目前的镜像版本。

    ![cd:ci11](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci11.png)

    ![cd:ci10](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cd:ci10.png)
