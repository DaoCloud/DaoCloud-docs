# Maintain ChatBot

!!! note

    This article is only suitable for administrators with permissions to maintain chatbots on websites like docs.d.run and docs.daocloud.io.

## Environment

Currently used maintenance environment:
https://console.d.run/dak

DAK administrator permissions are required.

## Maintain Corpus

1. Clone [docs-processor](https://gitlab.daocloud.cn/ats/drun-appstore/docs-processor) repository
1. Use the main.py script to process documentation site markdown data into CSV corpus recognizable by d.run.
   Currently there are 2 corpora:

    - daocloud-docs corresponds to docs.daocloud.io
    - d.run-docs corresponds to docs.d.run

    ![prepare csv](./images/chatbot01.png)

1. For example, click daocloud-docs, click **...** in the top right corner -> Format Import

    ![import](./images/chatbot02.png)

1. Import the prepared CSV file and complete the wizard steps in order.
