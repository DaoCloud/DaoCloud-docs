---
date: 2022-10-08
categories: blog
authors: windsonsea
---

# DCE R&D Background

Nowadays, the concept of the metaverse is in the ascendant, and it is expected that everything has a virtual avatar. Industry giants are imitating the real world to build an immersive digital experience and establish another complete digital parallel time and space.
Everything in reality will be virtual fragmented on the cloud and endowed with real value, and distributed micro-service micro-scenes can be seen everywhere. In the past, the largest number of people online in the game world was on the order of millions.
But the grand and realistic digital world will be the activities of billions of people, which will generate massive amounts of concurrent data, prompting cloud computing power, cloud storage, and cloud bandwidth to be upgraded again.
Various emerging cloud-native technologies will emerge on this basis, everything is on the cloud, and everything is born for the cloud.

![meta](images/meta.png)

Cloud-native containerization platforms are rapidly becoming the foundation of modern application architectures. According to IDC, by 2022, 70% of enterprises will deploy unified virtual machines, containers, multi-cloud management processes and tools across multiple platforms.
Also by 2022, the proportion of global organizations/companies running containerized applications in production environments will increase significantly from less than 30% today to more than 75%.
And according to Gartner, cloud-native platforms will be the foundation of more than 95 percent of new digital initiatives by 2025, up from less than 40 percent in 2021.

[Free Trial](../dce/license0.md){ .md-button .md-button--primary }

## Cloud Native Wave

What is Cloud Native? The English name is Cloud Native, which is a concept proposed by Matt Stine, a veteran in the IT industry, including DevOps, CI/CD, microservices, containerization, etc.
Literally understood, cloud native means that everything is on the cloud. All applications must consider the cloud environment from the beginning of design, that is, they are originally designed for the cloud, run in the best posture on the cloud, and make full use of the elasticity and distributed advantages of the cloud platform.

According to iResearch's market research report, cloud-native container technology has entered the period of large-scale application since 2019. Container technology is closely integrated with the development of the domestic cloud computing industry, providing enterprises with more efficient, agile and reliable container cloud services.
The agility, simplicity, and high compatibility of the container cloud architecture make containers the most basic part of the cloud-native ecosystem. Whether it is hybrid cloud/multi-cloud, or the promotion of DevOps and microservice applications, containers will play a vital role , to help enterprises digitally transform and reduce costs and increase efficiency.

DaoCloud has been cultivating container cloud technology for many years and is a leader in the domestic container field.
Since Docker was open-sourced on GitHub in mid-2013, several founders of DaoCloud have keen insight into the container as a dynamic and malleable technology, and its future application prospects are bound to be very impressive.
After more than two years of hard work day and night by dozens of developers, DaoCloud Enterprise (DCE) container application cloud platform 1.0 was launched in early 2016.
Containerized platform products enable the rapid progress of DevOps, micro-services, serverless and other cloud-native applications, and help enterprises quickly respond to scenarios such as high-frequency online services, industrial Internet, financial digital transformation, and edge computing.

Today, the increasingly mature DCE version Roadmap has evolved to 5.0,
Become an industry-leading enterprise-level Kubernetes commercial platform and a cloud-native operating system, including modules such as Parcel intelligent network, UDS unified data storage, integrated graphic monitoring, and multi-cluster management.
After hundreds of domestic and foreign financial government and enterprise production verification, it can provide a reliable and consistent PaaS support environment, allowing enterprise application developers to focus on business capacity building, maintain competitiveness and exceed expectations to meet the ever-increasing customer expectations.
DaoCloud has also grown to nearly 500 employees, and the proportion of R&D personnel exceeds 70%. It brings together top talents from major domestic and foreign companies to focus on container technology.
Established a series of complete container technology assembly line systems from pre-sales, products, development, testing, delivery, and after-sales to serve domestic and foreign customers wholeheartedly.

![rank](images/ops-rank.png)

In July 2020, Gartner's 2020 China ICT Technology Maturity Curve Report mentioned DaoCloud as a professional container vendor.
The main force of container technology lies in the open source community, and the ranking of the contribution of the open source community can prove the deep understanding of container technology by container manufacturers.
DaoCloud has had a great influence in the global open source community in recent years. Stackalytics.io statistics show that in the past year, DaoCloud ranked No. 3 for Kubernetes globally and No. 1 domestically.
This fully proves that the DaoCloud development team has a deep understanding of cloud native technology, from network, storage, computing power and other resources arrangement, to large-screen visual monitoring, to multi-cluster management and customer scenario solution customization,
DaoCloud has comprehensively led thousands of industries in China to realize cloud-native digital transformation, established strategic partnerships with Huawei Cloud and nearly 100 domestic manufacturers, and responded to the call of the country to build an industrial ecology of Xinchuang.

## Containers vs virtualization

The two are not in parallel, but in a trade-off relationship. Containers are the future.

![container vs vm](images/trend.png)

For the past 15 years, server virtualization has been the method of choice for application deployment in enterprise data centers.
Hypervisors are nearly ubiquitous. The most common unit of sale for public cloud IaaS service providers is the virtual machine (VM).
However, in the cloud-native era, in order to improve application traffic and user experience, enterprises need to find faster and more flexible ways to deploy and manage new applications and services.
Many applications need to be deployed both on-premises and in the cloud. In addition, in order to speed up the launch of new applications, enterprises must deploy containerized applications in addition to running single applications in virtual machines.

