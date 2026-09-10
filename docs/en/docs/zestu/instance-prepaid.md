# Annual & Monthly Container Instances

Annual and monthly container instances are a prepaid subscription model for computing resources, designed to provide a cost-effective solution for users who need long-term, reliable GPU power.  
With this billing method, you pay upfront and enjoy lower rates compared to pay-as-you-go, while guaranteeing that the GPU resources you need are always available.

This model is ideal for:

- **Long-term project development**: Continuous AI research, model training, and other projects that require steady compute power.  
- **Production deployments**: Mission-critical services and applications that need to run 24/7 without interruption.  
- **Cost-conscious usage**: Save money with prepaid subscriptions and get the best value for your GPU resources.  
- **Guaranteed resources**: Ensure that key workloads always have the GPU capacity they need, avoiding downtime due to resource shortages.

Unlike pay-as-you-go instances, annual and monthly instances retain GPU resources even when powered off. You can restart them instantly without waiting for allocation.  
Plus, d.run offers flexible auto-renewal and management features to help you optimize both cost and resource usage.

## Prerequisites

- A d.run account.  
- An account balance that covers the total cost of your chosen subscription.  
- A clear understanding of your GPU resource and configuration needs.

## How to Subscribe

1. Log in to d.run and go to **Compute Cloud**. By default, you’ll land in the **Compute Marketplace**, where **Annual/Monthly** billing is available.  
   Choose the GPU type you need and click **Buy Now**; or switch to **Container Instances** and click **Create**.



2. On the container instance creation page, set **Billing Type** to **Annual/Monthly**.  
   Configure subscription details and fill out instance info (name, region, resource type, image, etc.), then click **Confirm** to finish.



!!! note

    For full details on other instance options like region, resource type, system disk, storage, image, and access tools, see the [Create Container Instance](./instance.md) guide.

## Subscription Options

When selecting annual/monthly billing, configure the following:

| Option | Description |
| ------ | ----------- |
| Subscription Duration | Choose 1–12 months. The system will show applicable discounts—longer subscriptions usually save more. |
| Auto-Renewal Mode | Three options at expiration:<br/>- **Auto-renew (Annual/Monthly)**: Automatically renew at the same rate.<br/>- **Shut down on expiration**: Stops the instance and billing.<br/>- **Switch to Pay-as-You-Go**: Automatically converts the instance to pay-as-you-go. |
| Renewal Duration | If auto-renew is selected, configure how many months to renew (1–12). |

!!! tip

    - Longer subscriptions usually mean bigger discounts, perfect for ongoing workloads.  
    - Pick a subscription duration aligned with your project to avoid wasted resources or frequent renewals.  
    - Auto-renewal settings can be updated anytime after creation for flexibility.

## Managing Your Annual/Monthly Instance

### Change Auto-Renewal Mode

After creating an instance, you can update the auto-renewal mode at any time:

1. Go to **Compute Cloud** -> **Container Instances** and locate your instance.  
2. Click the instance menu and select **Change Renewal Mode**.  
3. Adjust the renewal type and duration as needed.


### Release Instance

You can release an instance early, and the system will automatically calculate your refund:

- **Refund Calculation**: Pro-rated based on remaining time.  
- **Service Fee**: Early refunds incur a small fee.  
- **Refund Method**: Returned automatically to your account wallet.


### Shutdown & Resource Guarantee

Shutting down annual/monthly instances works differently from pay-as-you-go:

- **Resources Reserved**: GPU resources remain reserved for instant restart.  
- **Billing**: Subscription fees continue while shut down.  
- **Quick Start**: Instantly restart without waiting for resource allocation.

## Renewal Process

For instances set to **Auto-renew (Annual/Monthly)**, the platform ensures uninterrupted service by renewing ahead of time.

### Timing

- **Advance Charge**: Attempts auto-deduction 7 days before expiration.  
- **Daily Retry**: From 7 days out, daily attempts are made according to your renewal settings.  
- **Multiple Safeguards**: Ensures services aren’t interrupted due to temporary low balance.

### Handling Success & Failure

**Success**:

- Automatically renews according to your settings.  
- Instance continues running without manual intervention.  
- System sends a renewal confirmation.

**Failure**:

- If deduction fails for 7 consecutive days, the instance will automatically shut down on expiration.  
- Billing stops but configuration is retained temporarily.  
- You can restart the instance manually after topping up your account, choosing to continue annual/monthly or switch to pay-as-you-go.

!!! warning

    - Annual/monthly instances bill continuously during the subscription.  
    - Ensure your account balance is sufficient to avoid auto-shutdown.  
    - Renewal mode can be updated anytime; changes apply from the next renewal.  
    - Releasing an instance is permanent—backup your data before proceeding.

## Notes

!!! note

    - Billing starts upon instance creation and continues until subscription ends or you release the instance.  
    - Shutdown does not stop billing but keeps resources reserved for instant restart.  
    - Early release refunds are proportional to remaining time minus a small service fee.

For assistance, contact our support hotline: **1-400-002-6898**
