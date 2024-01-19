# Integrate Microservice Gateway with Rate Limit Server

The microservice gateway supports integration with third-party rate limit servers. This document demonstrates the steps to integrate with the default rate limit server.

## Prerequisites

- [Create a cluster](../../kpanda/user-guide/clusters/create-cluster.md) or [integrate an existing cluster](../../kpanda/user-guide/clusters/integrate-cluster.md)
- [Create a gateway](../gateway/index.md)

## Select a Rate Limit Server

You have the option to choose the default rate limit server or integrate your own.

### Default Rate Limit Server

Apply the provided rate limit server template directly. For specific logic, refer to the [rate limit server code](https://github.com/projectsesame/ratelimit).

```bash
kubectl apply -f gateway-rls.yaml -n plugin-ns
```

??? note "Default Rate Limit Server"

    ```yaml title="gateway-rls.yaml"
    ---
    # NOTE: this deployment is intended for demonstrating global
    # rate limiting functionality only and should NOT be considered
    # production-ready.

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: ratelimit
      name: gateway-rls
    spec:
      replicas: 1
      strategy:
        type: RollingUpdate
        rollingUpdate:
          # This value of maxSurge means that during a rolling update
          # the new ReplicaSet will be created first.
          maxSurge: 50%
      selector:
        matchLabels:
          app: ratelimit
      template:
        metadata:
          labels:
            app: ratelimit
        spec:
          affinity:
            podAntiAffinity:
              preferredDuringSchedulingIgnoredDuringExecution:
              - podAffinityTerm:
                  labelSelector:
                    matchLabels:
                      app: ratelimit
                  topologyKey: kubernetes.io/hostname
                weight: 100
          containers:
            - name: redis
              image: release-ci.daocloud.io/skoala/redis:6.2.6
              env:
                - name: REDIS_SOCKET_TYPE
                  value: tcp
                - name: REDIS_URL
                  value: redis:6379
            - name: ratelimit
              image: release-ci.daocloud.io/skoala/envoy-ratelimit:v2  # latest a/o Mar 24 2022
              ports:
                - containerPort: 8080
                  name: http
                  protocol: TCP
                - containerPort: 8081
                  name: grpc
                  protocol: TCP
                - containerPort: 6070
                  name: debug
                  protocol: TCP
              volumeMounts:
                - name: ratelimit-config
                  mountPath: /data/ratelimit/config
                  readOnly: true
              env:
                - name: USE_STATSD
                  value: "false"
                - name: LOG_LEVEL
                  value: debug
                - name: REDIS_SOCKET_TYPE
                  value: tcp
                - name: REDIS_URL
                  value: localhost:6379
                - name: RUNTIME_ROOT
                  value: /data
                - name: RUNTIME_SUBDIRECTORY
                  value: ratelimit
                - name: RUNTIME_WATCH_ROOT
                  value: "false"
                # need to set RUNTIME_IGNOREDOTFILES to true to avoid issues with
                # how Kubernetes mounts configmaps into pods.
                - name: RUNTIME_IGNOREDOTFILES
                  value: "true"
              command: ["/bin/ratelimit"]
              livenessProbe:
                httpGet:
                  path: /healthcheck
                  port: 8080
                initialDelaySeconds: 5
                periodSeconds: 5
          volumes:
            - name: ratelimit-config
              configMap:
                name: gateway-rls

    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: gateway-rls
    spec:
      ports:
      - port: 8081
        name: grpc
        protocol: TCP
      - port: 6070
        name: debug
        protocol: TCP
      selector:
        app: ratelimit
      type: NodePort

    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: gateway-rls
    data:
      ratelimit-config.yaml: |
        domain: gateway-rls.skoala-dev
        descriptors:
          - name: test1
            key: foo
            value: goo
            rate_limit:
              name: test1
              unit: Minute
              requests_per_unit: 20
            descriptors:
              - name: test2
                key: foo1
                value: goo1
                rate_limit:
                  name: test2
                  unit: Minute
                  requests_per_unit: 15
                descriptors:
                  - name: test3
                    key: foo2
                    value: goo2
                    rate_limit:
                      name: test3
                      unit: Minute
                      requests_per_unit: 10
    ```

### Integrating with a Rate Limit Server

1. Obtain the external access address of the gateway-rls deployed in the previous steps.

    ```bash
    kubectl get svc -n plugin-ns
    ```

    Rate Limit Server address: 10.6.222.21:32003

    Rate Limit Server configuration address: http://10.6.222.21:32004

    ```bash
    NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
    gateway-rls        NodePort   10.233.56.164   <none>        8081:32003/TCP,6070:32004/TCP   1m
    ```

2. Create a global rate limit plugin in the plugin center.

    - Rate Limit Response Header: Enable printing rate limit-related information in the response header.
    - Fast Success: Allow continuing to access requests when the rate limit server is unreachable.
    - Access Address: The address of the rate limit server, corresponding to port 8081, with the GRPC protocol.
    - Load Balancing Strategy: Access strategy for multiple rate limit servers.
    - Configuration Retrieval Interface: Address for retrieving rate limit server configuration, corresponding to port 6070, with the HTTP protocol.
    - Timeout: Timeout for the rate limit server response.

    ![RATELIMIT Plugin](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/rls-plugin.png)

3. Configure the gateway with the global rate limit plugin.

    ![Configure Global Rate Limit Plugin](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/gateway-rls.png)

4. Create a domain and enable global rate limiting.

    ![Enable Global Rate Limiting for Domain](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/virtualhost-rls.png)

5. Create an API under the gateway, enter the newly created domain in the "Associated Domain" field, set the path matching to "/", and deploy the API. The API will inherit the global rate limit configuration of the domain by default, but you can also customize the rate limit rules.

    ![API with Global Rate Limiting](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/api-rls.png)

6. Now you can access the API through the rate limit server.

    ```bash
    while true; do curl -w " http_code: %{http_code}" http://gateway.demo:30000/; let count+=1; echo " count: ${count}"; done
    ```

    The access result is as follows: after accessing 10 times, it is rate limited.

    ```
    adservice-springcloud: hello world! http_code: 200 count: 1
    adservice-springcloud: hello world! http_code: 200 count: 2
    adservice-springcloud: hello world! http_code: 200 count: 3
    adservice-springcloud: hello world! http_code: 200 count: 4
    adservice-springcloud: hello world! http_code: 200 count: 5
    adservice-springcloud: hello world! http_code: 200 count: 6
    adservice-springcloud: hello world! http_code: 200 count: 7
    adservice-springcloud: hello world! http_code: 200 count: 8
    adservice-springcloud: hello world! http_code: 200 count: 9
    adservice-springcloud: hello world! http_code: 200 count: 10
    http_code: 429 count: 11
    http_code: 429 count: 12
    http_code: 429 count: 13
    http_code: 429 count: 14
    http_code: 429 count: 15
    http_code: 429 count: 16
    http_code: 429 count: 17
    http_code: 429 count: 18
    http_code: 429 count: 19
    http_code: 429 count: 20
    ...
    ```

### Global Rate Limiting Based on IP

!!! note

    The key for IP rate limit rules must be set as `remote_address`.

#### Rate Limiting for All IPs

1. Edit the configmap of the rate limit server and add the following content to the descriptors (pay attention to the format):

    ```yaml
    data:
      ratelimit-config.yaml: |
        domain: gateway-rls.test
        descriptors:
          - name: ip-rls
            key: remote_address
            rate_limit:
              name: ip-rule
              unit: Minute
              requests_per_unit: 5
    ```

2. The rate limit server will hot-reload the configuration. Just wait for the configuration to take effect. Alternatively, you can access the configuration interface of the rate limit server and check if the following configuration appears.

    ```
    $ curl http://10.6.222.21:32004/rlconfig
    gateway-rls.test.remote_address: unit=MINUTE requests_per_unit=5, shadow_mode: false
    ```

3. Configure the global rate limit policy for the domain (assuming that the gateway has enabled the global rate limit plugin).


4. Access the API based on the domain. Execute the following command:

    ```
    while true; do curl -w " http_code: %{http_code}"  http://ip.test:30000/; let count+=1; echo " count: ${count}"; done
    ```

    The access result is as follows: after accessing 5 times, it is rate limited.

    ```
    adservice-springcloud: hello world! http_code: 200 count: 1
    adservice-springcloud: hello world! http_code: 200 count: 2
    adservice-springcloud: hello world! http_code: 200 count: 3
    adservice-springcloud: hello world! http_code: 200 count: 4
    adservice-springcloud: hello world! http_code: 200 count: 5
    http_code: 429 count: 6
    http_code: 429 count: 7
    http_code: 429 count: 8
    http_code: 429 count: 9
    http_code: 429 count: 10
    ...
    ```

#### Rate Limiting for Specific IPs

1. Edit the configmap of the gateway-rls and add the following content to the descriptors (pay attention to the format):

    - Rate limit all IPs to 10 requests per minute.
    - Rate limit IP 10.6.222.90 to 5 requests per minute.
    - Rate limit IP 10.70.4.1 (local machine) to 3 requests per minute.

    ```yaml
    data:
    ratelimit-config.yaml: |
      domain: gateway-rls.test
      descriptors:
        - name: ip-rls
          key: remote_address
          rate_limit:
            name: ip-rule
            unit: Minute
            requests_per_unit: 10
        - key: remote_address
          value: 10.6.222.90
          rate_limit:
            unit: Minute
            requests_per_unit: 5
        - key: remote_address
          value: 10.70.4.1
          rate_limit:
            unit: Minute
            requests_per_unit: 3
    ```

2. The rate limit server will hot-reload the configuration. Just wait for the configuration to take effect. Alternatively, you can access the configuration interface of the rate limit server and check if the following configuration appears.

    ```
    $ curl http://10.6.222.21:32004/rlconfig
    gateway-rls.test.remote_address: unit=MINUTE requests_per_unit=10, shadow_mode: false
    gateway-rls.test.remote_address_10.6.222.90: unit=MINUTE requests_per_unit=5, shadow_mode: false
    gateway-rls.test.remote_address_10.70.4.1: unit=MINUTE requests_per_unit=3, shadow_mode: false
    ```

3. Configure the global rate limit policy for the domain.

4. Access the API based on the domain. Execute the following command:

    ```
    while true; do curl -w " http_code: %{http_code}"  http://ip.test:30000/; let count+=1; echo " count: ${count}"; done
    ```

    The access result for executing the command on the local machine is as follows: it is rate limited after accessing 3 times.

    ```
    adservice-springcloud: hello world! http_code: 200 count: 1
    adservice-springcloud: hello world! http_code: 200 count: 2
    adservice-springcloud: hello world! http_code: 200 count: 3
    http_code: 429 count: 4
    http_code: 429 count: 5
    http_code: 429 count: 6
    http_code: 429 count: 7
    http_code: 429 count: 8
    http_code: 429 count: 9
    http_code: 429 count: 10
    ...
    ```

    The access result for executing the command on the host with IP 10.6.222.90 is as follows: it is rate limited after accessing 5 times.

    ```
    adservice-springcloud: hello world! http_code: 200 count: 1
    adservice-springcloud: hello world! http_code: 200 count: 2
    adservice-springcloud: hello world! http_code: 200 count: 3
    adservice-springcloud: hello world! http_code: 200 count: 4
    adservice-springcloud: hello world! http_code: 200 count: 5
    http_code: 429 count: 6
    http_code: 429 count: 7
    http_code: 429 count: 8
    http_code: 429 count: 9
    http_code: 429 count: 10
    http_code: 429 count: 11
    http_code: 429 count: 12
    ...
    ```

    The access result for executing the command on other hosts without additional rate limit rules is as follows: it is rate limited after accessing 10 times.

    ```
    adservice-springcloud: hello world! http_code: 200 count: 1
    adservice-springcloud: hello world! http_code: 200 count: 2
    adservice-springcloud: hello world! http_code: 200 count: 3
    adservice-springcloud: hello world! http_code: 200 count: 4
    adservice-springcloud: hello world! http_code: 200 count: 5
    adservice-springcloud: hello world! http_code: 200 count: 6
    adservice-springcloud: hello world! http_code: 200 count: 7
    adservice-springcloud: hello world! http_code: 200 count: 8
    adservice-springcloud: hello world! http_code: 200 count: 9
    adservice-springcloud: hello world! http_code: 200 count: 10
    http_code: 429 count: 11
    http_code: 429 count: 12
    http_code: 429 count: 13
    http_code: 429 count: 14
    http_code: 429 count: 15
    http_code: 429 count: 16
    http_code: 429 count: 17
    ...
    ```