The problem is that if an enterprise is going to adopt containers, it needs to work hard to understand what infrastructure solution best suits the business needs.
Most enterprises naturally want to run containers in a virtual machine environment, given the money they have invested in virtual machines and the years of experience their IT teams have in managing virtual machines.
That's what many enterprise IT teams do. Admittedly, this is a great way to get familiar with containers.
However, as the containerization process progressed from proof of concept, through development and testing, to production deployment, IT teams gradually discovered that containers based on virtual machine deployments were not ideal.

With the maturity and popularity of cloud-native technologies, enterprises have begun to try to deploy containers directly on physical machines, also known as bare metal containers. This deployment method has the following advantages:

- Fewer layers of management for easier troubleshooting
- higher efficiency
- run with a higher density of containers
- better performance
- better predictability
- Lower total cost of ownership

When deploying containers on top of an existing virtual machine environment, containers are just another form of virtualization layer.
In this way, two types of IT operation and maintenance personnel are needed, one uses and manages the container environment, and the other manages the virtual machine environment. Operation and maintenance may require two sets of teams.
In actual work, no matter how well the container and virtual machine teams work together, there will inevitably be communication problems, duplication of work, and often one team waiting for the other, which will inevitably cause delays and reduce the overall work efficiency.

Once a fault occurs at this time, the troubleshooting process is more complicated. Derived questions include: Can failures be resolved at the container level?
Is the problem caused by the virtual machine? Or is it a problem with the physical hardware? If you have to call for after-sales support, how can you tell what is wrong?
In addition, can the virtual machine effectively support the container stack?

Compared with virtual machine-based containers, bare metal containers reduce the number of layers to be managed, and because bare metal is more efficient, fewer hardware resources are required to run the same number of containers, reducing the total number of managed devices.

![vm-based](images/compare.png)

As can be seen from the figure above, bare metal container deployment, management, and troubleshooting require fewer team members, but support higher application density.

DaoCloud grasps the pulse of the times, with the DCE container application cloud platform as the core, the ingeniously built cloud-native all-in-one machine adopts the infrastructure of smart bare metal + leading container technology, based on native open source container technology,
Fully synchronized with global standards and norms, and continuously exporting industry best practices to enterprises.
In a differentiated cluster operating environment, it can adapt to the diversified IT infrastructure of enterprises such as bare metal, virtual machines, and cloud hosts, support multiple virtual platforms, and realize unified resource allocation on the diversified infrastructure of enterprises.

## DCE and Kubernetes

DCE includes container, network, storage, monitoring, container registry, load balancing, DNS service discovery, authentication and authorization solutions that enterprises need. These components are thoroughly tested,
Run reliably on new dynamic environments such as bare metal environments, public clouds, private clouds, and hybrid clouds.

- Container computing, adapting to x86 architecture and ARM architecture, carrying the operation, scheduling and management of hybrid applications.
- Container storage, which provides application-oriented data persistence capabilities and facilitates stateful application loads.
- Container network, providing a high-performance dual-state network for applications, taking into account both traditional enterprise infrastructure and software-defined infrastructure.

DCE has built-in 260 container platform risk checkpoints, multi-dimensional cluster monitoring and alarm cutting-edge practice,
Guarantee the continuous operation of hosts, cluster services, and business applications, the overall platform high-availability design and comprehensive resource guarantee mode (QoS),
Realize end-to-end application security assurance, provide high SLA guarantee, and availability reach 99.99%.

DCE takes technology leadership as its own responsibility, helps enterprise customers implement cloud native technology, and continuously strengthens, optimizes and expands Kubernetes in practice,
It meets the requirements of an enterprise-level, large-scale, and highly stable production environment. At the same time, as one of the leaders of the domestic Kubernetes open source community,
He has a deep understanding of core open source technologies, and contributes to the open source community by constantly summarizing production practices to promote the continuous development of the Kubernetes community.

## DCE Product Introduction

DCE adopts industry-leading container orchestration technology, and its product capabilities cover the development, delivery, operation and maintenance of cloud-native applications, as well as the full lifecycle management of operations.
It can help financial governments and enterprises realize agile delivery, elastic support and governance of distributed business applications, and improve enterprises' ability to support and manage distributed applications.
At the same time, the product has built an end-to-end cloud-native overall solution of "Innovation architecture + cloud-native platform" with domestic mainstream Xinchuang partners.
At present, it has provided container cloud solutions based on cloud-native technology for hundreds of leading customers in key industries including finance, securities, industrial interconnection, Internet of Vehicles, intelligent manufacturing, and e-commerce.
And the corresponding Xinchuang container cloud solution has been implemented in many industries such as government affairs and finance.

![dce](images/position.png)

For application developers, DCE can be regarded as a cluster operating system. DCE provides functions such as service discovery, scaling, load balancing, self-healing and even election.
Free developers from infrastructure-related configuration, etc. DCE can treat a large number of servers as a huge server and run applications on a large server.
Regardless of the number of servers in a cloud-native cluster, the method of deploying an application on DCE will always be the same.

## CNCF certified KCSP

The currently authorized and compliant Kubernetes versions of DaoCloud include but are not limited to:

current version:

[![1.23](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.23.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/2072)
[![1.24](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.24.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/2239)
[![1.25](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.25.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/2240)
[![1.26](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.26.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/2451)

historic version:

[![1.7](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.7.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/68)
[![1.9](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.9.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/210)
[![1.13](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.13.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/418)
[![1.15](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.15.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/794)
[![1.18](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.18.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/1144)
[![1.20](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/1.20.png){ width="100" }](https://github.com/cncf/k8s-conformance/pull/1463)

Learn more about [What is DCE 5.0](../dce/what.md)

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }