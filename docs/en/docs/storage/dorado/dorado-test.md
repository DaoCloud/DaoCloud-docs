---
hide:
  - navigation
---

# Test K8S CSI Driver Dorado Storage

Standardized testing of CSI capabilities and storage container awareness capabilities

Git: <https://gitee.com/daocloud/huawei-dorado-test>

## Test Conclusion

**DaoCloud d.run AI Computing Scheduling Platform (also known as DCE5 v3.0 Cloud Native Container Platform) fully supports all container volume functions of OceanStor Dorado based on "CNCF-CSI standard", and also supports all container volume awareness functions based on "Huawei CSM standard".**

**The above conclusion applies to all models included in HUAWEI OceanStor Dorado V700 All-Flash Storage System and OceanStor Hybrid V700 Hybrid Flash Storage System.**

## Test Environment

| Component | Version |
| ------------------------- | ----------------------------- |
| Storage Model | Huawei OceanStor Dorado 5000 v6 |
| Storage Version | V700R001C00SPC200 |
| d.run | DCE5 v3.0.0 |
| Kubernetes | v1.31.6 |
| CSI Driver | eSDK_K8S_Plugin v4.8.0 |
| Storage Monitoring Container | Huawei CSM v2.3.0 |
| csi-attacher | v4.4.0 |
| csi-node-driver-registrar | v2.9.0 |
| csi-provisioner | v3.6.0 |
