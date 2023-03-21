---
hide:
  - toc
---

# Appearance customization

In DCE 5.0, you can change the logo on the login interface and the top navigation bar through `Appearance Customization` to help users better identify products.

## Custom login page and top nav bar

1. Log in to the web console as a user with `admin` role. Click `Global Management` - `Custom Appearance` at the bottom of the left navigation bar.

    ![Global Management](../../images/ws01.png)

2. Click `Platform Settings` and select `Custom Appearance`.

    ![Appearance customization](../../images/visual04.png)

3. In the `Login Page Customization` tab, after modifying the icon and text of the login page, click `Save`.

    ![Login Page](../../images/visual02.png)

4. Click the `Top Nav Bar Customization` tab, modify the icon and text of the navigation bar, and click `Save`.

    ![Top Nav Bar](../../images/visual06.png)

!!! note

    If you want to restore the default settings, you can click `One Key Restore`. Note that all custom settings will be discarded after a one-click restore.

## Advanced customization

Advanced customization can modify the color, font spacing, font size, etc. of the entire container platform through CSS styles.
You need to be familiar with CSS syntax. Delete the contents of the black input box to restore to the default state, of course, you can also click the `one-key restore` button.

![Advanced Custom](../../images/advanced-custom.png)

**CSS sample for login page customization:**

```css
.test {
  width: 12px;
}

#kc-login {
 /* color: red!important; */
}
```

**CSS sample for page customization after login:**

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
