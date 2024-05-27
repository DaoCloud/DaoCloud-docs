# Keycloak Unable to Start

*[Ghippo]: The dev code for DCE 5.0 Global Management

## Common Issues

### Symptoms

MySQL is ready with no errors. After installing the global management, Keycloak fails to start (more than 10 times).

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart01.png)

### Checklist

- If the database is MySQL, check if the Keycloak database encoding is UTF8.
- Check the network connection from Keycloak to the database, ensure the database resources
  are sufficient, including but not limited to resource limits, storage space, and physical machine resources.

### Troubleshooting Steps

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart02.png)

1. Check if MySQL resource usage has reached the limit
2. Check if the number of tables in the Keycloak database in MySQL is 92
3. Delete and recreate the Keycloak database with the command
   **CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8**
4. Restart the Keycloak Pod to resolve the issue

## CPU does not support ×86-64-v2

### Symptoms

Keycloak cannot start normally, the Keycloak pod is in the `CrashLoopBackOff` state, and the Keycloak log shows:

![img.png](../images/14.png)

### Checklist

Run the following script to check the supported CPU types:

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

### Solution

1. Since this issue is caused by a Keycloak upgrade (Ghippo v0.27.0), roll back Ghippo to the previous version (Ghippo < v0.27.0).
2. Upgrade your virtual machine or physical machine CPU type to support x86-64-v3 or above.
   For upgrading, you may need to consult your virtual machine platform provider or physical machine provider.
