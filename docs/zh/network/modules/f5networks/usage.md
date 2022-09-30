# 使用

## 4层负载均衡

当组件安装为 4 层负载均衡模式时，可为集群中的service 创建 F5 的负载均衡服务，具体使用，可参考[F5 官方文档](https://clouddocs.f5.com/containers/latest/userguide/loadbalancer/)

以下给出简单的例子：

1. 当本组件以nodePort转发方式工作时，必须为应用创建一个 LoadBalancer 类型的service

        apiVersion: v1
        kind: Service
        metadata:
          name: http-server
          annotations:
            cis.f5.com/ipamLabel: LabelName
            cis.f5.com/health: '{"interval": 10, "timeout": 31}'
        spec:
          type: LoadBalancer
          ports:
          - port: 80
            targetPort: 80
            name: http
          selector:
            app: http-server

    注意如上yaml中的 annotaiton:
    (1) 必须打上"cis.f5.com/ipamLabel"，注意替换该key的值，请设置为安装时填写"BIGIP L4 IP Pool"的 LabelName，否则该转发规则不会分配到 VIP
    (2) "cis.f5.com/health" 是可选的
    (3) 更多的 annotaiton 支持，请参考 [ F5 官方文档 ](https://clouddocs.f5.com/containers/latest/userguide/loadbalancer/#parameters)


2. 创建service后，即可观测到分配到的 EXTERNAL-IP

       # kubectl get service -o wide
       NAME             TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE     SELECTOR
       http-server      LoadBalancer   172.21.25.10   172.110.185.51   80:31548/TCP   3d14h   app=http-server


3. 登录到 F5 WEBUI，切换到所使用的 partition，即可观测到下发的转发规则

    ![f5network usage1](../../images/f5-usage1.png)

    ![f5network usage1](../../images/f5-usage2.png)


4. 在集群外发，访问 F5 分配到的 VIP ，即可访问到服务 


## 7层负载均衡

当组件安装为 4 层负载均衡模式时，可为集群中的 ingress 创建 F5 的负载均衡服务，具体使用，可参考[F5 官方文档](https://clouddocs.f5.com/containers/latest/userguide/ingress.html)

以下给出简单的例子：

1. 确认 F5 的 ingressClass

        # kubectl get ingressClass
        NAME   CONTROLLER                 PARAMETERS   AGE
        f5     f5.com/cntr-ingress-svcs   <none>       41h


2. 当本组件以nodePort转发方式工作时，必须为应用创建一个 nodePort 类型的 service 和 ingress 对象

        apiVersion: v1
        kind: Service
        metadata:
          name: http-server
        spec:
          type: nodePort
          ports:
          - port: 80
            targetPort: 80
            name: http
          selector:
            app: http-server
        ---
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        metadata:
          name: http-server
        spec:
          ingressClassName: f5
          rules:
          - http:
              paths:
               - path: /http-server
                 pathType: Prefix
                 backend:
                   service:
                     name: http-server
                     port:
                       number: 80

    注意如上 ingress yaml： 
    （1）ingressClassName 使用 F5 的 ingressClass
    （2）ingress 支持的更多 annotaiton ，请参考 [ F5 官方文档 ](https://clouddocs.f5.com/containers/latest/userguide/ingress.html#supported-ingress-annotations)


3. 创建 ingress 后，可观测到 ingress 对象分配到的 ADDRESS

        # kubectl get ingress
        NAME          CLASS   HOSTS   ADDRESS           PORTS   AGE
        http-server   f5      *       172.110.185.190   80      40h


4. 登录到 F5 WEBUI，切换到所使用的 partition，即可观测到下发的转发规则

   ![f5network usage3](../../images/f5-usage3.png)

   ![f5network usage4](../../images/f5-usage4.png)


5。 在集群外发，访问 F5 分配到 URL http://VIP/http-server ，即可访问到服务 

