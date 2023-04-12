---
hide:
  - toc
---

# OpenAPI 文档制作流程

本页以 Ghippo 为例，说明制作 OpenAPI 文档的步骤。
主要是生成一个 swagger json 文件，然后自动向文档站提 PR。

![OpenAPI and Swagger](./images/index.png)

1. 在 Makefile 中添加这几行代码：

    ```go title="Makefile"
    .PHONY += doc.openapi
    doc.openapi:
        $(eval swagger_path ?= swagger)
        @bash hack/gen-openapi-json.sh ghippo $(GHIPPO_VERSION) $(swagger_path)
    ```

1. 编写生成 swagger json 的脚本

    ```bash title="gen-openapi-json.sh"
    #!/bin/bash

    set -o errexit
    set -o nounset
    set -o pipefail

    # 参数1: 产品名称(dce5 ghippo kpanda ...)
    # 参数2: 产品版本(建议是 tag 值)
    # 参数3: swagger 输出文件夹
    readonly PRODUCT=${1}
    readonly PRODUCT_VERSION=${2}
    readonly OUTPUT_DIR=${3}

    # proto 所在的文件夹
    PROTO_DIR=./api/proto
    # proto vendor 所在文件夹
    PROTOVENDOR_DIR=./api/protovendor

    # 输出文件夹不存在，就创建
    [ ! -e ${OUTPUT_DIR} ] && mkdir ${OUTPUT_DIR}

    # 合并生成一个 swagger json 文件
    protoc \
        --proto_path=".:${PROTOVENDOR_DIR}" \
        --openapiv2_out ${OUTPUT_DIR} \
        --openapiv2_opt logtostderr=true \
        --openapiv2_opt allow_merge=true \
        --openapiv2_opt output_format=json \
        --openapiv2_opt merge_file_name="${PRODUCT}.${PRODUCT_VERSION}." \
        ${PROTO_DIR}/*/*.proto
    ```

