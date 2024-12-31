# FAQs

This page lists some common issues that may be encountered in the cloud edge collaboration module, providing convenient troubleshooting solutions.

1. **TLS certificate authentication issues when downloading container images**

   If you encounter this issue, you need to bypass TLS certificate authentication for private https services. The solution varies by runtime as follows:

   **containerd:**

   Configure the **/etc/containerd/config.toml** file. The following content is a reference configuration, which can be customized according to your needs.

   ```config
   ...
   [plugins."io.containerd.grpc.v1.cri".registry.configs]
       [plugins."io.containerd.grpc.v1.cri".registry.configs."reg.xxx.cn".tls]
           insecure_skip_verify = true
   ```

   **Docker:**

   Configure the **/etc/docker/daemon.json** file. The following content is a reference configuration, which can be customized according to your needs.

   ```json
   {
       ...
       "insecure-registries": [
           "0.0.0.0/0"
       ],
       ...
   }
   ```

2. **CNI cannot be used correctly**

   The steps to resolve this issue are as follows:

   1. **Download and extract the CNI plugin package**

      Visit the [containernetworking release](https://github.com/containernetworking/plugins/releases) page and download the **cri-plugins-{os}-{arch}-{version}.tar.gz** package. This package will contain the cni tools. Use the command to extract the binary files from the compressed package to the **/opt/cni/bin** directory.

      ```shell
      mkdir -p /opt/cni/bin 
      tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
      ```

   2. **Create default CNI configuration file**

      Create the default CNI configuration file in the **/etc/cni/net.d/** directory. The filename can be something like: 10-mynet.conf. The specific configuration is as follows:

      ```json
      {
        "cniVersion": "1.0.0",
        "name": "mynet",
        "plugins": [
          {
            "type": "bridge",
            "bridge": "cni0",
            "isGateway": true,
            "ipMasq": true,
            "promiscMode": true,
            "ipam": {
              "type": "host-local",
              "ranges": [
                [{
                  "subnet": "10.88.0.0/16"
                }],
                [{
                   "subnet": "2001:db8:4860::/64"
                }]
              ],
              "routes": [
                { "dst": "0.0.0.0/0" },
                { "dst": "::/0" }
              ]
            }
          },
          {
            "type": "portmap",
            "capabilities": {"portMappings": true}
          }
        ]
      }
      ```
