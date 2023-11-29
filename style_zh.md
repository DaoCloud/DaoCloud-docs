# DaoCloud 写作风格指南

[English Style Guide](./style.md) | 中文

本风格指南适用于 DaoCloud 所有文档。

## 目录

- [图片](#图片)
- [代码和命令](#代码和命令)
- [列表](#列表)
- [表格](#表格)
- [文本](#文本)
- [Makdown 使用提示](#makdown-使用提示)

### 图片

您可以输出一些关于架构、模块、原理、特性描述等方面的图表。

**千言万语不如一张好图**

书籍或网站中的所有图片应该风格一致：

- 显示清晰的文本
- 填写所有参数，不要留空
- 截图不要大片留白
- 最好使用 mermaid 图片，便于翻译和本地化

#### 示例

不佳示例:

![截图](https://github.com/DaoCloud/DaoCloud-docs/blob/main/docs/zh/docs/blogs/images/style02.png?raw=true)

截图清晰，但空白较多。这种情况下，您可以先拖动浏览器边框到合适大小，再截图。

良好示例:

![截图](https://github.com/DaoCloud/DaoCloud-docs/blob/main/docs/zh/docs/blogs/images/style03.png?raw=true)

### 代码和命令

软件产品的用户指南，可以展示代码及其输出，复现实际情境。

**废话连篇不如展示代码**

提供代码片段时，请记住以下几点：

- 显示清晰
- 便于阅读
- 便于复制/粘贴
- 尽可能提供注释
- 突出显示代码标记（c、c++、yaml、java、shell、bash或 go ）

#### 不佳示例

有时须避免使用图片。
例如，一篇长文章中，当您运行一个简单的命令，输出结果呈现在屏幕上。
在这种情况下，您最好直接复制/粘贴屏幕上的文本，而不是截图。错误案例如下：

![截图](https://github.com/DaoCloud/DaoCloud-docs/blob/main/docs/zh/docs/blogs/images/style01.png?raw=true)

如上所示，单一截图难以适应不同的设备和云环境。
并且您的开发、测试和使用环境难以通过截图复现。
一些读者因为看不清图片，无法按照您的截图逐字输入命令！

#### 良好示例 1

运行如下命令以检查当前的 Pod：

```sh
kubectl get pods
```

输出类似于：

```none
NAME                                      READY   STATUS    RESTARTS      AGE
piraeus-cs-controller-6d7c6c9d75-5k2tw    1/1     Running   2 (16d ago)   20d
piraeus-csi-controller-65fbdb58dd-q2fp5   6/6     Running   4 (16d ago)   20d
piraeus-csi-node-6s5tx                    3/3     Running   3 (14d ago)   20d
piraeus-csi-node-7rwcf                    3/3     Running   3 (14d ago)   20d
piraeus-csi-node-q6nn7                    3/3     Running   1 (17d ago)   20d
```

#### 良好示例 2

您需要确保一些 YAML 文件的缩进全部正确，并在开头附上代码符号。
参考 [yaml.org](https://yaml.org/)。

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello
spec:
  template:
    # pod 模板
    spec:
      containers:
        - name: hello
          image: busybox:1.28
          command: ["sh", "-c", 'echo "Hello, Kubernetes!" && sleep 3600']
      restartPolicy: OnFailure
    # pod 模板到此结束
```

### 列表

DCE 5.0 网站使用 Mkdocs 编译和构建，构建列表需要使用 4 个空格。

以下是列表写作提示:

- 列表至少包含两个项目，单一项目不要使用列表。
- 有顺序的步骤，请使用有序列表。
- 没有顺序的功能、优点等，请使用无序列表。

```none
1. 有序列表 1
    - 无序列表 1
        - 下级无序列表 (1)
        - 下级无序列表 (2)
    - 无序列表 2
1. 有序列表 2
    1. 嵌套列表 1
        1. 嵌套列表 (1)
        1. 嵌套列表 (2)
    1. 嵌套列表 2
1. 有序列表 3
```

输出为:

1. 有序列表 1
    - 无序列表 1
        - 下级无序列表 (1)
        - 下级无序列表 (2)
    - 无序列表 2
1. 有序列表 2
    1. 嵌套列表 1
        1. 嵌套列表 (1)
        1. 嵌套列表 (2)
    1. 嵌套列表 2
1. 有序列表 3

参考 [MkDocs 列表](https://squidfunk.github.io/mkdocs-material/reference/lists/#using-unordered-lists)。

### 表格

数据表是为了呈现表格数据。

DCE 文档是使用 markdown 编写的。 不建议使用表格，但很难避免。
使用表格时，表格不能缩进，否则将丢失表格样式。
建议将所有参数表放在一个页面中。

此外，表格可以轻松显示比较，例如：

```none
| 建议                      | 不建议                         |
| --------------------------- | -------------------------------|
| 创建 ReplicaSet，           |为了创建 ReplicaSet，           |
| 查看配置文件。              | 请查看配置文件。                |
| 查看 Pod。                 | 用下面的命令，我们将查看 pods。 |
```

输出为：

| 建议                          | 不建议                                    |
| --------------------------- | -------------------------------------------- |
| 创建 ReplicaSet，            |为了创建 ReplicaSet，|
| 查看配置文件。 | 请查看配置文件。          |
| 查看 Pod。             | 用下面的命令，我们将查看 pods。 |

参考 [MkDocs 表格](https://squidfunk.github.io/mkdocs-material/reference/data-tables/)

### 文本

好的手册可以快速回答用户可能提出的问题。

#### 简单一致

使用技术行话会让读者困惑，阻碍读者找寻答案。
使用客户好理解的语言。使用技术术语时，请解释或链接到词汇表。

为保证文档一致，您编写的主题应清晰易懂，并包含每个步骤所需的重要组件。
保持内容一致，包括但不限于：

- 步骤
- 警告和提示
- 字体
- 大小
- 颜色
- 术语表

#### 示例: 您或我们

用户手册应始终侧重于读者。
编写涉及读者的信息（例如说明）时，请使用**您**和主动语态。

直接与读者交流将：

- 强调信息是为读者而设计的
- 吸引读者阅读文档
- 避免被动语态

缺乏对读者关注的不良示例：

```none
有三个查看编辑器内容的选项。
我们有三个查看编辑器内容的选项。
```

关注读者的良好示例：

```none
您有三个选项来查看编辑器中的内容。
```

这个句子使用了“您”，侧重于读者，并清楚地表明读者是执行动作的人。
您应该在写作中使用“您”，使内容与读者更相关。

### Makdown 使用提示

推送更改的 Markdown 文件之前，建议运行以下命令使您的 Markdown 文件格式更加美观：

```
npx prettier --w 文件名
```

查阅 [prettier 安装文档](https://prettier.io/docs/en/install.html)。

> 注意: 运行 prettier 命令后，您应该手动检查格式和布局，该命令自动将您的 Markdown 调整为标准格式。
