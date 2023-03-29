# 批量生产 PDF 文件

## 转换为 Word

### 生成所有文档的 Word 文件

下方命令可以批量生成一个全量的 Word 文件，包含所有的文档。

```bash
cd /path/to/this/repo
python3 scripts/md2docx-v2.py docs/zh/docs # 生成 Word 文件
```

但是，生成的 Word 文件中，所有的文档都是在一个文件中，不方便阅读。

> 目前此命令会生成大量 word 文件，注意不要提交到 github 上。

建议操作一下命令，来操作移除缓存的 word 文件

```bash
find ./docs -type f -name "*.docx" ! -name "TiDBonHwameiStor.docx" | xargs rm -f
```

### 生成具体项目的 Word 文件

```bash
cd /path/to/this/repo
python3 scripts/md2docx-v2.py docs/zh/docs/kpanda # 生成 Word 文件
```

> 以上为例，这里是生成单个 Kpanda 项目的文档。

## 转换为 PDF

### 生成所有文档的 PDF 文件

目前全部文档过大，所以生成全量文档的 PDF 文件会失败。

> 暂不支持

### 生成具体项目的 PDF 文件

1. 修改 pdf.yaml 文件，目前修改 2 个配置：
   1. docs_dir 需要读取的项目名称
   2. output_path 对应的导出位置
2. 然后执行 mkdocs build 命令
   1. `mkdocs build -f pdf.yaml`

采用开源项目为基础，进行二次开发，目前支持的功能有限，后续会继续完善。
