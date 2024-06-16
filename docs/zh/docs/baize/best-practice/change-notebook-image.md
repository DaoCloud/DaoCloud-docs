---
hide:
  - toc
---

# 更新 Notebook 内置镜像

![image-20240616110541271](./images/notebook-images.png)

在 Notebook 中，默认提供了多个可用的基础镜像，供开发者选择；大部分情况下，这会满足开发者的使用。

DaoCloud 提供了一个默认的 Notebook 镜像，包含了所需的任何开发工具和资料。

```markdown
baize/baize-notebook
```

这个 Notebook 里面包含了基础的开发工具，以 `baize-notebook:v0.5.0` （2024 年 5 月 30 日）为例，相关依赖及版本如下：

| 依赖         | 版本编号 | 介绍                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| Ubuntu       | 22.04.3  | 默认 OS                                                      |
| Python       | 3.11.6   | 默认 Python 版本                                             |
| pip          | 23.3.1   |                                                              |
| conda(mamba) | 23.3.1   |                                                              |
| jupyterlab   | 3.6.6    | JupyterLab 镜像，提供完整的 Notebook 开发体验                |
| codeserver   | v4.89.1  | 主流 Code 开发工具，方便用户使用熟悉的工具进行开发体验       |
| *baizectl    | v0.5.0   | DaoCloud 内置 CLI 任务管理工具                               |
| *SSH         | -        | 支持本地 SSH 直接访问到 Notebook 容器内                      |
| *kubectl     | v1.27    | Kubernetes CLI，可以使用 kubectl 在 Notebook 内 管理容器资源 |

> 随着版本发展，DCE 会主动维护并在每次版本迭代时更新。

但有时用户可能需要自定义镜像，本文介绍了如何更新镜像，并增加到 Notebook 创建界面中选择。

## 构建自定义镜像（仅供参考）

!!! note

    注意，构建新镜像 **需要以 `baize-notebook` 作为基础镜像**，以保证 Notebook 的正常运行

在构建自定义镜像时，建议先了解 baize-notebook 镜像的 Dockerfile，以便更好的理解如何构建自定义镜像。

### baize-noteboook 的 Dockerfile

