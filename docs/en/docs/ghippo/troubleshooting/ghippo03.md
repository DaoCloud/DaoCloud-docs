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
2. Check if the number of tables in the MySQL database keycloak is 95. (The number of tables may
   vary across different versions of Keycloak, so you can compare it with the number of tables in
   the Keycloak database of the same version in development or testing environments). If the number
   is fewer, it indicates that there may be an issue with the database table initialization (The
   command to check the number of tables is: show tables;).
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
cat <<"EOF" > detect-cpu.sh
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

Execute the command below to check the current CPU features. If the output contains sse4_2, it indicates that your processor supports SSE 4.2.

```bash
lscpu | grep sse4_2
```

### Solution
You need to upgrade your virtual machine or physical machine CPU to support x86-64-v2 and above, ensuring that the x86 CPU instruction set supports SSE4.2. For details on how to upgrade, you should consult your virtual machine platform provider or your physical machine provider.

For more information, see: https://github.com/keycloak/keycloak/issues/17290