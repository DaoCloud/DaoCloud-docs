# Grav Login Plugin

The **login plugin** for [Grav](http://github.com/getgrav/grav) adds login, basic ACL, and session wide messages to Grav.  It is designed to provide a way to secure front-end and admin content throughout Grav.

| IMPORTANT!!! This plugin is currently in development as is to be considered a **beta release**.  As such, use this in a production environment **at your own risk!**. More features will be added in the future.


# Installation

The **login** plugin actually requires the help of the **email** and **form** plugins. The **email** plugin is needed to ensure that you can recover a password via email if required.  The **form** plugin is used to generate the forms required.

These are available via GPM, and because the plugin has dependencies you just need to proceed and install the login plugin, and agree when prompted to install the others:

```
$ bin/gpm install login
```

# Creating Users

You can either use the built-in CLI capabilities, or you create a user manually by creating a new YAML file in your `user/acounts` folder.

### CLI NewUser

The simplest way to create a new user is to simply run the `bin/grav newuser` command. This will take you through a few questions to gather information with which to create your user.

```
> bin/grav newuser
Create new user

Enter a username: joeuser
Enter a password: 8c9sRCeBExAiwk
Enter an email:   joeuser@grav.org
Please choose a set of permissions:
  [a] admin access
  [s] site access
  [b] admin and site access
 > b
Enter a fullname: Joe User
Enter a title:    Site Administrator

Success! User joeuser created.
```

### Manual User Creation

Here is example user defined in `user/accounts/admin.yaml`:

```
password: password
email: youremail@mail.com
fullname: Johnny Appleseed
title: Site Administrator
access:
  admin:
    login: true
    super: true
```

>> Note: the username is based on the name of the YAML file.

# Usage

You can add ACL to any page by typing something like below into the page header:

```
access:
  site.login: true
  admin.login: true
```

Users who have any of the listed ACL roles enabled will have access to the page.
Others will be forwarded to login screen.

Because the admin user contains an `admin.login: true` reference he will be able to login to the secured page because that is one of the conditions defined in the page header. You are free to create any specific set of ACL rules you like.  Your user account must simply contain those same rules if you wish th user to have access.

# Login Page

>> Note: the **frontend site** and **admin plugin** use different sessions so you need to explicitly provide a login on the frontend.

The login plugin can **automatically generate** a login page for you when you try to access a page that your user (or guest account) does not have access to.

Alternatively, you can also provide a specific login route if you wish to forward users to a specific login page. To do this you need to create a copy of the `login.yaml` from the plugin in your `user/config/plugins` folder and provide a specific route (or just edit the plugin setttings in the admin plugin).

```
route: /user-login
```

You would then need to provide a suitable login form, probably based on the one that is provided with the plugin.

# Logout

The login plugin comes with a simple Twig partial to provide a logout link (`login-status.html.twig`).  You will need to include it in your theme however.  An example of this can be found in the Antimatter theme's `partials/navigation.html.twig` file:

```
{% if config.plugins.login.enabled and grav.user.username %}
    <li><i class="fa fa-lock"></i> {% include 'partials/login-status.html.twig' %}</li>
{% endif %}
```

You can also copy this `login-status.html.twig` file into your theme and modify it as you see fit.



