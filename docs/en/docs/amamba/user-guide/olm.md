---
hide:
  - toc
---

# OLM Applications

Operator Lifecycle Manager (OLM) is part of the Kubernetes Operator ecosystem, used for managing Operator installation, upgrades, and permission control.

- **Operator**: A controller that extends Kubernetes functionality
- **ClusterServiceVersion (CSV)**: Defines Operator version and metadata
- **CatalogSource**: Stores index of Operators and their related resources
- **Subscription**: Tracks Operator installation and upgrade status

## Create OLM Application

1. On the **Overview** page, click **OLM Application** -> **Create Application**
1. Follow the wizard to fill in **Basic Information** and **Resource Configuration** parameters
1. Return to the OLM application list and wait for its status to become **Running**

Through the integration with OLM, you can more efficiently manage applications and Operators in Kubernetes clusters.
