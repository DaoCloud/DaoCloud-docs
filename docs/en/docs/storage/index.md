# Cloud Native Storage

Cloud native transformation encompasses three types of storage:
traditional storage, software-defined storage, and cloud native local storage.

Traditional storage can be integrated with the Kubernetes platform through the CSI standard.
This type of storage is widely used as it allows users to leverage their existing storage infrastructure.
It provides stable cloud native storage capabilities and offers strong SLA guarantees.

Software-defined storage is compatible with both traditional and cloud native applications.
It also integrates with Kubernetes using the CSI standard, making it versatile and adaptable to different environments.

Local storage, known as HwameiStor, is specifically designed for cloud native environments.
It is built on a cloud native platform and has been selected as an open-source local storage solution
for cloud native stateful workloads with High-Availability (HA) capabilities by CNCF sandbox.
HwameiStor addresses the limitations of local volumes by enabling data drifting with applications,
ensuring data availability and reliability.

HwameiStor is based on the Kubernetes CSI standard and can be connected to CSI-compliant storage
according to different SLA requirements and use cases. The cloud native local storage launched by
DaoCloud naturally has cloud native features and meets the characteristics of high scalability and
high availability in container use cases.

HwameiStor, a cloud native local storage solution, provides high-performance and high availability
with its IO localization feature. It ensures 100% local throughput and redundant data backup,
ensuring in uninterrupted data access even in node failures. The solution supports seamless switching
and offers continuous data availability. HwameiStor's linear expansion capability allows for easy
scalability, while its efficiency minimizes CPU and memory overhead. With features such as node and
disk migration, the solution provides operational manageability, empowering businesses to optimize
their cloud native environments with reliable data management.
