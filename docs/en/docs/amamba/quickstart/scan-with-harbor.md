# Integrate Harbor to scan image security

This page will introduce how to integrate Harbor in the pipeline and implement image security scanning.

## Enable automatic scanning of images in Harbor

1. Log in to Harbor and click on a specific project.

     <!--![]()screenshots-->

2. Select the `Configuration Management` tab, and check `Automatically scan images`.

     <!--![]()screenshots-->

## Configure the pipeline in Workbench

1. In Workbench, create a pipeline, refer to [Quickly create a pipeline](deploy-pipeline.md), and click `Run Now` after the configuration is complete.

     <!--![]()screenshots-->

1. In the pop-up dialog box, enter the address of the mirror warehouse in the above Harbor configuration project.

     <!--![]()screenshots-->

1. Wait for the pipeline to run successfully.

## View image security scan information in Harbor

Visit `Project` → `Mirror Warehouse` in turn in Harbor to view the vulnerability information of the mirror.

<!--![]()screenshots-->