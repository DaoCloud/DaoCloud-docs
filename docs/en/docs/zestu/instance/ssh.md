# SSH

**SSH (Secure Shell)** is a network protocol that enables secure remote login and command execution over insecure networks.  
Using SSH, users can securely access container instances on the platform from their local machines.

## Log in to a Container Instance Using SSH Username/Password

1. In the container’s terminal, install the `openssh-server` service.

    If it's already installed, you may skip this step and proceed to Step 2.

    - Run the following command to install the SSH server:

        ```bash
        apt-get update && apt install openssh-server
        ```

    - Verify the installation:

        - Check for SSH processes:

            ```bash
            ps -e | grep ssh
            ```

        - Check installed packages:

            ```bash
            dpkg -l | grep ssh
            ```

2. After the container starts, click the **SSH Login** button in the container instance list to open a dialog with login information.

    <!-- ![ssh1](../images/ssh1.png) -->

3. Use the provided username and password in your local terminal to log in. If successful, you'll see a confirmation message:

    <!-- ![ssh2](../images/ssh2.png) -->

## Passwordless SSH Login

After importing your SSH public key in **User Center** → **SSH Keys**, newly created or restarted instances will support passwordless login.

### Step 1: Check for Existing SSH Public Key

Before generating a new SSH key, check if you already have one. SSH key pairs are usually stored in the local user’s home directory.

For Linux/macOS, use the commands below.  
Windows users can use WSL (Windows 10+) or Git Bash.

- **ED25519 key:**

    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```

- **RSA key:**

    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

If a long string starting with `ssh-ed25519` or `ssh-rsa` is returned, a key already exists.  
You may skip [Step 2](#step-2-generate-ssh-key) and proceed to [Step 3](#step-3-copy-public-key).

### Step 2: Generate SSH Key

If [Step 1](#step-1-check-for-existing-ssh-public-key) returns nothing, generate a new SSH key:

1. Open your terminal (on Windows, use [WSL](https://docs.microsoft.com/zh-cn/windows/wsl/install) or [Git Bash](https://gitforwindows.org/)) and run `ssh-keygen`.

2. Choose the algorithm and optional comment (usually your email address):

    - For **ED25519**:

        ```bash
        ssh-keygen -t ed25519 -C "<your-comment>"
        ```

    - For **RSA**:

        ```bash
        ssh-keygen -t rsa -C "<your-comment>"
        ```

3. Press Enter to accept the default save path:

    Example (ED25519):

    ```console
    Enter file in which to save the key (/home/user/.ssh/id_ed25519):
    ```

    - Private key: `/home/user/.ssh/id_ed25519`  
    - Public key: `/home/user/.ssh/id_ed25519.pub`

4. Optionally set a passphrase:

    ```console
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    ```

    You can leave it empty to avoid entering a password every time.

5. Press Enter to complete the key pair generation.

### Step 3: Copy Public Key

You can either copy the key manually from the terminal or use one of the following commands depending on your OS:

- **Windows** (in [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) or [Git Bash](https://gitforwindows.org/)):

    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```

- **macOS**:

    ```bash
    tr -d '\n' < ~/.ssh/id_ed25519.pub | pbcopy
    ```

- **GNU/Linux** (requires `xclip`):

    ```bash
    xclip -sel clip < ~/.ssh/id_ed25519.pub
    ```

### Step 4: Add SSH Key on the Platform

1. Log in to the **d.run** UI, and go to **User Center** → **SSH Keys**.

    <!-- ![ssh3](../images/ssh3.png) -->

2. Paste your SSH public key into the input field.

    <!-- ![ssh4](../images/ssh4.png)

    ![ssh5](../images/ssh5.png) -->

    - **Key Title**: A name to help you identify the key.
    - **Expiration Time**: Set a key expiration date. The key becomes invalid after that time. Leave blank for permanent validity.