1. 编写向 doc repo 提 PR 的脚本

    ```bash title="update_openapi_doc.sh"
    #!/usr/bin/env bash

    set -o errexit
    set -o nounset
    set -o pipefail
    set -x

    # 参数1：产品名称-英文（ghippo kpanda ...)
    # 参数2：产品名称-中文（全局管理 ...)
    # 参数3：swagger json 的版本
    # 参数4：swagger json 文件夹路径
    # 参数5：github token
    readonly PRODUCT=${1}
    readonly PRODUCT_ZH=${2}
    readonly SWAGGER_VERSION=${3}
    readonly SWAGGER_PATH=${4}
    readonly GITHUB_TOKEN=${5}

    # 在流水线中项目所在的目录，以 ghippo 为例：/builds/ndx/ghippo
    readonly PRODUCT_LOCAL_PATH=$(pwd)
    # 文档站本地 git 仓库地址
    readonly LOCAL_GIT_REPO=$(mktemp -d)
    # 文档站远程 git 仓库地址
    readonly REMOTE_GIT_REPO="https://${GITHUB_TOKEN}@github.com/windsonsea/DaoCloud-docs.git"

    function main() {
        local current_pwd=$(pwd)

        # 拉取线上文档站 main 分支最新的代码，并且在本地创建一个名字叫 ${branch_name} 的分支
        local branch_name="openapi-${PRODUCT}-${SWAGGER_VERSION}"

        # 只拉取 main 分支，depth 为 1 的代码
        git clone --single-branch --depth 1 ${REMOTE_GIT_REPO} ${LOCAL_GIT_REPO}
        cd ${LOCAL_GIT_REPO}
        git checkout -b ${branch_name}

        # 创建 doc 文件
        check_bash_dir
        update_openapi_index_page
        create_openapi_detail_files

        local git_uname=$(git config --get user.name)
        if [ "${git_uname}" == "" ]; then
            git config --global user.email "haifeng.yao@daocloud.io"
            git config --global user.name "DaoCloud CI Robot"
        fi
        git add .
        git commit -m "openapi: ${PRODUCT} version updated to ${SWAGGER_VERSION}"
        git push ${REMOTE_GIT_REPO} ${branch_name} -f
        cd ${current_pwd}

        create_pull_request ${branch_name}
    }

    function check_bash_dir() {
        local openapi_dir="${LOCAL_GIT_REPO}/docs/zh/docs/openapi"
        # 检查目标文件是否存在，不存在就创建
        if [ ! -d ${openapi_dir} ]; then
            mkdir ${openapi_dir}
        fi
        local product_dir="${LOCAL_GIT_REPO}/docs/zh/docs/openapi/${PRODUCT}"
        if [ ! -d ${product_dir} ]; then
            mkdir ${product_dir}
        fi
    }

    # 更新项目的 openapi index 页面
    function update_openapi_index_page() {
        local target_file="${LOCAL_GIT_REPO}/docs/zh/docs/openapi/${PRODUCT}/index.md"
        local text="- [版本 ${SWAGGER_VERSION}](./${SWAGGER_VERSION}.md)"
        # 检查目标文件是否存在，不存在就创建,并添加文本
        if [ ! -f ${target_file} ]; then
            echo "# ${PRODUCT_ZH} OpenAPI" >${target_file}
        fi

        # 向 index.md 文件的第 2 行末尾添加文本
        sed -i "1a ${text}" ${target_file}
    }

    # 创建 swagger json 详情文件
    function create_openapi_detail_files() {
        local target_dir="${LOCAL_GIT_REPO}/docs/zh/docs/openapi/${PRODUCT}"
        local target_file="${LOCAL_GIT_REPO}/docs/zh/docs/openapi/${PRODUCT}/${SWAGGER_VERSION}.md"
        # 检查 md 目标文件是否存在，不存在就创建
        if [ ! -f ${target_file} ]; then
            echo "# <swagger-ui src="${SWAGGER_VERSION}.json">" >${target_file}
        fi

        # 对每个 swagger json 文件进行操作，修改 json 文件中的字段。并将生成的文件输出到 openapi 的文件夹下
        readonly text="{\"title\":\"${PRODUCT_ZH}\",\"version\":\"${SWAGGER_VERSION}\"}"
        for file in $(ls "${PRODUCT_LOCAL_PATH}/${SWAGGER_PATH}"); do
            # 对每个文件进行操作，修改 json 文件中的字段。
            # eg.
            # "info": {
            #    "title": "api/proto/v1alpha1/about.proto",
            #    "version": "version not set"
            #  }
            # to
            # "info": {
            #    "title": "ghippo",
            #    "version": "0.14"
            #  }
            jq --argjson v ${text} '.info = $v' ${PRODUCT_LOCAL_PATH}/${SWAGGER_PATH}/${file} >${target_dir}/${SWAGGER_VERSION}.json
        done
    }

    # 给文档站创建一个 PR
    function create_pull_request() {
        local branch_name=${1}
        local msg="openapi: ${PRODUCT} version updated to ${SWAGGER_VERSION}"
        local body_json='{"title": "'${msg}'", "body": "'${msg}'", "head": "windsonsea:'${branch_name}'", "base": "main"}'
        local status_code=$(
            curl -L --retry 3 -X POST -i -s -w %{http_code} -o /dev/null \
                -H "Accept: application/vnd.github+json" -H "Authorization: Bearer ${GITHUB_TOKEN}" \
                -d "${body_json}" \
                https://api.github.com/repos/DaoCloud/DaoCloud-docs/pulls
        )
        if [ "${status_code}" -lt 200 ] || [ "${status_code}" -ge 400 ]; then
            echo "failed to create pull request. http status code is ${status_code}."
            exit -1
        fi
        echo ${status_code}
    }

    main $@
    ```

1. 更新 GitLab CI 文件

    ```yaml title=".gitlab-ci.yml"
    doc.openapi:
    stage: doc
    rules:
        - if: '$CI_COMMIT_TAG =~ /v[0-9]+(\.[0-9]+)+$/ && $CI_DEPLOY == null'
    tags:
        - docker
    script:
        - make doc.openapi
        - bash /go/update_openapi_doc.sh ghippo 全局管理 ${CI_COMMIT_TAG} swagger ${GITHUB_TOKEN}
    ```
