---
MTPE: windsonsea
Date: 2024-04-08
---

# Offline Clipper Script User Manual

The offline package contains offline resources for all products of DCE 5.0. However, in actual usage,
customers may not need to deploy all products. Therefore, the offline package clipper script
`offline/utils/offline-clipper.sh` in installer v0.16.0 provides the `offline-clipper.sh` script
to trim the offline package. This allows customers to decide which products' offline resources to use based on their actual needs.

## Prerequisites

- Clipper is only for GProduct. Before clipping, you need to understand which GProducts are included
  and their corresponding product codes. Refer to the information in the `components` section of
  the [product list file manifest.yaml](../commercial/manifest.md).

- The `kubean`, `ghippo`, and `kpanda` components must exist, meaning these three components will be retained by default.

## Operating Guide

- If the input is an offline package tarball and the output is an offline package tarball, for example, to keep the `insight` component:

    ```shell
    offline-clipper.sh --in-tar-path ./offline-v0.15.0-amd64.tar --out-tar-path ./offline.tar --enable-only insight
    ```

- If the input is the `offline` directory extracted from the offline package and the output is the source directory of the extracted offline package, for example, to keep the `insight` component:

    ```shell
    offline-clipper.sh --offline-path ./offline --enable-only insight
    ```

- If the input is an offline package tarball and the output is the extracted offline package directory, for example, to trim only the `insight` component:

    ```shell
    offline-clipper.sh --in-tar-path ./offline-v0.15.0-amd64.tar --disable-only insight
    ```

- If the input is the offline package directory and the output is an offline package tarball, for example, to keep the `insight` and `skoala` components:

    ```shell
    offline-clipper.sh --offline-path ./offline --out-tar-path ./offline.tar --enable-only insight,skoala
    ```

- View the names of trimmable components:

    ```shell
    offline-clipper.sh --offline-path ./offline -l
    ```

- View the help document:

    ```shell
    offline-clipper.sh -h
    ```
