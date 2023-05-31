# Manage toolchain instances

Manage the integrated tool chain, which is divided into two types: the tool chain integrated by the workspace, and the tool chain integrated by the administrator

## Unintegrate

### Workspace

For toolchain instances of `workspace allocation`, the `disintegrate` operation is supported:

<!--![]()screenshots-->

The `disintegrate` operation is not supported for `platform-assigned` toolchain instances:

### Admin

After unintegrating, the instances assigned to the workspace will also be deleted automatically.

## assign items

### Workspace

For the toolchain instance of `Workspace Assignment`, it is supported to use the projects under the instance of `Binding` to the current workspace.

In addition, bound projects support unbinding.

<!--![]()screenshots-->

For the toolchain instance of `platform distribution`, only viewing is supported, and `binding` operation is not supported.

### Admin

Support `assign project` to the workspace. After the assignment is successful, an instance will be generated under the workspace, and the project can be used by the workspace.

<!--![]()screenshots-->