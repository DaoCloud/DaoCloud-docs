---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2023-01-13
---

# Common commands

This page explains how to use the spiderpoolctl program to debug from the CLI command line.

- spiderpoolctl gc

Trigger a garbage collection request to the spiderpool-controller.

```shell
    --address string [optional] address for spider-controller (default to service address)
```

- spiderpoolctl ip show

Show the Pods that are using this IP. 

```shell
    --ip string [required] ip
```

- spiderpoolctl ip release

Try to release an IP.

```shell
    --ip string [optional] ip
    --force [optional] force release ip
```

- spiderpoolctl ip set

Set the IP to be used by a Pod. This will update the ippool and workload endpoint resources.

```shell
    --ip string [required] ip
    --pod string [required] pod name
    --namespace string [required] pod namespace
    --containerid string [required] pod container id
    --node string [required] the node name who the pod locates
    --interface string [required] pod interface who taking effect the ip
```
