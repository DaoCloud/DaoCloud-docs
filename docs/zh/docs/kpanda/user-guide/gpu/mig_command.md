# MIG 相关命令

MIG 相关命令

| 主命令                                                  | 子命令                                                       | 说明                                                         |
| :------------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| GI                                                      | $ nvidia-smi mig -lgi                                        | 查看创建gi实例列表                                           |
| $ nvidia-smi mig -dgi -gi {Instance ID}                 | 删除指定的gi实例                                             |                                                              |
| $ nvidia-smi mig -lgip                                  | 查看gi 的profile                                             |                                                              |
| $ nvidia-smi mig -cgi {profile id}                      | 通过指定profile 的 id 创建gi.                                |                                                              |
| CI                                                      | $ nvidia-smi mig -lcip  { -gi {gi Instance ID}}              | 查看ci的profile，如果指定 -gi 则查看指定 gi 实例可以创建的ci. |
| $ nvidia-smi mig -lci                                   | 查看创建的ci实例列表                                         |                                                              |
| $ nvidia-smi mig -cci {profile id} -gi {gi instance id} | 指定的gi创建ci实例                                           |                                                              |
| $ nvidia-smi mig -dci -ci {ci instance id}              | 删除指定ci实例                                               |                                                              |
| GI+CI                                                   | `$ nvidia-smi mig -i 0 -cgi {gi profile id} -C {ci profile id}` | 直接创建GI + CI 实例                                         |

