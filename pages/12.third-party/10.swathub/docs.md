---
title: 功能测试（SWATHub）
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!-- reviewed by fiona -->

>>>>> 自动化测试平台 [SWATHub](http://swathub.com) 是 DaoCloud 的合作伙伴，他们为各类互联网应用提供了自动化测试的服务。我们推荐 DaoCloud 用户在完成持续集成单元测试等环节后，把应用部署在测试集群之上，运行自动化测试，进一步检验软件质量。以下内容由 SWATHub 提供。

---

>[SWATHub](http://swathub.com) 是云端的自动化测试 SaaS 平台。通过创新的非编码的流程搭建和执行方式，SWATHub 能够帮助团队简单、高效地保障互联网服务的质量。

自动化测试是持续集成过程中至关重要的一个环节，否则系统的质量就无法保证。在高速迭代的开发过程中，完全依赖人工进行功能的验证无疑是天方夜谭。按照经典的「测试金字塔」理论，从底层的单元测试，到模块之间的集成测试，再到基于 UI 的端到端测试，不同层次、不同类型的自动化测试，是互为补充、缺一不可的。

相对于更偏重于开发人员的单元测试和集成测试，SWATHub 为端到端测试，提供了一种非编码的、云端的、多平台并行的实现方式，极大地提升了端到端测试的速度，加快了持续集成中自动化的反馈。特别是，SWATHub 提供了外部调用的[Webhook API](http://swathub.com/docs/#!api.md)，使得第三方应用能够无缝触发自动化测试的执行，并且获取执行状态和结果报告。

>DaoCloud 是业界领先的企业级容器云平台和解决方案提供商，致力于以Docker为代表的容器技术，为企业打造面向下一代互联网应用的交付和运维平台。

目前，DaoCloud 使用自主研发的 CI 执行引擎，支持诸如 Golang、Python、Ruby、Java 等多种语言和 MySQL、Redis、MongoDB 等多种外部服务。DaoCloud 通过解析和执行代码库根目录下的 `daocloud.yml` 文件来完成持续集成。下面这个典型的文件，演示了 DaoCloud CI 如何与 SWATHub 服务进行整合：

1. 设置环境变量。
2. 执行 install 脚本，安装必要支撑软件。
3. 克隆源代码，切换到对应的提交。
4. 执行 before_script 脚本，比如更新测试环境。
5. 执行 script 脚本，依次执行单元、集成和 SWATHub 的端到端（End-to-End）测试。

```
image: daocloud/ci-golang:1.4

services:
    - mysql

env:
    - TESTSERVER = "1.2.3.4"

install:
    - echo "Run scripts to setup a base environment"
    - echo "e.g., apt-get install -y git-core"

before_script:
    - echo "Run scripts to prepare our test environment"
    - echo "e.g., scp php-sample.zip $TESTSERVER | ssh $TESTSERVER 'docker build' | ssh $TESTSERVER 'docker run'"

script:
    - echo "Run unit tests, integration tests and end-to-end tests here"
    - echo "e.g., phpunit test"
    - echo "We use cloud test automation powered by SWATHub.com for end-to-end tests"
    - curl --user support:3641623E61464C31A5D --data-urlencode "platform=Windows + Firefox" -d nodeName=swathub -d nodeType=swathub -d tags=DaoCloud -d isSequential=false -d setID=131 http://cn.swathub.com/api/support/samples/run
```

DaoCloud CI 提供了详细的日志信息，方便调试。如下图所示，持续集成各个步骤都成功执行，并且触发了 SWATHub 上的一个端到端的自动化测试 Job，在 **Windows + Firefox** 的平台上，并发地执行所有的测试用例。相关的测试用例和结果都可以在 SWATHub 网站上找到，只需要注册 SWATHub 用户，登录后即可在共享的 samples 项目中看到。

![](dao_logs.png)

细心的同学可能注意到了，在上述的 `daocloud.yml` 中有个准备测试环境的 before_script，我们是通过将最新的代码 push 到外部测试服务器，然后再通过 Docker 搭建测试环境的。其实，最完美的方法应该是直接利用 DaoCloud 来构建最新的 Docker 镜像，然后部署到DaoCloud 的集群上去，这样就可以直接基于这个集群节点进行自动化测试。这个自动构建并部署的 API 接口已经在开发中，预计很快就可以付诸实现。
