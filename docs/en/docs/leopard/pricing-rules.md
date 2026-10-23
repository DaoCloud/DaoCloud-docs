---
hide:
  - toc
---

# Billing Rules

Welcome to the d.run Cloud Service Platform! To help you better understand and manage your expenses, we have prepared this billing rules document.  
This document explains in detail the billing mechanisms, pricing standards of each product, and related expense management policies to help you plan and control costs effectively.

## Billing System Overview

The platform adopts an enterprise-grade multi-layer billing architecture, consisting of the application layer, billing engine layer, and data layer, ensuring the billing process is accurate, fair, and transparent.

**System Features:**

- **Professional Billing Engine**: Independent billing processing layer to ensure professionalism and high reliability of financial transactions  
- **Robust Data Management**: Dedicated data layer to manage account balances, orders, bills, and usage information  
- **Full Audit Tracking**: Detailed data records support expense queries and audits, improving financial transparency  

## Billing Principles and Service Commitments

### Accurate Billing Commitment

**Per-second billing with hourly settlement**

- Billing is calculated per second, ensuring you only pay for actual resource usage  
- Fees are settled at the top of the hour, maximizing your benefits  

**Smart Trigger Mechanism**

- Node trigger: Billing automatically starts when a resource is created or launched  
- Event trigger: Billing precisely stops or adjusts when a resource is shut down, deleted, or reconfigured  
- Prevents duplicate charges for idle or deleted resources  

### Service Guarantee Mechanism

**Fault Tolerance**

- Abnormal orders caused by system failures are automatically voided, ensuring you won’t be charged incorrectly  
- Comprehensive handling processes protect your rights in case of exceptions  

**Real-time Monitoring**

- 24/7 real-time monitoring of resource status ensures billing accuracy  
- Supports differentiated billing strategies for different products  

**User-friendly Policies**

- A grace period is provided when the balance is insufficient, preventing sudden service interruption  
- Flexible refund mechanisms safeguard your legitimate rights  

## Product Billing Details

### Container Instances

**Pay-as-you-go**

- **Billing start**: When the resource is launched  
- **Settlement**: Hourly on the clock, or immediately when the resource is shut down/deleted  
- **Precision**: Billed per second for accuracy  
- **Use cases**: Short-term usage, testing & development, uncertain duration  

**Subscription (Yearly/Monthly)**

- **Billing start**: Effective immediately after order payment  
- **Refund policy**: Refunds supported based on actual usage duration  
- **Use cases**: Long-term stable usage with clear budget planning  

### File Storage

**Billing Rules**

- **Free quota**: Each account gets 20GB of free storage  
- **Billing start**: Charges apply once usage exceeds 20GB  
- **Settlement**: Hourly on the clock  
- **Billing mode**: Pay-as-you-go  

### MaaS (Model as a Service)

**Billing mode**: Pay-as-you-go, based on actual calls  

**Text Models**

- **Rule**: Billed by the number of input and output tokens  
- **Settlement**: By billing cycle  

**Image Generation Models**

- **Rule**: Billed by the number of successfully generated images  
- **Settlement**: By billing cycle  

### Private Models

**Billing Rules**

- **Billing start**: When the model instance is launched  
- **Settlement**: Hourly on the clock, or immediately when the resource is shut down/deleted  
- **Configuration changes**: After scaling, charges follow the new configuration  
- **Billing mode**: Pay-as-you-go  

## Billing Rules Summary

| Product Type     | Billing Mode   | Billing Start Time   | Settlement Cycle            | Notes |
| ---------------- | -------------- | -------------------- | --------------------------- | ----- |
| Container Instance | Pay-as-you-go | Resource launch      | Hourly or when resource stops | Per-second billing |
|                  | Subscription   | Order payment success | Refund supported by usage   | More cost-effective for long-term, flexible refund |
| File Storage     | Pay-as-you-go  | Exceeding 20GB quota | Hourly                      | 20GB free quota, extra usage billed |
| MaaS Model Service | Pay-as-you-go | Actual API call      | By billing cycle            | Text billed by tokens, image billed per generation |
| Private Model    | Pay-as-you-go  | Resource launch      | Hourly or when resource stops | Supports dynamic scaling, billed by new config |

## Expense Management Recommendations

**Cost Optimization Tips**

1. **Choose the right billing mode**: Subscription for long-term usage, pay-as-you-go for temporary needs  
2. **Manage resources promptly**: Shut down or delete unused resources to avoid unnecessary charges  
3. **Monitor usage**: Regularly check bills and usage to plan resources efficiently  
4. **Utilize free quota**: The 20GB free storage quota can cover basic needs  

**Billing Query & Management**

- Log in to the console to view detailed billing and usage information  
- Bills can be queried by time, product type, and more  
- Clear expense analysis and trend charts are provided  

## Customer Service Commitment

We promise to provide you with:

- **Transparent billing**: All rules are public and transparent, with no hidden charges  
- **Accurate measurement**: Advanced billing system ensures precision  
- **Timely settlement**: Fees are settled punctually as promised  
- **Professional support**: Our support team is always ready to assist with billing questions  

Thank you for choosing our services! If you have any questions about billing rules, please contact the DaoCloud support team.  
