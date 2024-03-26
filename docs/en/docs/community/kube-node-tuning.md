# kube-node-tuning

kube-node-tuning is aimed at kernel tuning by kubernetes. It's useful to:

* High performance application
* Large Scale Cluster
* Network Tuning

## Quick Start

```bash
export VERSION=v0.3.1
helm repo add kube-node-tuning https://kubean-io.github.io/kube-node-tuning/
helm install -n kube-node-tuning kube-node-tuning kube-node-tuning/kube-node-tuning --version $VERSION --create-namespace
```

!!! tip

    If the machine is in China, you should following by: [quick-start-in-china](docs/quick-start-in-china.md)

The kernel's sysctl settings are applied to the node at /etc/99-kube-node-tuning.conf.

Check if the settings are applied by the following command.
SSH to the node of cluster

```bash
cat /etc/sysctl.d/99-kube-node-tuning.conf
sysctl -a # view the sysctl setting
```

## Configuration

```bash
# Change the config
kubectl -n kube-node-tuning edit cm/kube-node-tuning-config -o yaml

# Restart the DaemonSet
kubectl -n kube-node-tuning rollout restart ds kube-node-tuning
```

## Roadmap

* Different OS Support. (Ubuntu, CentOS, RHEL, etc.)
* Multi profile
* Operator instead of Daemonset

## Reference

- [kube-node-tunning repo](https://github.com/kubean-io/kube-node-tuning)
