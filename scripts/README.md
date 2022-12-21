# 翻译使用指南

主要采用 google translate openapi 进行翻译，优势是不会影响 markdown 文件中的超链及图片

> 调研的竞品有

- [付费] 阿里云机器翻译
- [付费] 百度翻译 API
- [免费] google translate openapi
- [免费] 有道翻译 API
- [免费] md_docs-trans-app (with webdriver)


## 采用技术方案

- 主要使用翻译能力 [py-googletrans](https://github.com/ssut/py-googletrans)，注意安装 `googletrans==3.1.0a0`
  - 没有 api call limit
  - 可以在终端执行，配合 github action.
- 脚本逻辑主要是将翻译能力封装为方便文档同学使用，主要提供能力如下：
  - 翻译单个文件
  - 翻译单个文件夹
  - 全量翻译 （在 `docs/zh/`下遍历`.md`文件，并将翻译结果存放特定目录，并且 copy 图片等主要静态资源）
- 使用内置函数 `argparse` 处理命令行参数
- 使用 `pyinstaller` 将脚本编译为可执行文件，方便使用

### 未处理小问题

- google 翻译，默认限制 5000 字符一下，超过 5000 字符不会翻译。
  - 处理方案，按照 `##` or `###` 进行分段分割，然后翻译完成后拼接


## 使用注意事项

- 需要本地环境可以访问 google 翻译，简而言之：需要科学上网。
- 翻译单个文档 `translate_md --file=xxx.md`，翻译结果保存为 `xxx_translate.md`
- 批量翻译整个文件夹 `translate_md --folder=xxx`， 翻译结果保存到文件夹下 `/_translated` 文件夹

## 翻译流程

- 将 `scripts/config-sample.py` 重命名为 `scripts/config.py`，并根据本地的代理情况配置文件
- 安装依赖
    1. 切换路径到 `cd scripts` 目录下
    2. 依赖翻译库 `googletrans`， 安装方式 `pip3 install googletrans==3.1.0a0`
    3. 依赖 pyinstaller 制作个人指令，安装方式 `pip3 install pyinstaller`
    4. 将编译后的指令保存到系统环境变量中使用，`cp dist/translate_md /usr/local/bin`
    5. 可以在任意路径下执行命令：

        - 如果是 intel 芯片的 Mac，运行 `cp translate_md_amd64 /usr/local/bin/translate_md`
        - 如果是 m1 芯片的 Mac，运行 `cp translate_md_arm64 /usr/local/bin/translate_md`
        - 如果是 Windows，需要自己编译 `pyinstaller -F translate_md.py --clean`，然后执行第 4 步

## 翻译指令使用案例

翻译单个文件和单个文件夹不会自动 copy 图片资料，所以这里图片需要手工替换

### 翻译单个文件

```bash
~ translate_md --file=Features.md     
Features.md
Namespace(file=['Features.md'], folder=None, full_translate=None)

~ ls
Features.md Features_translated.md
```

### 翻译整个文件夹

```bash
~ translate_md --folder=01ProductBrief    
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
~ translate_md --full_translate=True
```
