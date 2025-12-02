# Custom LLM Inference Runtime

*[Hydra]: Codename of the large-model service platform

The current platform’s LLM inference service supports three built-in runtimes: vLLM, SGLang, and Image Generation. To meet more diverse scenario requirements, the platform provides the ability to define custom runtimes. Users may freely define new runtime types based on their business needs and configure startup scripts, runtime parameters, and other related information, enabling more flexible inference service deployments.

You can follow the steps below to configure and use Hydra’s custom runtime feature.

## Add a Custom Runtime to the Global Service Cluster

1. Go to the global service cluster, click **Configuration & Secrets** -> **Configurations**, search for `hydra-runtime-template`, where the `config.yaml` file is used to define runtime templates.

2. Click **Edit YAML** and modify the `config.yaml` file to add a custom runtime.

    The structure corresponding to config.yaml is as follows:

    ```yaml
    templates:
      - runtime: string            # Runtime type in English (e.g., vllm), required
        runtimeZH: string          # Runtime type in Chinese
        podTemplate:               # Pod template definition
          initContainers: []       # Init containers, same as k8s resource definitions
          podSecurityContext: {}   # Pod security context, same as k8s resource definitions
          volumes: []              # Volume definitions, same as k8s resource definitions
          containerTemplate:       # Container template
            commandTemplate:       # Startup command template, array, using Go template syntax
              - ""
            argsTemplate:          # Startup args template, array, using Go template syntax
              - ""
            volumeMounts: []       # Volume mounts, same as k8s resource definitions
            ports: []              # Ports, same as k8s resource definitions
            securityContext: {}    # Container security context, same as k8s resource definitions
    ```

    **Example: Add vllm-cpu runtime template**

    ```yaml
    templates:
      - runtime: vllm-cpu
        runtimeZH: vLLM
        podTemplate:
          containerTemplate:
            commandTemplate:
              - "/bin/bash"
              - "-c"
            argsTemplate:
              - |-
                {{- if .IS_DISTRIBUTED -}}
                  {{- if .IS_LEADER -}}
                    ray start --head --port={{ .RAY_PORT }} && vllm serve {{ .MODEL_PATH }} --served-model-name {{ .MODEL_NAME }} --trust-remote-code --tensor-parallel-size={{ .TP_SIZE }} --pipeline-parallel-size={{ .PP_SIZE }}
                  {{- else -}}
                    ray start --block --address=$(LWS_LEADER_ADDRESS):{{ .RAY_PORT }}
                  {{- end -}}
                {{- else -}}
                  vllm serve {{ .MODEL_PATH }} --served-model-name {{ .MODEL_NAME }} --trust-remote-code {{- if gt .TP_SIZE 1 }} --tensor-parallel-size {{ .TP_SIZE }} {{- end -}}
                {{- end -}}
                {{- if .CUSTOM_ARGS -}} {{ range .CUSTOM_ARGS }} {{ . }} {{- end -}} {{- end -}}
    ```

    **Available Variable Description**

    Set the variables in the template according to your actual needs. Available variables include:

    * RUN_TIME: Runtime type, such as vllm, image-gen, sglang, mindie, etc.
    * MODEL_NAME: Model name, e.g., the `--served-model-name` parameter for vLLM
    * IS_DISTRIBUTED: Whether distributed deployment is enabled
    * MODEL_PATH: Model path, currently fixed as `/data/serving-model`
    * IS_LEADER: Whether this is the leader node in a distributed setup
    * TP_SIZE: Tensor parallel size
    * PP_SIZE: Pipeline parallel size
    * MODEL_ID: Model ID
    * CLUSTER: Deployment cluster
    * NAMESPACE: Deployment namespace
    * MODEL_HOST: Model serving host address, currently fixed at `0.0.0.0`
    * MODEL_PORT: Model serving port, currently fixed at `8000`

    **CUSTOM_ARGS Parameter Description**

    To reduce configuration complexity, parameters configured in the deployment template and in `hydra-agent` will be passed into the template as a single `CUSTOM_ARGS` variable. It is recommended to follow the approach below:

    * Define only the startup command in `commandTemplate`, such as `"/bin/bash -c"`. It will be rendered into the container’s command. Add `{{- if .CUSTOM_ARGS -}} {{ range .CUSTOM_ARGS }} {{ . }} {{- end -}} {{- end -}}` at the end of `argsTemplate` to ensure custom parameters are correctly rendered.
    * If no template is defined, the parameters configured in `model_deployment` and `hydra-agent` will be used as the container's arguments.
    * If `commandTemplate` is not defined, note that `argsTemplate` should be multiple lines rather than a single-line args entry, and args should use **equals signs** to connect values (e.g., `--model={{ .MODEL_PATH }}`).
    * The command uses `/bin/bash -c` because this method requires args to be a single-line string. Therefore, CUSTOM_ARGS must be added to the template.
    * If no command is specified and args is a multi-line array, CUSTOM_ARGS does not need to be added manually; it will be automatically appended during final rendering to avoid argument parsing failures.

## Add Image Information in the Work Cluster

1. Go to the work cluster, click **Configuration & Secrets** -> **Configurations**, search for `hydra-agent`, and add custom runtime image information and compute-capability matching rules in `configmap/deployment_templates`.

2. Click **Edit YAML** and modify the `configmap` file to add image information for the custom runtime.

    **YAML Example**

    ```yaml
    deployment_templates:
    - match_runtimes: [vllm-cpu] # Name of the custom runtime
        match_gpu_types: [cpu]     # Compute capability of the environment
        container_template: 
        image:                   # Custom runtime image
            registry: swr.cn-south-1.myhuaweicloud.com
            repository: ascendhub/mindie
            tag: 2.1.RC1
    ```

## Start Using It

After completing the above steps, the operations administrator can select the custom runtime in the deployment configuration and set up model deployment information.
