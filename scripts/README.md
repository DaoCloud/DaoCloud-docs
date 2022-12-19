# 翻译使用指南

google 翻译，默认限制 5000 字符一下，超过 5000 字符不会翻译。

## 使用注意事项

- 需要本地环境可以访问 google 翻译，简而言之：需要科学上网。
- 翻译单个文档 `make trans file=xxx.md`，翻译结果保存为 `xxx_translate.md`
- 批量翻译整个文件夹 `make trans folder=xxx`， 翻译结果保存到文件夹下 `/_translated` 文件夹

## 翻译流程

- 将 `scripts/config-sample.py` 重命名为 `scripts/config.py`，并根据本地的代理情况配置文件
- 安装依赖
    1. 切换路径到 scripts/ 目录下
    2. 依赖翻译库 `googletrans`， 安装方式 `pip3 install googletrans==3.1.0a0`
    3. 依赖 pyinstaller 制作个人指令，安装方式 `pip3 install -g pyinstaller`
    4. 将编译后的指令保存到系统环境变量中使用，`cp dist/translate_md ../.venv/bin/`
    5. 可以在任意路径下执行命令

## 翻译指令使用案例

翻译单个文件和单个文件夹不会自动 copy 图片资料，所以这里图片需要手工替换

### 翻译单个文件

```bash
~ translate_md-arm64 --file=Features.md     
Features.md
Namespace(file=['Features.md'], folder=None, full_translate=None)

~ ls
Features.md Features_translated.md
```

### 翻译整个文件夹

```bash
~ translate_md-arm64 --folder=01ProductBrief    
01ProductBrief
01ProductBrief/Benefits.md
01ProductBrief/WhatisAmamba.md
01ProductBrief/release-notes.md
01ProductBrief/Concepts.md
01ProductBrief/Scenarios.md
01ProductBrief/Features.md
Namespace(file=None, folder=['01ProductBrief'], full_translate=None)

ls -R 01ProductBrief
_translated  Benefits.md  Concepts.md  Features.md  release-notes.md  Scenarios.md  WhatisAmamba.md

01ProductBrief/_translated:
Benefits.md  Concepts.md  Features.md  release-notes.md  Scenarios.md  WhatisAmamba.md
```

### 翻译 DaoCloud Docs

这里特殊指令会翻译全部文件，翻译全部文件的同时，会自动copy相关的图片资料

```bash
~ translate_md-arm64 --full_translate=True
```
