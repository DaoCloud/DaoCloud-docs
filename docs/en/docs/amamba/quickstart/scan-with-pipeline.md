# Implementing Code Scanning with Pipelines

The source code in the code repository is the initial and raw form of software, and its security vulnerabilities are a direct root cause of software vulnerabilities. Therefore, analyzing and discovering security vulnerabilities in the source code through code scanning is an important method to reduce potential software vulnerabilities.

For example, SonarQube is an automated code review tool used to detect bugs and improve test coverage in project code. It can be integrated into existing workflows in the project to enable continuous code inspection between project branches and pull requests.

This article will explain how to integrate SonarQube into pipelines to implement code scanning capabilities.

## Integrating SonarQube into Workspaces

Ensure that you have a SonarQube environment and that it is properly connected to the current network environment.

1. Go to the __Toolchain Integration__ page and click the __Add Tool Integration__ button.


2. Configure the relevant parameters according to the following instructions:

    - Tool: Select a toolchain type for integration.
    - Integration Name: The name of the integrated tool, should not be duplicate.
    - SonarQube URL: The accessible URL of the toolchain, starting with http:// or https:// followed by a domain name or IP address.
    - Token: Generate an admin token (Token) in SonarQube. The operation path is: My Account -> Profile -> Security -> Generate -> Copy



3. Click __OK__ to complete the integration and return to the toolchain list page.

## Creating a Pipeline

1. On the Pipelines page, click __Create Pipeline__ .



2. Select __Custom Creation__ .



3. Enter a name and use default values for other fields, then click __OK__ .



## Editing Pipeline Steps

1. Click a pipeline to enter its details page, and click __Edit Pipeline__ in the upper right corner.



2. Configure global settings:



3. In the graphical interface, define Stage 1 __git clone__ with the following configuration:



4. In the graphical interface, define Stage 2 __SonarQube analysis__ with the following configuration:

    - SonarQube Instance: Select the previously integrated SonarQube instance.
    - Code Language: Different code languages correspond to different scanning commands in SonarQube. If it is Java language, select Maven; otherwise, choose other. For this example, we select "other".
    - Project: Define the project to be scanned in SonarQube.
    - Scan Files: Specify the directory address of the code repository to be scanned.


5. Save the changes and immediately run the pipeline, then wait for the pipeline to run successfully.

## Viewing Code Scanning Results

1. After the pipeline runs successfully, click __Code Quality Check__ on the pipeline details page.



2. View the code scanning results. Click __View More__ to go to the SonarQube backend for more scanning information.

