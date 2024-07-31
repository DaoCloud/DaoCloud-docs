---
MTPE: windsonsea
Date: 2024-07-17
hide:
   - toc
---

# Authorization Policy

The authorization policy is similar to a L4 to L7 "firewall".
It will analyze and match the data flow like a traditional firewall, and then perform corresponding actions.
The authorization policy applies whether the request is from internal or external.

A reference YAML example for an authorization policy is as follows:

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
   name: "ratings-viewer"
   namespace: default
spec:
   selector:
     matchLabels:
       app: ratings
   action: ALLOW
   rules:
   - from:
     - source:
         principals: ["cluster.local/ns/default/sa/bookinfo-reviews"]
     to:
     - operation:
         methods: ["GET"]
```

Service mesh provides two creation methods: wizard and YAML.
The specific steps to create through the wizard are as follows:

1. In the left navigation bar, click __Security__ -> __Authorization Policy__ ,
   and click the __Create__ button in the upper right corner.

    ![Create](../images/authorize01.png)  

2. In the __Create Request Authentication Policy__ interface, firstly fill in
   the basic settings and then click __Next__ .

    ![Basic](../images/authorize02.png)

3. After setting the policy according to the screen prompts, click __OK__ .
   See [Policy Setting Parameter Description](./params.md#policy-settings).

    ![Policy settings](../images/authorize03.png)

4. Return to the authorization list, and the screen prompts that the creation is successful.

    ![Successful submission](../images/authorize04.png)

5. On the right side of the list, click __┇__ in the operation column to
   perform more operations through the pop-up menu.

    ![More operations](../images/authorize05.png)

!!! note

     - For the configuration of specific parameters, refer to
       [Authorization Policy Parameter Configuration](./params.md#authorization-policies).
     - For a more intuitive operation demonstration, refer to [Video Tutorial](../../../videos/mspider.md).
