# 升级注意事项

本页说明将 baize 升级到新版本时需要注意的相关事项。

## 从 v0.24.1（或更低版本）升级到 v0.25.1

Baize v0.25.1 重构数据空间依赖的组件 dataset，请参考下述步骤进行手动升级。
Baize v0.25.1 重构调度感知组件 kueue，请参考下述步骤进行手动升级。

### 升级 dataset

baize 使用的 dataset 的 crd 从 **datasets.dataset.baize.io** 变为 **datasets.dataset.baizeai.io**，下文将详细阐述如何平滑升级，保留原有数据的办法。

- 旧版本的 crd 的 apiVersion: **datasets.dataset.baize.io**
- 新版本的 crd 的 apiVersion: **datasets.dataset.baizeai.io**

#### Break change 详情

1. baize 和 hydra 都会使用[BaizeAI/dataset](https://github.com/BaizeAI/dataset)这个项目来处理 dataset 的调谐

2. baize 项目里将不再包含 dataset controller 相关的代码

3. [BaizeAI/dataset](https://github.com/BaizeAI/dataset) 将会以 helm 的方式部署在 dataset-system 命名空间里

4. datasets.dataset.baizeai.io 的 cr 以 **"app.kubernetes.io/part-of"** 为 key 的 label 来区分是由 baize 还是 hydra 创建的

#### 升级步骤

1. 升级 Global 集群的 baize 的 apiserver, 升级后暂时在页面看不到 dataset, 因为 apiserver 查询的是新版本的 cr。

2. 停止运行 **baize-agent-cluster-controller** 和 **baize-agent-jobset-controller** 这两个 deployment, 保留 **kueue-controller-manager**。

    !!! note

        目前不要升级 worker 集群的 baize-agent, 避免旧版的 crd 被删除。

3. 在 worker 集群安装[BaizeAI/dataset](https://github.com/BaizeAI/dataset)的 helm 应用，安装完成后,在 **dataset-system** 命名空间里把唯一的 deployment 停止。

4. 这个时候 worker 集群会有两个版本的 crd 并存的情况, 这个时候不要创建任何新的 dataset, 不论是从页面还是调 API 接口。

    ```bash
    kubectl get crd | grep dataset
    datasets.dataset.baize.io                              2026-03-05T07:28:15Z
    datasets.dataset.baizeai.io                            2026-03-05T09:10:29Z
    ```

5. 如果是支持预热类型的(非 pvc 和 nfs)的 dataset 执行下面的脚本, 第一个参数是命名空间, 第二个参数是 dataset 的名字

    !!! note

        这个脚本会把 **dataset-datasetname-round-1** 的 job 删除, 如果这个 job 和其对应的 pod 的日志有意义的话，先保存。

    ```bash
    #!/bin/bash

    # 检查参数
    if [ $# -ne 2 ]; then
        echo "Usage: $0 <namespace> <dataset-name>"
        echo "Example: $0 default my-dataset"
        exit 1
    fi

    NAMESPACE="$1"
    DATASET_NAME="$2"
    PVC_NAME="$DATASET_NAME"
    JOB_NAME=dataset-"${DATASET_NAME}-round-1"

    echo "Namespace: $NAMESPACE"
    echo "Dataset Name: $DATASET_NAME"
    echo "PVC Name: $PVC_NAME"
    echo "Job Name: $JOB_NAME"
    echo ""

    # ========== 第零步：获取 Dataset 信息并判断类型 ==========
    echo "Step 0: Checking Dataset source type..."
    DATASET_TYPE=$(kubectl get dataset.dataset.baize.io "$DATASET_NAME" -n "$NAMESPACE" -o jsonpath='{.spec.source.type}' 2>/dev/null)

    if [ -z "$DATASET_TYPE" ]; then
        echo "Error: Failed to get dataset source type"
        exit 1
    fi
    echo "Dataset source type: $DATASET_TYPE"

    # 判断是否需要创建 Job
    SKIP_JOB=false
    if [ "$DATASET_TYPE" = "NFS" ] || [ "$DATASET_TYPE" = "PVC" ]; then
        SKIP_JOB=true
        echo "Type is NFS or PVC, will skip Job creation"
    fi
    echo ""

    # ========== 第一步：更新 Dataset ==========
    echo "Step 1: Updating Dataset..."

    # 构建 jq 命令，根据类型决定是否添加 rcloneOp
    if [ "$DATASET_TYPE" = "S3" ] || [ "$DATASET_TYPE" = "HTTP" ]; then
        echo "Type is S3 or HTTP, setting rcloneOp to syncMode"
        kubectl get dataset.dataset.baize.io "$DATASET_NAME" -n "$NAMESPACE" -o json | jq '
          del(
            .metadata.resourceVersion,
            .metadata.uid,
            .metadata.creationTimestamp,
            .metadata.managedFields,
            .metadata.generation,
            .metadata.selfLink
          )
          | .apiVersion="dataset.baizeai.io/v1alpha1"
          | .spec.dataSyncRound=1
          | .status.phase="Ready"
          | .status.inProcessingRound=1
          | .metadata.labels["app.kubernetes.io/part-of"] = "baize"
          | .spec.source.options.syncMode = .spec.source.options.rcloneOp
          | del(.spec.source.options.rcloneOp)
        ' | kubectl apply -f -
    else
        kubectl get dataset.dataset.baize.io "$DATASET_NAME" -n "$NAMESPACE" -o json | jq '
          del(
            .metadata.resourceVersion,
            .metadata.uid,
            .metadata.creationTimestamp,
            .metadata.managedFields,
            .metadata.generation,
            .metadata.selfLink
          )
          | .apiVersion="dataset.baizeai.io/v1alpha1"
          | .spec.dataSyncRound=1
          | .status.phase="Ready"
          | .status.inProcessingRound=1
          | .metadata.labels["app.kubernetes.io/part-of"] = "baize"
        ' | kubectl apply -f -
    fi

    if [ $? -ne 0 ]; then
        echo "Error: Failed to update dataset"
        exit 1
    fi
    echo "Dataset updated successfully"
    echo ""

    # 如果类型为 PVC，只执行完第一步就结束
    if [ "$DATASET_TYPE" = "PVC" ]; then
        echo "Type is PVC, only updating Dataset. Done."
        exit 0
    fi

    # 等待 Dataset 创建完成
    sleep 10

    # ========== 第二步：获取 Dataset 的 UID ==========
    echo "Step 2: Getting Dataset UID..."
    DATASET_UID=$(kubectl get dataset.dataset.baizeai.io "$DATASET_NAME" -n "$NAMESPACE" -o jsonpath='{.metadata.uid}')

    if [ -z "$DATASET_UID" ]; then
        echo "Error: Failed to get dataset UID"
        exit 1
    fi
    echo "Dataset UID: $DATASET_UID"
    echo ""

    # ========== 第三步：更新 PVC ==========
    echo "Step 3: Checking PVC before update..."
    echo "Current PVC ownerReferences:"
    kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o json | jq '.metadata.ownerReferences // "null"'
    echo ""

    echo "Step 3: Updating PVC..."
    kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o json | jq --arg uid "$DATASET_UID" --arg name "$DATASET_NAME" '
      del(.metadata.ownerReferences)
      | .metadata.ownerReferences = [{
          "apiVersion": "dataset.baizeai.io/v1alpha1",
          "kind": "Dataset",
          "name": $name,
          "uid": $uid,
          "controller": true,
          "blockOwnerDeletion": true
        }]
      | .metadata.labels["baize.io/dataset-name"] = $name
      | del(.metadata.labels["dataset.baize.io/name"])
    ' | kubectl replace -f -

    if [ $? -ne 0 ]; then
        echo "Error: Failed to update PVC"
        exit 1
    fi
    echo "PVC updated successfully"
    echo ""

    # ========== 第三步（附加）：如果是 NFS 类型，更新 PV ==========
    if [ "$DATASET_TYPE" = "NFS" ]; then
        echo "Step 3.5: Getting PV name from PVC..."
        PV_NAME=$(kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o jsonpath='{.spec.volumeName}')
        if [ -z "$PV_NAME" ]; then
            echo "Error: Failed to get PV name from PVC"
            exit 1
        fi
        echo "PV Name: $PV_NAME"
        echo ""

        echo "Step 3.5: Updating PV..."
        kubectl get pv "$PV_NAME" -o json | jq --arg uid "$DATASET_UID" --arg name "$DATASET_NAME" '
          del(.metadata.ownerReferences)
          | .metadata.ownerReferences = [{
              "apiVersion": "dataset.baizeai.io/v1alpha1",
              "kind": "Dataset",
              "name": $name,
              "uid": $uid,
              "controller": true,
              "blockOwnerDeletion": true
            }]
          | .metadata.labels["baize.io/dataset-name"] = $name
          | del(.metadata.labels["dataset.baize.io/name"])
        ' | kubectl replace -f -

        if [ $? -ne 0 ]; then
            echo "Error: Failed to update PV"
            exit 1
        fi
        echo "PV updated successfully"
        echo ""
    fi

    # ========== 第四步：创建 Job（条件判断）==========
    if [ "$SKIP_JOB" = true ]; then
        echo "Step 4: Skipping Job creation (type is $DATASET_TYPE)"
    else
        echo "Step 4: Creating Job..."
        kubectl delete job "$JOB_NAME" -n "$NAMESPACE" 2>/dev/null || true
        cat <<-EOF | kubectl apply -f -
	apiVersion: batch/v1
	kind: Job
	metadata:
	  name: $JOB_NAME
	  namespace: $NAMESPACE
	  ownerReferences:
	  - apiVersion: dataset.baizeai.io/v1alpha1
	    kind: Dataset
	    name: $DATASET_NAME
	    uid: $DATASET_UID
	    controller: true
	    blockOwnerDeletion: true
	spec:
	  template:
	    spec:
	      containers:
	      - name: main
	        image: 10.6.178.191:5000/demo/busybox:latest
	        command: ["sh", "-c", "sleep 1"]
	        resources:
	          requests:
	            memory: "16Mi"
	            cpu: "10m"
	          limits:
	            memory: "32Mi"
	            cpu: "50m"
	      restartPolicy: Never
	  backoffLimit: 2
	EOF

        if [ $? -ne 0 ]; then
            echo "Error: Failed to create Job"
            exit 1
        fi
        echo "Job created successfully"
    fi
    echo ""

    # ========== 验证结果 ==========
    echo "=== Verification ==="
    echo "Dataset UID: $(kubectl get dataset "$DATASET_NAME" -n "$NAMESPACE" -o jsonpath='{.metadata.uid}' 2>/dev/null || echo 'N/A')"
    echo "PVC Owner UID: $(kubectl get pvc "$PVC_NAME" -n "$NAMESPACE" -o jsonpath='{.metadata.ownerReferences[0].uid}' 2>/dev/null || echo 'N/A')"
    if [ "$SKIP_JOB" = false ]; then
        echo "Job Status:"
        kubectl get job "$JOB_NAME" -n "$NAMESPACE" 2>/dev/null || echo "Job not found"
    fi
    echo ""
    echo "Success! All resources created/updated."
    ```

7. 所有的 dataset 都用这个脚本执行完成后, 可以升级 baize-agent。
8. 确认 baize-agent 升级完成后, 可以删除旧版的 cr 及 crd(看需求, 也可以留着不删)
9. 恢复 **dataset-system** 里的 deployment, 查看页面上的数据空间里的列表项状态是否正常

    !!! note

        如果类型是 NFS, 脚本会修改 pvc 及 pvc 对应的 pv 的 label 和 ownerReferences, 其他类型只会修改 pvc


### 升级 kueue

从 Baize v0.25.1 版本起，kueue 组件从 baize-agent 中独立出来，作为一个单独的插件(addon)部署在 **kueue-system** 命名空间下。目的是为了让 baize 和 hydra 两个系统能够共享使用 kueue 组件。下文将详细介绍升级操作步骤。

1. 升级到 v0.25.1 版本后，执行以下脚本:

    !!! note

        注意此脚本需要保证所有的 workload 都被 admitted。

    ```bash
    #!/bin/bash
    set -e

    # ==========================================
    # 环境变量配置区 (根据你的实际情况核对)
    # ==========================================
    OLD_NAMESPACE="baize-system"
    OLD_RELEASE="baize-agent"
    NEW_NAMESPACE="kueue-system"
    NEW_RELEASE="kueue"
    BACKUP_DIR="./kueue-migration-backup"
    VISIBILITY_ROLE_NAME="kueue-visibility-server-auth-reader"
    VISIBILITY_ROLE_NAMESPACE="kube-system"

    annotate_release() {
      local resource="$1"

      kubectl annotate "$resource" \
        meta.helm.sh/release-name="$NEW_RELEASE" \
        meta.helm.sh/release-namespace="$NEW_NAMESPACE" \
        --overwrite
    }

    annotate_release_in_namespace() {
      local kind="$1"
      local name="$2"
      local namespace="$3"

      kubectl annotate "$kind" "$name" -n "$namespace" \
        meta.helm.sh/release-name="$NEW_RELEASE" \
        meta.helm.sh/release-namespace="$NEW_NAMESPACE" \
        --overwrite
    }

    annotate_release_ignore_error() {
      local resource="$1"

      kubectl annotate "$resource" \
        meta.helm.sh/release-name="$NEW_RELEASE" \
        meta.helm.sh/release-namespace="$NEW_NAMESPACE" \
        --overwrite 2>/dev/null || true
    }

    annotate_release_in_namespace_ignore_error() {
      local kind="$1"
      local name="$2"
      local namespace="$3"

      kubectl annotate "$kind" "$name" -n "$namespace" \
        meta.helm.sh/release-name="$NEW_RELEASE" \
        meta.helm.sh/release-namespace="$NEW_NAMESPACE" \
        --overwrite 2>/dev/null || true
    }

    annotate_keep_policy() {
      local resource="$1"

      kubectl annotate "$resource" helm.sh/resource-policy=keep --overwrite
    }

    echo "🚀 开始：Kueue 资源所有权转移与旧控制器停机..."

    # 1. 数据备份
    echo "📦 [1/4] 正在备份当前集群中的 Kueue CRD 和实例数据..."
    mkdir -p "$BACKUP_DIR"
    kubectl get crd -o yaml | grep -A 10 "kueue.x-k8s.io" > "$BACKUP_DIR/kueue-crds-backup.yaml" || true
    kubectl get clusterqueue,localqueue,resourceflavor,workload,topology -A -o yaml > "$BACKUP_DIR/kueue-data-backup.yaml" 2>/dev/null || true
    echo "✅ 备份完成，保存在 ${BACKUP_DIR} 目录下。"

    # 2. 转移 CRD 所有权并添加防删保护
    echo "🔀 [2/4] 正在将集群级别 CRD 的 Helm 所有权转移给新 Release (${NEW_RELEASE})..."
    CRDS=$(kubectl get crd -o name | grep 'kueue.x-k8s.io' || true)
    if [ -n "$CRDS" ]; then
      for crd in $CRDS; do
        annotate_release "$crd"
        annotate_keep_policy "$crd"
        echo "  - 已接管: $crd"
      done
    else
      echo "⚠️ 未找到任何 Kueue CRD，请确认集群状态。"
    fi

    # 批量修改 v1beta1 和 v1beta2 的所有权标记
    for version in v1beta1 v1beta2; do
      annotate_release "apiservice/${version}.visibility.kueue.x-k8s.io"
      echo "✅ APIService ${version} 已成功转移所有权"
    done

    # 3. 转移 ClusterRole 和 Binding 所有权
    echo "🔀 [3/4] 正在转移 ClusterRole 和 ClusterRoleBinding 的所有权..."
    ROLES=$(kubectl get clusterrole,clusterrolebinding -o name | grep 'kueue' || true)
    if [ -n "$ROLES" ]; then
      for role in $ROLES; do
        annotate_release "$role"
      done
    fi

    # 4. 控制面平滑静默
    echo "⏸️  [4/4] 正在停止旧的 Kueue 控制器并清理 Webhook..."
    kubectl scale deployment -l app.kubernetes.io/name=kueue -n "$OLD_NAMESPACE" --replicas=0 || echo "⚠️ 未找到旧 Deployment，可能已停止。"
    kubectl delete validatingwebhookconfigurations,mutatingwebhookconfigurations -l app.kubernetes.io/name=kueue --ignore-not-found

    annotate_release_in_namespace rolebinding "$VISIBILITY_ROLE_NAME" "$VISIBILITY_ROLE_NAMESPACE"

    annotate_release_in_namespace_ignore_error role "$VISIBILITY_ROLE_NAME" "$VISIBILITY_ROLE_NAMESPACE"

    # 给所有名字包含 kueue 的 ClusterRole 和 ClusterRoleBinding 加上 keep 策略
    for res in $(kubectl get clusterrole,clusterrolebinding,serviceaccount -o name | grep kueue); do
      annotate_keep_policy "$res"
      echo "🛡️ 已为 $res 添加防删保护"
    done
    echo ""
    echo "🎉 完成！此时集群内的旧控制器已静默，CRD 已安全隔离。"
    echo "👉 现有的 Job 不受影响，但新提交的 Job 会短暂 Pending。"
    echo "请立即执行: kueue的安装与baize-agent的升级。"
    ```

2. 进入工作集群 的 **Helm 应用** -> **Helm 模板** 页面，找到 **kueue** 插件并安装。
3. 进入工作集群的 **Helm 应用** -> **Helm 应用** 页面，找到 **baize-agent** ，执行更新操作。

以上操作完成后，kueue 组件即可正常使用。