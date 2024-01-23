# Node Authentication

## Authenticate Nodes Using SSH Keys

If you choose to authenticate the nodes of the cluster-to-be-created using SSH keys, you need to configure the public and private keys according to the following instructions.

1. Run the following command on **any node within the management cluster of the cluster-to-be-created** to generate the public and private keys.

    ```shell
    cd /root/.ssh
    ssh-keygen -t rsa
    ```

2. Run the __ls__ command to check if the keys have been successfully created in the management cluster. The correct output should be as follows:

    ```shell
    ls
    id_rsa  id_rsa.pub  known_hosts
    ```

    The file named __id_rsa__ is the private key, and the file named __id_rsa.pub__ is the public key.

3. Run the following command to load the public key file __id_rsa.pub__ onto all the nodes of the cluster-to-be-created.

    ```shell
    ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.0.0.0
    ```

    Replace the user account and node IP in the above command with the username and IP of the nodes in the cluster-to-be-created. **The same operation needs to be performed on every node in the cluster-to-be-created**.

4. Run the following command to view the private key file __id_rsa__ created in step 1.

    ```shell
    cat /root/.ssh/id_rsa
    ```

    The output should be as follows:

    ```bash
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpQIBAAKCAQEA3UvyKINzY5BFuemQ+uJ6q+GqgfvnWwNC8HzZhpcMSjJy26MM
    UtBEBJxy8fMi57XcjYxPibXW/wnd+32ICCycqCwByUmuXeCC1cjlCQDqjcAvXae7
    Y54IXGF7wm2IsMNwf0kjFEXjuS48FLDA0mGRaN3BG+Up5geXcHckg3K5LD8kXFFx
    dEmSIjdyw55NaUitmEdHzN7cIdfi6Z56jcV8dcFBgWKUx+ebiyPmZBkXToz6GnMF
    rswzzZCl+G6Jb2xTGy7g7ozb4BoZd1IpSD5EhDanRrESVE0C5YuJ5zUAC0CvVd1l
    v67AK8Ko6MXToHp01/bcsvlM6cqgwUFXZKVeOwIDAQABAoIBAQCO36GQlo3BEjxy
    M2HvGJmqrx+unDxafliRe4nVY2AD515Qf4xNSzke4QM1QoyenMOwf446krQkJPK0
    k+9nl6Xszby5gGCbK4BNFk8I6RaGPjZWeRx6zGUJf8avWJiPxx6yjz2esSC9RiR0
    F0nmiiefVMyAfgv2/5++dK2WUFNNRKLgSRRpP5bRaD5wMzzxtSSXrUon6217HO8p
    3RoWsI51MbVzhdVgpHUNABcoa0rpr9svT6XLKZxY8mxpKFYjM0Wv2JIDABg3kBvh
    QbJ7kStCO3naZjKMU9UuSqVJs06cflGYw7Or8/tABR3LErNQKPjkhAQqt0DXw7Iw
    3tKdTAJBAoGBAP687U7JAOqQkcphek2E/A/sbO/d37ix7Z3vNOy065STrA+ZWMZn
    pZ6Ui1B/oJpoZssnfvIoz9sn559X0j67TljFALFd2ZGS0Fqh9KVCqDvfk+Vst1dq
    +3r/yZdTOyswoccxkJiC/GDwZGK0amJWqvob39JCZhDAKIGLbGMmjdAHAoGBAN5k
    m1WGnni1nZ+3dryIwgB6z1hWcnLTamzSET6KhSuo946ET0IRG9xtlheCx6dqICbr
    Vk1Y4NtRZjK/p/YGx59rDWf7E3I8ZMgR7mjieOcUZ4lUlA4l7ZIlW/2WZHW+nUXO
    Ti20fqJ8qSp4BUvOvuth1pz2GLUHe2/Fxjf7HIstAoGBAPHpPr9r+TfIlPsJeRj2
    6lzA3G8qWFRQfGRYjv0fjv0pA+RIb1rzgP/I90g5+63G6Z+R4WdcxI/OJJNY1iuG
    uw9n/pFxm7U4JC990BPE6nj5iLz+clpNGYckNDBF9VG9vFSrSDLdaYkxoVNvG/xJ
    a9Na90H4lm7f3VewrPy310KvAoGAZr+mwNoEh5Kpc6xo8Gxi7aPP/mlaUVD6X7Ki
    gvmu02AqmC7rC4QqEiqTaONkaSXwGusqIWxJ3yp5hELmUBYLzszAEeV/s4zRp1oZ
    g133LBRSTbHFAdBmNdqK6Nu+KGRb92980UMOKvZbliKDl+W6cbfvVu+gtKrzTc3b
    aevb4TUCgYEAnJAxyVYDP1nJf7bjBSHXQu1E/DMwbtrqw7dylRJ8cAzI7IxfSCez
    7BYWq41PqVd9/zrb3Pbh2phiVzKe783igAIMqummcjo/kZyCwFsYBzK77max1jF5
    aPQsLbRS2aDz8kIH6jHPZ/R+15EROmdtLmA7vIJZGerWWQR0dUU+XXA=
    ```

Copy the content of the private key and paste it into the interface's key input field.
