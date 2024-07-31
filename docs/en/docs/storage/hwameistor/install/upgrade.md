---
hide:
  - toc
---

# Upgrade

Helm makes it very easy to upgrade HwameiStor. Just run the following command:

```sh
helm upgrade -n hwameistor hwameistor -f new.values.yaml
```

Each HwameiStor pod will be rebooted in a rolling manner during the upgrade.

!!! warning

    During the upgrade of HwameiStor, these volumes will continue to serve pods without interruption.
