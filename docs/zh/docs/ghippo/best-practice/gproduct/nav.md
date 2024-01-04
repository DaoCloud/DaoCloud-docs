---
hide:
  - toc
---

# 对接导航栏

以容器管理（开发代号 `kpanda` ）为例，对接到导航栏。

对接后的预期效果如图：

![对接效果](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/gproduct01.png)

## 对接方法

参照以下步骤对接 GProduct：

1. 通过 GProductNavigator CR 将容器管理的各功能项注册到导航栏菜单。

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

    1. 当前只支持概览、工作台、容器、微服务、数据服务、管理，六选一
    2. 数字越大排在越上面

    全局管理的导航栏 __category__ 配置在 ConfigMap，暂时不能以注册方式增加，需要联系全局管理团队来添加。

2. `kpanda` 前端作为微前端接入到 DCE 5.0 父应用 Anakin 中

    前端使用 [qiankun](https://qiankun.umijs.org/zh) 来接入子应用 UI，
    可以参考[快速上手](https://qiankun.umijs.org/zh/guide/getting-started)。

    在注册 GProductNavigator CR 后，接口会生成对应的注册信息，供前端父应用注册使用。
    例如 `kpanda` 就会生成以下注册信息：

    ```go
    {
      "id": "kpanda",
      "title": "容器管理",
      "url": "/kpanda",
      "uiAssetsUrl": "/ui/kpanda/", // 结尾的/是必须的
      "needImportLicense": false
    },
    ```

    以上注册信息与 qiankun 子应用信息字段的对应关系是：

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

    container 和 loader 由前端父应用提供，子应用无需关心。
    props 会提供一个包含用户基本信息、子产品注册信息等的 pinia store。

    qiankun 启动时会使用如下参数：

    ```go
    start({
      sandbox: {
        experimentalStyleIsolation: true,
      },
      // 去除子应用中的favicon防止在Firefox中覆盖父应用的favicon
      getTemplate: (template) => template.replaceAll(/<link\s* rel="[\w\s]*icon[\w\s]*"\s*( href=".*?")?\s*\/?>/g, ''),
    });
    ```

请参阅前端团队出具的 [GProduct 对接 demo tar 包](./gproduct-demo-main.tar.gz)。
