# 自动检测并上传 Markdown 图片到 UCloud

## 介绍

解决目前文档站内的图片引用问题，目前文档站内的图片引用都是使用相对路径，导致图片 build 时间太长，所以需要将图片上传到 UCloud，并且修改文档站内的图片引用路径

- 具体脚本内容：`scripts/upload_img_ucloud.py`

## 使用方式

- 提前设置 `U_PUBLIC_KEY`、`U_PRIVATE_KEY`、`U_UPLOADSUFFIX`、`U_BUCKET`、`U_BUCKET_FOLDER`、`U_REMOTE_DOMAIN`
- 执行脚本
  - 切换到仓库根目录
  - 执行 `make sync-image`
  - 执行 `make upload-images DOCS_PATH=docs`
    - 检查是否存在路径的存储问题
  - 上传成功后，会自动修改文档站内的图片引用路径
