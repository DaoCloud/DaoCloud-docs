---
hide:
  - toc
---

# Access Management

Access Management on the d.run platform enables users to expose services to the public internet. It allows exposing any container port externally—except for reserved ports: **22/5555/6666/10001/10002**.

This guide uses **nginx** as an example to demonstrate how to open a port using the container instance's access management feature. The generated external access URL can be used by anyone to access the service.

## Prerequisites

- Logged in to your d.run account
- A container instance has already been [created via Compute Cloud](../instance.md), and its status is **Running**

## Steps

1. Log in to your **d.run** account. In the top navigation bar, click **Compute Cloud**, then click **Container Instances** in the left sidebar. Choose the container instance you want to configure.

    <!-- ![Container Instance List](../images/ins1.png) -->

2. On the container instance list page, click **SSH Login** and log in to the container instance via SSH.

    <!-- ![SSH Login 1](../images/sshsecret.png) -->
    
    ![SSH Login 2](../images/terminal1.jpeg)

3. Install and start the **nginx** service.

    ```bash
    apt update
    apt install -y nginx && nginx && ps -ef | grep master
    apt install lsof # install lsof
    ```

4. The default port for nginx is **80**. Check whether nginx started properly:

    ```bash
    lsof -i:80
    ```
    
    If nginx is running correctly, you should see output like this:

    ```bash
    COMMAND  PID USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
    nginx   2693 root    6u  IPv4 723250562      0t0  TCP *:80 (LISTEN)
    nginx   2693 root    7u  IPv6 723250563      0t0  TCP *:80 (LISTEN)
    ```

5. Add **port 80** to the Access Management section and wait for the external port to be assigned (this usually takes around 1 minute).

    <!-- ![Open Port 2](../images/openport2.png)
    
    ![Open Port 3](../images/openport3.png) -->

6. Click the generated **external access link** to access the nginx service.

    ![nginx1](../images/NGINX1.png)
