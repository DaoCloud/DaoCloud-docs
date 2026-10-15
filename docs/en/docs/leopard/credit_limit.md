# Credit Limits

**Credit Limits** provide primary accounts with fine-grained control over the use of sub-account funds. By setting virtual wallet limits, a primary account can effectively isolate the budgets of different sub-accounts and prevent a single sub-account from over-consuming the overall balance of the primary account.

By default, sub-accounts share the real balance of the primary account. Once credit limits are enabled, a sub-account can only view and use the **virtual wallet balance** allocated to it. When the virtual balance reaches the preset threshold, the system triggers the corresponding service protection mechanism. When the virtual wallet charge of a sub-account turns from a positive value to a negative value, the system immediately sends an arrears notification SMS message to the phone number bound to that sub-account.

## Steps

1. In the **Credit Limits** list, you can view all sub-accounts with a limit policy configured and their running status.
    Click the account search box, and select or search for a specific sub-account in the drop-down list to locate it quickly.
    The table shows the sub-account name, available amount, and arrears protection status.

2. Click the **Create Credit Limit** button on the right side of the page, select the target sub-account,
    set the **Available Amount** (that is, the balance threshold that triggers service suspension, which can be set to a non-zero value),
    and configure **Stop Services When in Arrears**: when enabled, if the balance is lower than the limit, the running resources under that sub-account are forcibly stopped.

    ![limit](./images/createSub.png)

3. Click the **More (...)** icon on the far right of each row in the list to perform the following operations on an existing limit configuration:
    modify the **Available Amount**, adjust whether to **Stop Services When in Arrears**,
    or **delete** the policy — after deletion, the sub-account returns to the state of sharing the real balance of the primary account.

    ![limit](./images/subuser1.png)

### Fields

| Field | Description |
| --- | --- |
| Sub-account Name | The username of the sub-account for which the limit policy is set. |
| Available Amount | The balance threshold that the sub-account is allowed to consume. When the virtual balance reaches this value, the sub-account is considered in arrears. |
| Stop Services When in Arrears | A status switch. When enabled, arrears on the sub-account causes its related resources to be shut down automatically. |
