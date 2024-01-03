---
hide:
  - toc
---

# Login loop with error 401 or 403

This issue occurs when the MySQL database connected to ghippo-keycloak encounters a failure, causing the __OIDC Public keys__ to be reset.

For Global Management version 0.11.1 and above, you can follow these steps to restore normal operation by updating the Global Management configuration file using __helm__ .

```shell
# Update helm repository
helm repo update ghippo

# Backup ghippo parameters
helm get values ghippo -n ghippo-system -o yaml > ghippo-values-bak.yaml

# Get the current deployed ghippo version
version=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')

# Perform the update operation to make the configuration file take effect
helm upgrade ghippo ghippo/ghippo \
-n ghippo-system \
-f ./ghippo-values-bak.yaml \
--version ${version}
```
