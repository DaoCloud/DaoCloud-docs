# Managing Model Files with Dataset

*[Hydra]: Codename for LLM Studio

Hydra uses **BaizeAl/Dataset** to manage model weight files. The Dataset resource abstracts the usage of Kubernetes Volumes, significantly simplifying the creation and maintenance of PV/PVC, and supports a wide range of data source types:

| DatasetType  | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| GIT          | Download via Git protocol                                   |
| S3           | Files stored in S3 or S3-compatible object storage          |
| PVC          | Access data via pre-created Persistent Volume Claims (PVC)  |
| NFS          | Access via NFS protocol                                     |
| HTTP         | Download via HTTP                                           |
| CONDA        | Download Python packages via Conda                          |
| REFERENCE    | Reference other Datasets to access their data               |
| HUGGING_FACE | Download model files from Hugging Face                      |
| MODEL_SCOPE  | Download model files from ModelScope                        |

Dataset also supports **auto-preloading**: for supported types, a preprocessing Job will be created to download and store model data into a mounted PV, enabling fast model initialization and reuse.

## Auto Download

### From Hugging Face and ModelScope

We’ve organized the metadata needed to deploy Hydra models in [BaizeAl/ModelHub](https://github.com/BaizeAl/modelhub). For example, for `qwen2-0.5b-instruct`, the metadata is available in this [metadata.yaml](https://github.com/BaizeAl/modelhub/blob/main/models/alibaba/qwen2-0.5b-instruct/metadata.yaml):

```yaml
apiVersion: model.hydra.io/v1alpha1
kind: ModelSpec
metadata:
  name: qwen2-0.5b-instruct
spec:
  descriptor:
    description:
      enUS:
        A 0.5B parameter instruction-tuned model from the Qwen2 series, suitable
        for multilingual text generation and understanding.
      zhCN: Qwen2 系列的 0.5B 参数指令微调模型，适用于多语言文本生成和理解。
    display: Qwen2-0.5B-Instruct
  source:
    huggingface:
      name: Qwen/Qwen2-0.5B-Instruct
    modelscope:
      name: Qwen/Qwen2-0.5B-Instruct
```

This shows the download paths for Hugging Face and ModelScope.

To download `qwen2-0.5b-instruct` from **Hugging Face**:

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

To download it from **ModelScope**:

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

**Important field settings**:

* `metadata.labels.hydra.io/model-id` must be set to match the corresponding model ID.
* If used for model trial, set `namespace` to `public`. For model deployments, use the relevant namespace.
* Set `spec.share` to `true` to allow other model services to reuse the Dataset via `REFERENCE`, avoiding duplicate downloads.

### From Git

You can also download via Git. For example, using a ModelScope Git URL:

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

If credentials are required, create a `Secret` with the following structure:

```yaml
kind: Secret
type: Opaque
metadata:
  name: qwen-git-secret
  namespace: public
data:
  username: xxx                  # Used for MODEL_SCOPE, HTTP, and GIT
  password: xxx                  # Used for HTTP and GIT
  ssh-privatekey: xxx            # Used for GIT
  ssh-privatekey-passphrase: xxx # Used for GIT
  token: xxx                     # Used for HUGGING_FACE, MODEL_SCOPE, and GIT
  access-key: xxx                # Used for S3
  secret-key: xxx                # Used for S3
```

## Manual Download

If internet access is limited, you can prepare resources manually and create the Dataset accordingly.

### Using NFS

Prepare the model files on NFS. For example, with path `nfs://192.168.1.11/dataset/Qwen/Qwen2.5-0.5B-Instruct`:

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

### Using MinIO or Other S3 Storage

Upload model files to an S3-compatible storage system like MinIO. Then declare the storage address and credentials in the Dataset:

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

You may also use AWS S3, Azure Blob Storage, or other cloud providers if accessible.

### Using Pre-created PV/PVC

For persistent storage systems like JuiceFS or local volumes, you can create PV and PVC ahead of time, then reference the PVC in your Dataset:

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

### Referencing Another Dataset

To avoid duplicate downloads, you can reference an existing Dataset. The referenced Dataset must have `share: true` and its `shareToNamespaceSelector` must either be empty or include the referencing namespace:

```yaml
apiVersion: dataset.baizeai.io/v1alpha1
kind: Dataset
metadata:
  labels:
    hydra.io/model-id: "qwen2-0.5b-instruct"
  name: qwen2-5-0-5b-instruct
  namespace: another-namespace
spec:
  source:
    type: REFERENCE
    uri: dataset://public/qwen2-5-0-5b-instruct
```

## Dataset Spec Reference

A full reference of the Dataset spec structure and field definitions is provided below:

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
