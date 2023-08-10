---
hide:
  - toc
---

# Login infinite loop, error 401 or 403

The reason for this problem is: the Mysql database connected to ghippo-keycloak fails, causing `OIDC Public keys` to be reset

In the global management version 0.11.1 and above, you can refer to the following steps to use `helm` to update the global management configuration file to return to normal.

```shell
# Update the helm repository
helm repo update ghippo

# Backup ghippo parameters
helm get values ​​ghippo -n ghippo-system -o yaml > ghippo-values-bak.yaml

# Get the currently deployed ghippo version number
version=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')

# Run the update operation to make the configuration file take effect
helm upgrade ghippo ghippo/ghippo \
-n ghippo-system\
-f ./ghippo-values-bak.yaml \
--version ${version}
```