# 自动设置反代

反代指的是反向代理，以实现绑定域名访问的需求。

## SSH 到 DCE

```bash
ssh -l root {dce_master_node_ip}
```

## 下载离线安装包

```bash
wget http://dao-get.daocloud.io/dx-arch-0.4.4.tar.gz
```

## 解压安装包

```bash
tar xvzf dx-arch-0.4.4.tar.gz
```

解压安装包后的内容包含备份脚本 backup-pg.sh 等：

```console
dx-arch-package-0.4.4/dx-arch-images-0.4.1.tar
dx-arch-package-0.4.4/helm/
.....
dx-arch-package-0.4.4/helm/hack/pg-backup-cronjob-tmpl.yaml
dx-arch-package-0.4.4/install.sh
dx-arch-package-0.4.4/[README.md](http://readme.md/)
dx-arch-package-0.4.1/tools/
dx-arch-package-0.4.1/tools/backup-pg.sh
dx-arch-package-0.4.1/tools/push-offline-images.sh
dx-arch-package-0.4.1/tools/set-reverse-proxy.sh
dx-arch-package-0.4.1/update-dx-arch.sh
```

## 运行自动化脚本升级 DX-ARCH

```bash
cd dx-arch-package-0.4.4
./tools/set-reverse-proxy.sh
```

### 设置反代地址

!!! tip

    把 dx-arch 的入口地址设置为反向代理的地址
    （反向代理需另外自行配置，可把反向代理设置为转发到 dx-arch-ui 这个 service，或者之前设的 nodeport 地址或者 LB 地址）。
    反代地址格式：`scheme://host:port` 或者 `scheme://host:port/path` 都可以，

    - scheme 可以是 https 或 http
    - host 可以是 ip 或域名
    - port 也需要填，例如 http 的 port80 或 https 的 port443

    注意：设置的反代 url 最后不要加 `/`，加了后续访问会出问题

此情况为 DX ARCH 还没有设置反代，指定反代 url 后，可成功设置反代。第一次设置反代走此流程即可。

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch): http://10.0.0.1/dx-arch

Input reverse proxy url: http://10.0.0.1/dx-arch

Continue set reverse proxy? [y/n]: y

exec update cmd: helm -n dx-arch upgrade --wait --timeout 5m dx-arch /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/../helm/dx-arch-0.4.4-409.tgz -f /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/.update-dx-arch-values.yaml.tmp --set baseUrl=http://10.0.0.1/dx-arch

Release "dx-arch" has been upgraded. Happy Helming!
NAME: dx-arch
LAST DEPLOYED: Mon Nov 2 11:25:26 2020
NAMESPACE: dx-arch
STATUS: deployed
REVISION: 4
TEST SUITE: None

Reverse Proxy Successfully Set!
UI Access URL: http://10.0.0.1/dx-arch
```

注意：如果反代使用的是测试域名（例如 dx-arch.com），不是真正的公网域名，dx-arch-ram 的 Pod 访问不到该域名，
则需要临时修改 dx-arch-ram 的 deployment 加 hostAliases 来作测试，如是公网域名则没有这个问题。

```yaml
spec:
    hostAliases:
    - hostnames:
        - dx-arch.com
        ip: 10.6.165.11
```

### 修改反代地址

此情况为 DX ARCH 设置过反代，且这次设置的 url 为新的 url，即可修改反代地址。
想要修改反代设置的走此流程即可。反代修改后，DX ARCH SSO 的地址信息也会改变，请记得前往 AnyProduct 修改 DX ARCH 配置信息。

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch) [current: http://10.0.0.1/dx-arch]: http://10.0.0.2/dx-arch

Original reverse proxy url: http://10.0.0.1/dx-arch

Input reverse proxy url: [http://10.0.0.2/dx-arch](http://10.0.0.1/dx-arch)

Continue set reverse proxy? [y/n]: y

exec update cmd: helm -n dx-arch upgrade --wait --timeout 5m dx-arch /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/../helm/dx-arch-0.4.4-409.tgz -f /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/.update-dx-arch-values.yaml.tmp --set baseUrl=[http://10.0.0.2/dx-arch](http://10.0.0.1/dx-arch)

Release "dx-arch" has been upgraded. Happy Helming!
NAME: dx-arch
LAST DEPLOYED: Mon Nov 2 11:34:59 2020
NAMESPACE: dx-arch
STATUS: deployed
REVISION: 5
TEST SUITE: None

Reverse Proxy Successfully Set!
UI Access URL: [http://10.0.0.2/dx-arch](http://10.0.0.1/dx-arch)
```

### 清除反代

此情况为 DX ARCH 设置过反代，且这次设置的 url 为空，即可清除反代。
清除反代后会用之前在环境里设置的 nodeport 或 LB 的方式来访问 dx-arch。
想要取消反代设置的走此流程即可。反代清除后，DX ARCH SSO 的地址信息也会改变，
请记得前往 AnyProduct 修改 DX ARCH 配置信息。

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch) [current: http://10.0.0.1/dx-arch]:

Original reverse proxy url: http://10.0.0.1/dx-arch

Reverse proxy url entered is empty
The reverse proxy that has been set will be cleared

Continue set reverse proxy? [y/n]: y

exec update cmd: helm -n dx-arch upgrade --wait --timeout 5m dx-arch /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/../helm/dx-arch-0.4.4-409.tgz -f /root/dist/dx-arch-package-0.4.4-9c437f8-409/tools/.update-dx-arch-values.yaml.tmp

Release "dx-arch" has been upgraded. Happy Helming!
NAME: dx-arch
LAST DEPLOYED: Mon Nov 2 11:34:59 2020
NAMESPACE: dx-arch
STATUS: deployed
REVISION: 5
TEST SUITE: None

Reverse Proxy Successfully Set!
UI Access URL: https://10.6.165.2:30034
```

### 异常情况说明

#### 未设置反代，且反代输入值为空

此情况为 DX ARCH 还没有设置反代，且设置的 url 是空（为填写），那么会因为 url 相同且为空而退出设置脚本。

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch):

The received value is the same as the original value...
Exit the process of setting up the reverse proxy...
```

#### 设置了反代且设置的反代有输入值且与已设置的反代相同时

此情况为 DX ARCH 设置过反代，且这次设置的 url 和目前的 url 相同，那么会因为 url 相同而退出设置脚本。

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch) [current: http://10.0.0.1/dx-arch]:http://10.0.0.1/dx-arch

The received value is the same as the original value...
Exit the process of setting up the reverse proxy...
```
