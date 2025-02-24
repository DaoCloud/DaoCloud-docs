# Upgrading EgressGateway

This guide walks you through upgrading `EgressGateway` using the `helm upgrade` command.

## Basic Command Format

```shell
helm upgrade [RELEASE] [CHART] [flags]
```

- `[RELEASE]` → The name of the installed release.
- `[CHART]` → The Helm chart reference.
- `[flags]` → Additional options.

For a full list of options, refer to the [Helm upgrade documentation](https://helm.sh/docs/helm/helm_upgrade/).

## Version Upgrade

Follow these steps to upgrade `EgressGateway` to a newer version:

### Step 1: Update Local Helm Chart Repository

Ensure you have the latest Helm chart version:

```shell
helm repo update
```

### Step 2: Check Available Versions

List the available `EgressGateway` chart versions:

```shell
helm search repo egressgateway
```

### Step 3: Upgrade to a Specific Version

Use the following command to upgrade:

```shell
helm upgrade \
  egress \
  egressgateway/egressgateway \
  --reuse-values \
  --version [version]
```

Replace `[version]` with the desired version number.

💡 **Tip**: The `--reuse-values` flag ensures that your existing configuration is retained.

## Configuration Upgrade

If you need to update configuration values during the upgrade, follow these steps:

### Step 1: Check Available Configuration Options

Refer to the [EgressGateway values documentation](https://github.com/spidernet-io/egressgateway/tree/main/charts) for all configurable parameters.

### Step 2: Apply Configuration Changes

To change specific parameters, use the `--set` flag. For example, to update the **Egress Agent log level to `debug`**, run:

```shell
helm upgrade \
  egress \
  egressgateway/egressgateway \
  --set agent.debug.logLevel=debug \
  --reuse-values
```

This command:

- Retains existing values (`--reuse-values`).
- Overrides only the specified field (`agent.debug.logLevel`).

By following these steps, you can safely upgrade `EgressGateway` while preserving your existing configuration. 🚀
