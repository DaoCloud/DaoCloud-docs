# Grav Form Plugin

The **form plugin** for [Grav](http://github.com/getgrav/grav) adds the ability to create and use forms.  This is currently used extensively by the **admin** and **login** plugins.

| IMPORTANT!!! This plugin is currently in development as is to be considered a **beta release**.  As such, use this in a production environment **at your own risk!**. More features will be added in the future.

# Installation

The form plugin is easy to install with GPM.

```
$ bin/gpm install form
```

# Configuration

Simply copy the `user/plugins/forms/forms.yaml` into `user/config/plugins/forms.yaml` and make your modifications.

```
enabled: true
```  

# How to use the Form Plugin

The Learn site has two pages describing how to use the Form Plugin: 
- [Forms](http://learn.getgrav.org/advanced/forms) 
- [Add a contact form](http://learn.getgrav.org/advanced/contact-form)

# Using email

Note: when using email functionality in your forms, make sure you have configured the Email plugin correctly. In particular, make sure you configured the "Email from" and "Email to" email addresses in the Email plugin with your email address