```dockerfile
ARG BASE_IMG=docker.m.daocloud.io/kubeflownotebookswg/jupyter:v1.8.0

FROM $BASE_IMG

USER root

# install - useful linux packages
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get -yq update \
 && apt-get -yq install --no-install-recommends \
    openssh-server git git-lfs bash-completion \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# remove default s6 jupyterlab run script
RUN rm -rf /etc/services.d/jupyterlab

# install - useful jupyter plugins
RUN mamba install -n base -y jupyterlab-language-pack-zh-cn \
  && mamba clean --all -y

ARG CODESERVER_VERSION=v4.89.1
ARG TARGETARCH

RUN curl -fsSL "https://github.com/coder/code-server/releases/download/$CODESERVER_VERSION/code-server_${CODESERVER_VERSION/v/}_$TARGETARCH.deb" -o /tmp/code-server.deb \
  && dpkg -i /tmp/code-server.deb \
  && rm -f /tmp/code-server.deb

ARG CODESERVER_PYTHON_VERSION=2024.4.1
ARG CODESERVER_JUPYTER_VERSION=2024.3.1
ARG CODESERVER_LANGUAGE_PACK_ZH_CN=1.89.0
ARG CODESERVER_YAML=1.14.0
ARG CODESERVER_DOTENV=1.0.1
ARG CODESERVER_EDITORCONFIG=0.16.6
ARG CODESERVER_TOML=0.19.1
ARG CODESERVER_GITLENS=15.0.4

# configure for code-server extensions
# # https://github.com/kubeflow/kubeflow/blob/709254159986d2cc99e675d0fad5a128ddeb0917/components/example-notebook-servers/codeserver-python/Dockerfile
# # and
# # https://github.com/kubeflow/kubeflow/blob/709254159986d2cc99e675d0fad5a128ddeb0917/components/example-notebook-servers/codeserver/Dockerfile
RUN code-server --list-extensions --show-versions \
  && code-server --list-extensions --show-versions \
  && code-server \
    --install-extension MS-CEINTL.vscode-language-pack-zh-hans@$CODESERVER_LANGUAGE_PACK_ZH_CN \
    --install-extension ms-python.python@$CODESERVER_PYTHON_VERSION \
    --install-extension ms-toolsai.jupyter@$CODESERVER_JUPYTER_VERSION \
    --install-extension redhat.vscode-yaml@$CODESERVER_YAML \
    --install-extension mikestead.dotenv@$CODESERVER_DOTENV \
    --install-extension EditorConfig.EditorConfig@$CODESERVER_EDITORCONFIG \
    --install-extension tamasfe.even-better-toml@$CODESERVER_TOML \
    --install-extension eamodio.gitlens@$CODESERVER_GITLENS \
    --install-extension catppuccin.catppuccin-vsc-pack \
    --force \
  && code-server --list-extensions --show-versions

# configure for code-server
RUN mkdir -p /home/${NB_USER}/.local/share/code-server/User \
  && chown -R ${NB_USER}:users /home/${NB_USER} \
  && cat <<EOF > /home/${NB_USER}/.local/share/code-server/User/settings.json
{
  "gitlens.showWelcomeOnInstall": false,
  "workbench.colorTheme": "Catppuccin Mocha",
}
EOF

RUN mkdir -p /tmp_home/${NB_USER}/.local/share \
  && mv /home/${NB_USER}/.local/share/code-server /tmp_home/${NB_USER}/.local/share

# set ssh configuration
RUN mkdir -p /run/sshd \
 && chown -R ${NB_USER}:users /etc/ssh \
 && chown -R ${NB_USER}:users /run/sshd \
 && sed -i "/#\?Port/s/^.*$/Port 2222/g" /etc/ssh/sshd_config \
 && sed -i "/#\?PasswordAuthentication/s/^.*$/PasswordAuthentication no/g" /etc/ssh/sshd_config \
 && sed -i "/#\?PubkeyAuthentication/s/^.*$/PubkeyAuthentication yes/g" /etc/ssh/sshd_config \
 && rclone_version=v1.65.0 && \
       arch=$(uname -m | sed -E 's/x86_64/amd64/g;s/aarch64/arm64/g') && \
       filename=rclone-${rclone_version}-linux-${arch} && \
       wget http://10.6.100.13:8081/repository/github.com/rclone/rclone/releases/download/${rclone_version}/${filename}.zip -O ${filename}.zip && \
       unzip ${filename}.zip && mv ${filename}/rclone /usr/local/bin && rm -rf ${filename} ${filename}.zip

# Init mamba
RUN mamba init --system

# init baize-base environment for essential python packages
RUN mamba create -n baize-base -y python \
  && /opt/conda/envs/baize-base/bin/pip install tensorboard \
  && mamba clean --all -y \
  && ln -s /opt/conda/envs/baize-base/bin/tensorboard /usr/local/bin/tensorboard

# prepare baize-runtime-env directory
RUN mkdir -p /opt/baize-runtime-env \
  && chown -R ${NB_USER}:users /opt/baize-runtime-env

ARG APP
ARG PROD_NAME
ARG TARGETOS

COPY out/$TARGETOS/$TARGETARCH/data-loader /usr/local/bin/
COPY out/$TARGETOS/$TARGETARCH/baizectl /usr/local/bin/

RUN chmod +x /usr/local/bin/baizectl /usr/local/bin/data-loader && \
    echo "source /etc/bash_completion" >> /opt/conda/etc/profile.d/conda.sh && \
    echo "source <(baizectl completion bash)" >> /opt/conda/etc/profile.d/conda.sh && \
    echo "source <(kubectl completion bash)" >> /opt/conda/etc/profile.d/conda.sh && \
    echo '[ -f /run/baize-env ] && export $(cat /run/baize-env | xargs)' >> /opt/conda/etc/profile.d/conda.sh && \
    echo 'alias conda="mamba"' >> /opt/conda/etc/profile.d/conda.sh

USER ${NB_UID}
```

### 构建你的镜像

```dockerfile
ARG BASE_IMG=release.daocloud.io/baize/baize-notebook:v0.5.0

FROM $BASE_IMG
USER root

# Do Customization
RUN mamba install -n baize-base -y pytorch torchvision torchaudio cpuonly -c pytorch \
 && mamba install -n baize-base -y tensorflow \
 && mamba clean --all -y

USER ${NB_UID}

```

## 增加到 Notebook 镜像列表（Helm）

!!! warning

    注意，必须由平台管理员操作，谨慎变更

目前，镜像选择器需要通过更新 `baize` 的 `Helm` 参数来修改，具体步骤如下：

在 kpan-global-cluster 全局管理集群的 `Helm 应用`列表，找到 baize，进入更新页面，在 `YAML` 参数中修改，Notebook 镜像即可：

![Update Baize](./images/update-baize.png)

注意参数修改的路径如下 `global.config.notebook_images` :

```yaml
...
global:
  ...
  config:
    notebook_images:
      ...
      names: release.daocloud.io/baize/baize-notebook:v0.5.0
      # 在这里增加你的镜像信息
```

更新完成之后，待 Helm 应用重启成功之后，即可在 Notebook 创建界面中的选择镜像看到新的镜像。
