# Q&A

This page lists some of the problems you may encounter when using the application workbench and provides solutions.

## Execution pipeline times are incorrect

When the Jenkins cluster and the application deployment cluster cross the data center, the network communication delay becomes high, and the following error messages may be reported:

```bash
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

**Solution**：

Change the deployment command from `kubectl apply -f` to `kubectl apply -f. --request-timeout=30m` in the pipeline"s Jenkinsfile

## When building images via Jenkins, the container cannot access the private image repository ****

When you encounter this problem, you can add the following command to the pipeline Jenkinsfile:

```bash
cat > /etc/containers/registries.conf << EOF
[registries.insecure]
registries = ['temp-registry.daocloud.io']
EOF
```

<!--![]()screenshots-->

## Error adding GitHub repository under GitOps module

Because GitHub has removed support for username/password, the **GitHub** repository fails to be imported through HTTP. The following error message may be displayed:

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/DaoCloud/dce-installer.git/'
```

**Solution**：

Import **GitHub** to the warehouse using SSH.

## Adding a repository in the GitOps module under a workspace prompts that the repository already exists

Currently, a warehouse binding can only be bound to one workspace, not to different workspaces.
