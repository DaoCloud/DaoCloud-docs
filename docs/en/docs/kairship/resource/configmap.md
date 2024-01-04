# Multicloud ConfigMaps

ConfigMap is an API object used to save non-confidential data into key-value pairs.
When used, Pods can use it as an environment variable, as a command-line argument, or as a configuration file in a storage volume.

Multicloud ConfigMaps can decouple multicloud environment configuration information from container images, making it easy to modify the configuration of multicloud applications.

Two creation methods are currently provided: wizard creation and YAML creation. This article takes wizard creation as an example, and follows the steps below.

1. After entering a multicloud instance, in the left navigation bar, click __Resource Management__ -> __Multicloud ConfigMaps__ , and click the __Create Multicloud ConfigMaps__ button in the upper right corner.

    ![Create ConfigMap](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/config01.png)

2. On the __Create Multicloud ConfigMaps__ page, enter the name, select the namespace and other information, and click __OK__ .

    ![Fill ConfigMap](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/config02.png)

3. Return to the list of multicloud configuration items, and the newly created one will be the first one by default. Click __⋮__ on the right side of the list to edit YAML, update, export and delete configuration items.

    ![Update/Delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/config03.png)

    !!! note

        If you delete a configuration item, its related information will also be deleted, please operate with caution.

## YAML example

Here is an example YAML for a multicloud configuration item that you can use with a little modification.

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: cluster-info
  namespace: default
  uid: e8bf0788-d5e6-4b1f-8588-1b58c6d010d5
  resourceVersion: '1647402'
  creationTimestamp: '2022-09-26T07:26:25Z'
  labels:
    a: '1'
    b: '2'
    c: c
  annotations:
    c: '3'
    kairship.io/describe: '123'
    kpanda.io/describe: '13243'
    shadow.clusterpedia.io/cluster-name:k-kairshiptest
data:
  jws-kubeconfig-8utcre: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6Ijh1dGNyZSJ9..7-9oX6oeZsV5QJ_VsxBKFE7LPFMmfYX4bQM3IDDBw80
  jws-kubeconfig-faw64f: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6ImZhdzY0ZiJ9..Hbtgm5MFOOfLekYn-NnGFCj4vm-D1QS1h-Tm3ywcMr4
  jws-kubeconfig-kew06y: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6ImtldzA2eSJ9..nOG2817zEvF8tkmPGrE_r1vWM4kvA-5v6i29EA73Jb0
  kubeconfig: |
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpN QjRYRFRJeU1Ea3lOakF6TXprek5Wb1hEVE15TURreU16QXpNemt6TlZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQ VFvQ2dnRUJBTVhYCkNSS2F6QnlFRithVWNuVHFGVVFST0JxUXZabjc4Q3h5Rnl5QVdvU0NhK1hFTkZJZVBPaGdudmd2Z1VadzZ1bmYKZWN4ZHJRblltMzRNOE1rQ0dDK21hTDNtWXJ HTUNpVGl0dnNqMllOd3NCMjh4TlZPQ052UG5iZWRKOTFIYWdhbAprQ3psWGR0STlNLzdCK0xoQWdYcXlPS0NpVTd4U1ZGKzl6dGYvTU9odGlXVmpGR3RxUjZNZUk3TnRaZmY2cXZx CkJmMUVpSlR2QXBVK0l4NWh6ajJJYUVHWStzTTUzSC8vSnhjVHFRdmRjVXJOUW5SbXVZS2t0eDV5TWwzTHh5K28KcjJkbElhTVRnQi9GeWF1ZEIrTmZzLzF2a3IxcTdnek5xc1 NGSFVhQlhZWUlTYXQ5V1MwRmhpVXpHbENDZjFjdQpaRjBlNU10V2M2UXRVSXZZenI4Q0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQ WY4d0hRWURWUjBPQkJZRUZMd0VUMm1PZlVQc3hjZHhTZ1Z1VVpvdVRtekRNQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJB QWRQSHlNSW1zc1JLOTY0eWExbQpHRXVBMzNwUU9wdkJzSWJRZHI4R1diRWoyakk1eUZ1UVBJV3loOGRJTjE1VnN0YldSekZSZkRHQ1pWSGh6RWdMCks1U1dsMFU3MDVzQUd4UGFaQ3hEVUx 0alBRSEgwNVdodzBaUkYxdHB5K2RPNk5MeWJwTVdpU2FndlFqQmpTMy8KVjZZbHc2NDFMdDc0eU9QcUJDckFKWUtYOTUzanhEdWZNSjNVV0dBa1VpaVVLWTcycXBCWGxvNVkyU2RCTmVTZwo5ME 1TQ25VdDA2YkRtQ0lMaGI0OVVnZTFvamdldVVFVHJkeGppNWplQWp3bHpvZTFRcmY1bnZnRnlNV0tlK05oCnRIajdHRktHRnArVHJxSVh1TmVPc1dER3o0WldtQ3Z1bm8zRXdhSUdRNThKZ Wk3YjM5d2F0ZWY1K3FlOStNTWIKZ1BzPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
        server: https://10.6.168.131:6443
      name: ""
    contexts: null
    current-context: ""
    kind: Config
    preferences: {}
    users: null
```
