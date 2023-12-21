# MIG 相关命令

GI 相关命名：

| 子命令                                  | 说明                          |
| --------------------------------------- | ----------------------------- |
| nvidia-smi mig -lgi                   | 查看创建 GI 实例列表          |
| nvidia-smi mig -dgi -gi {Instance ID} | 删除指定的 GI 实例            |
| nvidia-smi mig -lgip                  | 查看 GI 的 __profile__           |
| nvidia-smi mig -cgi {profile id}      | 通过指定 profile 的 ID 创建 GI |

CI 相关命令：

| 子命令                                                  | 说明                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| nvidia-smi mig -lcip  { -gi {gi Instance ID}}         | 查看 CI 的 __profile__ ，指定 __-gi__ 可以查看特定 GI 实例可以创建的 CI |
| nvidia-smi mig -lci                                   | 查看创建的 CI 实例列表                                       |
| nvidia-smi mig -cci {profile id} -gi {gi instance id} | 指定的 GI 创建 CI 实例                                       |
| nvidia-smi mig -dci -ci {ci instance id}              | 删除指定 CI 实例                                             |

GI+CI 相关命令：

| 子命令                                                       | 说明                 |
| ------------------------------------------------------------ | -------------------- |
| nvidia-smi mig -i 0 -cgi {gi profile id} -C {ci profile id} | 直接创建 GI + CI 实例 |
