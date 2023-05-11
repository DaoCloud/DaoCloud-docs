# FAQs

This page lists some failures you may encounter when using the App Workbench and gives solutions.

## Execute the pipeline and report an error

When the cluster where Jenkins resides and the application deployment cluster cross data centers, the network communication delay will become higher, and the following error message may be encountered:

```bash
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

**solution**:

In the Jenkinsfile of the pipeline, modify the deployment command from `kubectl apply -f` to `kubectl apply -f . --request-timeout=30m`

## When building an image through Jenkins, the container cannot access the private image repository****

When encountering this problem, you can add the following command to the Jenkinsfile of the pipeline:

```bash
cat > /etc/containers/registries.conf << EOF
[registries. insecure]
registries = ['temp-registry.daocloud.io']
EOF
```

![Add command](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/faq01.png)

## Adding a GitHub repository under the GitOps module reports an error

Since GitHub has removed the support for username/password, when importing **GitHub** repositories via HTTP, the import will fail, and the following error message may appear:

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/DaoCloud/dce-installer.git/'
```

**solution**:

Import the **GitHub** repository using SSH.

## When adding a warehouse in the GitOps module under a certain workspace, it prompts that the warehouse already exists

Currently, a warehouse can only be bound to one workspace, and cannot be bound to different workspaces.