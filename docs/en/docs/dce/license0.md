---
hide:
  - toc
---

# Free Trial

The modules included in DCE Community are [Global Management](../ghippo/intro/index.md),
[Container Management](../kpanda/intro/index.md), [Workbench](../amamba/intro/index.md),
[Insight](../insight/intro/index.md), and more.

```mermaid
graph LR

apply[1. Apply for a license] --> get[2. Get offline authorization] --> activate[3. Activate offline authorization]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class apply,get,activate k8s
```

## Apply for a License

Follow the steps below to get a license for your DCE Community:

1. Click [Apply for license](https://qingflow.com/f/58604bf8){ .md-button } and click __Submit__ after you fill in required information in the form.

    ![license](./images/license011.png)

2. Follow the on-screen instructions, check your email containing the license, and then click [Get an offline authorization code](https://license.daocloud.io/dce5-license){ .md-button }.

    ![get-auth-code](./images/license012.png)

3. Input the license you just received and input your ESN, click __Get an offline authorization code__ .

    ESN is the unique device code of the cluster system.
    Follow the steps to get your ESN: Open DCE, click __Global Management__ -> __Settings__ -> __Licenses__ , click __Manage License__ , and copy the ESN code.

    ![esn](./images/license02.png)

4. Paste the offline authorization code, and click __Activate Now__ . Congratulations! :smile: It's time to explore the new DCE 5.0 now!

!!! info "📢 Tips"

    The offline authorization code is bound to the device ESN. Please keep the license key email safe and secure.
    You can contact the DaoCloud delivery team at any time to reapply, as we have saved all your license keys for you.

## Renew License

If your license expires for any reason, you can follow the steps below to renew it.

### Recommended Approach

1. First, [clear the device code](https://qingflow.com/f/58604bf8). In the form, select __Remove ESN/Cluster ID__ and enter the [previous license key](https://license.daocloud.io/dce5-licenses). Once completed, click __SUBMIT__ .

    ![clear ESN](./images/esn.png)

2. Refer to the previous section to reapply for the license.

### Renew License by Modules

This method requires renewing the license for each installed module.
For example, DCE Community includes three modules: Container Management, Global Management, and Observability, each with its own license.
To do this, go to the [license page](https://qingflow.com/f/58604bf8) and select __Renew License__ for each module.

![renew](./images/extend.png)

## Reference Links

The pages you may frequently access in the process of above procedure are listed as follows:

[Apply for a license](https://qingflow.com/f/58604bf8){ .md-button .md-button--primary }
[View your license](https://license.daocloud.io/dce5-licenses){ .md-button .md-button--primary }
[Get an offline authorization code](https://license.daocloud.io/dce5-license){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
