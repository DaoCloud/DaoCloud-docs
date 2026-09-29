# Troubleshooting

## Grafana Dashboard data is not displayed

1. Run `kubectl get pods -n unifabric -o wide` to check the status of the unifabric pods.
2. Run `curl unifactric-pod:5026` to check metrics of Pod are available.
3. Run `curl unifactric-svc:5026` to check metrics of Service available.
4. Run `kubectl get switchendpoint` to check the status of the switch if connected.

## Common Issues

### 1. The lldpd container fails to start

**Symptom:** The lldpd container cannot start or restarts frequently

**Troubleshooting steps:**

```bash
# View the container log
kubectl logs -l app=unifabric-agent -c lldpd

# Check the container status
kubectl describe pod <pod-name>
```

**Possible causes:**

- Insufficient permissions: Make sure the container has the `privileged: true` permission
- The network interface does not exist: Check whether the configured interface exists

### 2. Neighbor devices cannot be discovered

**Symptom:** `lldpcli show neighbors` returns an empty result

**Troubleshooting steps:**

```bash
# Check the LLDP service status
kubectl exec -it <pod-name> -c lldpd -- lldpcli -v

# View the interface status
kubectl exec -it <pod-name> -c lldpd -- lldpcli show interfaces

# Check the network connection
kubectl exec -it <pod-name> -c lldpd -- ip link show
```

**Possible causes:**

- LLDP is not enabled on the neighbor device
- The network interface is not configured correctly
- The firewall blocks LLDP packets

### 3. JSON parsing error

**Symptom:** A JSON parsing error appears in the unifabric-agent log

**Troubleshooting steps:**

```bash
# View the agent log
kubectl logs -l app=unifabric-agent -c unifabric-agent

# Manually test the JSON output
kubectl exec -it <pod-name> -c unifabric-agent -- lldpcli show neighbors -f json0
```

**Solution:**

- Check the lldpcli version compatibility
- Verify the JSON output format

### 4. ScaleoutGroup issues

**Symptom:** The ScaleoutGroup is not created or its status is abnormal

**Troubleshooting steps:**

```bash
# View all ScaleoutGroups
kubectl get scaleoutgroups.unifabric.io

# View the details of a specific group
kubectl get scaleoutgroups.unifabric.io scaleoutgroup-a1b2c3d4 -o yaml

# View the controller log
kubectl logs -l app=unifabric-controller -n unifabric
```

**Solution:**

Check the LLDP neighbor information of FabricNode

```bash
kubectl get fabricnodes.unifabric.io -o jsonpath='{range .items[*]}{.metadata.name}{": "}{.status.computeNics[*].lldpNeighbor.hostname}{"\n"}{end}'

# Check the neighbor information of a specific node
kubectl get fabricnodes.unifabric.io sh-cube-gpu-13 -o jsonpath='{.status.computeNics[*].lldpNeighbor.hostname}'
```

## Debug Commands

```bash
# View LLDP neighbors (detailed information)
lldpcli show neighbors -f keyvalue

# View LLDP statistics
lldpcli show statistics

# View the LLDP configuration
lldpcli show configuration

# View local information
lldpcli show chassis
```
