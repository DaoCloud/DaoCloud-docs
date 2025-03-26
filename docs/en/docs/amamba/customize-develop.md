# Custom Step Development Guide  

## YAML File Template  

The declaration file is used to define information such as the custom step's name, version, and parameters. To align more closely with cloud-native practices, the plugin definitions in the Application Workbench follow the style of Kubernetes resources. Although they currently do not exist as CRDs, the plugin definition is as follows:  

```yaml
apiVersion: pipeline.amamba.io/v1alpha1
kind: PipelinePlugin
metadata:
  name: deploy-application      # required. Plugin ID; only lowercase letters, numbers, and delimiters ("- _") are allowed.
  labels:
    pipeline.amamba.io/category: build   # Must be one of: others, build, test, security, release, deploy, command, general, repository, quality.
    pipeline.amamba.io/hidden: false     # Whether the plugin is hidden.
    pipeline.amamba.io/version: 1.0.0    # required. Plugin version; must be unique in combination with name.
  annotations:
    pipeline.amamba.io/description: Deploy applications to the Kubernetes cluster   # Plugin description.
    pipeline.amamba.io/versionDescription: Fixed xxx issue  # Plugin version description.
    pipeline.amamba.io/icon: Plugin icon URL              # Icon URL.
spec:
  image: "docker.m.daocloud.io/amambadev/jenkins-agent-base:v0.3.2-podman"  # required. Base image for the plugin. Must be a public image with no login required.
  entrypoint: ""                    # Optional custom entry script, essentially replacing --entrypoint.
  shell: "/bin/bash"
  script: "kubectl apply -f ."      # required. The script to be executed in the container.
  params:                           # required
    - name: namespace               # required. Must be unique.
      sort: 2                       # Display order of the parameter.
      uiType: NamespaceSelector
      type: string
      uiConfig:
        displayName: "Namespace"
        placeholder: "namespace"
        tips: "Namespace where the application will be deployed."
        helper: "Namespace not found? Go to global management to configure."
      validate:
        required: true
        requiredMessage: "Namespace cannot be empty."
        pattern: ^[a-zA-Z0-9_-]+$
        patternMessage: "Namespace can only contain letters, numbers, underscores, and hyphens."
        minLength: 1
        maxLength: 64
        immutable: false               # Whether the parameter is editable.
        default: "my-namespace"        # Default value.
        options:
          - label: Default
            value: default
      env: NAMESPACE                  # If the 'env' field exists, the value will be used as the environment variable key; otherwise, it defaults to the parameter name.
      dependProperties:                # Property dependencies for frontend interaction. For example, the namespace field may depend on the cluster field.
        cluster: cluster
        namespace: namespace
```

## Parameter Description  

| Attribute Name | Meaning | Example |
| -------------- | ------- | ------- |
| name | Parameter name | cluster |
| type | Parameter type | Supported types: string, int, bool, float, array, map |
| env | Corresponding environment variable; defaults to `name` if not provided | CLUSTER_NAME |
| validate | Parameter validation rules | {} |
| uiConfig | UI display options | {} |
| dependProperties | Parameter dependencies for frontend usage | e.g., `namespace` depends on `cluster`; used for frontend interaction |

### Introduction to dependProperties  

Some parameters have dependency relationships. For example, `namespace` depends on `cluster`. For a better UI interaction experience, you can define these dependencies in `dependProperties`. The frontend will dynamically fetch and display data based on `uiType` and `dependProperties`.  

`dependProperties` is a map structure where the key is the parameter name used in the frontend component, and the value is the name of the parameter defined in `params`. Multiple dependencies can be declared.  

#### Dependency Example  

**NamespaceSelector Example:**  

```yaml
params:
  - name: cls                 
    uiType: ClusterSelector
  - name: namespace                 
    uiType: NamespaceSelector
    dependProperties:
      cluster: cls      # Key is used in the frontend; value refers to the parameter defined in params.
```

**WorkloadSelector Example:**  

```yaml
params:
  - name: cls                 
    uiType: ClusterSelector
  - name: namespace                 
    uiType: NamespaceSelector
    dependProperties:  
      cluster: cls
  - name: workloadType
    uiType: Select
  - name: workloadName                 
    uiType: WorkloadSelector    # Cascading dependencies on cluster, namespace, and workloadType.
    dependProperties:  
      cluster: cls
      namespace: namespace   
      workloadType: workloadType  
```

**ContainerSelector Example:**  

```yaml
params:
  - name: cls                 
    uiType: ClusterSelector
  - name: namespace                 
    uiType: NamespaceSelector
    dependProperties:  
      cluster: cls
  - name: workload_type
    uiType: Select
  - name: workloadName                 
    uiType: WorkloadSelector
    dependProperties:  
      cluster: cls
      namespace: namespace   
      workloadType: workload_type 
  - name: containerName
    uiType: ContainerSelector
    dependProperties:
      cluster: cls
      namespace: namespace
      workloadType: workload_type
      workloadName: workloadName
```

### validate (Parameter Validation Rules)  

```yaml
required:  true                 # Required field or not.
requiredMessage: 'Required'      # Prompt when the field is required but not filled in.
pattern: '*'                    # Valid regular expression pattern.
patternMessage: 'Not matched'    # Prompt when the regex doesn't match.
min: 0                          # Minimum value (valid number).
max: 1                          # Maximum value (must be > min).
minLength: 64                   # Minimum length.
maxLength: 64                   # Maximum length.
integer: true                   # Whether the value must be an integer.
immutable: false                # Whether the field is editable (false = editable, true = read-only).
default: 'cluster1'             # Default value.
options:
  - label: 'Cluster 1'          # For dropdown selectors.
    value: 'cluster1'
```

## uiConfig Parameter Description  

`uiConfig` must be a predefined type and is primarily used for display configurations on the UI:  

```yaml
displayName: Display name
helper: Help information (displayed below the input box)
tips: Tooltip (appears when hovering or clicking the “?”)
placeholder: Placeholder text
```

Predefined UI types and their usage scenarios:  

| UI Type | Parameter Type | Description | Dependencies |
| ------- | -------------- | ----------- | ---------------------- |
| Text | string | Large text input field | |
| Shell | string | Shell syntax-highlighted input box | |
| Yaml | string | YAML syntax-highlighted input box | |
| Input | string | Single-line input field | |
| Select | string | Dropdown selector (used with `options`) | |
| Radio | string | Radio button | |
| Switch | bool | Switch toggle | |
| Password | string | Password field (`****`) | |
| Number | int | Numeric input field | |
| ImageInput | string | Image selector | |
| ClusterSelector | string | Cluster selector | |
| NamespaceSelector | string | Namespace selector | Depends on the `cluster` parameter. |
| CredentialSelector | string | Credential selector | |
| WorkloadSelector | string | Workload selector | Depends on `cluster`, `namespace`, and `workloadType` parameters. |
| ContainerSelector | string | Container selector | Depends on `cluster`, `namespace`, `workloadType`, and `workloadName`. |
| Strings | array | Array of strings | |
| Numbers | array | Array of numbers | |
| KV | map | Key-value pair structure (e.g., environment variables) | |
| Ignore | bool | Field will not be displayed | |
| CPUNumber | float | CPU quantity input box | |
| MemoryNumber | float | Memory quantity input box | |
