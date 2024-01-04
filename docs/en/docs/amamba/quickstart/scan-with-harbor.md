# Integrate Harbor to scan image security

This page will introduce how to integrate Harbor in the pipeline and implement image security scanning.

## Enable automatic scanning of images in Harbor

1. Log in to Harbor and click a specific project.

     <!--![]()screenshots-->

2. Select the __Configuration Management__ tab, and check __Automatically scan images__ .

     <!--![]()screenshots-->

## Configure the pipeline in Workbench

1. In Workbench, create a pipeline, refer to [Quickly create a pipeline](deploy-pipeline.md), and click __Run Now__ after the configuration is complete.

     <!--![]()screenshots-->

1. In the pop-up dialog box, enter the address of the mirror warehouse in the above Harbor configuration project.

     <!--![]()screenshots-->

1. Wait for the pipeline to run successfully.

## View image security scan information in Harbor

Visit __Project__ → __Mirror Warehouse__ in turn in Harbor to view the vulnerability information of the mirror.

<!--![]()screenshots-->