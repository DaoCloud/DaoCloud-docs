# Customizing Keycloak Identity Provider (IdP)

Requirements: keycloak >= v20

Known issue in keycloak >= v21, support for old version themes has been removed and
may be fixed in v22. See [Issue #15344](https://github.com/keycloak/keycloak/issues/15344).

This demo uses Keycloak v20.0.5.

## Source-based Development

### Configure the Environment

Refer to [keycloak/building.md](https://github.com/keycloak/keycloak/blob/main/docs/building.md)
for environment configuration.

Run the following commands based on [keycloak/README.md](https://github.com/keycloak/keycloak/blob/main/quarkus/README.md):

```sh
cd quarkus
mvn -f ../pom.xml clean install -DskipTestsuite -DskipExamples -DskipTests
```

### Run from IDE

![Run from IDE](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp01.png)

### Add Service Code

#### If inheriting some functionality from Keycloak

Add files under the directory __services/src/main/java/org/keycloak/broker__ :

The file names should be __xxxProvider.java__ and __xxxProviderFactory.java__ .

![java](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp02.png)

**[xxxProviderFactory.java](./examples/xxxProviderFactory.java) example:**

Pay attention to the variable __PROVIDER_ID = "oauth";__ , as it will be used in the HTML definition later.

**[xxxProvider.java](./examples/xxxProvider.java) example:**

#### If unable to inherit functionality from Keycloak

Refer to the three files in the image below to write your own code:

![none heritance](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp03.png)

**Add xxxProviderFactory to resource service**

Add xxxProviderFactory to __services/src/main/resources/META-INF/services/org.keycloak.broker.provider.IdentityProviderFactory__ so that the newly added code can work:

![running](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp04.png)

**Add HTML file**

Copy the file __themes/src/main/resources/theme/base/admin/resources/partials/realm-identity-provider-oidc.html__ 
and rename it as __realm-identity-provider-oauth.html__ (remember the variable to pay attention to from earlier).

Place the copied file in __themes/src/main/resources/theme/base/admin/resources/partials/realm-identity-provider-oauth.html__ .

All the necessary files have been added. Now you can start debugging the functionality.

## Packaging as a JAR Plugin

Create a new Java project and copy the above code into the project, as shown below:

![pom](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp04.png)

Refer to [pom.xml](./examples/pom.xml).

Run __mvn clean package__ to package the code, resulting in the __xxx-jar-with-dependencies.jar__ file.

Download [Keycloak Release 20.0.5](https://github.com/keycloak/keycloak/releases/tag/20.0.5) zip package and extract it.

![release](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/oem/images/idp05.png)

Copy the __xxx-jar-with-dependencies.jar__ file to the __keycloak-20.0.5/providers__ directory.

Run the following command to check if the functionality is working correctly:

```sh
bin/kc.sh start-dev
```
