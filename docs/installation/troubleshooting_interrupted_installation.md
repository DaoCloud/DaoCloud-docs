# Troubleshooting Interrupted Installation

If the `dce5-installer` command is interrupted, follow these steps to clean up your environment and prepare for a reinstallation:

## Step-by-Step Cleanup Guide

1. **Stop Running Containers**
   - Use the following command to list all running containers:
     ```bash
     podman ps
     ```
   - Stop any containers related to the installation using:
     ```bash
     podman stop <container_id>
     ```

2. **Remove Temporary Files and Configurations**
   - Clear any temporary files or configurations that may have been partially applied.