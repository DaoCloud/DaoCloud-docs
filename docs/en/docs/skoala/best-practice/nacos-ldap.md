# Nacos LDAP Integration for User Management

Nacos is called Service Registry in DCE Microservice Engine.
This article explains how to manage users by integrating Nacos with LDAP (Lightweight Directory Access Protocol).

## Deploy LDAP on Kubernetes

First deploy ldap.yaml

```shell
kubectl apply -f ldap.yaml
```

```yaml title="ldap.yaml"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ldap
  labels:
    app: ldap
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ldap
  template:
    metadata:
      labels:
        app: ldap
    spec:
      containers:
        - name: ldap
          image: docker.m.daocloud.io/osixia/openldap:latest
          volumeMounts:
            - name: ldap-data
              mountPath: /var/lib/ldap
            - name: ldap-config
              mountPath: /etc/ldap/slapd.d
            - name: ldap-certs
              mountPath: /container/service/slapd/assets/certs
          ports:
            - containerPort: 389
              name: openldap
          env:
            - name: LDAP_LOG_LEVEL
              value: "256"
            - name: LDAP_ORGANISATION
              value: "Example Inc."
            - name: LDAP_DOMAIN
              value: "example.org"
            - name: LDAP_ADMIN_PASSWORD
              value: "admin"
            - name: LDAP_CONFIG_PASSWORD
              value: "config"
            - name: LDAP_READONLY_USER
              value: "false"
            - name: LDAP_READONLY_USER_USERNAME
              value: "readonly"
            - name: LDAP_READONLY_USER_PASSWORD
              value: "readonly"
            - name: LDAP_RFC2307BIS_SCHEMA
              value: "false"
            - name: LDAP_BACKEND
              value: "mdb"
            - name: LDAP_TLS
              value: "true"
            - name: LDAP_TLS_CRT_FILENAME
              value: "ldap.crt"
            - name: LDAP_TLS_KEY_FILENAME
              value: "ldap.key"
            - name: LDAP_TLS_CA_CRT_FILENAME
              value: "ca.crt"
            - name: LDAP_TLS_ENFORCE
              value: "false"
            - name: LDAP_TLS_CIPHER_SUITE
              value: "SECURE256:+SECURE128:-VERS-TLS-ALL:+VERS-TLS1.2:-RSA:-DHE-DSS:-CAMELLIA-128-CBC:-CAMELLIA-256-CBC"
            - name: LDAP_TLS_VERIFY_CLIENT
              value: "demand"
            - name: LDAP_REPLICATION
              value: "false"
            - name: LDAP_REPLICATION_CONFIG_SYNCPROV
              value: "binddn=\"cn=admin,cn=config\" bindmethod=simple credentials=$LDAP_CONFIG_PASSWORD searchbase=\"cn=config\" type=refreshAndPersist retry=\"60 +\" timeout=1 starttls=critical"
            - name: LDAP_REPLICATION_DB_SYNCPROV
              value: "binddn=\"cn=admin,$LDAP_BASE_DN\" bindmethod=simple credentials=$LDAP_ADMIN_PASSWORD searchbase=\"$LDAP_BASE_DN\" type=refreshAndPersist interval=00:00:00:10 retry=\"60 +\" timeout=1 starttls=critical"
            - name: LDAP_REPLICATION_HOSTS
              value: "#PYTHON2BASH:['ldap://ldap-one-service', 'ldap://ldap-two-service']"
            - name: KEEP_EXISTING_CONFIG
              value: "false"
            - name: LDAP_REMOVE_CONFIG_AFTER_SETUP
              value: "true"
            - name: LDAP_SSL_HELPER_PREFIX
              value: "ldap"
      volumes:
        - name: ldap-data
          hostPath:
            path: "/data/ldap/db"
        - name: ldap-config
          hostPath:
            path: "/data/ldap/config"
        - name: ldap-certs
          hostPath:
            path: "/data/ldap/certs"
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: ldap
  name: ldap-service
spec:
  ports:
    - port: 389
  type: NodePort
  selector:
    app: ldap
```

