# Integrate DeepFlow

DeepFlow is an observability product based on eBPF. Its community edition has been integrated into Insight, and here is the integration process.

## Prerequisites

- Insight is already installed on the Global cluster.
- Insight minimum version requirement is v0.23.0.

## Install DeepFlow Server

1. Install the DeepFlow chart

    DeepFlow Server needs to be installed in the Global cluster (it will also install the DeepFlow Agent by default). Go to the kpanda-global-cluster cluster, click on `Helm Applications` -> `Helm Templates` in the left navigation bar. Select the `community` repository, and search for deepflow in the search box:
    
    
    
    Click on the deepflow card to view the details:
    
    
    
    Click on Install to proceed to the installation page:
    
    
    
    Most of the values have default settings. Clickhouse and Mysql, which are dependencies of DeepFlow, require persistent volumes. Their default size is `10Gi`, and you can modify them by searching for the `persistence` keyword in the configuration.
    
    Once the configuration is set, click on Install to start the installation process.

2. Modify Insight configuration

    After installing DeepFlow, you need to enable the related feature gates in Insight. Click on `Configurations & Secrets` -> `ConfigMaps` in the left navigation bar. Search for insight-server-config in the search box and edit it:
    
    
    
    In the configuration, find the `eBPF Flow feature` gate and enable it:
    
    
    
    Save the changes and restart the insight-server. After that, the Insight main interface will display the `Network Observability` feature:
    
    

## Install DeepFlow Agent

DeepFlow Agent is installed in the subcluster to collect eBPF observability data from the subcluster and report it to the Global cluster. Similar to installing DeepFlow Server, go to `Helm Applications` -> `Helm Templates` in the left navigation bar. Select the `community` repository, and search for deepflow-agent in the search box. Follow the installation process and pay attention to the configuration in the `Parameter Configuration` section:



`DeepflowServerNodeIPS` corresponds to the node address of the deepflow server installation cluster. After configuring it, click on Confirm to complete the installation.

## Usage

After successfully installing DeepFlow, click on `Network Observability` to access the DeepFlow Grafana UI. It includes a wide range of pre-built dashboards for viewing and helping analyze issues. Click on `DeepFlow Templates` to browse all available dashboards:




