# Kafka message queue Release Notes

This page lists the Release Notes of Kafka message queue, so that you can understand the evolution path and feature changes of each version.

##v0.1.6

Release date: 2022-11-28

- **Improved** Improve and optimize the copy function
- **Improved** Instance Details - Access Settings, Remove Cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **NEW** Docking alarm capability
- **New** Added the function of judging whether sc supports capacity expansion and prompting in advance
- **Optimization** Optimize the prompt logic of installation environment detection & adjust its style
- **Optimize** middleware style walkthrough optimization
- **Fix** The offline image has numbers and capital letters that cannot be scanned

##v0.1.4

Release date: 2022-11-08

- **FIXED** The correct field cannot be verified when updating, such as managerPass
- **IMPROVED** Password validation adjusted to MCamel low password strength
- **NEW** Returns the verification of whether the sc capacity can be updated
- **Add** public field when returning list or details
- **NEW** Added return alert
- **Add** Validation Service annotation
- **FIX** operator select by name
- **Fix** service address display error
- **Fix** When Kafka uses NodePort, the creation fails

##v0.1.2

Release date: 2022-10-28

- **NEW** Sync Pod status to instance details page
- **Optimize** workspace interface logic adjustment
- **Optimization** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimize** cpu&memory request amount should be less than limit logic adjustment

## v0.1.1

Release date: 2022-9-25

- **New** supports kafka list query, status query, creation, deletion and modification
- **NEW** Support kafka-manager to manage kafka
- **NEW** Support kafka indicator monitoring, check the monitoring chart
- **Add** support for ghippo permission linkage
- **New** `mcamel-elasticsearch` interface to get user list
- **Optimize** Update the release note script and execute the release-process specification