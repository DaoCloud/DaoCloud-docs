# Introduction to Custom Steps

Different organizations have various scenarios when defining pipelines, so the required pipeline steps also vary. The Workbench provides the ability to define custom steps, allowing organizations to quickly develop custom steps that fit their real-world use cases.

## Developing Custom Steps

The development of custom steps is defined through a pure YAML declaration model. You can learn more by referring to the [Custom Step Development Guide](./customize-develop.md).

Additionally, the DCE 5.0 Workbench offers several built-in custom steps for users.

## Creating Custom Steps

1. Go to __Workbench__ -> __Workbench__ -> __Pipelines__ -> __Custom Steps__

2. In the __Custom Steps__, you can see steps from two sources: System Built-in and Platform Defined. The System Built-in steps are provided by the platform.

3. Click the __Create Custom Step__ button to enter the creation page.

4. Fill in the declaration file you have prepared according to the [Custom Step Development Guide](./customize-develop.md) into the editor, and then click __Create__.

   <!-- ![cus-step1](./images/custermize1.jpg) -->

## Enabling and Disabling Custom Steps

Custom steps can be set to either Enabled or Disabled. During development, it is recommended to mark steps that are not yet production-ready as disabled.  
Once a step is fully tested, administrators can mark it as enabled, making it available for use by all members across all workspaces.

## Using Custom Steps

### Configuring Jenkins

The custom plugin feature depends on Jenkins' [Shared Library](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) functionality.  
Therefore, you must first configure the shared library in Jenkins.

Modify Jenkins' Casc configuration to enable it:

1. Click the __≡__ button in the upper left corner to open the navigation bar, select __Container Management__ -> __Cluster List__, find the cluster where Jenkins is installed, and click the cluster name.
2. Navigate to __Configuration & Secrets__ -> __Configurations__, select the namespace __amamba-system__, search for __global-jenkins-casc-config__, and click __Edit YAML__ in the action column.
3. Under the __data__ -> __jenkins.yaml__ -> __unclassified__ field, add the following content:

    ```yaml
    unclassified:
      globalLibraries: # (1)!
        libraries:
          - name: amamba-shared-lib
            defaultVersion: main
            implicit: true # (2)!
            retriever:
              modernSCM:
                libraryPath: ./
                scm:
                  git:
                    remote: https://github.com/amamba-io/amamba-shared-lib.git # (3)!
   ```

    1. This is the shared library configuration.
    2. If set to `true`, this shared library is automatically included in all pipelines, so you __do not__ need to use the `@Library` annotation in the Jenkinsfile.  
       Note that enabling this will slightly increase pipeline execution time. If not needed, set it to `false`.  
       In that case, when a pipeline needs to use custom plugin functionality, you will need to manually add `@Library('amamba-shared-lib@main') _` in the Jenkinsfile.
    3. This is the address of the shared library repository maintained by the workbench. The repository is public.  
       __If your environment has network restrictions, you can clone this repository to your internal Git server and update the URL accordingly.__

### Using Custom Plugins

1. Select a pipeline, enter the details page, and click __Edit Pipeline__.

2. Click __Add Step__, and you will see the list of custom steps. Select one and fill in the required parameters.

    ![cus-step2](./images/custermize2.jpg)

Note the following limitations for custom steps:

- They must run inside a container with Docker or Podman. Therefore, you need to select __Use Container__.
- Since scripts are essentially executed within containers, certain scripts may require special permissions. If the custom step cannot achieve your needs, it is recommended to use the __Execute Shell__ step and write the script manually.

When used, custom plugins will be rendered into Jenkinsfile fragments like this:

```groovy
container("base") {
    amambaCustomStep(
        pluginID: 'printEnv',      // Plugin name
        version: 'v1.0.0',         // Plugin version
        docker: [
            image: 'alpine',       // Image used by the plugin
            shell: '/bin/bash',    // Interpreter
            script: 'env',         // Script to execute inside the container
        ],
        args: [
            key1: 'val',           // Parameters defined in the plugin
            key2: [
                'key3': 'val3'
            ],
            key4: ["val4", "val5"]
        ],
    )
}
```

All parameters in `args` are passed into the plugin as environment variables. You can reference them in the script using `$key1`.  
If the parameter type is key-value (kv), the keys will be joined with an underscore when passed in, for example, `key2_key3=val3`.  
If the parameter is an array, it will be passed in as `["val4", "val5"]`. You will need to handle parsing according to the language you are using.

This means that even if you're not using DAG-based orchestration, you can still use custom plugins in Jenkinsfiles following this standard.  
Just note that when parameter values are of type `string`, use single quotes to avoid issues with environment variable replacement.

### Environment Variables and Credentials

Environment variables and credentials defined in the Jenkinsfile can be read by the plugin. For example:

```groovy
withCredential([usernamePassword(credentialsId: 'my-credential', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    amambaCustomStep(
        pluginID: 'printEnv',
        version: 'v1.0.0',
        docker: [
            image: 'alpine',
            shell: '/bin/bash', // USERNAME and PASSWORD will be available inside the script
            script: 'env',
        ],
        args: [],
    )
}
```

### Pulling Private Images

If the plugin you define uses a private image, follow these steps:

1. In the workbench, create a credential of type "username and password" to store the private registry username and password.
2. Before using the custom step, add a __Use Credentials__ step. Set the username variable as `PLUGIN_REGISTRY_USER` and the password variable as `PLUGIN_REGISTRY_PASSWORD`.

The rendered Jenkinsfile snippet will look like this:

```groovy
withCredential([usernamePassword(credentialsId: 'my-credential', usernameVariable: 'PLUGIN_REGISTRY_USER', passwordVariable: 'PLUGIN_REGISTRY_PASSWORD')]) {
    amambaCustomStep(
        ...
    )
}
```

After that, you will be able to use private images as the base image for your plugin.
