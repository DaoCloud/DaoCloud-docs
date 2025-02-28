---
MTPE: windsonsesa
date: 2024-01-10
---

# Deploy Pluggable Components for the Workbench

Some features in the Workbench leverage the capabilities of open-source components. Starting from
v0.21.0 of the Workbench, a pluggable design pattern is adopted to decouple these functional
components. Therefore, when deploying the Workbench, you can choose whether to enable them in
the __manifest.yaml__ file of the installer. If they are not enabled during installation, you can
follow the instructions below to enable them.

The corresponding functionalities for each component are as follows:

| Component   | Features | Remarks |
| ----------- | -------------- | ------- |
| argo-cd     | Continuous Deployment | Installed by default |
| argo-rollouts | Canary Release | Not installed by default |
| vela-core   | OAM Applications | Not installed by default |

!!! note

    If you want to enable or disable the related components of the Workbench during the deployment
    of DCE 5.0, you can set the __enable__ keyword in the __manifest.yaml__ file to true or false to
    choose whether to enable them.

## Deploying the argo-cd component

If you chose not to enable it during the deployment of DCE 5.0, follow the instructions below
to deploy it and use the continuous deployment capability provided by the Workbench.

1. In the DCE 5.0 product module, go to __Container Management__ -> __Clusters__ and enter the details page of the __kpanda-global-cluster__ .

2. In the cluster details page, navigate to the menu on the left side and go to __Helm Apps__ -> __Helm Charts__
   -> select the __All__ repository. Search for __argo-cd__ , click it to enter the details page, and install it.

3. On the installation interface, fill in the required installation parameters.

    ![argocd01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/argocd01.png)

    Parameter descriptions:

    - Name: Enter __argocd__
    - Version: The default version is __5.34.6__ , which is the only version available in the addon repository
    - Namespace: Select __argocd__

    !!! note

        You can use the default values for the rest of the parameters.

4. Click the __OK__ button at the bottom right to complete the installation. Confirm that the related argo-cd resources in the __argocd__ namespace are all in the __Running__ state.

5. After successfully deploying the resources mentioned above, go to the __ConfigMaps & Secrets__ -> __ConfigMaps__
   menu on the left side of the current cluster details page. Choose namespace __amamba-system__ , then search for 
   __amamba-config__ and click __Edit YAML__ .

6. Add the following parameters in the __data->amamba-config.yaml__ section:

    ```yaml
    generic:
      argocd:
        host: argocd-server.argocd.svc.cluster.local:80  # (1)!
        namespace: argocd  # (2)!
    ```

    1. argocd server address, format: argocd-server service name.namespace.svc.cluster.local:80
    2. argocd deployment namespace

    ![argocd02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/argocd02.png)

7. After making the changes, go to the __Workloads__ -> __Pods__ menu on the left side of the current cluster details
   page and search for __amamba-apiserver__ and __amamba-syncer__ . Restart them one by one.

8. Once the restart is successful, you can go to the __Workbench__ module to use the continuous deployment capability.

### Notes

For the argo-cd component in the addon, we made some configuration changes based on the open-source version. The main changes are as follows:

- Modified the helm template to use the three-part structure of __registry:repository:tag__ for the image,
  which can be set using __global.imageRegistry__ for the global registry address.
- Modified two configmaps of argo-cd for authentication. These can be installed directly through
  the argo-cd component in the addon, and no manual operation is required.

```shell
[root@demo-dev-master1 ~]# kubectl get cm -n argocd argocd-cm -o yaml
```
```yaml
apiVersion: v1
data:
  accounts.amamba: apiKey
  admin.enabled: "true"
kind: ConfigMap
metadata:
  name: argocd-cm

[root@demo-dev-master1 ~]# kubectl get cm -n argocd argocd-rbac-cm -o yaml
apiVersion: v1
data:
  policy.csv: |
    g, amamba, role:admin
  policy.default: ""
  scopes: '[groups]'
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
```

## Deploying the vela-core component

If you chose not to enable it during the deployment of DCE 5.0, follow the instructions below
to deploy and utilize the OAM application capabilities provided by the Workbench.

1. In the DCE 5.0 product module, go to __Container Management__ -> __Clusters__ and enter
   the details page of the __kpanda-global-cluster__ cluster.

2. In the cluster details page, navigate to the left sidebar menu and select __Helm Apps__ -> __Helm Charts__ -> choose the addon repository. Search for __vela-core__ , click it to enter the details page, and proceed with the installation.

