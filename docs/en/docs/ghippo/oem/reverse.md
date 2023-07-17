# Automatic Reverse Proxy Configuration

Reverse proxy refers to the reverse proxy server used to meet the requirement of accessing via a bound domain name.

## SSH into DCE

```bash
ssh -l root {dce_master_node_ip}
```

## Download Offline Installation Package

```bash
wget http://dao-get.daocloud.io/dx-arch-0.4.4.tar.gz
```

## Extract the Installation Package

```bash
tar xvzf dx-arch-0.4.4.tar.gz
```

The extracted contents of the installation package include backup scripts such as `backup-pg.sh`:

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

## Run the Automation Script to Upgrade DX-ARCH

```bash
cd dx-arch-package-0.4.4
./tools/set-reverse-proxy.sh
```

### Set Reverse Proxy Address

!!! tip

    Set the entry address of `dx-arch` as the address of the reverse proxy
    (the reverse proxy needs to be configured separately, such as forwarding to the `dx-arch-ui` service
    or the previously set NodePort address or LB address).
    The reverse proxy address format can be `scheme://host:port` or `scheme://host:port/path`.

    - The scheme can be either `https` or `http`.
    - The host can be an IP address or a domain name.
    - The port must also be specified, such as `port80` for HTTP or `port443` for HTTPS.

    Note: Do not add a `/` at the end of the reverse proxy URL, as it may cause issues in subsequent access.

In this case, `DX ARCH` has not yet set up a reverse proxy. Specify the reverse proxy URL,
and the reverse proxy can be successfully configured. This process is only needed for the initial setup of the reverse proxy.

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

Note: If the reverse proxy uses a test domain name (e.g., dx-arch.com) instead of a real public domain name,
the `dx-arch-ram` Pod cannot access that domain name. In this case, you need to temporarily modify the
deployment of `dx-arch-ram` by adding `hostAliases` for testing. If it is a public domain name, then this issue does not exist.

```yaml
spec:
    hostAliases:
    - hostnames:
        - dx-arch.com
        ip: 10.6.165.11
```

### Modify Reverse Proxy Address

In this case, `DX ARCH` has already set up a reverse proxy, and you want to change the URL for this setting.
To modify the reverse proxy address, follow this process. After modifying the reverse proxy,
the address information for DX ARCH SSO will also change. Remember to update the DX ARCH configuration in AnyProduct accordingly.

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

### Clear Reverse Proxy

In this case, `DX ARCH` has already set up a reverse proxy, and you want to clear the URL for this setting.
To clear the reverse proxy, leave the URL field empty. After clearing the reverse proxy, you will access
`dx-arch` using the previously set NodePort or LB method. Follow this process to cancel the reverse proxy setting.
After removing the reverse proxy, the address information for DX ARCH SSO will also change.
Remember to update the DX ARCH configuration in AnyProduct accordingly.

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

### Exceptional Cases

#### No Reverse Proxy Set and Empty Input Value for Reverse Proxy

In this case, `DX ARCH` has not yet set up a reverse proxy, and the input value for the reverse proxy URL
is empty (not filled in). In this situation, the script will exit because the URL is the same and empty.

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch):

The received value is the same as the original value...
Exit the process of setting up the reverse proxy...
```

#### Reverse Proxy Already Set and Input Value Matches the Existing Reverse Proxy

In this case, `DX ARCH` has already set up a reverse proxy, and the URL for this setting is
the same as the current URL. In this situation, the script will exit because the URLs are the same.

```console
=============== Set DX-ARCH Reverse Proxy ===============

Version: 0.4.4-409

Enter Installed DX-ARCH Namespace [default: dx-arch]:

Notice: If the input is null, the reverse proxy address that has been set will be removed
Enter reverse proxy url(example: http://10.0.0.1/dx-arch) [current: http://10.0.0.1/dx-arch]:http://10.0.0.1/dx-arch

The received value is the same as the original value...
Exit the process of setting up the reverse proxy...
```
