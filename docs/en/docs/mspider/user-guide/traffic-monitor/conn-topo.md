# traffic topology

Click `Traffic Topology` in the left navigation bar to open the page. This function displays the topological relationship of all services under the mesh. Users can select `View Mode` and `Namespace` to filter and display service nodes.



## Display setting

`Namespace Boundary` is used to set whether to display the namespace boundary wireframe. If selected, services under the same namespace will be framed and the namespace name will be marked.



## Service metric data information

Click any service, and the sidebar will pop up to display service-related metrics based on the protocol type:

- HTTP service: request rate (RPM), error rate (%), average delay (ms)

- TCP service: number of connections (number), receiving throughput (B/S), sending throughput (B/S)



## health status

The health status is used to reflect the status information of services and connections, which are divided into normal, warning, abnormal and unknown, and judged by comparing the error rate and delay index data.

- OK (gray): error rate = 0 and latency does not exceed 100 ms

- Warning (orange): 0 < error rate <= 5% or 100 ms < delay <= 200 ms

- Abnormal (red): Error rate > 5% or latency > 200 ms

- Unknown (dotted line): no metric data is available