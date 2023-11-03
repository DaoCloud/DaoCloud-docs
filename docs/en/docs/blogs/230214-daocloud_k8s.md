# DaoCloud and Kubernetes

> Seek Global Optimal Solutions for Digital World

## Challenges

[DaoCloud](https://www.daocloud.io/en/), founded in 2014, is an innovation leader in the field of cloud native. It boasts independent intellectual property rights of core technologies for crafting an open cloud platform to empower the digital transformation of enterprises.

DaoCloud has been engaging in cloud native since its inception. As containerization is crucial for cloud native business, a cloud platform that does not have containers as infrastructure is unlikely to attract its potential users.Therefore, the first challenge confronting DaoCloud is how to efficiently manage and schedule numerous containers while maintaining communication between them.

As cloud native gains momentum, cloud native solutions proliferate like mushrooms after rain. However, having more choices is not always a good thing, because choosing from various products to globally maximize benefits and minimize cost is always challenging and demanding. Therefore, another obstacle ahead of DaoCloud is how to pick out the best runner in each field and organize them into one platform that can achieve global optimum for cloud native.

## Solutions

As the de facto standard for container orchestration, Kubernetes is undoubtedly the preferred container solution. Paco Xu, head of the Open Source and Advanced Development team at DaoCloud, stated, "Kubernetes is a fundamental tool in the current container ecosystem. Most services or applications are deployed and managed in Kubernetes clusters."

Regarding finding the global optimal solutions for cloud native, Peter Pan, R&D Vice President of DaoCloud, believes that "the right way is to center on Kubernetes, coordinate relevant best practices and advanced technologies, and build a widely applicable platform."

## Results

In the process of embracing cloud native, DaoCloud continues to learn from Kubernetes and other excellent CNCF open source projects. It has formed a product architecture centered on [DaoCloud Enterprise](https://docs.daocloud.io/), a platform for cloud native applications. Using Kubernetes and other cutting-edge cloud native technologies as a foundation, DaoCloud provides satisfying cloud native solutions for military, finance, manufacturing, energy, government, and retail clients,It helps companies with their digital transformation, such as SPD Bank, Huatai Securities, Fullgoal Fund, SAIC Motor, Haier, Fudan University, Watsons, Genius Auto Finance, State Grid Corporation of China, etc.

!!! note ""

    "As DaoCloud Enterprise becomes more powerful and attracts more users, some customers need to use Kubernetes instead of Swarm for application orchestration. As a robust application orchestration system, Kubernetes has solid community support and recommendations from tech giants in the field. We, as providers, need to meet the needs of our users."

    [Kebe Liu](https://github.com/kebe7jun),

    Service Mesh Expert of DaoCloud

DaoCloud was founded to help traditional enterprises to move their applications to the cloud and realize digital transformation. The first product released after the company's establishment, DaoCloud Enterprise 1.0, is a Docker-based container engine platform that can easily build images and run them in containers.

However, as applications and containers increase in number, coordinating and scheduling these containers became a bottleneck that restricted product performance. DaoCloud Enterprise 2.0 used Docker Swarm to manage containers, but the increasingly complex container scheduling system gradually went beyond the competence of Docker Swarm.

Fortunately, Kubernetes began to stand out at this time. It rapidly grew into the industrial standard for container orchestration with its competitive rich features, stable performance, timely community support, and strong compatibility. Paco Xu said, "Enterprise container platforms need container orchestration to standardize the process of moving to the cloud. Kubernetes was accepted as the de facto standard for container orchestration around 2016 and 2017. Our products started to support it in 2017."

After thorough comparisons and evaluations, DaoCloud Enterprise 2.8, debuted in 2017, officially adopted Kubernetes (v1.6.7) as its container orchestration tool. Since then, DaoCloud Enterprise 3.0 (2018) used Kubernetes v1.10, and DaoCloud Enterprise 4.0 (2021) adopted Kubernetes v1.18. The latest version, DaoCloud Enterprise 5.0 (2022), supports Kubernetes v1.23 to v1.26.

Kubernetes served as an inseparable part of these four releases over six years, which speaks volumes about the fact that using Kubernetes in DaoCloud Enterprise was the right choice. DaoCloud has proven, through its own experience and actions, that Kubernetes is the best choice for container orchestration and that it has always been a loyal fan of Kubernetes.

!!! note ""

    "Kubernetes helped our product and research teams realized automation of test, build, check, and release process, ensuring the quality of deliverables. It also helped build our smart systems of collaboration about product requirements & definition, multilingual product materials, debugging, and miscellaneous challenges, improving the efficiency of intra- and inter-department collaboration. Kubernetes is the cornerstone for refining our products towards world-class software."

    Ting Ye,

    Vice President of Product Innovation of DaoCloud

On the one hand, Kubernetes makes our products more performant and competitive. DaoCloud integrates relevant practices and technologies around Kubernetes to polish its flagship offering – DaoCloud Enterprise. The latest 5th version, released in 2022, covers application stores, application delivery, microservice governance, observability, data services, multicloud management, cloud edge collaboration, and other features. DaoCloud Enterprise 5.0 is an inclusive integration of cloud native technologies.

DaoCloud deployed a Kubernetes platform for SPD Bank, improving its application deployment efficiency by 82%, shortening its delivery cycle from half a year to one month, and promoting its transaction success rate to 99.999%.

In terms of Sichuan Tianfu Bank, the scaling time was reduced from several hours to an average of 2 minutes, product iteration cycle was shortened from two months to two weeks, and application rollout time was cut by 76.76%.

As for a joint-venture carmaker, its delivery cycle shortened from two months to one or two weeks, success rate of application deployment increased by 53%, and application rollout became ten times more efficient. In the case of a multinational retailer, application deployment issues were solved by 46%, and fault location efficiency rose by more than 90%.

For a large-scale securities firm, its business procedure efficiency was enhanced by 30%, and resource costs were lowered by about 35%.

With this product, Fullgoal Fund shortened its middleware deployment time from hours to minutes, improved middleware operation and maintenance capabilities by 50%, containerization by 60%, and resource utilization by 40%.

On the other hand, our product development is also based on Kubernetes. DaoCloud deployed Gitlab based on Kubernetes and established a product development process of "Gitlab -> PR -> Auto Tests -> Builds & Releases", which significantly improved our development efficiency, reduced repetitive tests, and realized automatic release of applications. This approach greatly saves operation and maintenance costs, enabling technicians to invest more time and energy in product development to offer better cloud native products.

!!! note ""

    "Our developers actively contribute to open source projects and build technical expertise. DaoCloud has established a remarkable presence in the Kubernetes and Istio communities."

    Paco Xu,

    Header of Open Source & Advanced Development Team of DaoCloud

DaoCloud is deeply involved in contributing to Kubernetes and other cloud native open source projects. Our participation and contributions in these communities continue to grow. In the year of 2022, DaoCloud was ranked third globally in terms of cumulative contribution to Kubernetes (data from Stackalytics as of January 5, 2023).

In August 2022, Kubernetes officially organized an interview with community contributors, and four outstanding contributors from the Asia-Pacific region were invited. Half of them came from DaoCloud, namely [Shiming Zhang](https://github.com/wzshiming) and [Paco Xu](https://github.com/pacoxu). Both are Reviewers of SIG Node. Furthermore, at the KubeCon + CloudNative North America 2022, [Kante Yin](https://github.com/kerthcet) from DaoCloud won the 2022 Contributor Award of Kubernetes.

In addition, DaoCloud continue to practice its cloud native beliefs and contribute to the Kubernetes ecosystem by sharing source code of several excellent projects, including Clusterpedia, Kubean, CloudTTY, KLTS, Merbridge, HwameiStor, Spiderpool, and Piraeus, on Github.

In particular:

- Clusterpedia, compatible with Kubernetes OpenAPIs, is designed for resource synchronization across clusters and powerful search feature that allows quick, easy and effective retrieval of all resources in clusters.
- Kubean makes it possible to quickly create production-ready Kubernetes clusters and integrate clusters from other providers.
- CloudTTY is a web terminal and cloud shell operator for Kubernetes cloud native environment. It can manage Kubernetes clusters on a web page, anytime and anywhere.
- KLTS provides long-term free maintenance for earlier versions of Kubernetes.
- Piraeus is an easy and secure storage solution for Kubernetes with high performance and availability.

DaoCloud utilizes its practical experience across industries to contribute to Kubernetes-related open source projects, with an aim of making cloud native technologies, represented by Kubernetes, better feature in production environment.

!!! note ""

    "DaoCloud, as one of the first cloud native technology training partners certified by CNCF, will continue to carry out trainings to help more companies find their best ways for going to the cloud."

    Song Zheng,

    Technology GM of DaoCloud

Enterprise users need a global optimal solution, which can be understood as an inclusive platform that can maximize the advantages of multicloud management, application delivery, observability, cloud edge collaboration, microservice governance, application store, and data services. In today's cloud native ecosystem, these features cannot be achieved without Kubernetes as the underlying container orchestration tool. Therefore, Kubernetes is crucial to DaoCloud's mission of finding the optimal solution in the digital world, and all future product development will continue to be based on Kubernetes.

Kubernetes training and promotion activities have always been attached great importance in DaoCloud. In 2017, the company took the lead in passing CNCF's Certified Kubernetes Conformance Program by virtue of its featured product – DaoCloud Enterprise. In 2018, it became a CNCF-certified Kubernetes service provider and training partner.

On November 18, 2022, the "Kubernetes Community Days" event was successfully held in Chengdu, organized by CNCF, DaoCloud, Huawei Cloud, Sichuan Tianfu Bank, and OPPO. The event brought together end-users, contributions, and technical experts from open-source communities to share best practices and innovative ideas about Kubernetes and cloud native. In the future, DaoCloud will continue to contribute to Kubernetes projects, and expand the influence of Kubernetes through project training, community contributions and other activities.
