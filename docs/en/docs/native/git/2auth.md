# Enable Two-Factor Authentication on GitHub

To become a GitHub member, reviewer, approver, or owner of certain projects, besides signing the CLA,
your account needs to have two-factor authentication enabled.

## Enable Two-Factor Authentication

1. Log in to GitHub, click the dropdown arrow next to your avatar in the top right corner, and select __Settings__.

    ![Settings menu](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/2auth01.png)

2. Select __Password and authentication__ -> __Enable two-factor authentication__.

    ![Enable toggle](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/2auth02.png)

3. Select SMS authentication method.

    ![SMS authentication](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/2auth03.png)

4. Can't find China -_! Fortunately, there's always a solution. For example in Chrome, right-click on the current page, select __Inspect__ -> __Console__, and run the following command at the cursor:

    ```bash
    var option = new Option("China +86","+86");
    option.selected = true;
    document.getElementById('countrycode').options.add(option, 0);
    ```

5. Now +86 appears, enter your phone number, click __Send authentication code__, enter the six-digit code from SMS, and the screen will show 16 recovery codes.

    ![recovery code](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/native/knowledge/images/2auth04.png)