Then deploy phpadmin.yaml: <a id="phpadmin" />

```shell
kubectl apply -f phpadmin.yaml
```

```yaml title="phpadmin.yaml"
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    kompose.cmd: kompose convert -f docker-compose.yml
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: phpldapadmin
  name: phpldapadmin
spec:
  replicas: 1
  selector:
    matchLabels:
      io.kompose.service: phpldapadmin
  template:
    metadata:
      creationTimestamp: null
      labels:
        io.kompose.service: phpldapadmin
    spec:
      containers:
      - env:
        - name: PHPLDAPADMIN_HTTPS
          value: "false"
        - name: PHPLDAPADMIN_LDAP_HOSTS
          value: ldap-service
        image: docker.m.daocloud.io/osixia/phpldapadmin:latest
        name: phpldapadmin
        ports:
        - containerPort: 80
      restartPolicy: Always
---
apiVersion: v1
kind: Service
metadata:
  annotations:
    kompose.cmd: kompose convert -f docker-compose.yml
    kompose.version: 1.16.0 (0c01309)
  labels:
    io.kompose.service: phpldapadmin
  name: phpldapadmin
spec:
  ports:
  - name: "8080"
    port: 8080
    targetPort: 80
  type: NodePort
  selector:
    io.kompose.service: phpldapadmin
```

## Deploy Nacos

Deploy Nacos on a virtual machine.

1. Download the installation package.

    ```shell
    cd /opt
    wget https://github.com/alibaba/nacos/releases/download/2.3.2/nacos-server-2.3.2.tar.gz
    ```

2. Configure LDAP.

    ```shell
    tar -zxvf nacos-server-2.3.2.tar.gz
    cd nacos/conf/
    ```

    Edit the application.properties file to enable authentication and configure the ldap connection information:

    ```config title="application.properties"
    nacos.core.auth.system.type=ldap
    nacos.core.auth.enabled=true
    nacos.core.auth.server.identity.key=DefaultIdentityKey
    nacos.core.auth.server.identity.value=DefaultIdentityValue
    nacos.core.auth.plugin.nacos.token.secret.key=RGFvY2xvdWRTa29hbGFOYWNvc0F1dGhTZWNyZXRLZXk=
    nacos.core.auth.ldap.url=ldap://10.6.176.50:30326   # the ldap connection address installed in the previous step, node ip:the mapped port of 389
    nacos.core.auth.ldap.basedc=dc=example,dc=org
    nacos.core.auth.ldap.userDn=cn=admin,${nacos.core.auth.ldap.basedc}
    nacos.core.auth.ldap.password=admin
    nacos.core.auth.ldap.userdn=cn={0},dc=example,dc=org
    nacos.core.auth.ldap.filter.prefix=uid
    nacos.core.auth.ldap.case.sensitive=true
    nacos.core.auth.ldap.ignore.partial.result.exception=false
    ```

3. Start Nacos.

    ```shell
    cd ../bin
    ./startup.sh -m standalone
    ```

    After startup, you can access Nacos through the page on port 8848, such as `http://10.6.222.10:8848/nacos`

    The username and password are: nacos/nacos

