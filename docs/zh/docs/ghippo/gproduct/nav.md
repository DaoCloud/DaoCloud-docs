# 对接导航栏

以容器管理（开发代号 `kpanda`）为例，对接到导航栏。

对接后的预期效果如图：

[对接效果](../images/gproduct01.png)

## 对接方法

通过 GProductNavigator CR 将容器管理的各功能项注册到导航栏菜单。

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
  category: 容器   # 当前只支持概览、工作台、容器、微服务、数据服务、管理，六选一
  iconUrl: /kpanda/nav-icon.png
  order: 10 # 数字越大排在越上面
  menus:
  - name: 备份管理
    localizedName:
      zh-CN: 备份管理
      en-US: Backup Management
    iconUrl: /kpanda/bkup-icon.png
    url: /kpanda/backup
```

全局管理的导航栏 `category` 配置在 ConfigMap，暂时不能以注册方式增加，需要联系全局管理团队来添加。
