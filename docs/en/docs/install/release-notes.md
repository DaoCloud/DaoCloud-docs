---
MTPE: todo
Date: 2022-12-20
---

# Installer Release Notes

This page lists the Release Notes of the installer, so that you can understand the evolution path and feature changes of each version.

## 2022-11-30

### v0.3.29

#### New features

- **NEW** ARM64 support: build arm64 offline packages.
- **NEW** Added support for kylin v10 sp2 offline package.
- **NEW** Infrastructure Support 1.25: Upgrade redis-operator, eck-operator, hwameiStor and other components.
- **NEW** Added support for cluster deployment in private key mode.
- **New** The workload is elastically scaled based on custom indicators, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimized

- **Optimize** Create permanent harbor with operator, enable HTTPS, and use Postgressql operator.
- **Optimized** Commercial version uses contour as default ingress-controller.
- **Optimized** MinIO supports using VIP.
- **Optimized** coredns is automatically injected into warehouse VIP resolution.
- **Optimization** Optimize the offline package production process and speed up the packaging of docker images.

#### Bug fixes

- **FIX** Fixed issues with fair cloud service.
- **FIX** Fixed issues with mirroring and helm for various submodules.
- **FIXED** Bug fixes for offline package loading.

#### Known issues

- Because some operators need to be upgraded to support 1.25, DCE5 does not support 1.20 downwards.
- The default k8s version of kubean and the offline package are still limited to k8s 1.24 version, which has not been updated to 1.25 (postgres-operator is not supported yet).
- In the case of Image Load, the istio-ingressgateway imagePullPolicy is always.
- For the ARM version, step 16 (harbor) cannot be performed, because harbor does not support ARM for the time being. The mainfest.yaml file needs to be modified, the postgressql operator is fasle, and -j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 should be added when executing the installation command