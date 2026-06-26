# Upgrade Notes

This page describes the considerations and precautions when upgrading baize to a new version.

## Upgrading from v0.24.1 (or earlier) to v0.25.1

Baize v0.25.1 refactors the data space dependency component `dataset`. Please follow the steps below to perform a manual upgrade.

Baize v0.25.1 also refactors the scheduling-aware component `kueue`. Please follow the steps below to perform a manual upgrade.

### Upgrade `dataset`

The CRD used by baize changes from **datasets.dataset.baize.io** to **datasets.dataset.baizeai.io**. The following sections explain how to perform a smooth upgrade while preserving existing data.

* Old CRD apiVersion: **datasets.dataset.baize.io**
* New CRD apiVersion: **datasets.dataset.baizeai.io**

#### Breaking Changes Details

1. Both baize and hydra will use the [BaizeAI/dataset](https://github.com/BaizeAI/dataset) project to reconcile datasets.

2. The baize project no longer includes code related to the dataset controller.

3. [BaizeAI/dataset](https://github.com/BaizeAI/dataset) will be deployed as a Helm application in the `dataset-system` namespace.

4. The CRs of `datasets.dataset.baizeai.io` are distinguished by the label with the key **"app.kubernetes.io/part-of"**, indicating whether they are created by baize or hydra.

#### Upgrade Steps

1. Upgrade the baize `apiserver` in the Global cluster. After the upgrade, datasets will temporarily disappear from the UI because the `apiserver` queries the new version of the CR.

2. Stop the **baize-agent-cluster-controller** and **baize-agent-jobset-controller** deployments, and keep **kueue-controller-manager** running.

    !!! note

        Do not upgrade `baize-agent` in worker clusters at this stage to avoid deleting the old CRD.


3. Install the Helm application of [BaizeAI/dataset](https://github.com/BaizeAI/dataset) in the worker cluster. After the installation is complete, stop the only deployment in the **dataset-system** namespace.

4. At this point, two versions of the CRD coexist in the worker cluster. Do not create any new datasets, either through the UI or via API calls.

    ```bash
    kubectl get crd | grep dataset
    datasets.dataset.baize.io                              2026-03-05T07:28:15Z
    datasets.dataset.baizeai.io                            2026-03-05T09:10:29Z
    ```

5. For datasets that support the preheating type (non-PVC and non-NFS datasets), run the following script. The first parameter is the namespace, and the second parameter is the dataset name.

    !!! note

        This script deletes the **dataset-datasetname-round-1** job. If the logs of this job and its corresponding pod are important, save them beforehand.

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

7. After all datasets have been processed using this script, you can upgrade `baize-agent`.

8. After confirming that `baize-agent` has been successfully upgraded, you can delete the old CRs and CRD (depending on your requirements, you may also choose to keep them).

9. Restore the deployment in **dataset-system** and verify that the status of the Data Space entries in the UI is normal.

    !!! note

        If the dataset type is NFS, the script modifies the labels and `ownerReferences` of both the PVC and its corresponding PV. For other dataset types, only the PVC is modified.

### Upgrade `kueue`

Starting from Baize v0.25.1, the `kueue` component is decoupled from `baize-agent` and deployed as a standalone plugin (addon) in the **kueue-system** namespace. The purpose is to allow both baize and hydra to share the same `kueue` component. The following sections describe the upgrade procedure in detail.

1. After upgrading to v0.25.1, execute the following script:

    !!! note

        Ensure that all workloads have been admitted before running this script.

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

2. Navigate to the worker cluster's **Helm Apps** -> **Helm Templates** page, locate the **kueue** addon, and install it.

3. Navigate to the worker cluster's **Helm Apps** -> **Helm Apps** page, locate **baize-agent** , and perform an update.

After completing the preceding steps, the `kueue` component can be used normally.
