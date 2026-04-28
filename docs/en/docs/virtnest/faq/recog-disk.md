# Windows VM New Disk Not Recognized Issue

When adding a new disk through KubeVirt on a newly installed Windows Server, the disk cannot be recognized. You need to install virtio drivers following these steps:

1. Download stable virtio-win iso

    Download address:
    https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md

    ![img](./images/recog01.png)

1. Install virtio-win iso

    After mounting the iso image, click virtio-win-gt-x64 to install. After installation, you can see the added disk

    ![img](./images/recog02.png)

1. Effect after adding disk

    ![img](./images/recog03.png)
