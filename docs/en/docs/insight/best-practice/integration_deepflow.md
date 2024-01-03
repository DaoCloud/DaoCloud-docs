# Integrate DeepFlow

DeepFlow is an observability product based on eBPF. Its community edition has been integrated into Insight, and here is the integration process.

## Prerequisites

- Insight is already installed on the Global cluster.
- Insight minimum version requirement is v0.23.0.

## Install DeepFlow Server

1. Install the DeepFlow chart

    DeepFlow Server needs to be installed in the Global cluster (it will also install the DeepFlow Agent by default). Go to the kpanda-global-cluster cluster, click on __Helm Applications__ -> __Helm Templates__ in the left navigation bar. Select the __community__ repository, and search for deepflow in the search box:
    
    
    
    Click on the deepflow card to view the details:
    
    
    
    Click on Install to proceed to the installation page:
    
    
    
    Most of the values have default settings. Clickhouse and Mysql, which are dependencies of DeepFlow, require persistent volumes. Their default size is __10Gi__ , and you can modify them by searching for the __persistence__ keyword in the configuration.
    
    Once the configuration is set, click on Install to start the installation process.

2. Modify Insight configuration

    After installing DeepFlow, you need to enable the related feature gates in Insight. Click on __Configurations & Secrets__ -> __ConfigMaps__ in the left navigation bar. Search for insight-server-config in the search box and edit it:
    
    
    
    In the configuration, find the __eBPF Flow feature__ gate and enable it:
    
    
    
    Save the changes and restart the insight-server. After that, the Insight main interface will display the __Network Observability__ feature:
    
    

## Install DeepFlow Agent

DeepFlow Agent is installed in the subcluster to collect eBPF observability data from the subcluster and report it to the Global cluster. Similar to installing DeepFlow Server, go to __Helm Applications__ -> __Helm Templates__ in the left navigation bar. Select the __community__ repository, and search for deepflow-agent in the search box. Follow the installation process and pay attention to the configuration in the __Parameter Configuration__ section:



 __DeepflowServerNodeIPS__ corresponds to the node address of the deepflow server installation cluster. After configuring it, click on Confirm to complete the installation.

## Usage

After successfully installing DeepFlow, click on __Network Observability__ to access the DeepFlow Grafana UI. It includes a wide range of pre-built dashboards for viewing and helping analyze issues. Click on __DeepFlow Templates__ to browse all available dashboards:




