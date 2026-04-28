# Common Git Issues

After completing local edits and pushing to GitLab, it will trigger the pipeline. Please ensure the pipeline succeeds before merging the PR.

If there was a PR that couldn't be merged or doesn't need to be merged, please close it first.

For GitLab operations like pull, commit, push, rebase, squash, etc., you can use some Git GUI tools.

## Rebase Issues

If prompted to rebase when submitting a PR, you can try the following solutions.

### Solution 1

Other commands are the same as step 3 in [GitLab Documentation Upload Process](index.md). When making the second commit, run:

```bash
git commit --amend --no-edit 
```

> Because projects like kpanda advocate 1 commit per PR, this command will append changes to the previous commit.

Then run __git push origin docsite -f__ to force push to remote repository.

### Solution 2

After submitting PR and prompted to rebase, run the following commands in order:

```bash
git checkout main
```
