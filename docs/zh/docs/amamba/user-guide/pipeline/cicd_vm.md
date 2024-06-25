# Jenkins 发布应用至虚拟机

本文将重点介绍 Jenkins 如何发布应用至虚拟机，思路是通过流水线拉取代码、测试、编译、生成程序包(如 jar 包等)、通过 scp 或其他工具将安装包拷贝到对应服务器的指定位置，通过远程执行命令或脚本等方式替换老版本的程序包运行。

## 操作步骤

1. 准备流水线执行的镜像

    由于流水线中需要将程序包拷贝到应用所在的服务器上，需要使用到 `scp`、`ansible`、`sshpass` 命令工具，但是目前平台提供的默认构建惊喜没有安装，需要手动进行构建。
    
    参考[在 Jenkins 中使用自定义工具链](../../quickstart/jenkins-custom.md)实现安装。

1. 前往`应用工作台` -> `流水线` -> `流水线凭证`，为虚拟机创建 `访问令牌` 类型的凭证

    <!-- add images later -->

1. 前往`应用工作台` -> `流水线` -> `流水线`，创建流水线

    流水线步骤为：拉取代码 -> 代码构建 -> 部署应用程序，以下为一个省略代码构建步骤的示例：

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
              sh 'build commend'
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

1. 创建成功后，运行流水线
