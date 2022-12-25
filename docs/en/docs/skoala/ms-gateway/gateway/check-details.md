# View gateway details

You can check the detailed information of the gateway on the `Overview` page, including the name, deployment location, gateway running status, service entry method, health status of the control node/worker node, API, plug-ins and other information.

## Enter the gateway details page

On the `Gateway List` page, select the gateway instance to view, click `⋯` and select `Gateway Details` from the drop-down list.



## Gateway Details

Gateway details are divided into: basic information, network information, gateway data, resource status, resource load, plug-in information and other parts.

The description of some data is as follows:

- Number of manual service access: refers to the number of services manually added to the current gateway through the `Add Service` on the `Service List` page.
- Number of automatic service access: refers to the number of services that are automatically added to the current gateway through the `Managed Service` on the `Service List` page.
- Domain name management: refers to the number of domain names under the current gateway.
- Number of APIs: Refers to the number of APIs used in the current gateway.
- Number of Control/Worker Node Instances: Displays the total number and health of node instances. The number on the left of `/` indicates the number of instances currently online, and the number on the right indicates the total number of node instances.

    - If the online node `/left number` is equal to all should be online nodes `/right number`, it will be displayed in green.
    - If the online node `/number on the left` is smaller than all nodes `/number on the right` that should be online, it will be displayed in red.

- Top 10 APIs: The top 10 APIs are arranged in descending order according to the number of API response codes 2xx, 4xx, and 5xx. By default, they are arranged in descending order according to the number of response codes 200. You can view the data of the past 15 minutes, the past 1 hour, and the past 24 hours.
- Resource Load: Displays the CPU usage and Memory usage of the gateway control node and worker nodes in the past 1 hour or the past 3 hours in the form of a line graph.
- Plug-in information: Display the current gateway plug-in startup and stop status and other available plug-ins.


## Related operations

In addition to viewing gateway details, you can also perform operations such as updating gateway configuration, deleting gateways, and diagnosing gateways through the gateway details page.

- Update Gateway: Click `Edit` at the top of the page to jump to the page for updating the gateway configuration, see [Update Gateway Configuration](update-gateway.md) for specific steps.
- Delete gateway: Click `⋯` at the top of the page and select `Delete` to jump to the page for deleting a gateway. For details, see [Delete Gateway](delete-gateway.md).
- Diagnose Gateway: Click `Diagnose Mode` at the top of the page to enter the gateway debugging mode, see [Diagnose Gateway](diagnose-gateway.md) for specific steps.
- Access service: Click "Manual/Automatic Service Access Number" in the "Gateway Data" section to enter the service access page. For specific steps, see [Manual Access Service](../service/manual-integrate.md) or [Automatic Management Service](../service/auto-manage.md).
- Manage APIs: Click "API Quantity" in the "Gateway Data" section to enter the API list, and perform operations such as adding, deleting, modifying, and checking.
- Domain name management: Click "Domain Name Management" in the "Gateway Data" section to enter the domain name list, and perform operations such as adding, deleting, modifying, and checking.