# Manage toolchain instances

Manage the integrated tool chain, which is divided into two types: the tool chain integrated by the workspace, and the tool chain integrated by the administrator

## Unintegrate

### Workspace

For toolchain instances of __workspace allocation__, the __disintegrate__ operation is supported:

<!--![]()screenshots-->

The __disintegrate__ operation is not supported for __platform-assigned__ toolchain instances:

### Admin

After unintegrating, the instances assigned to the workspace will also be deleted automatically.

## assign items

### Workspace

For the toolchain instance of __Workspace Assignment__, it is supported to use the projects under the instance of __Binding__ to the current workspace.

In addition, bound projects support unbinding.

<!--![]()screenshots-->

For the toolchain instance of __platform distribution__, only viewing is supported, and __binding__ operation is not supported.

### Admin

Support __assign project__ to the workspace. After the assignment is successful, an instance will be generated under the workspace, and the project can be used by the workspace.

<!--![]()screenshots-->