---
hide:
  - toc
---

# Common Git Commands

This page lists some commonly used Git commands.

| Type | Command Description | Git Command |
| --- | ------- | -------- |
| Create | Create a branch | git checkout -b branch-name |
| | Switch to a branch | git checkout branch2 |
| View | List all local branches | git branch |
| | Check branch status | git status |
| | View git commit history | git log |
| | View command history | history |
| Commit | Stage a specific file | git add /docs/en/test.md |
| | Stage all current changes | git add . |
| | Commit local changes | git commit -m "change a text for chapter 1" |
| | First push to GitHub | git push origin branch-name |
| | Force push after modifications | git push origin branch-name -f |
| Delete | Delete a branch | git branch -D branchName |
| | Delete all branches except current | git branch | xargs git branch -d |
| | Delete branches containing 'dev' | git branch | grep 'dev\*' | xargs git branch -d |
| Rebase | Sync current branch with main | git rebase main |
| | Rebase or squash last 3 commits | git rebase -i HEAD~3 |

For more Git commands, please refer to the [Git Command Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf).
