# Microservice Configuration List

The microservice engine supports group management of microservices based on the microservice namespace, so that you can flexibly manage microservices and a large number of configurations of Spring according to your needs by grouping environment, application, and module. The configuration list mainly provides core management capabilities, such as adding, deleting, modifying, checking, viewing historical versions, rolling back, and subscriber query of microservice configurations.

## New configuration

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. Click __Configuration List__ in the left navigation bar, then click __Create__ in the upper right corner.

    ![Choose configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config02.png)

3. Enter the configuration information

    ![Enter the configuration information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config03.png)

    - Namespace: Select the microservice namespace to which the current configuration belongs. The default is `public`

        !!! note

            Services and configurations in different namespaces are strictly isolated and cannot reference each other. For example, A service in namespace A cannot reference a configuration in namespace B.

    - Data ID: indicates the name of the current configuration file. The Data ids in the same group cannot be the same.

        The full format is `${prefix}-${spring.profiles.active}.${file-extension}`.

        -  `prefix` default to `spring.application.name` value, can also through the configmaps `spring.cloud.nacos.config.prefix` to configure.
        -  `spring.profiles.active` Indicates the profile of the current environment. For details, see the Spring Boot documentation. Note: When `spring.profiles.active` is empty, the corresponding concatenator `-` also does not exist, and the Data ID concatenation format becomes `${prefix}.${file-extension}`.
        -  `file-exetension` Indicates the data format of the configuration content. You can configure the configmap `spring.cloud.nacos.config.file-extension`.

    - Group: Select the group to which the current configuration belongs. The default value is `DEFAULT_GROUP`.

        !!! note
  
            Namespaces are typically used to isolate environments and groups to separate projects.

    - Configuration format: Sets the format of the current configuration file.

    - Configuration content: Enter a configmap in the service source code with an annotation `@Value`.

        - Format verification is supported. If the format of the configuration is incorrect, the system automatically displays an error message.
        - ConfigMaps in the service source code with annotations `@RefreshScope` support dynamic updates.

    - More Configurations -> Owning Application (Optional) : Select the application to which the current configuration belongs.

       ![More configurations](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config04.png)

4. Click __OK__ in the bottom right corner of the page.

## Viewing configuration

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. In the left navigation bar, click __Configuration Management__ and click the Data ID of the target configuration.

    ![Choose configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config05.png)

3. You can view the basic configuration information, configuration content, historical version, listener, and example code.

    - Novice users can quickly consume this configuration using client-side programming with the help of sample code, lowering the threshold for novice users.
    - You can query the listener of the current configuration and the MD5 checksum to learn about the microservice that is using this configuration and whether the configuration changes are successfully pushed to the client.

    ![View configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config06.png)

## The historical version is rolled back

The microservice configuration list records the historical version of the configuration file and supports one-click rollback to a specific historical version. This helps users quickly recover incorrect configurations and reduces configuration availability risks in the microservice system. Comparison between the current version and the target rollback version is supported during the rollback. This helps you verify the changes and reduce risks caused by error correction.

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. In the left navigation bar, click __Configuration Management__ and click the Data ID of the target configuration.

    ![Choose configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config05.png)

3. Click the __History Version__ tab to find the corresponding record. Click __ⵗ__ on the right of the record and select __Rollback__ .

    ![View history version](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config07.png)

4. Compare the version differences and confirm, then click __Rollback__ in the lower right corner.

    ![Rollback](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config08.png)

## The GA configuration was updated

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. Click __Configuration Management__ in the left navigation bar, and click __ⵗ__ on the right of the target configuration and select __Edit GA Release__ .

    ![Edit GA release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config09.png)

3. Modify configuration content，and click __GA Release__ 。

    ![Update GA release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config10.png)

## New Beta configuration

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. Click __Configuration Management__ in the left navigation bar, and click __ⵗ__ on the right of the target configuration and select __Edit GA Release__ .

    ![Edit GA release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config09.png)

3. Enable  __Beta Release`, select service instance from the `Beta IP__ dropdown menu, modify the configuration content, and click __Beta Release__ .
   
    - When configuring Beta release, the Data ID of the configuration needs to match the microservice name. Otherwise, it will not be possible to select service instance.

    ![Create beta release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config11.png)

## The Beta configuration was updated

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. Click __Configuration Management__ in the left navigation bar, and click __ⵗ__ on the right of the target configuration and select __Edit Beta Release__ .

    ![Edit beta release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config12.png)

3. Modify configuration content，and click button in the lower right corner to delete beta release or publish GA release as required.

    - Click __Delete Beta__ ，then the beta configuration will be deleted.
    - Click __GA Release__ ,then the beta configuration will be published as GA release，and the original GA release will be deleted and is no longer effective.

    ![Update beta release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config13.png)

## The configuration was deleted

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![Choose hosted registry](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config01.png)

2. Click __Configuration Management__ in the left navigation bar, and click __ⵗ__ on the right of the target configuration to delete.

    ![Delete configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/config09.png)
