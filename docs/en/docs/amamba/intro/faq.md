# FAQ

This page provides solutions to some common problems you may encounter when using App Workbench.

## Error when running a pipeline

High network communication delay can lead to pipeline running errors, if Jenkins and the application are deployed in different data centers. The error message looks like:

```bash
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

**Solution:**

In the pipeline's Jenkinsfile, change the deployment command from `kubectl apply -f` to `kubectl apply -f. --request-timeout=30m`.

## Container cannot access private image registry when building images via Jenkins

If the container cannot access the private image registry, add the following command to the pipeline's Jenkinsfile:

```bash
cat > /etc/containers/registries.conf << EOF
[registries.insecure]
registries = ['temp-registry.daocloud.io']
EOF
```

![add command](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/faq01.png)

## Error when adding GitHub repo in GitOps section

When adding a **GitHub** repository in the GitOps section, the following error may appear due to GitHub removing support for username/password:

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/DaoCloud/dce-installer.git/'
```

**Solution:**

Use SSH to import the **GitHub** repository.

## Repo exists when adding it in GitOps section

One repo can be bound to only **one** workspace. When a repo is already bound to a workspace, but you try to add it in GitOps section under another workspace, such error will occur.

**Solution:**

Unbind the repo from its current workspace and then add it again in GitOps section under your target workspace.