# Integrate Harbor to realize image security scanning

This article will introduce how to integrate Harbor in the pipeline and implement image security scanning.

## Enable automatic scanning of images in Harbor

1. Log in to Harbor and click on a specific project.

    

2. Select the `Configuration Management` tab, and check `Automatically scan images`.

    

## Configure the pipeline in the App Workbench

1. In the App Workbench, create a pipeline, refer to [Quickly create a pipeline](deploypipline.md), and click `Execute Now` after the configuration is complete.

    

1. In the pop-up dialog box, enter the address of the container registry in the above Harbor configuration project.

    

1. Wait for the pipeline to execute successfully.

## View image security scan information in Harbor

Visit `Project` → `container registry` in turn in Harbor to view the vulnerability information of the image.

