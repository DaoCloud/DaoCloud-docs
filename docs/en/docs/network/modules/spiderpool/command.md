# Common commands

This page explains how to use the spiderpoolctl program to debug from the CLI command line.

## spiderpoolctl gc

Trigger a garbage collection request to the spiderpool-controller.

```shell
    --address string [optional] address for spider-controller (default to service address)
```

## spiderpoolctl ip show

Shows the Pods that are using this IP. The options are:

```shell
    --ip string [required] ip
```

## spiderpoolctl ip release

Try to release an IP. The options are:

```shell
    --ip string [optional] ip
    --force [optional] force release ip
```

## spiderpoolctl ip set

Sets the IP to use for a Pod. This will update the ippool and workload endpoint resources. The options are:

```shell
    --ip string [required] ip
    --pod string [required] pod name
    --namespace string [required] pod namespace
    --containerid string [required] pod container id
    --node string [required] the node name who the pod locates
    --interface string [required] pod interface who taking effect the ip
```