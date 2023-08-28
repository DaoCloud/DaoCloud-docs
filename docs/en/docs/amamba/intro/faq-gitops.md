# GitOps Issues

This page provides solutions to some common issues you may encounter when using the GitOPS feature.

## Error when adding a GitHub repo

When adding a **GitHub** repository in the GitOps section, the following error may appear due to GitHub removal of username/password auth:

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/DaoCloud/dce-installer.git/'
```

**Solution:**

Use SSH to import your **GitHub** repository.

## Repo exists when adding it in a certain workspace

One repo can be bound to only **one** workspace. When a repo is already bound to a workspace, but you try to add it in GitOps section under another workspace, such error will occur.

**Solution:**

Unbind the repo from its current workspace and then add it again in GitOps section under your target workspace.