4. Deploy nacos-ldap.yaml for the microservice

    ```shell
    kubectl apply -f nacos-ldap.yaml
    ```

    ```yaml title="nacos-ldap.yaml"
    apiVersion: nacos.io/v1alpha1
    kind: Nacos
    metadata:
      labels:
        sidecar.istio.io/inject: 'false'
        skoala.io/type: nacos
      name: nacos-ldap
      namespace: skoala-demo
    spec:
      certification:
        enabled: true
        ldap:
          admin: admin    # the cn value in the login DN. For example, when the login DN is "cn=admin,dc=example,dc=org", this value is admin
          basedc: dc=example,dc=org   # the basedc of the ldap
          password: admin     # the password of the ldap admin account
          url: ldap://10.6.176.50:30326   # the ldap address
        token: RGFvY2xvdWRTa29hbGFOYWNvc0F1dGhTZWNyZXRLZXk=
        token_expire_seconds: '18000'
        type: ldap
      database:
        mysqlDb: nacosjvm
        mysqlHost: 10.6.222.10
        mysqlPassword: dangerous
        mysqlPort: '3306'
        mysqlUser: root
        type: mysql
      image: docker.m.daocloud.io/nacos/nacos-server:v2.3.2-slim
      jvm_percentage: 0.75
      mysqlInitImage: docker.m.daocloud.io/arey/mysql-client:latest
      replicas: 1
      resources:
        limits:
          cpu: '1'
          memory: 2Gi
        requests:
          cpu: 500m
          memory: 500Mi
      serviceType: NodePort
      type: standalone
      volume:
        requests:
          storage: 1Gi
        storageClass: default
    ```

## User Management

Create users through LDAP:

1. Access phpLDAPadmin through the page.

    The URL is [the address of the phpadmin deployed above](#phpadmin): `node IP:the mapped port of 8080`

    <!--![]()screenshots-->

2. Log in to phpLDAPadmin.

    Click __login__ on the left to log in:

    - Login DN is cn=admin,dc=example,dc=org
    - Password is admin

    After entering the Login DN and Password, click __Authenticate__

    <!--![]()screenshots-->

    <!--![]()screenshots-->

3. Create user groups and users.

    1. Click __dc=example,dc=org__ on the left and then click __Create a child entry__ ,
       select __Generic: Organisational Unit__ to create the Group entry

        <!--![]()screenshots-->
        <!--![]()screenshots-->
        <!--![]()screenshots-->
        <!--![]()screenshots-->

    2. Create the user group nacos under __ou=Group__

        <!--![]()screenshots-->
        <!--![]()screenshots-->
        <!--![]()screenshots-->
        <!--![]()screenshots-->

    3. Similarly, click __dc=example,dc=org__ on the left and then click __Create a child entry__ ,
       select __Generic: Organisational Unit__ to create the People entry

        <!--![]()screenshots-->
        <!--![]()screenshots-->

    4. Create the user bob under __ou=People__

        <!--![]()screenshots-->
        <!--![]()screenshots-->

    5. Fill in the parameters according to the figure below:

        <!--![]()screenshots-->
        <!--![]()screenshots-->
        <!--![]()screenshots-->

        - first name is b
        - last name is ob
        - Set the password to 123456
        - Select nacos for GID number

    Then click __Create Object__ , and then click __Commit__

4. Authorize the user in Nacos.

    1. Log in to the Nacos page using the user bob created in LDAP.

        The username/password is: bob/123456

        <!--![]()screenshots-->

        After login, the username becomes LDAP_bob, and LDAP_bob can be used as the username for subsequent logins.

        Note that the password of LDAP_bob is nacos, not 123456; the password of bob is still 123456 when logging in.

        <!--![]()screenshots-->

    2. Authorize the LDAP_bob user.

        1. Log in to the nacos page as the user nacos again. Go to the __Permission Control__ -> __User List__ page,
           and you can see the LDAP_bob user

            <!--![]()screenshots-->

        2. Go to the Role Management page and click __Bind Role__ to create a role for the user

            <!--![]()screenshots-->

        3. Go to the Permission Management page and click __Add Permission__ to bind the read-only permission
           of public to the role, then the LDAP_bob user only has the read-only permission under the public namespace.

            <!--![]()screenshots-->

!!! note

    After the user bob is added in the ldap, it becomes LDAP_bob after being synchronized to the nacos side.
    After the user bob is deleted in the ldap, LDAP_bob on the nacos side can still be used normally.
