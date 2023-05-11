---
hide:
   - toc
---

# Collect container logs through Sidecar

Tailing Sidecar is a [streaming sidecar container](https://kubernetes.io/docs/concepts/cluster-administration/logging/#streaming-sidecar-container),
is a Kubernetes cluster-level logging proxy. Tailing Sidercar can automatically collect and summarize the log files in the container without changing when the container cannot write to the standard output or standard error stream.

Insight supports collecting logs through the Sidercar mode, that is, running a Sidecar container in each Pod to output log data to the standard output stream so that FluentBit can collect container logs.

The `tailing-sidecar operator` is installed by default in Insight Agent.
If you want to enable the collection of file logs in the container, please mark it by adding annotations to the Pod, `tailing-sidecar operator` will be automatically injected into the Tailing Sidecar container,
The injected Sidecar container reads the files in the business container and outputs them to the standard output stream.

The specific operation steps are as follows:

1. Modify the YAML file of the Pod, and add the following parameters in the `annotation` field:

     ```yaml
     metadata:
       annotations:
         tailing-sidecar: <sidecar-name-0>:<volume-name-0>:<path-to-tail-0>;<sidecar-name-1>:<volume-name-1>:<path-to -tail-1>
     ```

     Field description:

     - `sidecar-name-0`: tailing sidecar container name (optional, container name will be created automatically if not specified, it will start with "tailing-sidecar" prefix)
     - `volume-name-0`: storage volume name;
     - `path-to-tail-0`: the file path to the tail

     !!! note

         Each Pod can run multiple sidecar containers, which can be isolated through `;`, so that different sidecar containers can collect multiple files to multiple storage volumes.

2. Restart the Pod, and after the Pod status changes to `Running`, you can use the `Log Query` interface to search for the logs in the container of the Pod.
