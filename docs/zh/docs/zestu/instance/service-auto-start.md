# 容器实例内服务开机自启

在每一个算力云的容器实例中，都有一个 s6 守护进程，他会在开机时，将指定的服务自动拉起。
如果用户需要开启自启服务，只需要向 s6 中注册自己的自定义服务。

## 前提条件

- 登录 [d.run 账号](../../index.md)
- 已通过算力云[创建容器实例](../instance.md)，且容器实例状态为 **运行中**

## 注册自定义服务

在 `/etc/s6/` 目录下创建一个目录 <Your_service_name>，然后在这个目录下创建一个固定名称 `run` 的 Bash 脚本. 然后在 `run` 文件中填写服务启动命令。

!!! note
  
    注册自定义镜像后，需要关机保存镜像，这样才能将配置进行持久化。下次开机后，注册的自定义服务就会自动的启动了。

示例一：以 Nginx 举例

```bash
mkdir /etc/s6/nginx    # 注册自定义服务
cat <<EOF > /etc/s6/nginx/run  # 注册自定义服务的启动脚本
#!/bin/bash

echo "Starting Nginx..."

exec nginx         # 启动 nginx
EOF
```

示例二：以 Python 的 http 程序举例

```bash
mkdir /etc/s6/python_http    # 注册自定义服务
cat <<EOF > /etc/s6/python_http/run  # 注册自定义服务的启动脚本
#!/bin/bash

echo "Starting python http..."

exec python /root/data/http.py
EOF
```
