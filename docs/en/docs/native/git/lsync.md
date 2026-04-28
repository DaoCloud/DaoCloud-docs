# Batch Check Chinese-English Sync Issues

This article is based on [./scripts/lsync.sh](https://github.com/DaoCloud/DaoCloud-docs/blob/main/scripts/lsync.sh)
to batch detect sync issues between Chinese and English documents.

## MacOS

In the repository root directory,

1. Make lsync.sh script executable (mainly to solve __permission denied__ issue)

    ```sh
    sudo chmod +x ./scripts/lsync.sh
    ```

1. Check the sync status of Chinese and English documents in a folder

    ```sh
    ./scripts/lsync.sh docs/en/docs/kpanda
    ```

    Output similar to:

    ```diff
    1	1	docs/zh/docs/kpanda/user-guide/clusters/cluster-version.md
    7	7	docs/zh/docs/kpanda/user-guide/clusters/access-cluster.md
    7	5	docs/zh/docs/kpanda/user-guide/clusters/runtime.md
    ```

    The first number represents added lines, the second number represents deleted lines
