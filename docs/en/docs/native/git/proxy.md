# Git Proxy Settings

Proxy is commonly known as ladder, scientific internet access, crossing the firewall, etc. This is the first step to use GitHub.

For GitHub, sometimes even with proxy enabled, __git clone__ speed is still extremely slow, only a few KB per second, and often push timeout - this is unacceptable!

## Win10

Show hidden files, modify the __.gitconfig__ file in the user root directory on the system drive.

1. Find your HTTP proxy address and port number.

    ![http address and port](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/proxy1.png)

2. Find the __.gitconfig__ file in the system drive user root directory, for example on my computer:

    ```path
    C:\Users\michael\.gitconfig
    ```

3. Edit the __.gitconfig__ file, add these two lines at the bottom:

    ```bash
    [http]
        proxy = http://127.0.0.1:10809
    [https]
        proxy = https://127.0.0.1:10809
    ```

4. Save and exit, then run __git clone__ command again. The speed improved by 100 times, haha! My .gitconfig example configuration is as follows:
