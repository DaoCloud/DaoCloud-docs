# JWT feature of the microservice gateway

The microservice engine gateway supports JWT validation. Here"s how to use this feature.

## Prerequisites

- [Create a cluster](../../kpanda/user-guide/clusters/create-cluster.md) OR [Integrate a cluster](../../kpanda/user-guide/clusters/integrate-cluster.md)
- [Create a gateway](../gateway/index.md)
- Prepare a Token and the JWKS application used to validate the Token. If you do not already have a JWKS application, see [Create JWKS App](#jwks) to create one.

## Operation procedure

1. Reference [Create Domain](../gateway/domain/index.md) create a protocol for `https` domain, in the domain security policy enabled `JWT Auth`.

    - JWKS name: Unique JWKS name that identifies a specific JWT policy. This parameter is mandatory
    - JWKS Server Address: Returns the full FQDN address of the JWT service for the JWKS content. This parameter is mandatory
    - Token Transparent transmission: Whether to send the Token information of the JWT to the back-end service
    - Issuer: indicates the authentication of the Token issuer. If the value is not specified, the verification will not be performed
    - Audiences: audiences of the Token, if not filled in, no verification is performed
    - Token cache duration: Indicates the cache duration of the JWKS memory. The JWKS server address is not requested repeatedly within the cache validity period
    - Authentication timeout duration: Response timeout duration of the JWKS server. Obtaining JWKS fails after the timeout duration

        <!--![]()screenshots-->

2. See [Add API](../gateway/api/index.md) to create the API and enable the JWT authentication security policy.

    <!--![]()screenshots-->

3. With the Token access authentication, if the access succeeds, the JWT policy is successfully configured

    <!--![]()screenshots-->

## Create the JWKS application

If no JWKS application exists in the current environment, follow the following steps to deploy an application.

1. Download the JWKS generator code locally.

    ```
    git clone https://github.com/projectsesame/jwks-generator
    ```

2. Run the JWKS generator locally.

    ```
    mvn package -DskipTests && java -jar target/ROOT.war
    ```

    Go to <http://localhost:8080>. If the following screen appears, the JWKS generator is running locally successfully.

    <!--![]()screenshots-->

3. Refer to the instructions below to fill in the information, click `Generate` to generate the JWKS content.

    - KeySize: Generates the size of secret. Enter 256
    - KeyUse: Use, select a signature
    - Algorithm: indicates the algorithm. Select HS256
    - KeyID: Optional, matching parameter when JWKS has multiple values

        <!--![]()screenshots-->

4. Copy the value of `k` in the figure above and access <https://jwt.io> to generate a Token.

      - The algorithm selects HS256
      - Paste the copied k value into secret and check `secret base64 encoded`

        <!--![]()screenshots-->

5. Create the YAML file based on [YAML Template](https://github.com/projectsesame/enovy-remote-jwks-go/blob/main/all-in-one.yaml), and then install the JWKS application using the `kubectl apply` command

    - Change `namespace` to the namespace where the gateway resides, in this example `envoy-yang`
    - Change `jwks.json` to the JWKS content generated in Step 3 above

        <!--![]()screenshots-->

    ??? note "The YAML file configured in this example is shown below"

        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          labels:
            app: remote-jwks-go
          name: remote-jwks-go
          namespace: envoy-yang
        spec:
          selector:
            matchLabels:
              app: remote-jwks-go
          template:
            metadata:
              labels:
                app: remote-jwks-go
            spec:
              containers:
                - args:
                    - jwks
                    - -c
                    - /app/jwks.json
                  command:
                    - main
                  image: release-ci.daocloud.io/skoala/demo/remote-jwks-go:0.1.0
                  imagePullPolicy: IfNotPresent
                  name: remote-jwks-go
                  ports:
                    - containerPort: 8080
                      name: http
                      protocol: TCP
                  volumeMounts:
                    - name: config
                      mountPath: /app/jwks.json
                      subPath: jwks.json
              volumes:
                - name: config
                  configMap:
                    name: jwks-config
              restartPolicy: Always
              securityContext:
                runAsNonRoot: true
                runAsUser: 65534
                runAsGroup: 65534

        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: remote-jwks-go
          namespace: envoy-yang
          labels:
            app: remote-jwks-go
        spec:
          type: NodePort
          ports:
            - port: 8080
              targetPort: http
              protocol: TCP
              name: http
          selector:
            app: remote-jwks-go

        ---
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: jwks-config
          namespace: envoy-yang
          labels:
            app: remote-jwks-go
        data:
          jwks.json: |+
            {
              "keys": [
                {
                "kty": "oct",
                "use": "sig",
                "k": "veb4HPc6oaEAsCikZ7rzTKmu9LkOU4LpDUKBxFjnBcc",
                "alg": "HS256"
            }
              ]
            }
        ```

6. The `8080` port of the application is accessed. If `success` is displayed, the application is successfully installed.

    JWKS address should be composed of `gateway url/jwks`, e.g. <http://13.5.245.34:31456/jwks>

    > You can view the gateway address on the gateway overview page of the Micro Service Engine.

    <!--![]()screenshots-->
