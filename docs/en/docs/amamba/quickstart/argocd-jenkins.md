# CI/CD is realized based on pipeline and GitOps

This paper introduces how to implement CI/CD based on pipeline of application workbench and GitOps function.

## Overall process

<!--![]()screenshots-->

## prerequisite

Based on the overall process, we need to prepare the following information:

1. Prepare two code repositories on gitlab, one as a repository for business code and one as a repository for application configuration files (yaml).

    ```bash
    可以参考 github 中的配置：
   
    业务代码：<https://github.com/jzhupup/dao-2048.git>
    应用配置：<https://github.com/jzhupup/argocd-example-apps.git>
    ```

2. Prepare a Harbor mirror warehouse

3. Prepare the pipeline credentials, named git-credentials, git-app-credentials, and harbor-credentials

## Create pipeline

This example includes the following steps: pull the service code, build an image, and update the application configuration file

After the `更新应用配置文件` step is successfully executed, Argo CD detects the change and triggers the update to synchronize the latest configuration file and deploy it to the cluster.

1. For details about how to create a pipeline, see [创建流水线](../user-guide/pipelines/create/custom.md).

2. After successful creation, select the pipeline operation: `编辑 Jenkinsfile`

    ????? note "The following Jenkinsfile parameters can be updated as required"

        ```yaml
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

## Create continuous deployment applications

1. Import argocd-example-apps repository in Http mode, [参考步骤](../user-guide/gitops/import-repo.md)

2. Create a continuously deployed application

    <!--![]()screenshots-->

3. After the creation is complete, a record is generated, and the synchronization status is displayed `未同步`

    <!--![]()screenshots-->

4. Click Synchronize to complete application deployment

    <!--![]()screenshots-->

## CI/CD is triggered by running the pipeline

1. Select the pipeline created above and click Run Now

    <!--![]()screenshots-->

2. Viewing Run Logs

    <!--![]()screenshots-->

3. After the pipeline runs successfully, verify that the image is uploaded to Harbor and the tag defined in Jenkinsfile is v2.0.

    <!--![]()screenshots-->

4. Continue to verify the continuous deployment application and find that the status is `未同步`. See that Deployment resources are not synchronized and jump to `容器管理` to confirm the current image version.

    <!--![]()screenshots-->

    <!--![]()screenshots-->

5. Click `同步`, wait until the synchronization is successful, view Deployment resources and confirm the current image version.

    <!--![]()screenshots-->

    <!--![]()screenshots-->
