# 华为昇腾NPU快速使用指南


本节将介绍如何快速使用华为昇腾 NPU 运行推理案例。


## 前置条件

1. 安装昇腾 NPU 驱动
2. 安装昇腾 NPU Device plugin
3. 下载 昇腾 samples 代码库

能够运行 npu-smi info 命令，并且能够正常返回 npu 信息，表示 NPU 驱动与固件已就绪

![昇腾信息](./images/npu-smi-info.png)

NPU Device plugin 默认安装在kube-system 命名空间下，是个 daemonset 类型的工作负载，可以通过 `kubectl get pod -n kube-system | grep ascend` 命令查看，如下输出：

![昇腾DevicePlugin](./images/ascend-device-plugin.png)

如驱动与 device plugin 未安装，请参考昇腾官方文档进行安装：

1. 案例中为Ascend910，参考[910驱动安装文档](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/23.0.RC3/EP/installationguide/Install_87.html)，其他型号显卡[参考](https://support.huawei.com/enterprise/zh/category/ascend-computing-pid-1557196528909)
2. [昇腾 NPU Device plugin](https://www.hiascend.com/document/detail/zh/mindx-dl/50rc3/clusterscheduling/clusterschedulingig/dlug_installation_001.html)

下载昇腾 demo 示例代码库，并且请记住代码存放的位置，后续需要使用。

运行`git clone https://gitee.com/ascend/samples.git`

## 快速使用
此案例使用昇腾示例库中的[AscentCL图片分类应用](https://gitee.com/ascend/samples/tree/master/inference/modelInference/sampleResnetQuickStart/python)的示例

### 准备基础镜像

此案例使用 Ascent-pytorch 基础镜像，可访问[昇腾镜像仓库](https://ascendhub.huawei.com/#/index)获取

### 准备yaml

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: resnetinfer1-1-1usoc
spec:
  template:
    spec:
      containers:
      - image: ascendhub.huawei.com/public-ascendhub/ascend-pytorch:23.0.RC2-ubuntu18.04               # Inference image name
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
            huawei.com/Ascend910: 1             # Number of the Ascend 910 Processors.
          limits:
            huawei.com/Ascend910: 1             # The value should be the same as that of requests .
        volumeMounts:
        - name: hiai-driver
          mountPath: /usr/local/Ascend/driver
          readOnly: true
        - name: slog
          mountPath: /var/log/npu/conf/slog/slog.conf
        - name: localtime                       #The container time must be the same as the host time.
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

yaml中有一些字段需要更具实际情况进行修改

1. 脚本中：`atc ...  --soc_version=Ascend910`    示例中使用的是 `Ascend910` 请以实际情况为主，可以使用 `npu-smi info`  命令查看显卡型号然后加上 Ascend 前缀即可
2. `samples-path` 以实际情况为准
3. `resources` 以实际情况为准

### 部署Job 并查看结果

使用如下命令创建 job

```shell
kubectl apply -f ascend-demo.yaml
```

查看 pod 运行状态
![昇腾pod状态](./images/ascend-demo-pod-status.png)

运行成功后，查看日志结果，在屏幕上的关键提示信息示例如下，提示信息中的label表示类别标识、conf表示该分类的最大置信度，class表示所属类别。这些 值可能会根据版本、环境有所不同，请以实际情况为准：
![昇腾demo运行结果](./images/ascend-demo-pod-result.png)

图片结果展示：

![昇腾demo运行结果图片](./images/ascend-demo-infer-result.png)






