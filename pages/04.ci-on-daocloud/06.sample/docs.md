---
title: 举个例子
taxonomy:
    category:
        - docs
---

<!-- 

这是之前的例子，应该不需要修改，直接可以用，文字重新修饰排版一下即可，图可能要 load 进入 grav 中。
-->

## 代码构建

开启您的 DaoCloud 之旅，从「代码构建」开始。

让我们用一个小游戏来熟悉项目的创建和配置过程吧。这个叫做 2048 的小游戏相信大家对它都不陌生，这个镜像源自于 Docker Hub 镜像 **[cpk1224/docker-2048](https://registry.hub.docker.com/u/cpk1224/docker-2048/)**，大家也可以从 **[DaoCloud/dao-2048](https://github.com/DaoCloud/dao-2048/)** fork 一份构建用的 `Dockerfile` 到自己的 GitHub 仓库，然后一起开始配置。

<!-- TODO: 添加至术语表：代码仓库、GitHub -->

### 构建步骤

第一步：在控制台点击「代码构建」。

![控制台：点击代码构建](/img/screenshots/features/build-flows/dashboard.png)

---

第二步：在「代码构建」的界面中点击「创建新项目」。

![代码构建：准备创建新项目](/img/screenshots/features/build-flows/build-flows-index.png)

---

第三步：为项目指定「项目名称」，项目名称只能包含英文数字、下划线 `_`、小数点 `.`、和减号 `-`，并且不能与现有项目重名。

![代码构建：配置新项目](/img/screenshots/features/build-flows/new.png)

---

第四步：在「设置代码源」中选择 `dao-2048`，如果还未绑定 GitHub 账号登录，此时会跳出 GitHub 的 OAuth 登陆和授权界面，请根据要求完成授权。

> 提示：找不到 `dao-2048`？记得先从**[这里](https://github.com/DaoCloud/dao-2048/)** fork 一份到自己的 GitHub 仓库哦。
> 注意：我们强烈建议您在关联 GitHub 项目之前，确保您的 `Dockerfile` 可以在本地正常构建，Docker 镜像内的程序可以正常执行，以免增加在云端排错的难度。

---

第五步：DaoCloud 需要获取必要的 GitHub 读写权限，这是国际上绝大多数与 GitHub 对接的应用的通用做法，DaoCloud 将保证您代码的安全。

> 常见问题：为什么需要 GitHub 仓库的写入权限？这是因为持续集成和持续交付服务需要为仓库设置 WebHook。

---

<!-- TODO: 添加至术语表：持续集成、持续交付 -->

第六步：授权完成后，界面会出现您在 GitHub 加入的所有组织，通过下拉菜单可以选择具体的代码仓库，在这个例子中，我们点击选择 `dao-2048`。

---

第七步：设置「持续集成」，由于 `dao-2048` 没有持续集成的配置文件，这里可以设置为关闭。如果您的其他项目希望使用 DaoCloud 提供的持续集成服务，请将「持续集成」设置为「已开启」。

> 提示：要使用持续集成功能，请参阅[「持续集成」](../continuous-integration/README.md)。

---

第八步：设置构建位置，大部分项目都将 `Dockerfile` 置于项目的顶级目录并以 `Dockefile` 命名，`dao-2048` 亦是如此。如果您在其他项目中用到了特殊的结构，可以在这里指定：

* 构建目录：构建时的当前目录，会影响 COPY 和 ADD 时的相对路径。
* Dockerfile 路径：`Dockefile` 的位置，可以自定义 `Dockerfile` 的文件名。

> 小技巧：由于构建的服务器在海外，我们建议您配置多个 `Dockerfile` 以适应国内外不同的环境（例如 apt-get 使用不同的软件源，npm 使用不同的镜像站等）。

---

第九步：设定「发布应用镜像」的目标位置，当前仅支持「镜像仓库」，这是由 DaoCloud 提供的 Docker 镜像存储库，我们今后会支持 Docker Hub 和第三方私有 Registry。

---

第十步：点击「开始创建」，系统将自动根据您代码仓库主分支的最新代码启动第一次应用构建过程（标签为 `master-init`）。

![代码构建：项目开始构建](/img/screenshots/features/build-flows/build-start.png)

---

就这么简单，经过短暂的等待您已经成功关联了代码库，并完成了第一次 Docker 镜像的构建。

![代码构建：项目构建成功](/img/screenshots/features/build-flows/build-success.png)

### 查看项目清单

在项目清单列表中，您可以看到您的项目的构建状态，同时也会显示出代码源、编程语言、CI 服务、构建时间和镜像名称。

![代码构建：项目列表](/img/screenshots/features/build-flows/build-flows-index-with-project.png)

在项目清单中点击项目名称，您可以进入项目的「镜像构建」、「持续集成」和「设置」选项卡。

---

镜像构建选项卡可以查看 Docker 镜像的构建历史和在构建过程中产生的实时日志，了解镜像构建的历史和出错时的原因。

![「镜像构建」选项卡](/img/screenshots/features/build-flows/build-history.png)

---

持续集成选项卡提供了使用和触发 DaoCloud 持续集成的详细信息。

![「持续集成」选项卡](/img/screenshots/features/build-flows/build-ci.png)

---

设置界面中，可以重新配置持续集成服务、构建位置和镜像发布到的目标位置，也可以删除该项目。

![「设置」选项卡](/img/screenshots/features/build-flows/build-settings.png)

### 使用 DaoCloud 构建镜像的优势

我们很容易注意到，在 DaoCloud 进行 Docker 镜像的构建比在本地电脑要快很多，这得益于我们在网络拓扑、镜像存取加速等方面所做的大量优化工作。这些优化节约了国内 IT 人士的宝贵时间，再也不用因为网络等原因在屏幕前苦苦等待 Docker 镜像的构建了。

<!-- TODO: 添加至术语表：标签 -->

此外 DaoCloud 可以根据在 GitHub 代码库上的设置，完成由规则触发的自动构建 Docker 镜像。目前，DaoCloud 根据推送新的标签来触发。如果推送了新的标签，DaoCloud 就认为这是一次发布需要自动构建镜像。我们也可以通过手工启动构建的方式来触发镜像的重新构建。

如下图，在 Git 推送了名为「v1.0」的标签后 DaoCloud 会自动从 GitHub 拉取代码并完成 docker 镜像的自动构建。

![基于新标签的自动构建](/img/screenshots/features/build-flows/tagging.png)

这样的自动化触发，是通过 WebHook 机制完成的。我们可以在 `dao-2048` 项目的 GitHub 设置页中，看到这个 WebHook 回调的 URL。

![GitHub 上的 WebHook](/img/screenshots/features/build-flows/webhook.png)

> 警告：为了成功触发回调，请勿修改这个 URL。

### 下一步

至此，您已经掌握了如何在 DaoCloud 上创建、配置项目并完成第一次镜像构建。

下面您可以：

* 了解如何用 DaoCloud 进行持续集成：参考[持续集成](../continuous-integration/README.md)。
* 了解如何用为应用准备一个数据库服务：参考[服务集成](../services.md)。
* 了解如何部署一个刚刚构建好的应用镜像：参考[应用部署](../deployment.md)。





Grav has a variety of flexible linking options that allow you to link images from one page to another, and even from remote sources. If you have ever linked files using HTML or worked with a file system using a command line, a lot of this should be very easy to pick up.

We will run to some easy examples using this very basic, trimmed down model of what a Grav site's **Pages** directory might look like.

![Pages Directory](pages.png)

Using this directory structure as an example, we will take a look at the different types of links you can use to display media files in your content. We have image files in every folder, including one image for each blog post, and three images in a special `/images` directory which acts as a page, but contains only media files.

The use of the `/images` folder serves as an example of how you can maintain a simple centralized image directory to store files that are frequently used by multiple pages. This simplifies the linking process in these cases.

>>>> If you decide to use a centralized image directory, be advised that this directory should exist within the `/pages` folder as this folder is intended for front-facing content.

To get us started, here is a quick look at some of the common components of a Grav markdown-based image tag.

```
![Alt Text](../path/image.ext)
```

| String |                                                                           Description                                                                            |
| :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!`    | When placed at the beginning of a traditional markdown link tag, it indicates this is an image tag.                        |
| `[]`   | The square bracket is used to wrap the **optional** alt-text for the image. |
| `()`   | The parenthesis is used to surround the reference to the image itself. This is placed directly after the square bracket.                                                           |
| `../`  | When used in the link, it indicates a move up a directory.                                                                                                       |

>>>>>> You can combine a regular page link and an image link like to wrap an image in a link: `[![Alt text](/path/to/img.jpg)](http://example.net/)`

### Slug Relative

**Relative** image links use destinations set relative to the current page. This can be as simple as linking to another file in the current directory, such as an image file associated with the current page, or as complex as going up several directory levels and then back down to the specific folder/file where an image may reside.

With relative links, the location of the source file is every bit as important as that of the destination. If either file in the mix is moved, changing the path between them, the link can be broken.

The advantage of this type of linking structure is that you can easily switch between a local development server and a live server with a different domain name and as long as the file structure remains consistent, the links should work without a problem.

A file link points to a particular file by name, rather than its directory or slug. If you were creating an image link in `pages/01.blog/test-post-1/item.md` to `/pages/01.blog/test-post-3/test_image_3.jpg` you would use the following command.

```markdown
![Test Image 3](../test-post-3/test_image_3.jpg)
```

This link moves up one folder, as indicated by `../`, and then down one folder, pointing directly to `test_image_3.jpg` as the destination.

If we want to load `blog-header.jpg` from the `01.blog` directory, we would do the following:

```markdown
![Blog Header](../../blog/blog-header.jpg)
```

>>>>> You do not need to include ordering numerals (`01.`) for slug relative links.

Grav has integrated support for slugs in the header of the page's primary markdown file. This slug supersedes the folder name for the page, and any media files contained within.

For example, **Test Post 2** has a slug set through its markdown file (`/pages/01.blog/test-post-2/item.md`). The header of this file contains the following:

```yaml
---
title: Test Post 2
slug: test-slug
taxonomy:
    category: blog
---
```

You will notice the slug `test-slug` has been set. Slugs set this way are completely optional, and do not have to be present. As mentioned in the last chapter, they do provide an easy way of linking. If a slug is set, then any link you make to a media file within that folder will have to be either **Slug Relative** or **Absolute** with a full URL set for the link.

If we want to link `test_image_2.jpg` from **Test Post 2**, we would enter the following:

```markdown
![Test Image 2](../test-slug/test_image_2.jpg)
```

You will notice that we navigated up one directory using (`../`) and then down into the `test-slug` page folder using the slug which was set in `/pages/01.blog/test-post-2/item.md` file.

### Directory relative

**Directory Relative** image links use destinations set relative to the current page. The main difference between a slug relative, and directory relative link, is that rather than using the URL slugs, you reference via the full path with folder names.

An example of this would be something like:

```markdown
![Test Image 3](../../01.blog/02.my_folder/test_image_3.jpg)
```

>>> The main benefit of this, is that you can maintain link integrity in other systems outside of Grav, such as GitHub.

### Absolute

Absolute links are similar to relative links, but are relative to the root of the site. In **Grav**, this is typically based in your **/user/pages/** directory. This type of link can be done in two different ways.

You can do it in a similar fashion to the **Slug Relative** style which uses the slug, or directory name in the path for simplicity. This method removes potential issues of order changes later on (changing the number at the beginning of the folder name) breaking the link. This would be the most commonly used method of absolute linking.

In an absolute link, the link opens with a `/`. Here is an example of an absolute link made to `pages/01.blog/test-post-2/test_image_2.jpg` in the **Slug** style from `pages/01.blog/blog.md`.

```markdown
![Test Image 2](/blog/test-slug/test_image_2.jpg)
```

>>>>>> A powerful technique is to create a `user/pages/images/` folder in your Grav site and put your images here.  Then you can easily reference them with an absolute URL from any Grav page: `/images/test_image_4.jpg` and still be able to perform [media actions](../media) on them.

### Remote

Remote image links enable you to directly display pretty much any media file via its URL. This doesn't have to include your own site's content, but it can. Here is an example of how you would display to a remote image file.

```markdown
![Remote Image 1](http://getgrav.org/images/testimage.png)
```

You can link to pretty much any direct URL, including secured HTTPS links.

### Media Actions on Images

One of the main benefits of using images associated with pages is that it enables you to take advantage of [Grav's powerful media actions](../media). For example, here is a line you would use to load an image from `/pages/01.blog/test-post-3/test_image_3.jpg` from `/pages/01.blog/test-post-1/test_image_1.jpg`

```markdown
![Styling Example](../test-post-3/test_image_3.jpg?cropResize=400,200)
```

You will find more information about actions and other [media file functionality in the next chapter](../media).
