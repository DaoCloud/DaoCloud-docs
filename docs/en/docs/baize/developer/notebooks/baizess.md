# baizess Source Switch Tool Usage Guide

`baizess` is a built-in, out-of-the-box source switch tool within the Notebook of DCE 5.0 AI Lab module. It provides a streamlined command-line interface to facilitate the management of package sources for various programming environments. With baizess, users can easily switch sources for commonly used package managers, ensuring seamless access to the latest libraries and dependencies. This tool enhances the efficiency of developers and data scientists by simplifying the process of managing package sources.

## Installation

Currently, `baizess` is integrated within DCE 5.0 AI Lab. Once you create a Notebook, you can directly use `baizess` within it.

## Getting Started

### Basic Information

The basic information of the `baizess` command is as follows:

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

### Command Format

The basic format of the `baizess` command is as follows:

```bash
baizess [command] [package-manager]
```

Here,`[command]` refers to the specific operation command, and `[package-manager]` is used to specify the corresponding package manager for the operation.

#### Command

- `set`：Backup the source, perform speed test, and switch the specified package manager's source to the fastest domestic source based on speed test result.
- `reset`：Reset the specified package manager to default source.

#### Currently supported package-manager

- `apt`   (Source switch and reset require `root` privilege)
- `conda` (original source will be backed up in `/etc/apt/backup/`)
- `pip`   (updated source will be written to `~/.condarc`)
