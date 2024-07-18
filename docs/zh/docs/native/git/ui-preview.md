# 前端 UI 翻译后预览

前端 UI 翻译之后，可以参照以下步骤在本地预览实时效果。例如调整单词长度、大小写、查看一致性等。

1. 进入 repo 根目录，创建 __.env.local__ 本地环境文件。

    ```shell
    touch .env.local
    ```

2. 设置本地环境变量。

    ```shell
    cat <<EOF > .env.local
    VUE_APP_API_URL=http://demo-dev.daocloud.io
    VUE_APP_AUTH=eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJpYXQiOjE2ODUzNTY0NDMsImlzcyI6ImdoaXBwby5pbyIsInN1YiI6IjQzODIxMmI3LTFhNDYtNDE4Ny04ODI0LTYwZWE5ZDBkOTNiMyIsInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluIiwiZ3JvdXBzIjpbXSwiaWQiOiJmOWY3NmU5NC1mYjRjLTRlMGUtYmZlYy0wNmIwYmE0MzM0OWYifQ.dSQFtEIqe520ZMaT82vcQ8Y6YmIbWqz4SZPLHxJcjpCrHBg_Ke1asEymyz3AJC9WkF30JR7Eqpfmgt6Gc05op7Tt12-QG527fbW8pWQjZhWx8-u2ev6MZtCQQjoAA4w03MozUfiEI-VFdoI0in2MBi2bdKBVGRpeW2DwCQyN6jR5F-ZKm4ObP8dD7WnfcjsVSrLHBBJ1jeU9d1qAVNc1IxXSyG2p2FrIXa4_ds5Al_8l38NJ4LuyeVnoefzP6dDpemTGzavwfDtmXdATMV5jqHADji1Zbe-5YyV-3SwQCiN7XQmLCht4NpqA3NRYC1Tv134wrzsBvfB0HVIwAjgrpA
    EOF
    ```

3. 安装依赖项。

    ```shell
    npm install
    ```

4. 本地 build 预览: http://localhost:8120/ 

    ```shell
    npm run serve
    ```

!!! note

    切换 demo-dev 的语言，可修改文件 `src/plugins/vue-i18n/index.ts`：

    ```ts
    export function loadLanguageAsync(lang = 'zh-CN') {
    ```

    - 中文：zh-CN
    - 英文：en-US
