# Customizing DCE 5.0 Integration with IdP

Identity Provider (IdP): When DCE 5.0 needs to use a client system as the user source
and authenticate users through the client system's login interface, that client system
is referred to as the Identity Provider for DCE 5.

## Use Cases

If there is a high customization requirement for the Ghippo login IdP, such as
supporting WeCom, WeChat, or other social organization login requirements,
please refer to this document for implementation.

## Supported Versions

Ghippo 0.15.0 and above.

## Specific Steps

### Customizing Ghippo Keycloak Plugin

1. Customize the plugin

    Refer to the [official keycloak documentation](https://www.keycloak.org/guides#getting-started) and [customizing Keycloak IdP](./keycloak-idp.md) for development.

2. Build the image

    ```sh
    # FROM scratch
    FROM scratch
   
    # plugin
    COPY ./xxx-jar-with-dependencies.jar /plugins/
    ```

!!! note

    If you need two customized IdPs, you need to copy two jar packages.

### Deploying Ghippo Keycloak Plugin Steps

1. [Upgrade Ghippo to version 0.15.0 or above](../install/offline-install.md).
   You can also directly install and deploy Ghippo version 0.15.0, but make sure to
   manually record the following information.

    ```sh
    helm -n ghippo-system get values ghippo -o yaml
    ```

    ```yaml
    apiserver:
      image:
        repository: release.daocloud.io/ghippo-ci/ghippo-apiserver
        tag: v0.4.2-test-3-gaba5ec2
    controllermanager:
      image:
        repository: release.daocloud.io/ghippo-ci/ghippo-apiserver
        tag: v0.4.2-test-3-gaba5ec2
    global:
      database:
        builtIn: true
      reverseProxy: http://192.168.31.10:32628
    ```

1. After a successful upgrade, manually run an installation command with the values
   for the parameters obtained from the saved content mentioned above, along with
   additional parameter values:

    - global.idpPlugin.enabled: Whether to enable the custom plugin, default is disabled.
    - global.idpPlugin.image.repository: The image address used by the initContainer to initialize the custom plugin.
    - global.idpPlugin.image.tag: The image tag used by the initContainer to initialize the custom plugin.
    - global.idpPlugin.path: The directory file of the custom plugin within the above image.

    Here is an example:

    ```sh
    helm upgrade \
        ghippo \
        ghippo-release/ghippo \
        --version v0.4.2-test-3-gaba5ec2 \
        -n ghippo-system \
        --set apiserver.image.repository=release.daocloud.io/ghippo-ci/ghippo-apiserver \
        --set apiserver.image.tag=v0.4.2-test-3-gaba5ec2 \
        --set controllermanager.image.repository=release.daocloud.io/ghippo-ci/ghippo-apiserver \
        --set controllermanager.image.tag=v0.4.2-test-3-gaba5ec2 \
        --set global.reverseProxy=http://192.168.31.10:32628 \
        --set global.database.builtIn=true \
        --set global.idpPlugin.enabled=true \
        --set global.idpPlugin.image.repository=chenyang-idp \
        --set global.idpPlugin.image.tag=v0.0.1 \
        --set global.idpPlugin.path=/plugins/.
    ```

1. Select the desired plugin on the Keycloak administration page.
