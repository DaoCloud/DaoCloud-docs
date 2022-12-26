---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2022-12-26
---

# What is Falco

[Falco](https://falco.org) is a `cloudnative runtime security` tool designed to detect anomalous activity in applications, and can be used to monitor the runtime security of Kubernetes applications and internal components. With only a set of rules, Falco can continuously monitor and watch for anomalous activity in containers, applications, hosts, and networks.

## What does Falco detect?

Falco can detect and alert on any behavior involving Linux system calls. Falco alerts can be triggered using specific system calls, parameters, and properties of the calling process. For example, Falco can easily detect events including but not limited to the following:

- A shell is running inside a container or pod in Kubernetes.
- A container is running in privileged mode or mounting a sensitive path, such as /proc, from the host.
- A server process is spawning a child process of an unexpected type.
- A sensitive file, such as /etc/shadow, is being read unexpectedly.
- A non-device file is being written to /dev.
- A standard system binary, such as ls, is making an outbound network connection.
- A privileged pod is started in a Kubernetes cluster.
  
For more information on the default rules that come with Falco, see the [Rules documentation](https://github.com/falcosecurity/falco/blob/master/rules_inventory/rules_overview.md).

## What are Falco rules?

Falco rules define the behavior and events that Falco should monitor. Rules can be written in the Falco rules file or in a generic configuration file. For more information on writing, managing and deploying rules, see Falco [Rules](https://falco.org/docs/rules/).

## What are Falco Alerts?

Alerts are configurable downstream operations that can be as simple as logging or as complex as STDOUT passing a gRPC call to a client. For more information on configuring, understanding, and developing alerts, see Falco [Alerts](https://falco.org/docs/alerts/). Falco can send alerts t:

- Standard output
- A file
- A system log
- A spawned program
- An HTTP[s] endpoint
- A client via the gRPC API

## What are the components of Falco?

Falco consists of the following main components:

- Userspace program: a CLI tool that can be used to interact with Falco. The userspace program handles signals, parses messages from a Falco driver, and sends alerts.

- Configuration: define how Falco is run, what rules to assert, and how to perform alerts. For more information, see [Configuration](https://falco.org/docs/configuration).

- Driver: a software that adheres to the Falco driver specification and sends a stream of system call information. You cannot run Falco without installing a driver. Currently, Falco supports the following drivers:

    - Kernel module built on libscap and libsinsp C++ libraries (default)
    - BPF probe built from the same modules
    - Userspace instrumentation

        For more information, see Falco [drivers](https://falco.org/docs/event-sources/drivers/).

- Plugins: allow users to extend the functionality of falco libraries/falco executable by adding new event sources and new fields that can extract information from events. For more information, see [Plugins](https://falco.org/docs/plugins/).
