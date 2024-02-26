---
hide:
   - toc
---

# Collecting Container Logs through Sidecar

Tailing Sidecar is a Kubernetes cluster-level logging proxy that acts as a streaming sidecar container. It allows automatic collection and summarization of log files within containers, even when the container cannot write to standard output or standard error streams.

Insight supports log collection through the Sidecar mode, which involves running a Sidecar container alongside each Pod to output log data to the standard output stream. This enables FluentBit to collect container logs effectively.

The Insight Agent comes with the __tailing-sidecar operator__ installed by default. To enable file log collection within a container, you can add annotations to the Pod, which will automatically inject the Tailing Sidecar container. The injected Sidecar container reads the files in the business container and outputs them to the standard output stream.

Here are the specific steps to follow:

1. Modify the YAML file of the Pod and add the following parameters in the __annotation__ field:

    ```yaml
    metadata:
      annotations:
        tailing-sidecar: <sidecar-name-0>:<volume-name-0>:<path-to-tail-0>;<sidecar-name-1>:<volume-name-1>:<path-to -tail-1>
    ```

    Field description:

    - __sidecar-name-0__ : Name for the Tailing Sidecar container (optional; a container name will be created automatically if not specified, starting with the prefix "tailing-sidecar").
    - __volume-name-0__ : Name of the storage volume.
    - __path-to-tail-0__ : File path to tail.

    !!! note

        Each Pod can run multiple sidecar containers, separated by __;__ . This allows different sidecar containers to collect multiple files and store them in various volumes.

2. Restart the Pod. Once the Pod's status changes to __Running__ , you can use the __Log Query__ interface to search for logs within the container of the Pod.
