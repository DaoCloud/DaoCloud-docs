---
title: '如何构建具有持续交付能力的 Docker 化 Django 应用'
---

<!-- reviewed by fiona -->

> 目标：我们将之前实现的 **Django + MySQL + Redis** 留言板应用，送上云端，轻松实现应用在云端持续交付。
> 
> 本项目代码维护在 **[DaoCloud/python-django-cd-sample](https://github.com/DaoCloud/python-django-cd-sample)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

工欲善其器，必先利其器。首先，你需要 **[DaoCloud 帐号](https://www.daocloud.io/)**。

#### 云端镜像构建

> 比起本地创建，在云端创建会更简单。

- 第一步：在控制台点击「代码构建」。

![](http://help.daocloud.io/img/screenshots/features/build-flows/dashboard.png)

- 第二步：在「代码构建」的界面中点击「创建新项目」。

![](http://help.daocloud.io/img/screenshots/features/build-flows/build-flows-index.png)

- 第三步：为项目指定「项目名称」并设置代码源。

点击「开始创建」后稍等片刻，您的应用便在云端构建成咯。

#### 云端部署镜像

- 第零步：在控制台点击「服务集成」，创建 MySQL 和 Redis 服务
- 第一步：在控制台点击「镜像仓库」。
- 第二步：在「代码构建」的界面中找到需要部署的镜像，点击「部署」。
- 第三步：按照为项目指定「项目名称」，并在 「基础设置」中绑定上 MySQL 和 Redis 服务。

如果没有意外的话，您的应用便在云端航行起来咯！

#### 云端持续集成

首先我们需要编写一些测试代码。

```python
# chat/tests.py
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
class ChatTests(TestCase):
    client_class = Client

    def test(self):
        self.assertEqual(1 + 1, 2)
```

本地环境下可以使用以下命令来启动测试：

```bash
./manage.py test
```

当我们写完测试代码之后，我们需要一个持续集成环境来自动执行测试，报告项目的健康状况。

我们只需要在源代码的根目录放置 `daocloud.yml` 文件便可以接入 DaoCloud 持续集成系统，每一次源代码的变更都会触发一次 DaoCloud 持续集成。关于 `daocloud.yml` 的格式，您可以参考 **[这里](http://help.daocloud.io/features/continuous-integration/daocloud-yml.html)**。

***daocloud.yml***

```yaml
image: daocloud/ci-python:2.7
services:
    - mysql
    - redis

env:
    - DAO_TEST = "True"
    - MYSQL_INSTANCE_NAME = "test"
    - MYSQL_USERNAME = "root"
    - MYSQL_PASSWORD = ""

install:
    - pip install coverage

before_script:
    - pip install -r requirements.txt

script:
    - coverage run --source='.' manage.py test
    - coverage report
```
