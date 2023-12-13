# 在指定的节点上运行流水线

本文介绍如何在应用工作台中客户的流水线任务在指定的节点上运行。

## 修改配置文件 jenkins-casc-config

1. 前往 __容器管理__ 模块，进入目标集群的详情页面，例如 __kpanda-global-cluster__ 集群。

    ![进入集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node01.png)

2. 在左侧导航点击 __配置与密钥__ -> __配置项__ 。

    ![配置项](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node02.png)

3. 搜索 __jenkins-casc-config__ ，在列表选择 __编辑 YAML__ 。

    ![编辑 YAML](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node03.png)

4. 在 YAML 配置项 __jenkins.yaml__ 中的 __jenkins.cloud.kubernetes.templates__ 位置下为某个具体的
   Agent 添加 __nodeSelector: "ci=base"__ ，点击 __确定__ 保存更改。

    ![添加selector](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node04.png)

## 选择指定的节点添加标签

1. 进入 __容器管理__ 模块，在 __kpanda-global-cluster__ 集群的详情页面，在左侧导航点击 __节点管理__ 。

    ![节点管理](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node05.png)

2. 选择目标的工作节点（例如 demo-dev-worker-03），点击 __修改标签__ 。

    ![修改标签](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node06.png)

3. 添加 __ci=base__ 标签，点击 __确定__ 保存更改。

    ![添加标签](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node07.png)

## 访问 Jenkins Dashbord，重新加载配置

首先需要讲通过 NodePort 方式暴露 Jenkins Dashbord 的访问地址（其他暴露方式根据业务实际情况进行暴露）。

1. 进入 __容器管理__ 模块，在 __kpanda-global-cluster__ 集群页面，在左侧导航栏点击 __容器网络__ -> __服务__ 。

    ![进入服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node08.png)

2. 搜索 __amamba-jenkins__ ，在列表选择 __更新__ 。

    ![更新jenkins](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node09.png)

3. 将访问类型更改为 NodePort，节点端口选择自动生成即可。

    ![更改访问类型](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node10.png)

4. 点击确定，然后返回到详情页面点击链接访问 Jenkins Dashboard。

    ![访问jenkins dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node11.png)

5. 输入账号/密码（默认为 __admin/Admin01__ ），进入到 Jenkins Dashboard 页面。

    ![登录](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node12.png)

6. 在左侧导航栏选择 __Manage Jenkins__ 。

    ![manage jennkins](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node13.png)

7. 点击 __Configuration as Code__ 。

    ![configascode](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node14.png)

8. 在 __Configuration as Code__ 点击 __Reload existing configuration__ 。如果点击后在当前页面没有任何提示，说明配置加载生效。

    ![reload](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node15.png)

## 运行流水线，检查是否在指定的节点上

1. 在 __应用工作台__ 创建一个流水线任务，并编辑 __Jenkinsfile__ 如下：

    ```groovy        
    pipeline {
      agent {
        node {
          label 'base'
        }

      }
      stages {
        stage('Hello') {
          agent none
          steps {
            container('base') {
              echo 'Hello World'
              sh 'sleep 300'
            }

          }
        }

      }
    }
    ```

    !!! note

        需要注意 agent 部分需要选择 label 为 base。因为在配置文件中只为 base 设置了指定节点，
        如果需要为其他的 agent 设置。重复上述操作即可。

2. 点击 __立即执行__ 该流水线，前往 __容器管理__ 查看执行该任务的 Pod 运行的节点。

    ![查看pod节点](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline-node16.png)

3. 可以看到执行该流水任务的 Pod 运行在了预期的 __demo-dev-worker-03__ 节点上。
