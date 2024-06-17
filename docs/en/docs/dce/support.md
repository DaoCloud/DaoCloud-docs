---
hide:
  - navigation
---

# DaoCloud Product Support Policy

Unless otherwise specified, the policies described herein apply to the maintenance and support of DaoCloud Enterprise (DCE) software and its included modules.

"Customer" refers to an entity that has ordered product maintenance and support services from DaoCloud.

To obtain the maintenance or support services described under the following [Support Levels](#_1) from DaoCloud, the customer must:

- Have a signed maintenance order specifying the product, the applicable support level, selected optional service enhancements (if any), and the rates;
- Have a currently licensed and supported version of the software;
- Pay the fees related to maintenance and support services.

Software licenses based on subscriptions receive support specific to that type of software or product.

DaoCloud may use subcontractors when performing specific support tasks or services at specific locations. DaoCloud utilizes a national service support model, representing DaoCloud's ability to fully leverage employees from support centers across the country to carry out the following maintenance and support services, making the most of the experience and skills of employees nationwide. Any customer restrictions on this service model are considered non-standard and may result in changes to the maintenance and support policies described herein and additional costs. Due to customer restrictions on DaoCloud's national service support model, any changes to the delivery of maintenance and support must be agreed upon in writing.

"DaoCloud Product Support" is the support and service mechanism applicable to DaoCloud products, which can provide users with valuable support services, such as user manuals, software installation packages, incident tracking records, and best practice documents.

DaoCloud's product support policies may be changed at DaoCloud's discretion and will be published on DaoCloud's official website without further notice. For customers who have paid such support fees, DaoCloud's policy changes will not result in significant changes to the manner in which product support services are provided to the customer within the contract support period (as defined in the service order) that the customer does not recognize or accept.

## Incident Handling

Technical support classifies issues using the following definitions, and provides different response times for different levels of incidents according to the relevant service level agreements.

**Incident Level Classification:**

| Level | Incident Type        | Description                                                                                                                                                       |
|-------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Production Disaster  | Severely impacts customer production, causes system failure or difficulty in normal operations, leads to data loss, and has no workaround or backup method.         |
| 2     | Severe Impact        | Significantly disrupts customer systems, reducing efficiency, but the system can still function and maintain business operations with a corresponding workaround.  |
| 3     | General Impact       | The system works normally, affecting only some non-critical functional modules, and can self-adjust or require simple handling.                                     |
| 4     | Operational Issues   | The system is unaffected and requires no special handling, mainly involving guiding customers on system use or configuration according to relevant processes.       |
| 5     | Optimization Suggestion | Customer suggestions for product expansion or future modifications that do not affect the quality, functionality, or performance of the software or system.        |

When an incident is classified as Level 1 or Level 2, the customer needs to allow DaoCloud immediate and secure remote access to the affected product, or arrange for a DaoCloud service representative to be dispatched to the customer site. If remote access is delayed or the site is inaccessible, problem resolution will be affected and may be delayed.

Customers have the right to propose suggestions for DaoCloud products, which will be defined as Level 5 incidents. DaoCloud will fully analyze these suggestions based on product planning, community technology evolution, and customer usage scenarios, and respond whether the suggestion is accepted.

## Support Services

DaoCloud provides maintenance and support for its products within the scope of support services. For third-party licenses or ecosystem software and module products with DaoCloud copyrights or logos, DaoCloud is responsible for organizing support services, with specific technical support services provided by the original manufacturer.

DaoCloud offers the following types of support services:

- [Standard Services](#_3)
- [Premium Services](#_4)

### Standard Services

| **Service Code** | **Service Name**       | **Service Content**                                                                                                           | **Service Personnel**          | **Pricing Method** | **Recommended Users**                                                                                                                                                                                                                             |
|------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNS              | Product Support and Subscription | After-sales service<br>- Access to version upgrades                                                                            | After-sales Engineers          | Product scale     | Users whose products are already in production, whose after-sales service is about to expire, and who have not purchased S360, need to purchase SNS to provide basic protection for their production environment.                                   |
| PDS              | Product Deployment Service       | On-site or remote professional product deployment service<br>- Product delivery planning, deployment implementation<br>- Product training services<br>- Product maintenance and upgrade services | Delivery Engineers (Intermediate and above) | Per day          | Users who lack strong network, storage, and other infrastructure operation and maintenance capabilities; those with complex product deployment scenarios, or those with personalized product deployment needs. |

- SNS (Support and Subscription) services are provided by DaoCloud's professional cloud-native implementation team, covering the entire product subscription lifecycle: product launch support, operation and maintenance support, monitoring and alert support, and product upgrade support. Based on customer scenarios, this service offers product operation suggestions, operation and maintenance service suggestions, monitoring metric analysis and guidance, product patch/new feature suggestions, and product installation package downloads.

    - **After-sales Service**: Provides corresponding support services for product operation, including product launch guidance, operation and maintenance support during product operation, alert information support analysis, product fault support and repair; analysis of messages in the product alert system, monitoring system metric analysis, and suggestions.

    - **Access to Version Upgrades**: Support for known issues in product versions, support for new features and problem fixes in new versions, and support for downloading corresponding new versions and patches.

- PDS (Product Deployment Service) is provided by DaoCloud's professional cloud-native implementation team, covering the entire product implementation lifecycle, including delivery planning, deployment implementation, daily operation and maintenance, and product upgrades. Based on customer scenarios, this service offers overall deployment planning and detailed resource planning suggestions, full documentation of the product deployment process, standard product demonstrations and usage training services, operation and maintenance guidance and related standards, fault handling, and version upgrade implementation, helping customers complete product implementation and ensure business continuity.

    - **Planning Phase**: Based on the customer's actual environment, design and plan the overall delivery and deployment of the product, set overall goals, and advance in stages. Delivery content includes deployment architecture diagrams, overall environment requirements for deployment, and specific resource planning schemes including IP planning, operating system configuration, external dependency sorting, machine resource planning, network card planning, etc., required for development, testing, and production environments.

    - **Implementation Phase**: Deploy according to the plan, assist the customer in preparing the environment required for the deployment phase, and carry out corresponding deployment work, helping the customer with tenant authorization planning. Delivery content includes corresponding account and password information, product user manuals, and authorization planning operation manuals.

    - **Product Training Services**: Based on customer needs, develop training plans and organize product training to help relevant departments gain a deeper understanding of the product. Delivery content includes expert Q&A, training PPTs, and training videos.

    - **Product Operation and Maintenance**: Help customers address issues related to product use and maintenance during production practice, providing troubleshooting manuals and emergency handling manuals that include information on application startup issues, continuous container restarts, error messages, application inaccessibility, node status readiness, common Pod errors, network troubleshooting, and other cluster fault emergency handling.

    - **Product Upgrades**: Provide product upgrade services based on the customer's current version, including upgrade plan formulation, pre-upgrade checks, upgrade implementation operations, post-upgrade verification, and rollback plans.

### Premium Services

| **Service Code** | **Service Name**             | **Service Content**                                                                                                                                                           | **Service Personnel**                | **Pricing Model** | **Recommended Users**                                                                                                     |
|------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
| S360             | Success360 Critical Business Success | Provides enterprises with more proactive, systematic professional service support based on the product, and offers targeted personalized professional guidance.<br> - Dedicated customer service team<br> - Advanced product solution design<br> - Proactive inspection service<br> - Product upgrade notification service<br> - Operational support for critical events | - Project Manager<br> - Architect (Senior)<br> - Operation and Maintenance Engineer (Senior) | Product scale      | - Customers whose platforms carry important workloads<br> - Large cluster scale<br> - Platforms hosting a large number of applications |

S360 (Success 360, Customer Success 360 Service) is provided by DaoCloud to offer customers a dedicated cloud-native technical team that comprehensively supports customer success. Service personnel are dynamically allocated based on customer industry attributes and service requirements. The service includes customized advanced product solution design, regular health inspections of the product, proactive identification of potential issues, and production practice improvement or optimization suggestions. It also ensures business continuity during critical customer phases, such as peak business periods, key business launches, and application upgrades.

- **Dedicated Customer Service Team**: Form a dedicated expert service team based on the customer's industry attributes and service requirements to assist in customer success.
- **Advanced Product Solution Design**: Provide personalized product solutions according to customer needs, including blue-green deployment, disaster recovery plans, monitoring plans, logging plans, gray release plans, and large cluster solutions.
- **Proactive Inspection Service**: Conduct regular health inspections of the product and provide inspection reports, including overall information, management nodes, compute nodes, application status, functional requirements and issue handling, and overall evaluation.
- **Product Upgrade Notification Service**: Proactively provide customers with product update reports and community software vulnerability reports, and offer related product revision and version upgrade services based on specific circumstances.
- **Operational Support for Critical Events**: Provide business continuity support during critical customer phases (such as peak business periods, key business launches, and application upgrades). Offer change strategy design and plan discussions, assist in fault handling, and generate reports for future reference. Deliverables include service plans and personnel configurations, service process records, and service reports.

## Requesting Service

If customers encounter issues while using supported products, DaoCloud will provide DaoCloud product support services and activate its automatic incident creation diagnostic tools. Customers can report issues any time, 24/7, and DaoCloud will provide support within the coverage time specified in the order.

| Level | Standard Service Response Time | Standard Service Channel       | Premium Service Response Time | Premium Service Channel          | Professional Service Response Time | Professional Service Channel          |
|-------|-------------------------------|-------------------------------|-------------------------------|----------------------------------|------------------------------------|--------------------------------------|
| 1     | Four hours 24/7               | Customer Service/Phone/Remote | Two hours 24/7                | Customer Service/Phone/Remote/On-site | One hour 24/7                       | Customer Service/Phone/Remote/On-site |
| 2     | Eight hours 5*8 (9:00 - 18:00)| Customer Service/Phone/Remote | Four hours 24/7               | Customer Service/Phone/Remote/On-site | Two hours 24/7                      | Customer Service/Phone/Remote/On-site |
| 3     | Two business days 5*8 (9:00 - 18:00) | Customer Service/Phone/Remote | One business day 5*8 (9:00 - 18:00) | Customer Service/Phone/Remote     | Four hours 5*8 (9:00 - 18:00)       | Customer Service/Phone/Remote/On-site |
| 4     | Four business days 5*8 (9:00 - 18:00) | Customer Service/Phone/Remote | Two business days 5*8 (9:00 - 18:00) | Customer Service/Phone/Remote     | One business day 5*8 (9:00 - 18:00) | Customer Service/Phone/Remote/On-site |
| 5     | None                           | Customer Service/Phone/Remote | Regular Discussions            | Customer Service/Phone/Remote     | Monthly Discussions                 | Customer Service/Phone/Remote/On-site |

The general process of service support is illustrated in the following diagram:

![Service Process](./images/flow.png)

### Coverage Time

Coverage time refers to the time calculated based on the local time where the customer's system is located. If the service cannot be completed within the coverage time on the day of the request, it will continue during the next coverage period.

If the customer does not directly contact a DaoCloud service representative, the relevant personnel will call back the customer within the designated response time. When a customer reports an incident, the service representative will respond to the query and ensure the incident is resolved.

Remote response time is measured as the interval between the customer's initial contact (via electronic receipt of the incident or phone call) with DaoCloud and the first contact (via electronic receipt of the incident or phone call) with a DaoCloud representative within the agreed remote coverage time.

On-site response time is measured as the interval between the dispatch of a service representative from the DaoCloud service center and their arrival at the customer site within the agreed on-site coverage time. The dispatch of service representatives is at DaoCloud's discretion.

### Exclusions

Situations where product support services cannot be normally enjoyed (out-of-scope services):

- Illegal and unauthorized DaoCloud software maintenance services
- Deployments with unauthorized changes to DaoCloud software
- Major changes made directly by the customer
- Technical preview features unless otherwise specifically agreed
- Issues caused by any third-party software or underlying hardware issues. DaoCloud online service personnel can help users identify these issues, but users must contact the relevant suppliers to resolve issues with their products.

DaoCloud will only provide out-of-scope services ("Additional Services") if the applicable out-of-scope service fees have been agreed upon with the customer. If a service is an out-of-scope task, DaoCloud will inform the customer before commencing work. However, if DaoCloud has reason to believe that providing a certain product service would pose a security risk, the service will not be provided.

## Support Lifecycle

DaoCloud will provide remote software support for non-discontinued and certified software products during the customer's contract period. DaoCloud will offer diagnostic and problem-solving services for supported operating systems, DaoCloud software, and tools. Any on-site software services are at DaoCloud's discretion.

### Lifecycle Announcements

- DCE 5.y Series

    | **Abbreviation** | **Full Name**          | **Description**  |
    | ------------------------ | ----------------------------- | ---------------- |
    | GA                       | General Availability          | Product released on June 1, 2023 |
    | EOSS                     | End of Standard Support       | Patch development and full support will cease on June 1, 2026, after product release |
    | EOSL                     | End of Support Life           | Service will cease on October 30, 2028, after product release |

- DCE 4.y Series

    | **Abbreviation** | **Full Name**          | **Description**  |
    | ------------------------ | ----------------------------- | ---------------- |
    | GA                       | General Availability          | Product released on March 31, 2020 |
    | EOSS                     | End of Standard Support       | Patch development and full support will cease on March 31, 2023, after product release |
    | EOSL                     | End of Support Life           | Service will cease on March 31, 2025, after product release |

- DCE 3.y Series

    | **Abbreviation** | **Full Name**          | **Description**  |
    | ------------------------ | ----------------------------- | ---------------- |
    | GA                       | General Availability          | Product released on July 15, 2018 |
    | EOFS                     | End of Standard Support       | Patch development and full support will cease on July 30, 2021, after product release |
    | EOSL                     | End of Support Life           | Service will cease on July 30, 2023, after product release |

## Supported Software Versions

Most DaoCloud software products have several different types of software versions. These versions are distinguished by version numbers x.y.z:

- The number x refers to the major software version, which is also the DCE version number.
- The number y refers to the minor software version upgrades.
- The number z refers to maintenance version updates.

"Service Pack" and "Hotfix" are third-party names for software fixes. According to DaoCloud DCE version number definitions, a "Service Pack" is a maintenance version (z).

### Software Maintenance and Patch Version Access

All platform maintenance and support service levels include access to standard product software maintenance, patch downloads, and fix version downloads. For most issues, customers can access the DCE documentation site (docs.daocloud.io) to obtain updates for software patches and fix versions, or DaoCloud can provide a single media copy upon customer request at no extra charge. Customers can copy and/or install patches or maintenance version updates for each licensed software for which they have paid fees.

### Maintenance and Support for Deprecated Software

Code maintenance for deprecated software is not available. Support for deprecated products is not guaranteed and depends on the availability of specialized technical experts and other resources necessary to support the product.

### Maintenance and Support for Modified Software

If the customer has made changes to the designated software, it will be referred to as "Modified Software." DaoCloud does not provide any level (x, y, z) of software versions compatible with the modified version. When using new software in conjunction with modified versions, DaoCloud does not guarantee that the new software will operate in accordance with DaoCloud's specifications.

## Customer Installable and Upgradable Software

For customer-installable software, i.e., software that customers can download from the DCE documentation site, DaoCloud will provide access to user documentation, which is supported and discussed within the DaoCloud community. DaoCloud will also provide remote installation support, including:

- Guidance on how to find solutions to known issues through user documentation.
- Information to resolve procedural issues.
- Answers to frequently asked questions.
- Solutions for reported issues.

### Software Subscription/Subscription Licensing

Through this service, customers are entitled to major (x) and minor (y) versions of the licensed software for general commercial use. DaoCloud subscription or subscription licensing includes DaoCloud software, utilities, and tools covered by the customer maintenance and support agreement and any paid licensing fees. Subscription or subscription licensing does not include software implementation.

### Antivirus Scanning Software

DaoCloud does not provide bundled solutions for antivirus scanning software, nor does it offer consulting on the configuration and selection of any antivirus software.

DaoCloud is not responsible for viruses on the customer's system, and system repairs and virus isolation are not covered by maintenance and support services if a virus is detected on the customer's system hard drive. While DaoCloud will make commercially reasonable efforts to assist upon customer request, DaoCloud is not responsible for data loss related to such viruses.

## DaoCloud Software Programs

### DaoCloud Management Software and Other Software Support Lifecycle

For DaoCloud software, DaoCloud will provide software issue resolution services, including code-level maintenance and any existing corrections or temporary solutions to resolve reported software issues for the current major/minor software versions. When the customer's software version is no longer the latest version and the customer has not upgraded to the latest version, DaoCloud will provide "limited support" services within the support period, and such support may incur additional fees.

### Service Validity Period

Initial Product Deployment:

- **Software Products**: The service start time is the date when the software is first officially licensed and activated. The service end time is extended according to the purchased service duration.
- **Integrated Products**: The service start time is the date of delivery of the integrated product. The service end time is extended according to the purchased service duration.

Product Expansion:

- **New Cluster Installation**: If product expansion is implemented by installing a new cluster, the service validity period of the expanded product follows the definition of initial deployment.
- **Expansion within Existing Cluster**: If the product is expanded within the existing cluster, the service validity period of the expanded product is consistent with the service validity period of the original cluster.

### Extended Software Maintenance (EAM)

After the support expiration of certain software products, DaoCloud can provide extended software maintenance services for up to 2 additional years. Extended software maintenance services are offered in 1-year increments. Extended software maintenance services include:

- 24/7 incident call acceptance
- Code-level maintenance for Level 1 and Level 2 incidents, providing emergency fixes for new and existing issues
- Issue calls can be recorded through DaoCloud product support
- If no acceptable temporary solution exists, critical electronic fixes will be backported (if possible)
- Only remote service support methods are provided, no on-site support
- Continuation of the current level of coverage time

To qualify for extended software maintenance services, the customer must meet the following criteria:

- The customer must have a stable environment, with no growth in user load, or no plans for large-scale software changes. The customer must maintain the supported configuration according to the supported configuration matrix of their current version.
- The customer must be running the latest maintenance version of the major/minor version and be willing to upgrade to the latest electronic fixes to obtain corrections.
- EAM contracts do not allow any gaps in support coverage time. As soon as the electronic fix support for the current software version expires, customers are encouraged to migrate to an EAM contract. Any customer requesting support without a signed EAM agreement will need to sign a new EAM agreement and pay the arrears covering the period from the end of electronic fix support to the present.

Extended software maintenance services do not include:

- Illegal and unauthorized DaoCloud software maintenance services
- Deployments with unauthorized changes to DaoCloud software
- Major changes made directly by the customer
- Technical preview features unless otherwise specifically agreed
- Issues caused by any third-party software or underlying hardware issues. DaoCloud online service personnel can help users identify these issues, but users must contact the relevant suppliers to resolve issues with their products.

## Third-Party Software

Support for third-party software ecosystem products is provided by the relevant suppliers unless DaoCloud has a specific agreement with the supplier regarding third-party software support. When DaoCloud does have a specific agreement with a third party and the customer has a contract with DaoCloud to provide support for third-party products, the installation, implementation, upgrade, and update of third-party software and drivers are the responsibility of the customer, including backup and recovery of third-party software and drivers. If there is no formal support relationship between DaoCloud and the third-party supplier, DaoCloud will not perform any certification or testing of these software products. It is the customer's responsibility to determine if the supplier has certified the software for use in the customer's deployment environment. Even if third-party products are certified for use with DaoCloud products, DaoCloud assumes no responsibility for the installation, integration, maintenance, or support of third-party products.

In most cases, DaoCloud agrees to the installation and use of third-party software by customers unless DaoCloud has previously identified compatibility issues. If DaoCloud identifies that a particular third-party product may negatively impact performance, compatibility, or functionality, DaoCloud will recommend that the customer immediately disable or remove the product and contact the third-party supplier for support. If the customer does not accept DaoCloud's recommendation, this refusal may negatively impact the level of support provided by DaoCloud and may render the support agreement between the customer and DaoCloud legally ineffective. DaoCloud will document any issues related to third-party products. Any diagnostics and/or resolution of issues caused by third-party products will be considered "out-of-scope" services under the customer service agreement.

## Nationwide Support

DaoCloud provides after-sales support services for products nationwide.

DaoCloud's nationwide technical support centers are strategically located to efficiently connect you with the support center in your region. Each center is staffed with professional technical engineers who offer industry-leading cloud-native expertise and product usage experience. DaoCloud is committed to providing enterprise-grade global support with a mission to help customers achieve continuous success.

### Issue Resolution

Software issue resolution includes:

- Providing guidance on finding solutions to known issues through user documentation, information to resolve procedural issues, and answers to frequently asked questions.
- Offering upgrade recommendations when subsequent software versions can resolve issues.
- Providing temporary workarounds to avoid issues before delivering fixes/code-level changes.
- Offering fixes/code-level changes to resolve reported issues. Fixes/code-level changes are solely at DaoCloud's discretion for supported versions of tools and utilities/client software.
- Installation or step-by-step installation consulting.
- Testing of patches and maintenance versions installed by the customer.
- Product or system recovery after customer installation failure.

DaoCloud software issue resolution does not include:

- Illegal and unauthorized DaoCloud software maintenance services.
- Deployments with unauthorized changes to DaoCloud software.
- Major changes made unilaterally by the customer.
- Technical preview features unless otherwise specifically agreed.
- Issues caused by any third-party software or underlying hardware issues. DaoCloud online service personnel can help users identify these issues, but customers must contact the relevant suppliers to resolve issues with their products.

### Issue Reporting

DaoCloud's support process includes reporting, notification, and resolution guidance. The system will trigger these processes based on the severity of the incident and its impact on product performance.

#### Communicating Incident Reporting Status

All Level 1 incidents should be immediately reported to the on-duty supervisor and the designated DaoCloud customer service representative. The status of these issues will be provided to the customer hourly through conference calls and other means.
For Level 2 and Level 3 incidents, customers can use DaoCloud product support and choose the appropriate "View Incident" option to check the status as needed.
Customers can also request to automatically receive email updates regarding any incident.

#### Reporting Downtime Beyond Approved Change Control Plan

For change control on production systems that results in unplanned downtime, DaoCloud will immediately declare a Level 1 incident and fully address the issue until the system is fully operational again.
Once the system is restored, DaoCloud will review the incident with the customer to find ways to prevent the issue from recurring.

## Incident Management

When a customer initiates a Level 1 incident, DaoCloud will make every effort to bring the customer's system to an operational state immediately. To effectively resolve a Level 1 incident,
DaoCloud requires the customer to grant unrestricted access to the system immediately and ensure that appropriate customer staff are available to assist in resolving the issue. Otherwise, DaoCloud will reclassify the incident as a Level 2 incident.

Once remote DaoCloud support personnel begin to support a Level 1 incident, they will work continuously and without interruption to resolve the problem;
if deemed necessary, they will also dispatch DaoCloud on-site support personnel to assist in resolving the issue.
For Level 2 or Level 3 incidents, DaoCloud reserves the right to interrupt the work of the customer service representative and may reassign the customer service representative to resolve the issue.

### Incident Closure

After providing a solution to the incident, DaoCloud will request customer consent to close the incident. If the customer actively engages with DaoCloud upon receiving the solution and acknowledges that the solution has resolved and/or answered the issue, DaoCloud will close the incident.

If the customer is not directly involved when the solution is provided (for example, the customer is informed of the solution through DaoCloud product support or email), DaoCloud
will provide the customer with the opportunity to agree to close the incident. If the customer does not notify DaoCloud that the issue is unresolved, DaoCloud will mark the incident as "Transferred to Customer" and close it.
These incidents will be displayed as “Transferred to Customer” in DaoCloud product support for two years.

If the customer does not provide DaoCloud with the necessary information for correct diagnosis and resolution, DaoCloud will also close the incident. If
DaoCloud does not receive the requested information within a reasonable time frame (determined by the incident level), DaoCloud will close the incident and mark it as "Cancelled by Customer".
For Level 3 incidents, the customer should respond to requests within 7 days; for Level 4 incidents, within 14 days.

The definition of incident resolution is as follows:

- Consultation provided, resolving and/or answering the issue
- Countermeasure provided, deemed as a permanent solution
- Change request needed

### Change Control Requests

DaoCloud requires customers to provide at least 28 days' notice before implementing changes to facilitate the development of a change control plan.

## Customer Responsibilities

Customers are responsible for fulfilling specific obligations to ensure DaoCloud can provide services. If customers fail to meet the following obligations, DaoCloud may:

- Charge for additional, out-of-scope, or on-site work based on time and materials
- Reclassify the incident level
- Not perform the service

### On-Site Preparation

Customers are responsible for preparing (before delivering products to be used or serviced), maintaining, and/or updating the customer site per DaoCloud's specifications and providing safe and adequate working conditions for DaoCloud maintenance personnel.

#### Remote Connection

DaoCloud requires remote access to the customer's system to deliver all remotely deliverable services. Customers must allow DaoCloud and its support partners access to their systems for remote connection and to use DaoCloud support tools for the following operations. Additionally, customers must provide the login credentials required for remote access upon DaoCloud's request.
If the customer refuses to install or at any time does not allow DaoCloud to fully utilize the remote connection via a dedicated network, the support-related SLA will be void, and DaoCloud
will be unable to provide any remotely deliverable optional additional support and services.

For the integrated DaoCloud platform, if the customer does not allow support services to be delivered via DaoCloud's dedicated network remote connection,
the customer will need to pay additional fees related to on-site service delivery besides the annual support service fee.

In addition to remote connection, if the DaoCloud support service tool suite is not fully enabled, DaoCloud's support functions and applicable services with the highest level of security and automation cannot be provided,
and the customer will be responsible for managing these services. For example, using DaoCloud's communication system to notify DaoCloud of all faults and alerts within 24 hours and providing all incident log information.
Our support partners' monitoring/reporting tool suite also requires this remote connection.

#### Product Movement, Addition, or Recovery

If the customer needs to move, add, or delete products in service, or wishes to change the contract service time, written notice must be given to DaoCloud at least 30 days in advance.
The notice must provide the new data center and effective date of the change. If the customer does not provide the necessary notice, DaoCloud reserves the right to charge additional fees for delays caused by such issues (including situations such as DaoCloud's technicians being dispatched to the wrong location).

For products previously covered under a maintenance and support order and now requiring restoration under a new maintenance and support order, regardless of the service level or option selected by the customer,
all overdue maintenance and support fees and any applicable re-certification fees must be fully paid before DaoCloud accepts the product for service.
Products not covered by DaoCloud's warranty must be re-certified by DaoCloud before DaoCloud can provide service under the maintenance and support order.

### Operations

The customer is responsible for all operations related to the system, including:

- Obtaining appropriate training related to operations;
- Ensuring all installations, upgrades, and corrections related to the issue are performed according to DaoCloud's specifications;
- Providing backups and restoring the system, processes, and services in case of system failure;
- Restoring data, data connections, and software after DaoCloud performs any service;
- Safely storing all software data and removable storage at specified intervals before DaoCloud performs any service;
- Performing any necessary tests;
- Promptly installing correction programs provided by DaoCloud for reported issues;
- Resolving any system performance issues.

Customers must operate the product according to DaoCloud's documentation. Unless performed by DaoCloud or approved by DaoCloud, customers must not make or cause to make any corrections, repairs, or changes to the product, or perform or cause to perform any maintenance work.

Customers are responsible for accessing DaoCloud product support to check the status of change control and incidents. Customers must:

- Designate a reasonable number of trained personnel as support contacts to interface with the DaoCloud customer service team;
- Check support and product deactivation notifications on DaoCloud product support;
- Identify any target software and/or driver patches and their versions to be installed (other than those recommended by DaoCloud to resolve issues).

### Monitoring Tools

Customers must allow DaoCloud to install and run monitoring and diagnostic tools/agents. These tools are specifically used to collect and store detailed system data related to support,
assist in problem resolution and change control implementation, analyze and report system usage, and detect faults and notify DaoCloud. System usage data does not contain customer data.

### DaoCloud Product Support

Customers should designate two employees in writing as the primary and backup administrators for DaoCloud product support and ensure they are on standby during work hours.
Administrators are responsible for the following: approving DaoCloud product support users within their company and adding or removing DaoCloud product support functionalities.

### Initial Problem Resolution

Customers should attempt to isolate and document the problem and use DaoCloud product support to check for known issue fixes, track incident status,
submit and update all service incidents, and determine if there are fixes and new software versions available for the problem.

Customers should provide commercially reasonable cooperation and assistance to DaoCloud's technical support personnel and provide complete and accurate information related to the issue until it is resolved. Such customer support may include logging into the customer's system to diagnose the issue, downloading and installing software patches, retrieving and transmitting system logs/files, reinstalling existing products, and participating in repair testing.
