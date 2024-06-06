# Notebook SSH 访问指南

智能算力提供的 Notebook 支持在本地通过 SSH 的方式访问；

通过简单的配置，即可使用 SSH 访问 Jupyter Notebook 的功能。
无论您是使用 Windows、Mac 还是 Linux 操作系统，都可以按照以下步骤进行操作。

## 配置 SSH 访问凭证

### 生成 SSH 密钥对

首先，您需要在您的计算机上生成 SSH 公钥和私钥对。这个密钥对将用于认证过程，确保安全访问。

=== "Mac/Linux"

    1. 打开终端
    2. 输入命令：

        ```bash
        ssh-keygen -t rsa -b 4096
        ```

    3. 当系统提示您 “Enter a file in which to save the key”，您可以直接敲击 Enter 键使用默认路径，或者指定一个新的路径。
    4. 接下来，系统会提示您输入密码（可选），这将增加一个额外的安全层。如果选择输入密码，请记住这个密码，因为每次使用密钥时都会需要它。

=== "Windows"

    1. 安装 Git Bash（如果您尚未安装）
    2. 打开 Git Bash
    3. 输入命令：

        ```bash
        ssh-keygen -t rsa -b 4096
        ```

    4. 同 Mac/Linux 步骤

### 添加 SSH 公钥到个人中心（可选）

1. 打开生成的公钥文件，通常位于 `~/.ssh/id_rsa.pub`（如果您没有更改默认路径）
2. 复制公钥内容
3. 登录到系统的个人中心
4. 寻找 SSH 公钥配置区域，将复制的公钥粘贴到指定位置
5. 保存更改

## 在 Notebook 中开启 SSH 访问

1. 登录到 Jupyter Notebook 的 Web 界面。
2. 寻找您想要启用 SSH 访问的 Notebook。
3. 在 Notebook 的设置或详情页面，找到 **开启 SSH 访问** 的选项并启用它。
4. 记录或复制显示的 SSH 访问命令。这个命令将用于后续步骤中的 SSH 连接。

## 不同环境下的 SSH 访问方式

### 访问示例

假设您获得的 SSH 访问命令如下：

```bash
ssh username@mockhost -p 2222
```

请将 `username` 替换为您的用户名，`mockhost` 替换为实际的主机名，`2222` 替换为实际的端口号。

### Windows

推荐使用 PuTTY 或 Git Bash 进行 SSH 连接。

=== "PuTTY"
  
    1. 打开 PuTTY
    2. 在 **Host Name (or IP address)** 栏输入 `mockhost`（实际的主机名）
    3. 输入端口号 `2222`（实际的端口号）
    4. 点击 **Open** 开始连接
    5. 第一次连接时，可能会提示验证服务器的身份，点击 **Yes**

=== "Git Bash"
  
    1. 打开 Git Bash
    2. 输入访问命令：

        ```bash
        ssh username@mockhost -p 2222
        ```

    3. 按 Enter 键

### Mac/Linux

1. 打开终端。
2. 输入访问命令：

    ```bash
    ssh username@mockhost -p 2222
    ```

3. 如果系统提示您接受主机的身份，请输入`yes`。

## 配合 IDE 实现远程开发

除了使用命令行工具进行 SSH 连接，您还可以利用现代 IDE 如 Visual Studio Code (VSCode) 和 PyCharm 的 SSH 远程连接功能，
直接在本地 IDE 中开发并利用远程服务器的资源。

=== "在 VSCode 中使用 SSH 远程连接"

    VSCode 通过 **Remote - SSH** 扩展支持 SSH 远程连接，允许您直接在本地 VSCode 环境中编辑远程服务器上的文件，并运行命令。

    操作步骤为：

    1. 确保您已安装 VSCode 和 **Remote - SSH** 扩展。
    2. 打开 VSCode，点击左侧活动栏底部的远程资源管理器图标。
    3. 选择 **Remote-SSH: Connect to Host...** 选项，然后点击 **+ Add New SSH Host...**
    4. 输入 SSH 连接命令，例如：

        ```bash
        ssh username@mockhost -p 2222
        ```

    5. 敲击 Enter 键。请将 username、mockhost 和 2222 替换为实际的用户名、主机名和端口号。
    6. 选择一个配置文件来保存此 SSH 主机，通常选择默认即可。

    完成后，您的 SSH 主机将添加到 SSH 目标列表中。点击您的主机进行连接。
    如果是第一次连接，可能会提示您验证主机的指纹。接受后，您将被要求输入密码（如果 SSH 密钥设置了密码）。
    连接成功后，您可以像在本地开发一样在 VSCode 中编辑远程文件，并利用远程资源。

=== "在 PyCharm 中使用 SSH 远程连接"

    PyCharm Professional 版支持通过 SSH 连接到远程服务器，并在本地 PyCharm 中直接开发。

    操作步骤为：

    1. 打开 PyCharm，并打开或创建一个项目
    2. 选择 **File** -> **Settings** （在 Mac 上是 **PyCharm** -> **Preferences**
    3. 在设置窗口中，导航到 **Project: YourProjectName** -> **Python Interpreter**
    4. 点击右上角的齿轮图标，选择 **Add...**
        - 在弹出的窗口中，选择 **SSH Interpreter**
        - 输入远程主机的信息：主机名（mockhost）、端口号（2222）、用户名（username）。
        请使用您的实际信息替换这些占位符。
        - 点击 **Next** ，PyCharm 将尝试连接到远程服务器。如果连接成功，您将被要求输入密码或选择私钥文件。

    5. 配置完成后，点击 **Finish** 。现在，您的 PyCharm 将使用远程服务器上的 Python 解释器。

## 安全限制

在同一个 Workspace 内，任意用户都可以通过自己的 SSH 访问凭证来登录到启用了 SSH 的 Notebook。
这意味着，只要用户配置了自己的 SSH 公钥到个人中心，并且 Notebook 启用了 SSH 访问，就可以使用 SSH 进行安全连接。

请注意，不同用户的访问权限可能会根据 Workspace 的配置而有所不同。确保您了解并遵守您所在组织的安全和访问策略。

---

通过遵循上述步骤，您应该能够成功配置并使用 SSH 访问 Jupyter Notebook。如果遇到任何问题，请参考系统帮助文档或联系系统管理员。
