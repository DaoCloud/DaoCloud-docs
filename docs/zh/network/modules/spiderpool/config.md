# 配置参考

安装 Spiderpool 之后，请在 `/etc/cni/net.d/` 目录编辑 CNI 配置文件。

以下是 macvlan CNI 的例子。

```json
{
  "cniVersion": "0.3.1",
  "type": "macvlan",
  "mode": "bridge",
  "master": "eth0",
  "name": "macvlan-cni-default",
  "ipam": {
    "type": "spiderpool"
  }
}
```
