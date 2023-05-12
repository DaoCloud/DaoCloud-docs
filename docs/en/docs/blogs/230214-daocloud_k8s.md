# DaoCloud and Kubernetes

> Find the global optimal solution for the digital world

## challenge

[「DaoCloud 道客」](https://www.daocloud.io/) is an innovative leader in the field of cloud native. It was established at the end of 2014. It has core technologies with independent intellectual property rights and is committed to creating an open cloud operating system. Enterprise digital transformation empowerment. Such goals and missions determine that the company has worked in the cloud-native world since its inception. Different from traditional business scenarios, cloud-native business cannot do without containers, and cloud operating systems rely on containers as infrastructure. Therefore, the primary challenge facing DaoCloud is how to efficiently manage and schedule multiple containers, and how to ensure normal communication between containers.

In addition, today's cloud native is in a period of rapid development, and various cloud native technology solutions emerge in endlessly, each with its own advantages and disadvantages, which is dazzling. What users expect is not to solve the local optimal solution to the immediate problem, but to find the global optimal solution. How to integrate these independent projects, learn from each other's strengths, and build an overall cloud-native solution is another challenge faced by DaoCloud, and it is also a development problem for the cloud-native industry.

## solution

As the de facto standard for container orchestration, Kubernetes is undoubtedly the container solution of choice. Xu Junjie (Paco), architect and head of the open source team of DaoCloud, said, "Kubernetes is a relatively basic part of the current container ecosystem. Most services are deployed based on Kubernetes, and most applications are deployed in Kubernetes clusters. run and manage in."

Faced with the endless technical solutions, Peter Pan, vice president of research and development of DaoCloud, believes that "in the face of many technologies, insist on taking Kubernetes as the core, integrate the best practices and advanced technologies around, and create a suitable platform and solution. , is the correct path to find the global optimal solution.”

## Influence

In the process of embracing cloud-native, DaoCloud continues to learn from excellent CNCF open source projects such as Kubernetes, and gradually formed a cloud-native application cloud platform based on [DaoCloud Enterprise](https://docs.daocloud.io/) Core product architecture. DaoCloud adheres to the world's leading cloud-native technologies such as Kubernetes as the fulcrum, and provides cutting-edge cloud-native solutions for vertical industries such as military industry, finance, manufacturing, energy, government affairs, and retail. Funds, SAIC Motor, Haier, Fudan University, Watsons, Genius Auto Finance, State Grid and other outstanding companies in various industries have tailored satisfactory digital transformation solutions.

!!! note ""

     "As DaoCloud Enterprise becomes more and more powerful and the customer coverage is wider and wider, some customers need to use Kubernetes instead of Swarm for application orchestration. As a powerful application orchestration system, Kubernetes has strong community support and is also supported by many big favored by companies. We as providers need to meet the needs of users."

     [Liu Qijun (Kebe)](https://github.com/kebe7jun), DaoCloud service mesh expert

The original intention of the establishment of DaoCloud is to help traditional enterprises carry out digital transformation and realize application cloud. The first product DaoCloud Enterprise 1.0 released after the establishment of the company is a Docker-based container engine platform, which can easily package and build images and run containers. As the number of applications increases, there are more and more containers. How to coordinate and schedule these containers has gradually become the main bottleneck restricting product performance. DaoCloud Enterprise 2.0 began to use Docker Swarm to manage containers, but as the container scheduling system became more and more complex, Docker Swarm also began to appear powerless.

This coincided with the emergence of Kubernetes, which rapidly developed into the industry standard for container orchestration with its advantages of diverse functions, stable performance, timely community support, and strong compatibility. Paco said, "Enterprise container platforms need container orchestration to standardize the process of applying to the cloud. Kubernetes gradually became the de facto standard for container orchestration in 2016-2017, and we started to support both Docker Swarm and Kubernetes in 2017."

After a series of evaluations, DaoCloud Enterprise 2.8 released in 2017 officially adopted Kubernetes (v1.6.7) as a container orchestration tool. Since then, DaoCloud Enterprise 3.0 released in 2018 adopts Kubernetes 1.10 version, and DaoCloud Enterprise 4.0 released in 2021 adopts Kubernetes 1.18 version. DaoCloud Enterprise 5.0, released in 2022, supports Kubernetes versions 1.23 to 1.26.

Four major releases over a six-year period have been steadfastly using Kubernetes, which speaks volumes for the fact that it was the right choice at the time. "DaoCloud Taoist" has proved that Kubernetes is the best choice for container arrangement with practical experience, and also proved with his own actions that he has always been a loyal fan of Kubernetes.

!!! note ""

     "With the help of the value system of K8S "automation is greater than labor", the production and research team has completed from 0 to 1 the automation of R&D and construction, testing automation, security automation, and release automation to ensure the quality of software delivery. Secondly, it has realized intelligent collaborative communication, including The product requirements and definition system, the product multilingual collaboration system, the product defect repair collaboration system, and the difficult and miscellaneous disease tackling system have greatly improved the efficiency of collaboration between production and research departments and across departments. This is our goal for world-class infrastructure software products Cornerstone."

     Ting Ye, Vice President of Product Innovation of DaoCloud

With the help of Kubernetes, the product performance of DaoCloud is better and more competitive. DaoCloud adheres to Kubernetes as the core, integrates surrounding best practices and advanced technologies, and creates a DaoCloud Enterprise cloud-native application cloud platform that provides application stores, application delivery, microservice governance, observability, data services, and multi-cloud orchestration , Xinchuang heterogeneous, cloud-edge collaboration and other capabilities. DaoCloud Enterprise 5.0 is a complete form of cloud-native technology.

- After DaoCloud deployed the Kubernetes platform for Shanghai Pudong Development Bank, the application deployment efficiency increased by 82%, the delivery cycle was shortened from half a year to one month, and the transaction success rate reached 99.999%;
- Sichuan Tianfu Bank implemented a cloud-native platform based on Kubernetes, which greatly reduced the elastic response time from several hours to an average of 2 minutes, shortened the product iteration cycle from two months to two weeks, and shortened the application launch time by 76.76%;
- After building a Kubernetes-based cloud-native platform for a joint venture car company, the delivery cycle was shortened from two months to one or two weeks, the success rate of application deployment increased by 53%, and the efficiency of application launch increased by 24 times; deployed for a multinational retail group Multiple cloud-native platform modules based on Kubernetes have reduced application deployment problems by 46%, and improved monitoring and positioning efficiency by more than 90%;
- Build a unified cloud-native PaaS platform for a large-scale comprehensive securities company, which improves its business process efficiency by 30% and saves resource costs by about 35%;
- Created a new generation of Kubernetes-based cloud-native PaaS platform for Wells Fargo Fund, shortening the deployment time of standard middleware from hours to minutes, increasing middleware operation and maintenance capabilities by 50%, containerization by 60%, and resource utilization by 40% %.

On the other hand, DaoCloud's own product development work is also based on Kubernetes. The company deployed Gitlab based on Kubernetes, forming a product development process of "Gitlab —> PR —> Automated Testing —> Build and Release", which significantly improved development efficiency, reduced the workload of repeated testing, and realized the automatic release of applications. In this way, operation and maintenance costs are greatly saved, and technicians can invest more time and energy in product development to polish better cloud-native products.

!!! note ""

     "Our developers are actively contributing to open source, accumulating technical strength, and making more and more contributions in the Kubernetes and Istio communities. The company's fifth-generation products are also open source, contributing to cloud-native technology and improving the technical ecosystem. "

     Xu Junjie Paco, DaoCloud Architect/Open Source & AD Team Leader

DaoCloud has been deeply involved in and contributed to many cloud-native open source projects such as Kubernetes, and its participation and contribution in the cloud-native open source community continue to grow. In the past year, DaoCloud ranked third in the world in cumulative contribution to the open source list of Kubernetes (based on data from [Stackalytics website 2023/01/05](https://www.stackalytics.io/cncf ?project_type=kubernetes&date=365)).

In August 2022, in the official community contributor interview organized by Kubernetes, 4 outstanding contributors from the Asia-Pacific region were interviewed, including [Shiming Zhang](https://github.com/wzshiming) and [Paco Xu] (https://github.com/pacoxu) are both from "DaoCloud Taoist", both of them are Reviewers of SIG Node. In addition, at the 2022 Kubecon North America station, [Kante Yin] (https://github.com/kerthcet) of "DaoCloud Taoist" won the Kubernetes 2022 Contributor Award.

In addition, DaoCloud is also insisting on practicing cloud-native beliefs, continuing to give back to the cloud-native community, open-sourced Clusterpedia, Kubean, CloudTTY, KLTS.io, Merbridge, HwameiStor, Spiderpool, Piraeus and other excellent projects, and constantly improving the Kubernetes ecosystem in:

- Clusterpedia is compatible with Kubernetes OpenAPI, realizes the synchronization of multi-cluster resources, provides a more powerful search function, and can quickly, easily and effectively obtain all resource information in the cluster.
- Kubean supports the rapid creation of Kubernetes clusters and clusters from other vendors.
- CloudTTY is a web terminal and Cloud Shell Operator specially designed for the Kubernetes cloud-native environment. It can manage Kubernetes clusters anytime, anywhere through a web page.
- KLTS provides long-term free maintenance support for earlier versions of Kubernetes.
- Piraeus is a high performance, high availability, simple and secure storage solution for Kubernetes.

DaoCloud integrates its own practical experience in various industries, continues to contribute to the Kubernetes open source project, and is committed to making the cloud native technology represented by Kubernetes more stable and efficient to implement products and production practices.

!!! note

     "DaoCloud, as the first batch of cloud-native technology training partners officially certified by CNCF, will continue to carry out activities such as empowerment training, project guidance, etc., and work with partners to introduce cloud-native to customers and jointly create the best practice path for cloud-native capabilities."

     Zheng Song, technical general manager of DaoCloud in China

Pan Yuanhang (Peter), vice president of research and development of DaoCloud, believes that "enterprise users need a global optimal solution, which can be understood as covering multi-cloud orchestration, innovation heterogeneity, application delivery, observability, The greatest common divisor of capabilities such as cloud-side collaboration, microservice governance, application store, and data services.” In today’s cloud-native ecosystem, these functions are inseparable from Kubernetes as the underlying container orchestration technology. This means that DaoCloud cannot do without Kubernetes in the process of finding the optimal solution to the digital world, and future product development will continue to be based on Kubernetes.

In addition, DaoCloud has been committed to Kubernetes training and promotion activities. In 2017, the company became the first manufacturer in the world to pass the CNCF Kubernetes compatibility certification with its core product cloud-native application cloud platform DaoCloud Enterprise. In 2018, the company became a CNCF-certified Kubernetes service provider, and became the first batch of Kubernetes training partners in the world to obtain CNCF official certification, fully embracing the Kubernetes technology ecosystem.

November 18, 2022 by CNThe "Kubernetes Community Days Chengdu Station" jointly sponsored by CF and DaoCloud, Huawei Cloud, Sichuan Tianfu Bank, and OPPO was successfully held, gathering end users, contributors and technical experts from the open source community in the cloud native field to share about Native multi-industry practices, popular open source projects, community contribution experience and other rich content. In the future, DaoCloud will continue to contribute to Kubernetes, and continue to expand the influence of Kubernetes through project training, community contribution and other activities.
