---
hide:
  - toc
---

# Docking navigation bar

Take container management (codename `kpanda`) as an example, docking to the navigation bar.

The expected effect after docking is as follows:

## Docking method

Refer to the following steps to dock the GProduct:

1. Register all kpanda (container management) features to the nav bar via GProductNavigator CR.

    ```yaml
    apiVersion: ghippo.io/v1alpha1
    kind: GProductNavigator
    metadata:
      name: kpanda
    spec:
      gproduct: kpanda
      name: 容器管理
      localizedName:
        zh-CN: 容器管理
        en-US: Container Management
      url: /kpanda
      category: 容器  # (1)
      iconUrl: /kpanda/nav-icon.png
      order: 10 # (2)
      menus:
      - name: 备份管理
        localizedName:
          zh-CN: 备份管理
          en-US: Backup Management
        iconUrl: /kpanda/bkup-icon.png
        url: /kpanda/backup
    ```

    1. Only support one of overview, workbench, container, microservice, data service, and management
    2. The larger the number, the higher it is ranked

    The configuration for the global management navigation bar __category__ is stored in a ConfigMap and cannot be added through registration at present. Please contact the global management team to add it.

2. The `kpanda` front-end is integrated into the DCE 5.0 parent application `Anakin` as a micro-frontend.

    DCE 5.0 frontend uses [qiankun](https://qiankun.umijs.org) to connect the sub-applications UI.
    See [getting started](https://qiankun.umijs.org/guide/getting-started).

    After registering the GProductNavigator CR, the corresponding registration information will be generated for the front-end parent application. For example, `kpanda` will generate the following registration information:

    ```go
    {
      "id": "kpanda",
      "title": "容器管理",
      "url": "/kpanda",
      "uiAssetsUrl": "/ui/kpanda/", // The trailing / is required
      "needImportLicense": false
    },
    ```

    The corresponding relation between the above registration and the qiankun sub-application fields is:

    ```yaml
    {
        name: id,
        entry: uiAssetsUrl,
        container: '#container',
        activeRule: url, 
        loader,
        props: globalProps,
    }
    ```

    container and loader are provided by the frontend parent application. The sub-application does not need to concern it. Props will provide a pinia store containing user basic information and sub-product registration information.

    qiankun will use the following parameters on startup:

    ```go
    start({
      sandbox: {
        experimentalStyleIsolation: true,
      },
      // Remove the favicon in the sub-application to prevent it from overwriting the parent application's favicon in Firefox
      getTemplate: (template) => template.replaceAll(/<link\s* rel="[\w\s]*icon[\w\s]*"\s*( href=".*?")?\s*\/?>/g, ''),
    });
    ```

Refer to [Docking demo tar to GProduct](./gproduct-demo-main.tar.gz) provided by frontend team.
