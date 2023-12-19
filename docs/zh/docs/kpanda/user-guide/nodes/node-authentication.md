# 节点认证

## 使用 SSH 密钥认证节点

如果您选择使用 SSH 密钥作为待创建集群的节点认证方式，您需要按照如下说明配置公私钥。

1. 执行如下命令，在** 待建集群的管理集群中的任意节点 **上生成公私钥。

    ```shell
    cd /root/.ssh
    ssh-keygen -t rsa
    ```

2. 执行 __ls__ 命令查看管理集群上的密钥是否创建成功，正确反馈如下：

    ```shell
    ls
    id_rsa  id_rsa.pub  known_hosts
    ```

    其中名为 __id_rsa__ 的文件是私钥，名为 __id_rsa.pub__ 的文件是公钥。

3. 执行如下命令，分别将公钥文件 __id_rsa.pub__ 加载到待创建集群的所有节点上。

    ```shell
    ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.0.0.0
    ```

    将上面命令中的 __root@10.0.0.0__ 用户账号和节点 IP 替换为待创建集群的节点用户名和 IP。** 需要在待创建集群的每台节点都执行相同的操作 **。

4. 执行如下命令，查看步骤 1 所创建的私钥文件 __id_rsa__ 。

    ```shell
    cat /root/.ssh/id_rsa
    ```

    输出如下内容：

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

    将私钥内容复制后填至界面密钥输入框。

    ![SSH 认证](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/createcluster-ssh01.png)
