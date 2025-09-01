# 高级参数选项支持

## 全局参数选项支持

如果需要开启全局参数选项支持，需要在 Feature Flags 中开启 `AdminGlobalBuildParameter` 选项。具体操作可参考[特性门控](../../quickstart/feature-gates.md)

然后在 amamba 所在的命名空间下，更新 ConfigMap amamba-config ，指定 Jenkins 的部署名称和 ConfigMap 名称。内容如下：

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: amamba-config
  namespace: amamba-system
data:
  amamba-config.yaml: |
    custom:
      jenkins.configmap.name: amamba-jenkins  // Jenkins 的 ConfigMap 名称
      jenkins.deployment.name: amamba-jenkins   // Jenkins 的部署名称
    generic: {}
```

并且需要更新 Jenkins ConfigMap 中的启动脚本 `apply_config.sh`，添加以下内容：

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: amamba-jenkins
data:
  apply_config.sh: >-
    ...
    cp --no-clobber
    /var/jenkins_config/jenkins.model.JenkinsLocationConfiguration.xml
    /var/jenkins_home; # 如果目标文件已经存在，则不进行移动
    
    # 增加下面2行
    cp -f
    /var/jenkins_config/jp.ikedam.jenkins.plugins.extensible_choice_parameter.ExtensibleChoiceParameterDefinition.xml
    /var/jenkins_home;

    cp -f
    /var/jenkins_config/jp.ikedam.jenkins.plugins.extensible_choice_parameter.GlobalTextareaChoiceListProvider.xml
    /var/jenkins_home;
    # 结束
    mkdir -p /var/jenkins_home/init.groovy.d/;
```

此外，需要在 Jenkins 中安装 Extensible Choice Parameter 插件。可以参考 [Extensible Choice Parameter](https://plugins.jenkins.io/extensible-choice-parameter/)。


## 多选类型参数支持

### 使用

Jenkins 插件 [Extended Choice Parameter](https://plugins.jenkins.io/extended-choice-parameter/) 对于 Choice 类型的构建参数做了很多扩展，支持多选、单选、复选框等多种选择方式。

如果需要开启全局参数选项支持，需要在 Feature Flags 中开启 `PipelineAdvancedParameters` 选项。
具体操作可参考[特性门控](../../quickstart/feature-gates.md)

此外，需要在 Jenkins 中安装 Extended Choice Parameter 插件。可以参考 [Extended Choice Parameter](https://plugins.jenkins.io/extended-choice-parameter/)。

如果希望通过 Webhook 传递多个选项，可以使用 query parameter。

#### 运行

通过 OpenAPI 运行流水线的请求样例如下：

```bash
curl --location 'http://<host>/api/pipeline.amamba.io/v1alpha1/workspaces/<workspace>/pipelines/runs/<pipeline name>' \
--form 'single_select="1"' \
--form 'multi_select="2|3"' \
--form 'multi_select="4"' \
--form 'extensible_choice="b"'
```

通过 Webhook 运行流水线的请求样例如下：

```bash
curl --location 'http://<host>/unsafe/pipeline.amamba.io/v1alpha1/workspace/<workspace>/webhook?token=<token>'
-d '{
  "single_select": "1",
  "multi_select": ["2|3","4"],
  "extensible_choice": "b"
}' 
```

> 注意：Extended Choice Parameter 必须设置默认值，通过 Webhook 触发时才能捕捉到。
