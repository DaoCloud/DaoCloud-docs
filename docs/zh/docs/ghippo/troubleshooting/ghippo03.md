# Keycloak 无法启动

*[Ghippo]: DCE 5.0 全局管理的开发代号

## 常见故障

### 故障表现

MySQL 已就绪，无报错。在安装全局管理后 keycloak 无法启动（> 10 次）。

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart01.png)

### 检查项

- 如果数据库是 MySQL，检查 keycloak database 编码是否是 UTF8。
- 检查从 keycloak 到数据库的网络，检查数据库资源是否充足，包括但不限于资源限制、存储空间、物理机资源。

### 解决步骤

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart02.png)

1. 检查 MySQL 资源占用是否到达 limit 限制
2. 检查 MySQL 中 database keycloak table 的数量是不是 92
3. 删除 keycloak database 并创建，提示 **CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8**
4. 重启 keycloak Pod 解决问题

## CPU does not support ×86-64-v2

### 故障表现

keycloak 无法正常启动，keycloak pod 运行状态为 `CrashLoopBackOff` 并且 keycloak 的 log 出现如下图所示的信息

![img.png](../images/14.png)

### 检查项
运行下面的检查脚本，查询当前节点 cpu 的 x86-64架构的特征级别
```bash
cat <<EOF > detect-cpu.sh
#!/bin/sh -eu

flags=$(cat /proc/cpuinfo | grep flags | head -n 1 | cut -d: -f2)

supports_v2='awk "/cx16/&&/lahf/&&/popcnt/&&/sse4_1/&&/sse4_2/&&/ssse3/ {found=1} END {exit !found}"'
supports_v3='awk "/avx/&&/avx2/&&/bmi1/&&/bmi2/&&/f16c/&&/fma/&&/abm/&&/movbe/&&/xsave/ {found=1} END {exit !found}"'
supports_v4='awk "/avx512f/&&/avx512bw/&&/avx512cd/&&/avx512dq/&&/avx512vl/ {found=1} END {exit !found}"'

echo "$flags" | eval $supports_v2 || exit 2 && echo "CPU supports x86-64-v2"
echo "$flags" | eval $supports_v3 || exit 3 && echo "CPU supports x86-64-v3"
echo "$flags" | eval $supports_v4 || exit 4 && echo "CPU supports x86-64-v4"
EOF

chmod +x detect-cpu.sh
sh detect-cpu.sh
```

执行下面命令查看当前 cpu 的特性，如果输出中包含 sse4_2，则表示你的处理器支持SSE 4.2。
```bash 
lscpu | grep sse4_2
```

### 解决方法
需要升级你的虚拟机或物理机 cpu 以支持 x86-64-v2 及以上，确保x86 cpu 指令集支持 sse4.2，如何升级需要你咨询虚拟机平台提供商或着物理机提供商。

详见：https://github.com/keycloak/keycloak/issues/17290
