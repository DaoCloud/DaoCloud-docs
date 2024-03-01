# 批量生产 Word 和 PDF 文件

[English](./generate_pdf.md) | 中文

## 转换为 Word

### 生成所有文档的 Word 文件（不推荐）

下方命令可以批量生成一个全量的 Word 文件，包含所有的文档。

```bash
cd /path/to/this/repo
python3 scripts/md2doc-v2.py docs/zh/docs # 生成 Word 文件
```

但这样生成的 Word 文件包含了 docs.daocloud.io 所有的内容，不方便阅读。

> 目前此命令会生成大量 Word 文件，注意不要提交到 GitHub 上。

建议在提 PR 之前，运行以下命令，移除缓存的 Word 文件：

```bash
find ./docs -type f -name "*.docx" ! -name "TiDBonHwameiStor.docx" | xargs rm -f
```

### 生成具体项目的 Word 文件（推荐）

```bash
cd /path/to/this/repo
python3 scripts/md2doc-v2.py docs/zh/docs/kpanda # 生成 Word 文件
```

> 以上为例，这里是生成单个 `kpanda` 目录的文档。

如果导出时报错，可以尝试运行以下命令安装所需的依赖项：

```bash
pip install python-docx
brew install pandoc
```

## 转换为 PDF

### 生成所有文档的 PDF 文件（暂不支持）

目前全部文档过大，所以生成全量文档的 PDF 文件会失败。

> 暂不支持

### 生成具体项目的 PDF 文件（推荐）

1. 修改 [pdf.yaml](../docs/zh/pdf.yaml) 文件，只需修改 2 个字段：
   - `docs_dir` 需要读取的文件夹名称
   - `output_path` 导出 pdf 的位置
2. 然后执行 `mkdocs build` 命令，此时需要配置好 poetry 环境
   1. 使用 `poetry install` 安装依赖项
   2. 运行 `poetry run mkdocs build -f pdf.yaml` 生成 PDF 文件

文档站的二次开发以开源项目为基础，目前支持的功能尚有限，后续会继续完善。
