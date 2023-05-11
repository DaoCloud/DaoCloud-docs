# 外观定制

在 DCE 5.0 中，可通过`外观定制`更换登录界面及顶部导航栏的 logo，帮助用户更好地辨识产品。

## 定制登录页和顶部导航栏

1. 使用具有 `admin` 角色的用户登录 Web 控制台。点击左侧导航栏底部的`全局管理` -> `平台设置`。

    ![全局管理](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws01.png)

2. 选择`外观定制`。

    ![外观定制](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/visual04.png)

3. 在`登录页定制`页签中，修改登录页的图标和文字后，点击`保存`。

    ![登录页](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/visual02.png)

4. 点击`顶部导航栏定制`页签，修改导航栏的图标和文字后，点击`保存`。

    ![顶部导航栏](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/visual06.png)

!!! note

    如果想要恢复默认设置，可以点击`一键还原`。请注意，一键还原后将丢弃所有自定义设置。

## 高级定制

高级定制能够通过 CSS 样式来修改整个容器平台的颜色、字体间隔、字号等。
您需要熟悉 CSS 语法。删除黑色输入框的内容，可恢复到默认状态，当然也可以点击`一键还原`按钮。

![高级定制](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/advanced-custom.png)

**登录页定制的 CSS 样例：**

```css
.test {
  width: 12px;
}

#kc-login {
 /* color: red!important; */
}
```

**登录后页面定制的 CSS 样例：**

```css
.dao-icon.dao-iconfont.icon-service-global.dao-nav__head-icon {
   color: red!important;
}
.ghippo-header-logo {
  background-color: green!important;
}
.ghippo-header {
  background-color: rgb(128, 115, 0)!important;
}
.ghippo-header-nav-main {
  background-color: rgb(0, 19, 128)!important;
}
.ghippo-header-sub-nav-main .dao-popper-inner {
  background-color: rgb(231, 82, 13) !important;
}
```
