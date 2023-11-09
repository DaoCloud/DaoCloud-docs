# Gateway overview

You can view the gateway details on `Overview`, including the name, deployment location, gateway running status, service entry mode, controller/working node health status, API, and plug-in information.

## The gateway details page is displayed

On the `Gateway List` page, select the name of the target gateway to access the gateway overview page ".

<!--![]()screenshots-->

## Gateway details

Gateway details are divided into basic information, network information, TOP10 popular apis, resource information, resource load, and plug-in information.

Some of the data are described as follows:

- Control/Working Node Instances: Displays the total number and health of node instances. `/` The number on the left represents the number of instances currently online, and the number on the right represents the total number of node instances.

    - If the online node `/left no.` is equal to all the online nodes `/right no.`, it is displayed in green.
    - If the online node `/left no.` is less than all the nodes that should be online `/right no.`, it is displayed in red.

- Top 10 APIs: The top 10 apis in descending order by number of API response codes (2xx, 4xx, and 5xx) are in descending order by default by number of response codes (200). You can view the data of the past 15 minutes, 1 hour, or 24 hours.
- Resource load: The CPU usage and Memory usage of the gateway control node and the working node in the last 1 hour or the last 3 hours are displayed as line charts.
- Plug-in information: Displays the start and stop of the current gateway plug-in and other available plug-ins.

## Related operation

In addition to viewing the gateway details, you can update the gateway configuration and delete the gateway on the gateway details page.

- Update gateway: Click `Edit` at the top of the page to jump to the page for updating gateway configuration. For details, see [Update Gateway Settings](update-gateway.md).
- Delete gateway: Click `⋯` at the top of the page and select `Delete` to go to the page for deleting gateway. For details, see [Delete Gateway](delete-gateway.md).
<! -- Management API: Click API Quantity in the Gateway Data section to enter the API list. You can add, delete, modify, and query apis. -->
