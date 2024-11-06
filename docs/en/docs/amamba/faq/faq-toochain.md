# Toolchain Related Issues

This page lists some issues that may be encountered when using the toolchain features of the application workbench, along with corresponding solutions.

## Error When the Pipeline Runs with Maven as the Agent and Uses Integrated SonarQube for Java Code Scanning

In most cases, the error is caused by the Java environment provided by the pipeline being Java 11, which is incompatible with the Java version required by SonarQube. It is recommended to use the SonarQube deployment provided in the Helm template.

## What Are the Precautions When Deploying GitLab?

The Helm template supports GitLab deployment. During the deployment process, please pay attention to the following precautions:

- Currently, it only supports POC (Proof of Concept) use and does not meet production operation and maintenance conditions.
- The cluster needs to reserve 80GB of storage space.
- Online deployment may experience instability in the short term due to the use of an acceleration station.
