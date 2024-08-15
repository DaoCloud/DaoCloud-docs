---
MTPE: windsonsea
Date: 2024-07-30
---

# Use Ascend NPU

This section explains how to use Ascend NPU on the DCE 5.0 platform.

## Prerequisites

- The current NPU node has the Ascend driver installed.
- The current NPU node has the Ascend-Docker-Runtime component installed.
- The NPU MindX DL suite is installed on the current cluster.
- No virtualization is performed on the NPU card in the current cluster,
  and it is not occupied by other applications.

Refer to the [Ascend NPU Component Installation Document](ascend_driver_install.md)
to install the basic environment.

## Quick Start

This document uses the [AscentCL Image Classification Application](https://gitee.com/ascend/samples/tree/master/inference/modelInference/sampleResnetQuickStart/python) example from the Ascend sample library.

1. Download the Ascend repository

    Run the following command to download the Ascend demo repository,
    and remember the storage location of the code for subsequent use.

    ```git
    git clone https://gitee.com/ascend/samples.git
    ```

2. Prepare the base image

    This example uses the Ascent-pytorch base image, which can be obtained from the
    [Ascend Container Registry](https://www.hiascend.com/developer/ascendhub).

3. Prepare the YAML file

    ```yaml title="ascend-demo.yaml"
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: resnetinfer1-1-1usoc
    spec:
      template:
        spec:
          containers:
            - image: ascendhub.huawei.com/public-ascendhub/ascend-pytorch:23.0.RC2-ubuntu18.04 # Inference image name
              imagePullPolicy: IfNotPresent
              name: resnet50infer
              securityContext:
                runAsUser: 0
              command:
                - "/bin/bash"
                - "-c"
                - |
                  source /usr/local/Ascend/ascend-toolkit/set_env.sh &&
                  TEMP_DIR=/root/samples_copy_$(date '+%Y%m%d_%H%M%S_%N') &&
                  cp -r /root/samples "$TEMP_DIR" &&
                  cd "$TEMP_DIR"/inference/modelInference/sampleResnetQuickStart/python/model &&
                  wget https://obs-9be7.obs.cn-east-2.myhuaweicloud.com/003_Atc_Models/resnet50/resnet50.onnx &&
                  atc --model=resnet50.onnx --framework=5 --output=resnet50 --input_shape="actual_input_1:1,3,224,224"  --soc_version=Ascend910 &&
                  cd ../data &&
                  wget https://obs-9be7.obs.cn-east-2.myhuaweicloud.com/models/aclsample/dog1_1024_683.jpg &&
                  cd ../scripts &&
                  bash sample_run.sh
              resources:
                requests:
                  huawei.com/Ascend910: 1 # Number of the Ascend 910 Processors
                limits:
                  huawei.com/Ascend910: 1 # The value should be the same as that of requests
              volumeMounts:
                - name: hiai-driver
                  mountPath: /usr/local/Ascend/driver
                  readOnly: true
                - name: slog
                  mountPath: /var/log/npu/conf/slog/slog.conf
                - name: localtime # The container time must be the same as the host time
                  mountPath: /etc/localtime
                - name: dmp
                  mountPath: /var/dmp_daemon
                - name: slogd
                  mountPath: /var/slogd
                - name: hbasic
                  mountPath: /etc/hdcBasic.cfg
                - name: sys-version
                  mountPath: /etc/sys_version.conf
                - name: aicpu
                  mountPath: /usr/lib64/aicpu_kernels
                - name: tfso
                  mountPath: /usr/lib64/libtensorflow.so
                - name: sample-path
                  mountPath: /root/samples
          volumes:
            - name: hiai-driver
              hostPath:
                path: /usr/local/Ascend/driver
            - name: slog
              hostPath:
                path: /var/log/npu/conf/slog/slog.conf
            - name: localtime
              hostPath:
                path: /etc/localtime
            - name: dmp
              hostPath:
                path: /var/dmp_daemon
            - name: slogd
              hostPath:
                path: /var/slogd
            - name: hbasic
              hostPath:
                path: /etc/hdcBasic.cfg
            - name: sys-version
              hostPath:
                path: /etc/sys_version.conf
            - name: aicpu
              hostPath:
                path: /usr/lib64/aicpu_kernels
            - name: tfso
              hostPath:
                path: /usr/lib64/libtensorflow.so
            - name: sample-path
              hostPath:
                path: /root/samples
          restartPolicy: OnFailure
    ```

    Some fields in the above YAML need to be modified according to the actual situation:

    1. __atc ... --soc_version=Ascend910__ uses __Ascend910__, adjust this field depending on
       your actual situation. You can use the __npu-smi info__ command to check the GPU model
       and add the Ascend prefix.
    2. __samples-path__ should be adjusted according to the actual situation.
    3. __resources__ should be adjusted according to the actual situation.

4. Deploy a Job and check its results

    Use the following command to create a Job:

    ```shell
    kubectl apply -f ascend-demo.yaml
    ```

    Check the Pod running status: ![Ascend Pod Status](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/ascend-demo-pod-status.png)

    After the Pod runs successfully, check the log results. The key prompt information on the screen is shown in
    the figure below. The Label indicates the category identifier, Conf indicates the maximum confidence of
    the classification, and Class indicates the belonging category. These values may vary depending on the
    version and environment, so please refer to the actual situation:

    ![Ascend demo running result](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/ascend-demo-pod-result.png)

    Result image display:

    ![Ascend demo running result image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/ascend-demo-infer-result.png)

## UI Usage

1. Confirm whether the cluster has detected the GPU card. Click __Clusters__ -> __Cluster Settings__ -> __Addon Plugins__ ,
   and check whether the proper GPU type is automatically enabled and detected.
   Currently, the cluster will automatically enable __GPU__ and set the __GPU__ type to __Ascend__ .

    ![Cluster Settings](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/cluster-setting-ascend-gpu.jpg)

2. Deploy the workload. Click __Clusters__ -> __Workloads__ , deploy the workload through an image,
   select the type (Ascend), and then configure the number of physical cards used by the application:

    **Number of Physical Cards (huawei.com/Ascend910)** : This indicates how many physical cards
    the current Pod needs to mount. The input value must be an integer and **less than or equal to**
    the number of cards on the host.

    ![Workload Usage](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/workload_ascendgpu_userguide.jpg)

    > If there is an issue with the above configuration, it will result in
    > scheduling failure and resource allocation issues.
