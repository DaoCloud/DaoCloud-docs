# 自定义导航栏

当前自定义导航栏需要通过手动创建导航栏的 YAML ，并 apply 到集群中。

## 导航栏分类

![导航栏分类](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/images/nav01.png)

若需要新增或重新排序导航栏分类可以通过新增、修改 category YAML 实现。

category 的 YAML 示例如下：

```yaml
apiVersion: ghippo.io/v1alpha1
kind: NavigatorCategory
metadata:
  name: management-custom # (1)!
spec:
  name: Management # (2)!
  isCustom: true # (3)!
  localizedName: # (4)!
    zh-CN: 管理
    en-US: Management
  order: 100 # (5)!
```

1. 命名规则：由小写的"spec.name"与"-custom"而成
2. 若是用于修改category
3. 该字段必须为true
4. 定义分类的中英文名称
5. 排序，数字越大，越靠上

编写好 YAML 文件后，通过执行如下命令后，刷新页面即可看到新增、修改的导航栏分类。

```bash
kubectl apply -f xxx.yaml
```

## 导航栏菜单

![导航栏菜单](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/images/nav02.png)

若需要新增或重新排序导航栏菜单可以通过新增 navigator YAML 实现。

!!! note

    若需要编辑已存在的导航栏菜单（非用户自己新增的 custom 菜单），需要令新增 custom 菜单 gproduct 字段与需要覆盖的菜单的 gproduct 相同，
    新的导航栏菜单会将 menus 中 name 相同的部分执行覆盖，name 不同的地方做新增操作。

### 一级菜单

作为产品插入到某个导航栏分类下

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GProductNavigator
metadata:
  name: gmagpie-custom # (1)!
spec:
  name: Operations Management
  iconUrl: ./ui/gmagpie/gmagpie.svg
  localizedName: # (2)!
    zh-CN: 运营管理
    en-US: Operations Management
  url: ./gmagpie
  category: management # (3)!
  menus: # (4)!
    - name: Access Control
      iconUrl: ./ui/ghippo/menus/access-control.svg
      localizedName:
        zh-CN: 用户与访问控制
        en-US: Access Control
      url: ./ghippo/users
      order: 50 # (5)!
    - name: Workspace
      iconUrl: ./ui/ghippo/menus/workspace-folder.svg
      localizedName:
        zh-CN: 工作空间与层级
        en-US: Workspace and Folder
      url: ./ghippo/workspaces
      order: 40
    - name: Audit Log
      iconUrl: ./ui/ghippo/menus/audit-logs.svg
      localizedName:
        zh-CN: 审计日志
        en-US: Audit Log
      url: ./ghippo/audit
      order: 30
    - name: Settings
      iconUrl: ./ui/ghippo/menus/setting.svg
      localizedName:
        zh-CN: 平台设置
        en-US: Settings
      url: ./ghippo/settings
      order: 10
  gproduct: gmagpie # (6)!
  visible: true # (7)!
  isCustom: true # (8)!
  order: 20 # (9)!
  target: blank # (10)!
```

1. 命名规则：由小写的"spec.gproduct"与"-custom"而成
2. 定义菜单的中英文名称
3. 与parentGProduct二选一，用于区分一级菜单还是二级菜单，与NavigatorCategory的spec.name字段对应来完成匹配
4. 二级菜单
5. 排序，数字越小，越靠上
6. 定义菜单的标志，用于和parentGProduct字段联动，实现父子关系。
7. 设置该菜单是否可见，默认为true
8. 该字段必须为true
9. 排序，数字越大，越靠上
10. 新开标签页

### 二级菜单

作为子产品插入到某个一级菜单的二级菜单中

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GProductNavigator
metadata:
  name: gmagpie-custom # (1)!
spec:
  name: Operations Management
  iconUrl: ./ui/gmagpie/gmagpie.svg
  localizedName: # (2)!
    zh-CN: 运营管理
    en-US: Operations Management
  url: ./gmagpie
  parentGProduct: ghippo # (3)!
  gproduct: gmagpie # (4)!
  visible: true # (5)!
  isCustom: true # (6)!
  order: 20 # (7)!
```

1. 命名规则：由小写的"spec.gproduct"与"-custom"而成
2. 定义菜单的中英文名称
3. 与category二选一，用于区分一级菜单还是二级菜单, 若添加该字段，则会忽视掉menus字段，并将该菜单作为二级菜单插入到与gproduct为ghippo的一级菜单中
4. 定义菜单的标志，用于和parentGProduct字段联动，实现父子关系
5. 设置该菜单是否可见，默认为true
6. 该字段必须为true
7. 排序，数字越大，越靠上
