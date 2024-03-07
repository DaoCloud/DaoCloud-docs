# 生成导出文件

## 生成 Word 文件

本文档为生成 Word 文档的脚步使用说明

- 脚本所在位置 [../md2doc-v2.py](../md2doc-v2.py)
- 生成命令：`python3 md2doc-v2.py docs/zh/docs/`

### 依赖

```bash
pip install pandoc python-docx docxcompose
```

- pandoc (<https://github.com/jgm/pandoc>)

### 使用说明

执行脚本时，会根据传入的路径位置，会检测该路径下的所有 `.md` 文件，然后合并为一个 `.docx` 文件。

- 生成命令：`python3 md2doc-v2.py [md文件目录]`
- 默认目录：`docs/zh/docs/`
- 生成 Word 文件路径为： `docs/` 下

### 实现原理

- 轮询指定目录下所有的 `.md` 文件
- 将每个文件的内容读取出来，转换为一个 `.docx` 文件
- 最后，将所有的 `.docx` 文件合并为一个 `.docx` 文件
