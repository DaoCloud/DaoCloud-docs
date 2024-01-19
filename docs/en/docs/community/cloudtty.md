# CloudTTY：A Kubernates Cloud Shell (Web Terminal) Operator

CloudTTY is an easy-to-use operator to run a web terminal and cloud shell intended for a kubernetes-native environment. You can easily open a terminal on your own browser via CloudTTY. The community is always open for any contributor and those who want to have a try.

Literally, CloudTTY herein refers to a virtual console, shell, or terminal running on web and clouds. You can use it anywhere with an internet conneciton and it will be automatically connected to the cloud.

!!! info "What is TTY"

    Early user terminals connected to computers were electromechanical teleprinters or teletypewriters (TeleTYpewriter, TTY), which might be the origin of TTY. Gradually, TTY has continued to be used as the name for a text-only console, although now it is a virtual console not a physical one.

## Why Do You Need CloudTTY?

Currently, the community has explored TTY technology to a certain depth through projects like
[ttyd](https://github.com/tsl0922/ttyd), providing terminal capabilities on top of web browsers.

However, in the context of Kubernetes, these TTY projects require more cloud native capabilities.
How can ttyd be run inside containers? How can it be accessed through NodePort or Ingress?
How can multiple instances be created using CRDs?

CloudTTY provides solutions to these problems. Give CloudTTY a try 🎉!
CloudTTY has been selected for inclusion in the CNCF Landscape:

![landscape](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/community/images/cloudtty.png)

## Use Cases

CloudTTY is applicable to the following cases:

1. Many enterprises use a cloud platform to manage Kubernetes, but due to security reasons,
   you cannot use SSH to connect the node host to run `kubectl` commands.
   In this case, you may require a cloud shell capability.

2. A running container on Kubernetes can be "entered" (via `Kubectl exec`) on a browser web page.

3. The container logs can be displayed in real time (scrolling) on a browser web page.

The demo effect of CloudTTY is as follows:

![screenshot_gif](https://github.com/cloudtty/cloudtty/raw/main/docs/snapshot.gif)

After the CloudTTY is intergated to your own UI, it would look like:

![demo_png](https://github.com/cloudtty/cloudtty/raw/main/docs/demo.png)

[Go to CloudTTY repo](https://github.com/cloudtty/cloudtty){ .md-button }

<p align="center">
<img src="https://landscape.cncf.io/images/left-logo.svg" width="150"/>&nbsp;&nbsp;<img src="https://landscape.cncf.io/images/right-logo.svg" width="200"/>
<br/><br/>
CloudTTY enriches <a href="https://landscape.cncf.io/?selected=cloud-tty">CNCF Landscape.</a>
</p>
