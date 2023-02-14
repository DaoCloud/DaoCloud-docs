---
hide:
  - toc
---

# configuration reference

After installing Spiderpool, please edit the CNI configuration file in the `/etc/cni/net.d/` directory.

The following is a configuration example for MacVLAN CNI.

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
