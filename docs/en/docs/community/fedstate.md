---
MTPE: windsonsea
date: 2024-06-19
---

# FedState

FedState refers to the Federation Stateful Service, which is mainly designed to
provide stateful service orchestration, scheduling, deployment, and automated
operation and maintenance capabilities in scenarios with multiple clouds, clusters, and data centers.

## Overview

FedState is used to deploy middleware, databases, and other stateful services that
need to be deployed in a multi-cloud environment to each member cluster through Karmada,
so that they can work normally and provide some advanced operation and maintenance capabilities.

## Architecture

![architecture](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/community/images/structure.png)

FedState consists of the following components:

- FedStateScheduler: A multi-cloud stateful service scheduler, based on the Karmada scheduler,
  adds some scheduling policies related to middleware services.
- FedState: The multi-cloud stateful service controller is mainly responsible for configuring
  various control clusters as needed and distributing them through Karmada.
- Member Operator: A concept that refers to a stateful service operator deployed in the control plane.
  FedState has built-in Mongo operators and will support more stateful services in the future.
- FedStateCR: A concept representing a multi-cloud stateful service instance.
- FedStateCR-Member: A concept representing an instance of a multi-cloud stateful service that
  has been distributed to the control plane.

## References

- Blog: [Cloud Native Federation Middleware - FedState](../blogs/230605-fedstate.md)
- Repo url: https://github.com/fedstate/fedstate
