---
hide:
  - toc
---

# Peer Authentication

Peer authentication refers to providing two-way security authentication between services without intrusive modification of the application source code. At the same time, the creation, distribution, and rotation of secrets and certificates are also automatically completed by the system, which is transparent to users. The complexity of security configuration management is greatly reduced.

!!! note

    After peer authentication is enabled, the corresponding target rule also needs to enable mLTS mode, otherwise it will not be able to access normally.

A strict mTLS policy enforced across the mesh. Once in effect, inter-service access within the mesh will require mLTS to be enabled.

Example:

```yaml
apiVersion: "security.istio.io/v1beta1"
kind: "PeerAuthentication"
metadata:
  name: "default"
  namespace: "istio-system" #effective namespace
spec:
  mtls:
    mode: STRICT #strategy
```

Service mesh provides two creation methods: wizard and YAML. The specific steps to create through the wizard are as follows:

1. Click __Security__ -> __Peer Authentication__ in the left navigation bar, and click the __Create__ button in the upper right corner.

    ![Create Peer Authentication](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/peer01.png)

2. In the __Create Peer Authentication__ interface, first perform the basic configuration and then click __Next__ .

    ![Basic Info](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/peer02.png)

3. After completing the authentication settings according to the screen prompts, click __OK__ .

    ![Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/peer03.png)

4. The screen prompts that the creation is successful.

    ![Successfully Created](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/peer04.png)

5. On the right side of the list, click __⋮__ in the operation column to perform more operations through the pop-up menu.

    ![Edit/Delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/peer05.png)

!!! note

    - For the configuration of specific parameters, please refer to [Security Governance Parameter Configuration](./params.md).
    - For a more intuitive operation demonstration, please refer to [Video Tutorial](../../../videos/mspider.md).
    - See [Service Mesh Identity and Authentication](./mtls.md).
