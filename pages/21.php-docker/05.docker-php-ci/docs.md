---
title: '如何配置一个 Docker 化持续集成的 PHP 开发环境'
---

<!-- reviewed by fiona -->

> 目标：我们将为之前创建的 **[PHP + MySQL](https://github.com/DaoCloud/php-apache-mysql-sample)** 应用编写测试代码和创建持续集成环境。

> 本项目代码维护在 **[DaoCloud/php-apache-mysql-sample](https://github.com/DaoCloud/php-apache-mysql-sample)** 项目中。

### 利用 PHPUnit 编写单元测试（本地）

使用以下命令安装 PHPUnit 4.0：

```bash
composer global require "phpunit/phpunit=~4.0"
```

假设我们的工程包含两个文件，一个源代码文件 `Cal.php` 和一个测试代码文件 `CalTest.php`。

```php
<?php
// Cal.php

class Calculator{
    function add($p1,$p2)
    {
        return $p1+$p2;
    }
}
```

```php
<?php
// CalTest.php

require_once("Cal.php");
class CalTest extends PHPUnit_Framework_TestCase
{
    public $cal;
    function setUp()
    {
        $this->cal = new Calculator();
    }
    function tearDown() {
        unset($this->cal);
    }
    function testadd1()
    {
        $result = $this->cal->add(1,1);
        $this->assertEquals($result,2);
    }
    function testadd2()
    {
        $result = $this->cal->add(100,-50);
        $this->assertTrue($result == 50);
    }
}
```

使用以下命令来启动测试：

```bash
phpunit CalTest
```

### 利用 DaoCloud 配置持续集成环境（云端）

当我们写完测试代码之后，我们需要一个持续集成环境来自动执行测试，报告项目的健康状况。这里我们使用 DaoCloud 云端的持续集成能力来为我们的 **[PHP + MySQL](https://github.com/DaoCloud/php-apache-mysql-sample)** 应用配置持续集成环境。

我们只需要在源代码的根目录放置 `daocloud.yml` 文件便可以接入 DaoCloud 持续集成系统，每一次源代码的变更都会触发一次 DaoCloud 持续集成。关于 `daocloud.yml` 的格式，请参考 **[这里](http://help.daocloud.io/features/continuous-integration/daocloud-yml.html)**。

以下是我们为 **[PHP + MySQL](https://github.com/DaoCloud/php-apache-mysql-sample)** 应用编写的测试代码和 `daocloud.yml`。

```php
<?php
// DBTest.php

require_once("DB.php");
class DBTest extends PHPUnit_Framework_TestCase
{
    public $db;
    function setUp()
    {
        $this->db = new DB();
    }
    function tearDown() {
        unset($this->db);
    }
    function exist($name, $phone) {
        $contacts = $this->db->all();
        foreach ($contacts as $index => $contact) {
            if ($contact['name'] == $name && $contact['phone'] == $phone) {
                return true;
            }
        }
        return false;
    }
    function total() {
        return count($this->db->all());
    }
    function test001()
    {
        $this->db->add("abc", "123");
        $this->assertTrue($this->exist("abc", "123"));
    }
    function test002()
    {
        $pre = $this->total();
        $this->db->add("bcd", "1234");
        $post = $this->total();
        $this->assertTrue($post - $pre == 1);
    }
}
```

```yaml
# daocloud.yml
image: daocloud.io/ci-php:5.5

services:
  - mysql

env:
  - MYSQL_USERNAME = "root"
  - MYSQL_PASSWORD = ""
  - MYSQL_INSTANCE_NAME = "test"

install:
  - docker-php-ext-install pdo_mysql

script:
  - phpunit DBTest
```
