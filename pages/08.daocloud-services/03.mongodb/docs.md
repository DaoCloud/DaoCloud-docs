---
title: '使用和管理 Mongo 服务'
taxonomy:
    category:
        - docs
---

![](http://blog.daocloud.io/wp-content/uploads/2015/05/MongoDB.png)

## Mongo Express 是什么？

**Mongo Express** 是使用 Node.js 和 Express 框架实现的轻量级 MongoDB 数据库管理程序，通过它您可以轻松管理您的 MongoDB 数据库。

DaoCloud 平台有大量用户使用 MongoDB 服务，我们在镜像仓库中增加了 Mongo Express 工具，方便用户管理和维护 MongoDB 实例。

> 注意：目前在 DaoCloud 镜像仓库提供的 Mongo Express 版本不支持授权认证，您启动 Mongo Express 容器后，容器的 URL 是公开访问的。所以在您使用完毕后请立即「停止」容器，防止 MongoDB 数据库被他人操作。

## 如何部署 Mongo Express？

### 启动步骤

1. 从最新镜像启动 mongo-express 容器。
2. 绑定一个需要管理的 MongoDB 服务实例，设置服务别名为「MongoDB」（不区分大小写）。
3. 启动容器。

### 具体的创建过程

#### 首先保证存在一个或新建一个需要被管理的 MongoDB 服务实例（如果已有 MongoDB 服务实例，可跳过这个步骤）

1. 在控制台，点击「服务集成」。
2. 在 Dao 服务中，点击 MongoDB。
3. 点击「创建服务实例」。
4. 为服务实例命名，并点击“创建”。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-1.jpg)

#### 接着，我们启动 mongo-express 容器

1. 在控制台，点击「镜像仓库」。
2. 在 DaoCloud 镜像中，点击「mongo-express」图标。
3. 点击「部署新版本」。
4. 为 mongo-express 容器命名。
5. 选择容器配置和运行环境。
6. 点击「服务&环境」。
7. 点击之前创建的 MongoDB 实例，显示「待绑定」。
8. 在环境变量的服务别名中，输入 MongoDB。
9. 点击「立即部署」。
10. 部署完成后，访问返回的 URL，使用 Mongo Express。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-2.jpg)

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-3.jpg)

