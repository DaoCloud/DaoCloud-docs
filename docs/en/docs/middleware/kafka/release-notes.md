# Kafka message queue Release Notes

This page lists the Release Notes of Kafka message queue, so that you can understand the evolution path and feature changes of each version.

## 2023-04-27

### v0.5.1

#### new function

- **Added** `mcamel-kafka` details page displays related events
- **NEW** `mcamel-kafka` supports custom roles

#### Optimization

- **Optimize** `mcamel-kafka` scheduling strategy adds a sliding button

## 2023-03-28

### v0.4.0

#### new function

- **NEW** `mcamel-kafka` supports middleware link tracking adaptation.
- **NEW** Install `mcamel-kafka` to enable link tracking according to parameter configuration.

#### Optimization

- **Optimize** `mcamel-kafka` optimizes Kafka's default configuration.
- **upgrade** golang.org/x/net to v0.7.0
- **Upgrade** GHippo SDK to v0.14.0

## 2023-02-23

### v0.3.0

#### new function

- **Added** `mcamel-kafka` helm-docs template file.
- **Added** The Operator in the `mcamel-kafka` app store can only be installed in mcamel-system.
- **NEW** `mcamel-kafka` supports cloud shell.
- **NEW** `mcamel-kafka` supports separate registration of navigation bar.
- **NEW** `mcamel-kafka` supports viewing logs.
- **Added** `mcamel-kafka` Operator docking with chart-syncer.

#### Optimization

- **Optimize** `mcamel-kafka` upgrade offline mirror detection script.

#### fix

- **Fixed** the problem that `mcamel-kafka` instance name is too long and the custom resource cannot be created.
- **Fix** `mcamel-kafka` workspace Editor user cannot view instance password.
- **Add** log view operation instructions, support custom query, export and other functions.

## 2022-12-25

### v0.2.0

#### new function

- **NEW** `mcamel-kafka` NodePort port conflict early detection.
- **NEW** `mcamel-kafka` node affinity configuration.

#### Optimization

- **Optimize** `mcamel-kafka` manager removes the probe to prevent kafka from being unable to open the manager when it is not ready.
- **Optimize** `mcamel-kafka` zooEntrance repackage mirror address to 1.0.0.

## 2022-11-28

### v0.1.6

#### new function

- **Improved** Improve and optimize the copy function
- **IMPROVED** instance details - access settings, remove cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **NEW** Docking alarm capability
- **New** Added the function of judging whether sc supports capacity expansion and prompting in advance
- **Optimization** Optimize the prompt logic of installation environment detection & adjust its style
- **Optimize** middleware style walkthrough optimization
- **Fix** The offline image has numbers and capital letters that cannot be scanned

## 2022-11-08

### v0.1.4

#### new function

- **FIXED** The correct field cannot be verified when updating, such as managerPass
- **IMPROVED** Password validation adjusted to MCamel low password strength
- **NEW** Returns whether the sc capacity can be updated
- **Add** public field when returning list or details
- **NEW** Added return alert
- **Add** Validation Service annotation
- **FIX** operator select by name
- **Fix** service address display error
- **Fix** When Kafka uses NodePort, the creation fails

## 2022-10-28

### v0.1.2

#### new function

- **NEW** Sync Pod status to instance details page
- **Optimize** workspace interface logic adjustment
- **Optimization** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimize** cpu&memory request amount should be less than limit logic adjustment

## 2022-9-25

### v0.1.1

#### new function

- **New** supports kafka list query, status query, creation, deletion and modification
- **NEW** Support kafka-manager to manage kafka
- **NEW** Support kafka indicator monitoring, check the monitoring chart
- **Add** support for ghippo permission linkage
- **New** `mcamel-elasticsearch` interface to get user list
- **Optimize** Update the release note script and execute the release-process specification