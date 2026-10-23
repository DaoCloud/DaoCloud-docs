# Advanced Parameter Options

## Global Parameter Options

If you need to enable global parameter options, you need to enable the `AdminGlobalBuildParameter`
option in Feature Gates. For detailed operations, refer to [Feature Gates](../../quickstart/feature-gates.md).

Then, in the namespace where amamba is located, update the ConfigMap amamba-config to specify the
deployment name and ConfigMap name of Jenkins. The content is as follows:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: amamba-config
  namespace: amamba-system
data:
  amamba-config.yaml: |
    custom:
      jenkins.configmap.name: amamba-jenkins  // the name of the Jenkins ConfigMap
      jenkins.deployment.name: amamba-jenkins   // the name of the Jenkins Deployment
    generic: {}
```

You also need to update the startup script `apply_config.sh` in the Jenkins ConfigMap by adding the
following content:

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
    /var/jenkins_home; # if the target file already exists, do not move it
    
    # Add the following 2 lines
    cp -f
    /var/jenkins_config/jp.ikedam.jenkins.plugins.extensible_choice_parameter.ExtensibleChoiceParameterDefinition.xml
    /var/jenkins_home;

    cp -f
    /var/jenkins_config/jp.ikedam.jenkins.plugins.extensible_choice_parameter.GlobalTextareaChoiceListProvider.xml
    /var/jenkins_home;
    # End
    mkdir -p /var/jenkins_home/init.groovy.d/;
```

In addition, you need to install the Extensible Choice Parameter plugin in Jenkins. You can refer to
[Extensible Choice Parameter](https://plugins.jenkins.io/extensible-choice-parameter/).


## Multi-select Parameter Options

### Usage

The Jenkins plugin [Extended Choice Parameter](https://plugins.jenkins.io/extended-choice-parameter/)
provides many extensions for Choice-type build parameters, supporting multiple selection, single
selection, checkboxes, and other selection methods.

If you need to enable global parameter options, you need to enable the `PipelineAdvancedParameters`
option in Feature Gates. For detailed operations, refer to [Feature Gates](../../quickstart/feature-gates.md).

In addition, you need to install the Extended Choice Parameter plugin in Jenkins. You can refer to
[Extended Choice Parameter](https://plugins.jenkins.io/extended-choice-parameter/).

If you want to pass multiple options through Webhook, you can use query parameters.

#### Run

A sample request for running a pipeline through OpenAPI is as follows:

```bash
curl --location 'http://<host>/api/pipeline.amamba.io/v1alpha1/workspaces/<workspace>/pipelines/runs/<pipeline name>' \
--form 'single_select="1"' \
--form 'multi_select="2|3"' \
--form 'multi_select="4"' \
--form 'extensible_choice="b"'
```

A sample request for running a pipeline through Webhook is as follows:

```bash
curl --location 'http://<host>/unsafe/pipeline.amamba.io/v1alpha1/workspace/<workspace>/webhook?token=<token>'
-d '{
  "single_select": "1",
  "multi_select": ["2|3","4"],
  "extensible_choice": "b"
}' 
```

> Note: A default value must be set for the Extended Choice Parameter so that it can be captured when triggered through Webhook.
