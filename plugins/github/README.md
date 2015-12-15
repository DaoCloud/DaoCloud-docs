# Grav GitHub Plugin

`GitHub` is a [Grav][grav] Plugin that wraps the [GitHub v3 API][github-api].

The plugin itself relies on the [php-github-api][php-github-api] library to wrap GitHub.

# Installation

Installing the GitHub plugin can be done in one of two ways. Our GPM (Grav Package Manager) installation method enables you to quickly and easily install the plugin with a simple cli command, while the manual method enables you to do so via a zip file.

## GPM Installation (Preferred)

The simplest way to install this plugin is via the [Grav Package Manager (GPM)](http://learn.getgrav.org/advanced/grav-gpm) through your system's Terminal (also called the command line). From the root of your Grav install type:

    $ bin/gpm install github

This will install the GitHub plugin into your `/user/plugins` directory within Grav. Its files can be found under `/your/site/grav/user/plugins/github`.

## Manual Installation

To install this plugin, just download the zip version of this repository and unzip it under `/your/site/grav/user/plugins`. Then, rename the folder to `github`. You can find these files either on [GitHub](https://github.com/getgrav/grav-plugin-github) or via [GetGrav.org](http://getgrav.org/downloads/plugins#extras).

You should now have all the plugin files under

    /your/site/grav/user/plugins/github

>> NOTE: You might benefit from an additional layer of cache by using this plugin in combination with the [twigcache plugin][twigcache].

# Usage

To use `github`, you will need to trigger the plugin by adding the `github: true` setting in the header of the main page.

```
---
title: GitHub
github: true
---

# My GitHub page
```

You can use the `github` api from the _github.md_ file by enabling the _twig processing_ in the header, right where you added the `github: true`.

```
process:
    twig: true
```

The _github.md_ file will be loading the [_github.html.twig_][github.html.twig] that is provided by the plugin and that contains some useful examples to get started.

Although if you use a template, or override the default one, it is more efficient and fast.

If you want to override the [_github.html.twig_][github.html.twig], copy the template file into the templates folder of your custom theme and that is it.

```
/your/site/grav/user/themes/custom-theme/templates/github.html.twig
```

You can now edit the override and tweak it to meet your needs.


# Authentication

GitHub API has a limit imposed to 60 requests per hour when the API is interrogated as a guest. However, when authenticated, this limit is bumped to 5000 requests per hour.

`grav-plugin-github` provides a [configuration](github.yaml) for the authentication. You can create a `user/config/plugins/github.yaml` file and compile all the required fields.

There are two methods of authentication: `api` and `password`.

## API (adviced)

When deciding to use the API method, it is necessary to generate a _Personal Access Token_ from GitHub (https://github.com/settings/tokens). Click the _Generate new token_ button and you will be presented with a form where you can give your token a name as well as configure the permissions.

Be very careful about the permissions, allowing all is almost never what you really want. If you are planning to just read data, just limit the permissions to read access points, and so on.

Once you have generated your access token, it will be shown to you. Be adviced that this will be the first and only time you will ever see the token on GitHub. It is not possible to retrieve a token, however you can store it someplace safe of your own or, if lost, it can be regenerated.

With the token in hand, head back to the previously created `github.yaml` file and configure it as so:

``` yaml
enabled: true
auth:
    method: 'api'
    token: 'abcd1234...'
```

> The password field is not needed when using the API method


## Password (`CAUTION!`)

You can decide to authenticate through a credential method, the same way you would do when logging into GitHub.

Due to the nature of Grav, being flat-file and database free, this means your password will have to be written in plain text and it can potentially get exposed to unauthorized people.

It is **STRONGLY** adviced to never use this method of authentication but, if you really want to, this is how you would compile the `github.yaml` file that was previously created.

``` yaml
enabled: true
    method: 'password'
    token: 'username'
    password: 'your_password'
```

# Examples
A few examples. Note that the APIs are based on [php-github-api][php-github-api] which uses the [GitHub v3 API][github-api]. Refer to their docs for additional informations.

### List _stargazers_ count of a repository
```
Grav has currently <strong>{{ github.client.api('repo').show('getgrav', 'grav')['stargazers_count'] }} stargazers</strong>
```

### List all the _repositories_ of a user
Lists all the repositories of a user and for each of them shows the link to GitHub, the forks count and the stargazers count.

```
<ul>
    <li>Repositories (<strong>{{ github.client.api('user').repositories('getgrav')|length }}</strong>):
        <ul>
        {% for repo in github.client.api('user').repositories('getgrav') %}
            <li>{{ repo.name|e }} [<a href="{{ repo.html_url|e }}">link</a> | forks: <strong>{{ repo.forks_count|e }}</strong> | stargazers: <strong>{{ repo.stargazers_count|e }}</strong>]</li>
        {% endfor %}
        </ul>
    </li>
</ul>
```

### Paginator: Get all _repositories_ of a organization [getgrav]
You can use the `paginator` to manage GitHub pages. GitHub by default limits each page to 30 items maximum, but provides an API to know if there are subsequential pages and how to reach them.

Refer to the [KnpLabs/php-github-api](https://github.com/KnpLabs/php-github-api/blob/master/doc/result_pager.md) documentation for more details on how to use the pagination.

``` twig
{% set api = github.client.api('organization') %}
{% set result = github.paginator.fetchAll(api, 'repositories', ['getgrav']) %}
```

`fetchAll` will take care of navigating through all pages and return the full stack of data that you can then cycle through.

If a more manual approach is desired, then it shall be used `fetch`, which will allow to interrogate next and previous pages as well as fetch them again.

``` twig
{% set api = github.client.api('organization') %}
{% set result = github.paginator.fetch(api, 'repositories', ['getgrav']) %}
```

Same as the previous example, except for the `fetch` vs `fetchAll`. This call will return only the **first** page.

At this point we can interrogate the `paginator` about next and previous pages and for fetching them.

### Check for next page

``` twig
{% if (github.paginator.hasNext()) %}
```

### Fetch the next page

``` twig
{% set next = github.paginator.fetchNext() %}
```


### Check for previous page

``` twig
{% if (github.paginator.hasPrevious()) %}
```

### Fetch the previous page

``` twig
{% set Previous = github.paginator.fetchPrevious() %}
```

# Updating

As development for the GitHub plugin continues, new versions may become available that add additional features and functionality, improve compatibility with newer Grav releases, and generally provide a better user experience. Updating GitHub is easy, and can be done through Grav's GPM system, as well as manually.

## GPM Update (Preferred)

The simplest way to update this plugin is via the [Grav Package Manager (GPM)](http://learn.getgrav.org/advanced/grav-gpm). You can do this with this by navigating to the root directory of your Grav install using your system's Terminal (also called command line) and typing the following:

    bin/gpm update github

This command will check your Grav install to see if your GitHub plugin is due for an update. If a newer release is found, you will be asked whether or not you wish to update. To continue, type `y` and hit enter. The plugin will automatically update and clear Grav's cache.

## Manual Update

Manually updating GitHub is pretty simple. Here is what you will need to do to get this done:

* Delete the `your/site/user/plugins/github` directory.
* Downalod the new version of the GitHub plugin from either [GitHub](https://github.com/getgrav/grav-plugin-github) or [GetGrav.org](http://getgrav.org/downloads/plugins#extras).
* Unzip the zip file in `your/site/user/plugins` and rename the resulting folder to `github`.
* Clear the Grav cache. The simplest way to do this is by going to the root Grav directory in terminal and typing `bin/grav clear-cache`.

> Note: Any changes you have made to any of the files listed under this directory will also be removed and replaced by the new set. Any files located elsewhere (for example a YAML settings file placed in `user/config/plugins`) will remain intact.

[grav]: http://github.com/getgrav/grav
[github-api]: https://developer.github.com/v3/
[php-github-api]: https://github.com/KnpLabs/php-github-api/
[twigcache]: https://github.com/getgrav/grav-plugin-twigcache
[github.html.twig]: templates/partials/github.html.twig