> 提示：Mongo Express 的使用方式，请参考 NPM 上的 [mongo-express](https://www.npmjs.com/package/mongo-express)


Twig is a quick, optimized template engine for PHP. It is designed from the ground up to make creating templates easier on both the developer and the designer.

Its easy-to-follow syntax and straightforward processes make it a natural fit for anyone familiar with Smarty, Django, or Jinja,  Twig will likely be a very easy transition for you.

We use it for our Grav templates in part because of its flexibility and inherent security. The fact that it is also one of the fastest template engines for PHP out there made choosing it for use in Grav a no brainer.

Twig compiles templates down to plain PHP. This cuts the amount of PHP overhead down to a minimum, resulting in a faster, more streamlined user experience.

It is also a very flexible engine thanks to its *lexer* and *parser*. This enables the developer to create their own custom tags and filters. It also enables it to create its own [domain-specific language](http://en.wikipedia.org/wiki/Domain-specific_language) (DSL).

When it comes to security, Twig doesn't cut any corners. It gives the developer a sandbox mode that enables them to examine any untrusted code. This gives you the ability to use Twig as a template language for applications while giving users the ability to modify the template design.

Basically, it is a powerful engine that gives you control over the user interface. When combined with YAML for configuration, it makes for a powerful and simple system for any developer or site manager to work with.

## How Does Twig Work?

Twig works by taking all the hocus pocus out of template design. Templates are basically just text files that contain *variables* or *expressions* that are replaced by values as the template is evaluated.

*Tags* are also an important part of a template file, as these control the logic of the template itself.

Twig has two primary language constraints.

* `{{ }}` prints the result of an expression evaluation;
* `{% %}` executes statements.

Here is a basic template created using Twig:

``` markup
<!DOCTYPE html>
<html>
    <head>
        <title>All About Cookies</title>
    </head>
    <body>
        My name is {{ name }} and I love cookies.
        My favorite flavors of cookies are:
	<ul>
		{% for cookie in cookies %}
    			<li>{{ cookie.flavor }}</li>
		{% endfor %}
        </ul>

        <h1>Cookies are the best!</h1>
    </body>
</html>
```

In this example, we set the title of the site up as you would with any standard Web page. The difference is that we were able to use simple Twig syntax to present the author's name and create a dynamic list of types of items.

A template is first loaded, then passed through the **lexer** where its source code is tokenized and broken up into small pieces. At this point, the **parser** takes the tokens and turns them into the abstract syntax tree.

Once this is done, the compiler turns this into PHP code that can then be evaluated and displayed to the user.

Twig can also be extended to add additional tags, filters, tests, operators, global variables, and functions. More information about extending Twig can be found in its [official documentation](http://twig.sensiolabs.org/doc/advanced.html).

## Twig Syntax

A Twig template has several key components that help it to understand what it is you would like to do. These include tags, filters, functions, and variables.

Let's take a closer look at these important tools and how they can help you build an incredible template.

### Tags

Tags tell Twig what it needs to do. It allows you to set which code Twig should handle, and which code it should ignore during evaluation.

There are several different kinds of tags, and each has its own specific syntax that sets them apart.

#### Comment Tags

Comment tags (`{# Insert Comment Here #}`) are used to set comments that exist within the Twig template file, but aren't actually seen by the end user. They are removed during evaluation, and are neither parsed nor output.

A good use of these tags is to explain what a specific line of code or command does so that another developer or designer on your team can quickly read and understand.

Here is an example of a comment tag as you would find it in a Twig template file:

```
{# Chocolate Chip Cookies are great! Don't tell anyone! #}
```

#### Output Tags

Output tags (`{{ Insert Output Here }}`) set code that is output directly to the browser. This is where you would put anything you want to appear on the front end.

Here is an example of output tags being used in a Twig template:

```
My name is {{ name }} and I love cookies.
```

The variable `name` has been inserted into this line and will appear to the end user as `My name is Jake and I love cookies.` as `Jake` was the value of the name variable.

#### Action Tags

Action tags are the go-getters of the Twig world. These tags actually do something, as opposed to the others which either pass something along or sit idly in the source code waiting for a designer to read it.

Action tags set variables, loop through arrays, and test conditionals. Your `for` and `if` statements are made using these tags.

This is what an action tag might look like in a Twig template:

```
{% set hour = now | date("G") %}
{% if hour >= 9 and hour < 17 %}
    <p>Time for cookies!</p>
{% else %}
    <p>Time to bake more cookies!</p>
{% endif %}
```

The initial action tag sets the hour as the current hour in a 24-hour clock. That value is then used to gauge whether it is between 9am and 5pm. If it is, `Time for cookies!` is displayed. If it isn't, `Time to bake more cookies!` is displayed, instead.

It is very important that tags not overlap one another. You can't put an output tag inside of an action tag, or vice versa.

### Filters

Filters are useful, especially when you are using the output tags to display data that might not be formatted the way you want it.

Let's say the value of the `name` variable might include unwanted SGML/XML tags. You can filter them out using the code below:

```
{{ name|striptags }}
```

### Functions

Functions can generate content. They are typically followed by arguments, which appear within parenthesis placed directly after the function call. Even if no argument is present, the function will still have a `()` parenthesis placed directly after it.

```
{% if date(cookie.created_at) < date('-2days') %}
    {# Eat it! #}
{% endif %}
```

## Resources

* [Official Twig Documentation](http://twig.sensiolabs.org/documentation)
* [Twig for Template Designers](http://twig.sensiolabs.org/doc/templates.html)
* [Twig for Developers](http://twig.sensiolabs.org/doc/api.html)
* [6 Minute Video Introduction to TWig](http://www.dev-metal.com/6min-video-introduction-twig-php-templating-engine/)
* [Introduction to Twig](http://www.slideshare.net/markstory/introduction-to-twig)
