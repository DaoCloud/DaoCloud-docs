# 华为昇腾 NPU 快速使用指南

本节将介绍如何快速使用华为昇腾 NPU 运行推理例。

## 前置条件

1. 安装昇腾 NPU 驱动

    然后能够运行 `npu-smi info` 命令，并且能够正常返回 npu 信息，表示 NPU 驱动与固件已就绪。

    ![昇腾信息](./images/npu-smi-info.png)

2. 安装昇腾 NPU Device Plugin

    NPU Device Plugin 默认安装在 `kube-system` 命名空间下。这是一个 DaemonSet 类型的工作负载，
    可以通过 `kubectl get pod -n kube-system | grep ascend` 命令查看，输出如下：

    ![昇腾 Device Plugin](./images/ascend-device-plugin.png)

    如驱动与 Device Plugin 未安装，请参考昇腾官方文档进行安装：

    1. 例如 Ascend910，参考
      [910 驱动安装文档](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/23.0.RC3/EP/installationguide/Install_87.html)，
      和[其他型号显卡](https://support.huawei.com/enterprise/zh/category/ascend-computing-pid-1557196528909)
    2. [昇腾 NPU Device Plugin](https://www.hiascend.com/document/detail/zh/mindx-dl/50rc3/clusterscheduling/clusterschedulingig/dlug_installation_001.html)

3. 下载昇腾代码库。

    运行以下命令下载昇腾 demo 示例代码库，并且请记住代码存放的位置，后续需要使用。

    ```git
    git clone https://gitee.com/ascend/samples.git
    ```

## 快速使用

本文使用昇腾示例库中的
[AscentCL 图片分类应用](https://gitee.com/ascend/samples/tree/master/inference/modelInference/sampleResnetQuickStart/python)示例。

### 准备基础镜像

此例使用 Ascent-pytorch 基础镜像，可访问[昇腾镜像仓库](https://ascendhub.huawei.com/#/index)获取。

### 准备 yaml

```yaml
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
              huawei.com/Ascend910: 1 # Number of the Ascend 910 Processors.
            limits:
              huawei.com/Ascend910: 1 # The value should be the same as that of requests .
          volumeMounts:
            - name: hiai-driver
              mountPath: /usr/local/Ascend/driver
              readOnly: true
            - name: slog
              mountPath: /var/log/npu/conf/slog/slog.conf
            - name: localtime #The container time must be the same as the host time.
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

以上 yaml 中有一些字段需要根据实际情况进行修改：

1. `atc ... --soc_version=Ascend910` 使用的是 `Ascend910`，请以实际情况为主。
   您可以使用 `npu-smi info` 命令查看显卡型号然后加上 Ascend 前缀即可
2. `samples-path` 以实际情况为准。
3. `resources` 以实际情况为准。

### 部署 Job 并查看结果

使用如下命令创建 Job：

```shell
kubectl apply -f ascend-demo.yaml
```

查看 Pod 运行状态：

![昇腾 Pod 状态](./images/ascend-demo-pod-status.png)

Pod 成功运行后，查看日志结果。在屏幕上的关键提示信息示例如下图，
提示信息中的 label 表示类别标识，conf 表示该分类的最大置信度，class 表示所属类别。这些值可能会根据版本、环境有所不同，请以实际情况为准：

![昇腾 demo 运行结果](./images/ascend-demo-pod-result.png)

结果图片展示：

![昇腾 demo 运行结果图片](./images/ascend-demo-infer-result.png)
