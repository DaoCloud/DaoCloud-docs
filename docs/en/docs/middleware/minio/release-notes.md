# MinIO object storage Release Notes

This page lists the Release Notes of MinIO object storage, so that you can understand the evolution path and feature changes of each version.

##v0.1.4

Release date: 2022-11-28

- **Improve** Update the front-end interface and add the sc list to see if it can be expanded
- **IMPROVED** Password validation adjusted to MCamel medium password strength
- **NEW** Configure Bucket when creating MinIO cluster
- **Add** public field when returning list or details
- **NEW** Return to alarm list
- **Add** Validation Service annotation
- **Fix** When creating MinIO, the password check is adjusted from between to length
- **Improved** Improve and optimize the copy function
- **IMPROVED** Instance details - access settings, remove cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **New** minio supports built-in BUCKET creation when creating
- **NEW** Docking alarm capability
- **New** Added the function of judging whether sc supports capacity expansion and prompting in advance
- **Optimize** Optimize the prompt logic of installation environment detection & adjust its style
- **Optimize** middleware style walkthrough optimization

##v0.1.2

Release date: 2022-11-08

- **NEW** Add interface to get user list
- **New** minio instance creation
- **Add** modification of minio instance
- **Add** delete of minio instance
- **Add** configuration modification of minio instance
- **New** minio instances support nodeport's svc
- **Added** monitoring data export of minio instance
- **Add** monitoring and viewing of minio instances
- **Add** Multi-tenant global management docking
- **Add** mcamel-minio-ui create/list/modify/delete/view
- **NEW** APIServer/UI supports mtls
- **Fix** In singleton mode, there is only one pod, fix the problem that grafana cannot obtain data
- **Optimization** Improve the function of the calculator