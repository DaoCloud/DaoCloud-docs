# Alert Silence

Alert silence is a feature that allows alerts meeting certain criteria to be temporarily disabled from sending notifications within a specific time range. This feature helps operations personnel avoid receiving too many noisy alerts during certain operations or events, while also allowing for more precise handling of real issues that need to be addressed.

On the Alert Silence page, users can see two tabs: Active Rules and Expired Rules. Active rules represent the rules currently in effect, while expired rules are those that were defined in the past but have now expired (or have been deleted by the user).

## Creating a Silent Rule

1. In the left navigation bar, select __Alert Center__ -> __Alert Silence__ , and click the __New silence rule__ button.

    ![click button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/silent01.png)

2. Fill in the parameters for the silent rule, such as cluster, namespace, tags, and time, to define the scope and effective time of the rule, and then click __OK__ .

    ![silent rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/silent02.png)

3. Return to the rule list, and on the right side of the list, click __┇__ to edit or delete a silent rule.

Through the Alert Silence feature, you can flexibly control which alerts should be ignored and when they should be effective, thereby improving operational efficiency and reducing the possibility of false alerts.
