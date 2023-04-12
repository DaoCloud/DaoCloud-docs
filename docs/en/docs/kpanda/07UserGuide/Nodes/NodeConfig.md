# node configuration

## Authenticating Nodes Using SSH Keys

If you choose to use SSH keys to connect to all the nodes of the cluster to be created, you need to configure the public and private keys as described below.

1. Execute the following command to generate public and private keys on any node of the managed cluster.

    ```yaml
    cd /root/.ssh #Enter the .ssh path
    ssh-keygen -t rsa #generate key
    ```

2. Execute the `ls` command to check whether the key on the management cluster is successfully created, and the correct feedback is as follows:

    ```yaml
    ls #View all files in the directory, the expected output is as follows:
    id_rsa id_rsa.pub known_hosts
    ```

    Where the file named `id_rsa` is the private key and the file named `id_rsa.pub` is the public key.

3. Send the public key file `id_rsa.pub` to all nodes of the cluster to be created through SCP.

    ```yaml
    scp /root/.ssh/id_rsa.pub root@10.0.0.0:/root/.ssh/id_rsa.pub
    ```

    Replace the root@10.0.0.0 user account and IP in the above command with the node username and IP of the cluster to be created. Each planned node of the cluster to be created needs to perform the same operation.

4. Base 64 encode the private key file `id_rsa`.

    ```yaml
    base64 id_rsa #Encode the private key file in base64 format
    ```

5. Download the encoded private key file `id_rsa` to your current node, and upload the private key file on the interface.

    