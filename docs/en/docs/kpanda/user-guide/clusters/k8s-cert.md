# Kubernetes Cluster Certificate Renewal

To ensure secure communication between Kubernetes components, TLS authentication is used. This requires configuring cluster PKI certificates.

Cluster certificates are valid for one year. To prevent service disruption due to expired certificates, please renew them in time.

This document explains how to manually renew cluster certificates.

## Check if Certificates Are Expired

You can run the following command to check certificate expiration:

```shell
kubeadm certs check-expiration
```

Sample output:

```output
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Dec 14, 2024 07:26 UTC   204d                                    no      
apiserver                  Dec 14, 2024 07:26 UTC   204d            ca                      no      
apiserver-etcd-client      Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
apiserver-kubelet-client   Dec 14, 2024 07:26 UTC   204d            ca                      no      
controller-manager.conf    Dec 14, 2024 07:26 UTC   204d                                    no      
etcd-healthcheck-client    Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
etcd-peer                  Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
etcd-server                Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
front-proxy-client         Dec 14, 2024 07:26 UTC   204d            front-proxy-ca          no      
scheduler.conf             Dec 14, 2024 07:26 UTC   204d                                    no      

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Dec 12, 2033 07:26 UTC   9y              no      
etcd-ca                 Dec 12, 2033 07:26 UTC   9y              no      
front-proxy-ca          Dec 12, 2033 07:26 UTC   9y              no      
```

## Manually Renew Certificates

You can manually renew certificates with the following commands. Be sure to back up the current certificates before proceeding.

Renew a specific certificate:

```shell
kubeadm certs renew
```

Renew all certificates:

```shell
kubeadm certs renew all
```

The renewed certificates are stored in `/etc/kubernetes/pki`, and the new validity period is one year. The following configuration files will also be updated:

* `/etc/kubernetes/admin.conf`
* `/etc/kubernetes/controller-manager.conf`
* `/etc/kubernetes/scheduler.conf`

!!! note

    - If you're running a highly available (HA) cluster, you must run this command on **all** control plane nodes.
    - The command uses the CA (or front-proxy-CA) certificates and keys stored in `/etc/kubernetes/pki`.

## Restart Services

After renewing certificates, you must restart the control plane Pods. This is necessary because not all components and certificates support dynamic reloading.

Static Pods are managed by the local kubelet rather than the API server, so `kubectl` cannot be used to delete or restart them.

To restart static Pods, temporarily move the manifest files out of `/etc/kubernetes/manifests/` and wait about 20 seconds. This delay is based on the `fileCheckFrequency` value defined in the [KubeletConfiguration schema](https://kubernetes.io/zh-cn/docs/reference/config-api/kubelet-config.v1beta1/).

If a Pod's manifest is not present, kubelet will stop the Pod. Once you move the files back, kubelet will recreate the Pods and apply the new certificates.

```shell
mv ./manifests/* ./temp/
mv ./temp/* ./manifests/
```

!!! note

    If you're using Docker as the container runtime, you can restart the relevant services to apply the new certificates:

    ```shell
    docker ps | grep -E 'k8s_kube-apiserver|k8s_kube-controller-manager|k8s_kube-scheduler|k8s_etcd_etcd' | awk -F ' ' '{print $1}' | xargs docker restart
    ```

## Update KubeConfig

When creating a cluster, the **admin.conf** file is usually copied to **\$HOME/.kube/config**. To update the kubeconfig after renewing `admin.conf`, run:

```shell
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## Enable Kubelet Certificate Rotation

The steps above update almost all certificates in the cluster, except for kubelet.

Kubernetes supports **kubelet certificate rotation**, which automatically generates a new key and requests a new certificate when the current one is about to expire. The new certificate is then used for authenticating connections with the API server.

!!! note

    This feature is available in Kubernetes 1.8.0 and later.

To enable client certificate rotation, configure the following:

* Pass the `--rotate-certificates` flag to the kubelet process. This determines whether kubelet will auto-renew its certificate.
* Pass the `--cluster-signing-duration` flag (or `--experimental-cluster-signing-duration` in versions prior to 1.19) to the `kube-controller-manager` to set the certificate's validity duration.

For more details, refer to [Configure kubelet certificate rotation](https://kubernetes.io/zh-cn/docs/tasks/tls/certificate-rotation/).

## Automatic Certificate Renewal

To more efficiently handle expired or expiring certificates, refer to the following guide:
[k8s version cluster certificate renewal](https://github.com/yuyicai/update-kube-cert/blob/master/README-zh_CN.md).

## Disable Automatic Certificate Renewal

### For Newly Created Clusters

By default, Kubernetes automatically renews certificates every month, which causes control plane components (apiserver, controller, scheduler, etcd) to restart during the process.

To disable automatic renewal, set the following advanced configuration when creating the cluster:

```yaml
auto_renew_certificates: false
```

![Certificate](../images/zhengshu.png)

### For Existing Clusters

For already created clusters, each node has two systemd services that must be stopped and removed to disable auto-renewal. Run the following:

```bash
k8s-certs-renew.service
k8s-certs-renew.timer
```

## Configure Certificate Validity Period

By default, certificates are valid for one year. To change this duration, set the following parameters in the advanced cluster configuration:

```yaml
auto_renew_certificates: false  # Disable automatic renewal
kube_cert_validity_period: 87600h  # Set non-CA certificate validity to 10 years
kube_ca_cert_validity_period: 175200h  # Set CA certificate validity
```
