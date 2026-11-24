# Investment Payback Calculation

Investment payback calculation is an extended capability of the [Copilot Smart Workbench](./index.md) for compute investment planning. Through conversation, you can open the calculator, set the deployment plan, business workload, revenue and cost conditions, and calculate the one-time investment, annual revenue, annual net cash flow, and static payback period.

The calculator supports modifying all calculation parameters through conversation. Copilot syncs the changes to the form and recalculates. You can also adjust parameters directly in the UI to compare payback periods under different operating conditions.

## Start a Calculation Through Conversation

Describe your calculation needs in Copilot, for example:

!!! quote

    Open the investment payback calculator for me.

You can also state the initial conditions when making the request:

!!! quote

    Help me calculate the investment payback period of a compute project. Use the built-in reference plan first and calculate based on an average business workload of 50%.

After Copilot opens the calculator, you can choose a reference plan or customize the model, servers, and calculation parameters based on your actual project.

The calculator provides three built-in reference plans — GLM5.3 × H200, GLM5.2 × PPU (Zhenwu M890), and Kimi-K3 × B200 — based on actually verified data to help you start quickly. The operating conditions and costs of the project can be adjusted as needed.

## Adjust Parameters Through Conversation

During the calculation, you can continue to describe the conditions to adjust in conversation instead of searching form fields one by one. Parameters such as model and server configuration, deployment scale, throughput, business workload, Token price, operating time, and cost items can all be modified through conversation.

| Item to Adjust | Conversation Example |
| --- | --- |
| Business workload | Change the average business workload to 50%. |
| Pricing conditions | Adjust the actual pricing factor to 80%. |
| Deployment scale | Adjust the number of deployment units to 2. |
| Cost conditions | Change the rack and power fee to CNY 40,000 per month. |
| Multiple conditions | Set the average business workload to 50% and the actual pricing factor to 80%, then recalculate. |

Copilot updates the corresponding form parameters based on the conversation, recalculates, and refreshes the results. After the adjustment, you can view the current parameters and calculation details, continue modifying conditions, or ask why the results changed.

For example:

> The current business workload is only half. How does the payback period change?
>
> If the transaction price drops further, which costs have a greater impact on the payback period?

## View Calculation Results

The calculator provides three views — **Results Overview**, **Key Assumptions**, and **Professional Calculation** — for viewing conclusions, adjusting the main conditions, and verifying the full parameters respectively.

### Results Overview

**Results Overview** shows the main conditions and calculation results of the current plan, helping you quickly understand the investment and payback situation.

| Content | Description |
| --- | --- |
| Current conditions | Average business workload, actual pricing factor, and deployment scale |
| Static payback period | Estimated number of years required to recover the one-time investment under the current revenue and cost conditions |
| Annual net cash flow | Annual revenue minus annual recurring costs |
| One-time investment | One-time expenses such as equipment and networking included in the current plan |
| Annual revenue | Annual revenue calculated based on throughput, business workload, operating time, and pricing conditions |

The page also provides three operating scenarios to compare the impact of changes in business volume and price:

| Scenario | Average Business Workload | Actual Pricing Factor |
| --- | --- | --- |
| Full load, full price | 100% | 100% |
| Half load, full price | 50% | 100% |
| Half load, half price | 50% | 50% |

Use **Adjust Key Assumptions** to enter the main parameter area, and **View Full Parameters** to enter the Professional Calculation view.

### Key Assumptions

The **Key Assumptions** view prioritizes the main parameters that affect the results, suitable for quick adjustments and observation of payback period changes.

- **Average business workload**: Converts the reference capacity into the estimated business volume.
- **Actual pricing factor**: Adjusts the pricing level relative to the baseline Token price.
- **Number of deployment units**: Sets the deployment scale of the project.
- **More operating assumptions**: Expand to adjust the Token price and operating time.

You can modify the parameters directly in the UI or continue adjusting them through conversation. When finished, return to Results Overview or enter Professional Calculation to view the detailed configuration.

### Professional Calculation

The **Professional Calculation** view is used to set and verify the deployment, revenue, and cost conditions, while viewing the results and itemized details of the current plan.

| Parameter Category | Main Content |
| --- | --- |
| Deployment plan | Model, server type, number of deployment units, number of servers, GPUs per server, and throughput |
| Revenue calculation | Revenue calculation method, estimated throughput, business workload, standard input price, cached input price, output price, and operating time |
| Cost calculation | Cost mode, equipment and networking, software licenses and services, labor and equipment maintenance, data center and utilities, taxes, and other expenses |

Cost mode supports **Monthly equipment rental**, **Self-purchased equipment with rented racks**, and **Land purchase and construction**. You can adjust expenses based on the actual project, choose whether an expense item is included, or add or delete expense fields.

The results area shows the composition of annual revenue, one-time investment, and annual costs, helping you verify the calculation basis of revenue and expenses. All calculation parameters can be modified through conversation and are synchronously reflected in the form and results.

## Export Calculation Results

After confirming the current plan and parameters, click **Export Excel** in the results area to export the calculation results for plan discussion, internal review, or further analysis.

## Calculation Methodology

The calculator measures the payback period using the static payback period, based on the following relationships:

> Annual net cash flow = Annual revenue − Annual recurring costs
>
> Static payback period (years) = One-time investment ÷ Annual net cash flow

When the annual net cash flow is not positive, the current conditions show "Not recoverable" and no payback years are provided.

Reference plans provide a starting point for calculation; the final result depends on the business workload, actual pricing, operating time, and cost settings. The values in the screenshots only represent calculation examples under the corresponding parameters. When using the calculator, adjust based on the actual project conditions and verify that all expenses are fully included.
