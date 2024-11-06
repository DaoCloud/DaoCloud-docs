# baizess 换源工具使用指南

`baizess` 是 DCE 5.0 AI Lab 模块中 Notebook 内置的开箱即用的换源小工具。它提供了简洁的命令行界面，方便用户管理各种编程环境的包管理器源。
通过 baizess，用户可以轻松切换常用包管理器的源，确保顺利访问最新的库和依赖项。该工具通过简化包源管理流程，提升了开发者和数据科学家的工作效率。

## 安装

目前，`baizess` 已经集成在 DCE 5.0 AI Lab 中。
你在创建 Notebook 后，即可在 Notebook 中直接使用 `baizess`。

## 快速上手

### 基本信息

`baizess` 命令的基本信息如下：

```bash
jovyan@19d0197587cc:/$ baizess
source switch tool

Usage:
  baizess [command] [package-manager]

Available Commands:
  set     Switch the source of specified package manager to current fastest source
  reset   Reset the source of specified package manager to default source

Available Package-managers:
  apt     (require root privilege)
  conda
  pip
```

### 命令格式

`baizess` 命令的基本格式如下：

```bash
baizess [command] [package-manager]
```

其中，`[command]` 是具体的操作命令，`[package-manager]` 用于指定操作对应的包管理器。

#### command

- `set`：备份源，测速，将所指定的包管理器的源切换为测速结果最快的国内源。
- `reset`：将所指定的包管理器重置为默认源。

#### 目前支持的 package-manager

- `apt`   （源的切换与重置需要`root`权限）
- `conda` （原先的源将被备份在`/etc/apt/backup/`）
- `pip`   （更新后源信息将被写入`~/.condarc`）
