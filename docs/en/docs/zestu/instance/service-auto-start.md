# Auto-Start Services in Container Instances

Each container instance in Compute Cloud includes an **s6 supervisor daemon** that automatically starts designated services at boot time.  
To enable auto-start for your custom service, simply register it with **s6**.

## Prerequisites

- Logged in to your d.run account  
- A container instance has been [created via Compute Cloud](../instance.md), and its status is **Running**

## Register a Custom Service

Create a directory under `/etc/s6/` with the name of your service, and inside it, create a Bash script named `run`.  
Place the service startup command inside the `run` script.

!!! note

    After registering a custom service, you must **shut down and save** the container image.  
    This ensures the configuration is persisted and the service will auto-start on the next boot.

### Example 1: Auto-start Nginx

```bash
mkdir /etc/s6/nginx  # Register a custom service
cat <<EOF > /etc/s6/nginx/run  # Create the service start script
#!/bin/bash

echo "Starting Nginx..."

exec nginx  # Start nginx
EOF
```

### Example 2: Auto-start a Python HTTP Script

```bash
mkdir /etc/s6/python_http  # Register a custom service
cat <<EOF > /etc/s6/python_http/run  # Create the service start script
#!/bin/bash

echo "Starting python http..."

exec python /root/data/http.py
EOF
```
