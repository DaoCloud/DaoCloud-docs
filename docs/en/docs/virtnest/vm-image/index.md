# Build Virtual Machine Images

This document will explain how to build the required virtual machine images.

A virtual machine image is essentially a replica file, which is a disk partition with an installed operating system. Common image file formats include raw, qcow2, vmdk, etc.

## Build an Image

Below are some detailed steps for building virtual machine images:

1. Download System Images

    Before building virtual machine images, you need to download the required system images. We recommend using images in qcow2, raw, or vmdk formats. You can visit the following links to get CentOS and Fedora images:

    - [CentOS Cloud Images](https://cloud.centos.org/centos/7/images/?C=M;O=D): Obtain CentOS images from the official CentOS project or other sources. Make sure to choose a version compatible with your virtualization platform.
    - [Fedora Cloud Images](https://fedoraproject.org/zh-Hans/cloud/download): Get images from the official Fedora project. Choose the appropriate version based on your requirements.

2. Build a Docker Image and Push it to a Container Image Repository

    In this step, we will use Docker to build an image and push it to a container image repository for easy deployment and usage when needed.

    - Create a Dockerfile

        ```Dockerfile
        FROM scratch
        ADD --chown=107:107 CentOS-7-x86_64-GenericCloud.qcow2 /disk/
        ```
        
        The Dockerfile above adds a file named `CentOS-7-x86_64-GenericCloud.qcow2` to the image being built from a scratch base image and places it in the __/disk/__ directory within the image. This operation includes the file in the image, allowing it to provide a CentOS 7 x86_64 operating system environment when used to create a virtual machine.

    - Build the Image

        ```shell
        docker build -t release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1 .
        ```
        
        The above command builds an image named `release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1` using the instructions in the Dockerfile. You can modify the image name according to your project requirements.

    - Push the Image to the Container Image Repository

        Use the following command to push the built image to the `release-ci.daocloud.io` image repository. You can modify the repository name and address as needed.

        ```shell
        docker push release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1
        ```

These are the detailed steps and instructions for building virtual machine images. By following these steps, you will be able to successfully build and push images for virtual machines to meet your usage needs.
