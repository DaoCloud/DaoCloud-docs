# KWOK (`K`ubernetes `W`ith`O`ut `K`ubelet)

![kwok](./images/kwok.png){ align=right }

[kwok](https://sigs.k8s.io/kwok) is a toolkit that enables setting up a cluster of thousands of Nodes in seconds.
Under the scene, all Nodes are simulated to behave like real ones, so the overall approach employs
a pretty low resource footprint that you can easily play around on your laptop.

So far we provide two tools:

- **Kwok:** Core of this repo. It simulates thousands of fake Nodes.
- **Kwokctl:** A CLI to facilitate creating and managing clusters simulated by Kwok.

Please see [https://kwok.sigs.k8s.io](https://kwok.sigs.k8s.io) for more in-depth information.

![manage clusters](./images/manage-clusters.svg)

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- [Slack](https://kubernetes.slack.com/messages/sig-scheduling)
- [Mailing List](https://groups.google.com/forum/#!forum/kubernetes-sig-scheduling)

[Go to kwok repo](https://github.com/kubernetes-sigs/kwok){ .md-button }
