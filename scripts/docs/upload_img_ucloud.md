# 自动检测并上传 Markdown 图片到 UCloud

## 介绍

解决目前文档站内的图片引用问题，目前文档站内的图片引用都是使用相对路径，导致图片 build 时间太长，所以需要将图片上传到 UCloud，并且修改文档站内的图片引用路径

- 具体脚本内容：`scripts/upload_img_ucloud.py`

## 使用方式

- 提前替换脚本文件中的 public_key 和 private_key
- 执行脚本
  - 切换到仓库根目录
  - 执行 `python scripts/upload_img_ucloud.py`
    - 检查是否存在路径的存储问题
  - 上传成功后，会自动修改文档站内的图片引用路径
