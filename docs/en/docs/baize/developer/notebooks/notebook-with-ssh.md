---
MTPE: windsonsea
date: 2024-05-22
---

# Notebook SSH Guide

The intelligent computing power provided by Notebook supports local access via SSH;

With simple configuration, you can use SSH to access the Jupyter Notebook.
Whether you are using Windows, Mac, or Linux operating systems, you can follow the steps below.

## Configure SSH Credentials

### Generate SSH Key Pair

First, you need to generate an SSH public and private key pair on your computer. This key pair will be used for the authentication process to ensure secure access.

=== "Mac/Linux"

    1. Open the terminal.
    2. Enter the command:

        ```bash
        ssh-keygen -t rsa -b 4096
        ```

    3. When prompted with “Enter a file in which to save the key,” you can press Enter to use the default path or specify a new path.
    4. Next, you will be prompted to enter a passphrase (optional), which adds an extra layer of security. If you choose to enter a passphrase, remember it as you will need it each time you use the key.

=== "Windows"

    1. Install Git Bash (if you haven't already).
    2. Open Git Bash.
    3. Enter the command:

        ```bash
        ssh-keygen -t rsa -b 4096
        ```

    4. Follow the same steps as Mac/Linux.

### Add SSH Public Key to Personal Center

1. Open the generated public key file, usually located at `~/.ssh/id_rsa.pub` (if you did not change the default path).
2. Copy the public key content.
3. Log in to the system's personal center.
4. Look for the SSH public key configuration area and paste the copied public key into the designated location.
5. Save the changes.

## Enable SSH in Notebook

1. Log in to the Jupyter Notebook web interface.
2. Find the Notebook for which you want to enable SSH.
3. In the Notebook's settings or details page, find the option **Enable SSH** and enable it.
4. Record or copy the displayed SSH access command. This command will be used in subsequent steps for SSH connection.

## SSH in Different Environments

### Example

Assume the SSH command you obtained is as follows:

```bash
ssh username@mockhost -p 2222
```

Replace `username` with your username, `mockhost` with the actual hostname, and `2222` with the actual port number.

### Windows

It is recommended to use PuTTY or Git Bash for SSH connection.

=== "PuTTY"
  
    1. Open PuTTY.
    2. In the **Host Name (or IP address)** field, enter `mockhost` (the actual hostname).
    3. Enter the port number `2222` (the actual port number).
    4. Click **Open** to start the connection.
    5. On the first connection, you may be prompted to verify the server's identity. Click **Yes** .

=== "Git Bash"
  
    1. Open Git Bash.
    2. Enter the ssh command to access your machine:

        ```bash
        ssh username@mockhost -p 2222
        ```

    3. Press Enter.

### Mac/Linux

1. Open the terminal.
2. Enter the ssh command to access your machine

    ```bash
    ssh username@mockhost -p 2222
    ```

3. If prompted to accept the host's identity, type `yes`.

## Remote Development with IDE

In addition to using command line tools for SSH connection, you can also utilize modern IDEs such as Visual Studio Code (VSCode) and PyCharm's SSH remote connection feature to develop locally while utilizing remote server resources.

=== "Using SSH in VSCode"

    VSCode supports SSH remote connection through the **Remote - SSH** extension, allowing you to edit files on the remote server directly in the local VSCode environment and run commands.

    Steps:

    1. Ensure you have installed VSCode and the **Remote - SSH** extension.
    2. Open VSCode and click the remote resource manager icon at the bottom of the left activity bar.
    3. Select **Remote-SSH: Connect to Host...** and then click **+ Add New SSH Host...**
    4. Enter the SSH connection command, for example:

        ```bash
        ssh username@mockhost -p 2222
        ```

    5. Press Enter. Replace `username`, `mockhost`, and `2222` with your actual username, hostname, and port number.
    6. Select a configuration file to save this SSH host, usually the default is fine.

    After completing, your SSH host will be added to the SSH target list. Click your host to connect.
    If it's your first connection, you may be prompted to verify the host's fingerprint. After accepting, you will be asked to enter the passphrase (if the SSH key has a passphrase).
    Once connected successfully, you can edit remote files in VSCode and utilize remote resources just as if you were developing locally.

=== "Using SSH in PyCharm"

    PyCharm Professional Edition supports connecting to remote servers via SSH and directly developing in the local PyCharm.

    Steps:

    1. Open PyCharm and open or create a project.
    2. Select **File** -> **Settings** (on Mac, it's **PyCharm** -> **Preferences**).
    3. In the settings window, navigate to **Project: YourProjectName** -> **Python Interpreter**.
    4. Click the gear icon in the upper right corner and select **Add...**
        - In the pop-up window, select **SSH Interpreter**.
        - Enter the remote host information: hostname (`mockhost`), port number (`2222`), username (`username`).
        Replace these placeholders with your actual information.
        - Click **Next**. PyCharm will attempt to connect to the remote server. If the connection is successful, you will be asked to enter the passphrase or select the private key file.

    5. Once configured, click **Finish**. Now, your PyCharm will use the Python interpreter on the remote server.

## Security Restrictions

Within the same Workspace, any user can log in to a Notebook with SSH enabled using their own SSH credentials.
This means that as long as users have configured their SSH public key in the personal center and the Notebook has enabled SSH, they can use SSH for a secure connection.

Note that permissions for different users may vary depending on the Workspace configuration. Ensure you understand and comply with your organization's security and access policies.

---

By following the above steps, you should be able to successfully configure and use SSH to access the Jupyter Notebook. If you encounter any issues, refer to the system help documentation or contact the system administrator.