3. On the installation page, fill in the required installation parameters:

    ![vela01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/vela01.png)

    Parameter explanation:

    - Name: Enter __kubevela__ (recommended)
    - Version: By default, select __1.7.7__ as the addon repository only has this version available
    - Namespace: Select __vela-system__ (recommended)

    !!! note

        - Use the default values for the rest of the parameters.
        - Note that the parameter __applicationRevisionLimit__ indicates the limit on the number of OAM application versions, which is set to 10 by default but can be changed based on your preference.

4. Click the __OK__ button on the bottom right corner to complete the installation. You can check if the relevant workloads under the __vela-system__ namespace are all in the __Running__ state.

5. Once you have confirmed the successful deployment of the above workloads, go to the current cluster's details page and navigate to the left sidebar menu and select __ConfigMaps & Secrets__ -> __ConfigMaps__ . Search for __amamba-config__ in namespace __amamba-system__ and click __Edit YAML__ .

6. In the __data->amamba-config.yaml__ section, add the following parameters:

    ```yaml
    generic:
      kubevela:
        namespace: vela-system # (1)!
    ```

    1. The namespace where kubevela is installed

    ![vela02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/vela02.png)

7. After making the changes, go to the left sidebar menu of the current cluster's details page and select __Workloads__ -> __Containers__ . Search for __amamba-apiserver__ and __amamba-syncer__ respectively, and restart them one by one.

8. Once the restart is successful, you can access the __Workbench__ module to utilize the OAM application capabilities.

## Deploying the argo-rollouts component

If you chose not to enable it during the deployment of DCE 5.0, follow the instructions below to deploy and utilize the gray release capabilities provided by the Workbench.

1. In the DCE 5.0 product module, go to __Container Management__ -> __Clusters__ and enter the details page of the __kpanda-global-cluster__ cluster (the cluster where you want to perform gray releases on applications).

2. In the cluster details page, navigate to the left sidebar menu and select __Helm Apps__ -> __Helm Charts__ -> choose
   the addon repository. Search for __argo-rollouts__ , click it to enter the details page, and proceed with the installation.

3. Fill in the required installation parameters on the installation interface.

    ![argorolllout01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/argorollout01.png)

    **Parameter Description:**

    - Name: Please fill in __argo-rollouts__, recommended.
    - Version: Default selection is __2.32.0__, the addon repository currently only has this version.
    - Namespace: Please select __argo-rollouts__, recommended.

    **Enable contour**

    Workbench supports traffic control based on contour for gray release policy in the new v0.24.0. If you need to use this capability, you need to do the following:

    - Define the parameters under the `initContainers` field in `value.yaml`:

        ```yaml
        argo-rollouts:
          controller:
            initContainers:                                    
              - name: copy-contour-plugin
                image: release.daocloud.io/skoala/rollouts-plugin-trafficrouter-contour:v0.3.0 # (1)!
                command: ["/bin/sh", "-c"]                    
                args:
                  - cp /bin/rollouts-plugin-trafficrouter-contour /plugins
                volumeMounts:                                  
                  - name: contour-plugin
                    mountPath: /plugins
            trafficRouterPlugins:                              
              trafficRouterPlugins: |-
                - name: argoproj-labs/contour
                  location: "file:///plugins/rollouts-plugin-trafficrouter-contour" 
            volumes:                                           
              - name: contour-plugin
                emptyDir: {}
            volumeMounts:                                      
              - name: contour-plugin
                mountPath: /plugins
        ```

        1. When offline, the offline container registry address needs to be added before the image address.

    - After the argo-rollouts installation is completed, you also need to execute the following command to modify the clusterRole:

        ```shell
        # The name of the clusterRole needs to be modified according to the actual installation situation
        kubectl patch clusterrole argo-rollouts -n argo-rollouts --type='json' -p='[{"op": "add", "path": "/rules/-", "value": {"apiGroups":["projectcontour.io"],"resources":["httpproxies"],"verbs":["get","list","watch","update","patch","delete"]}}]'
        ```

    After the Rollout deployment is successful, you can create a canary release interface to select contour as the traffic control.

4. Click the confirm button in the lower right corner to complete the installation. You can check if the related loads under the __argo-rollouts__ namespace are all in the __running__ state.

5. After successful deployment, you can go to the __Workbench__ module to use the gray release capability based on `cloud-native gateway` in the current cluster.

    ![contour](images/contour01.png)

!!! note

    - Argo-rollouts is a tool for gray release and traffic management for Kubernetes applications, focusing on the deployment and update process of applications.
    - During use, it needs to be deployed in the cluster where the application is located. If you need to use gray release capability in multiple clusters, you need to deploy the argo-rollouts component in each corresponding cluster.
