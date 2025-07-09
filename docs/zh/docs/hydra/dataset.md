# 使用Dataset管理模型文件

Hydra基于BaizeAl/Dataset来管理模型的权重文件，Dataset基于kubernetes的Volume管理持久化的数据，简化了PV/PVC的创建和维护，来支持多种类型作为数据来源，包括：

| DatasetType  | 说明 |
| --- | --- |
| GIT  | 通过git 协议下载 |
| S3  | 文件存储在S3 或S3 协议兼容的对象存储里 |
| PVC  | 通过提前创建的PVC 访问Volume 的数据 |
| NFS  | 通过NFS 协议访问 |
| HTTP  | 通过HTTP 协议下载 |
| CONDA  | 通过Conda 下载python package  |
| REFERENCE  | 通过引用其他的Dataset 来访问对应的数据 |
| HUGGING_FACE | 从Hugging Face 下载对应的模型文件 |
| MODEL_SCOPE | 从Model Scope 下载对应的模型文件 |

并且对于特定类型支持预加载，会创建Job并完成数据的初始化到相应的PV中。

## 自动下载

### 通过HuggingFace和ModelScope

我们已经在BaizeAl/ModelHub将Hydra部署大模型需要的元信息都规整好了，以 qwen2-0.5b-instruct 为例，找到对应的 [metadata.yaml](https://github.com/BaizeAl/modelhub/blob/main/models/alibaba/qwen2-0.5b-instruct/metadata.yaml):


```yaml
apiVersion: model.hydra.io/v1alpha1
kind: ModelSpec
metadata:
  name: qwen2-0.5b-instruct
spec:
  descriptor:
    description:
      enUS: A 0.5B parameter instruction-tuned model from the Qwen2 series, suitable
        for multilingual text generation and understanding.
      zhCN: Qwen2 系列的 0.5B 参数指令微调模型，适用于多语言文本生成和理解。
    display: Qwen2-0.5B-Instruct
  source:
    huggingface:
      name: Qwen/Qwen2-0.5B-Instruct
    modelscope:
      name: Qwen/Qwen2-0.5B-Instruct
```

我们可以看到 spec.source 列出了从 [Hugging Face](https://huggingface.co/models) 和 [ModelScope](https://www.modelscope.cn/models) 下载该模型的路径。我们根据这个信息可以创建如下的Dataset：

从HF下载qwen2-0.5b-instruct

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    options:
      repoType: MODEL
    type: HUGGING_FACE
    uri: huggingface://Qwen/Qwen2.5-0.5B-Instruct
```

从MS下载qwen2-0.5b-instruct

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    options:
      repoType: MODEL
    type: MODEL_SCOPE
    uri: modelscope://Qwen/Qwen2.5-0.5B-Instruct
```

需要特别注意其中的字段设置：

- 需要指定 `metadata.labels.hydra.io/model-id` 为对应的模型ID来关联对应的模型服
- 如果是模型体验里的服务，需要指定namespace为public。如果是模型部署则需要指定到对应的命名空间下；
- 通过指定 `spec.share` 为true，我们允许其他的模型服务可以通过 REFERENCE的方式直接引用该Dataset及对应的文件，避免重复下载。具体配置参考目使用Dataset管理模型文件；

### 通过Git

你也可以使用git下载，以modelscope上的地址为例：

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    options:
      repoType: MODEL
    type: GIT
    uri: git://www.modelscope.cn/Qwen/Qwen2.5-0.5B-Instruct.git
  secretRef: qwen-git-secret
```

对于需要凭证访问的地址，需要提前创建Secret，结构如下：

```yaml
kind: Secret
type: Opaque
metadata:
  name: qwen-git-secret
  namespace: public
data:
  username: xxx    # 当类型为 MODEL_SCOPE、HTTP 和 GIT 时使用
  password: xxx    # 当类型为 HTTP 和 GIT 时使用
  ssh-privatekey: xxx    # 当类型为 GIT 时使用
  ssh-privatekey-passphrase: xxx    # 当类型为 GIT 时使用
  token: xxx        # 当类型为 HUGGING_FACE、MODEL_SCOPE 和 GIT 时使用
  access-key: xxx    # 当类型为 S3 时使用
  secret-key: xxx    # 当类型为 S3 时使用
```

## 手动下载

当网络访问不便的时候，你也可以通过提前下载并创建好对应的资源的方式来准备Dataset。

### 使用NFS

提前准备模型文件到NFS，以如下路径为例nfs://192.168.1.11/dataset/Qwen/Qwen2.5-0.5B-Instruct 为例，创建Dataset

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    type: NFS
    uri: nfs://192.168.1.11/dataset/Qwen/Qwen2.5-0.5B-Instruct 
```

### 使用Minio等S3存储

提前将模型文件上传到诸如Minio之类的S3协议兼容的存储系统里，也可以直接在Dataset直接申明地址和凭证，自动加载模型文件：

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    type: S3
    uri: s3://minio-svc/dataset/Qwen/Qwen2.5-0.5B-Instruct
  secretRef: minio-accesskey
```

当然，在外网可以访问的情况下，也可以直接填写AWS S3、Azure **Blob** **Storage** 等服务商提供的存储地址。

### 使用提前创建的PV/PVC

对于使用像JuiceFS、local等数据可以预先填充的持久化存储时，可以提前创建PV和PVC，然后在Dataset中引用该PVC即可：

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  share: true
  source:
    type: PVC
    uri: pvc://your-pvc-name/path/to/model
```

### 引用其他的Dataset

也可以直接引用其他创建过的Dataset，避免重复下载。前提是被引用的 Dataset 必须 share=true，且shareToNamespaceSelector 必须为空或者包含该 namespace ：

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: another-namepsace
spec:
  share: true
  source:
    type: PVC
    uri: dataset://public/qwen2-5-0-5b-instruct
```

## Dataset Spec Reference

完整的Dataset结构以及各个字段的含义如下：

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: public
spec:
  # Share indicates whether the model is shareable with others.
  # When set to true, the model can be shared according to the specified selector.
  share: true
  # ShareToNamespaceSelector defines a label selector to specify the namespaces
  # to which the model can be shared. Only namespaces that match the selector will have access to the model.
  # If Share is true and ShareToNamespaceSelector is empty, that means all namespaces can access this.  
  shareToNamespaceSelector: 
    matchExpressions:
      - key: env
        operator: In
        values: ["prod", "test"]
    matchLabels:
      region: sh-cn
  # dataSyncRound is the number of data sync rounds to be performed.
  # 
  dataSyncRound: 1
  source:
    # options is a map of key-value pairs that can be used to specify additional options for the dataset source, e.g. {"branch": "master"}
    # supported keys for each type of dataset source are:
    # - GIT: branch, commit, depth, submodules
    # - S3: region, endpoint, provider
    # - HTTP: any key-value pair will be passed to the underlying http client as http headers
    # - PVC:
    # - NFS:
    # - CONDA: requirements.txt, environment.yaml
    # - REFERENCE:
    # - HUGGING_FACE: repo, repoType, endpoint, include, exclude, revision
    # - MODEL_SCOPE: repo, repoType, include, exclude, revision
    options:
      repoType: MODEL
    type: MODEL_SCOPE
    # uri is the location of the dataset.
    # each type of dataset source has its own format of uri:
    # - GIT: http[s]://<host>/<owner>/<repo>[.git] or git://<host>/<owner>/<repo>[.git]
    # - S3: s3://<bucket>/<path/to/directory>
    # - HTTP: http[s]://<host>/<path/to/directory>?<query>
    # - PVC: pvc://<name>/<path/to/directory>
    # - NFS: nfs://<host>/<path/to/directory>
    # - CONDA: conda://<name>?[python=<python_version>]
    # - REFERENCE: dataset://<namespace>/<dataset>
    # - HUGGING_FACE: huggingface://<repoName>?[repoType=<repoType>]
    # - MODEL_SCOPE: modelscope://<namespace>/<model>
    uri: modelscope://Qwen/Qwen2.5-0.5B-Instruct
 # secretRef is the name of the secret that contains credentials for accessing the dataset source.
 secretRef: secret-name
 mountOptions:
   # path is the path to the directory to be mounted.
   # if set to "/", the dataset will be mounted to the root of the dest volume.
   # if set to a non-empty string, the dataset will be mounted to a subdirectory of the dest volume.
   path: /data
   mode: "0774"
   uid: 1000
   gid: 1000
 # volumeClaimTemplate defines the PVC spec generated by dataset controller, 
 # except for type `REFERENCE`
 volumeClaimTemplate: {}
```
