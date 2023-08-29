# MirageDebug

MirageDebug: Local remote debugging for Kubernetes apps, enabling fully authentic environment debugging.

![MirageDebug](./images/flow.d2.svg)

## Installation

### Install MirageDebug

MirageDebug currently requires the GO runtime environment for installation, and can be installed using the following method:

```bash
go install github.com/miragedebug/miragedebug/cmd/mirage-debug@latest
```

## Usage

### MirageDebug Server - Background Service

MirageDebug Server is a background service that manages debugging sessions and provides relevant information about the debugging sessions.

#### Start MirageDebug Server

```bash
mirage-debug server
```

### Initialize Debugging Application

Run the following command in the project root directory to initialize the debugging application, and fill in the relevant information as prompted.

```bash
mirage-debug init
```

### Write IDE Configuration Files

MirageDebug can automatically generate debugging configuration files for different IDEs, making it easy to start debugging locally.

```bash
mirage-debug config <APPNAME>
```

### Start Debugging

Once the IDE is configured, you can start debugging directly in the IDE.

## Demo

### VSCode debug rust applications in Kubernetes cluster

[![MirageDebug debugging Rust application in Kubernetes: using VSCode to debug ztunnel locally](https://img.youtube.com/vi/RpggulEd48M/0.jpg)](https://www.youtube.com/watch?v=RpggulEd48M)

### Goland debug istiod in Kubernetes cluster

[![MirageDebug: Using Goland to debug Istio (Pilot-discovery) in the cluster locally](https://img.youtube.com/vi/ZwG0uaG72_8/0.jpg)](https://www.youtube.com/watch?v=ZwG0uaG72_8)
