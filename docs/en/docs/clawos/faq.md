# FAQ

## Will OpenClaw lose its memory due to instance issues?

**No**

Memory will not be lost whether you restart OpenClaw, pause the instance (feature coming soon), or release the instance.

This is because all data under `~/.openclaw` is persistently stored in the DCE storage system.

## Is my OpenClaw secure?

**Yes**

DaoCloud’s ClawOS is an enterprise-grade “AI agent platform”:

- Uses container technology as a secure sandbox for each agent  
- Leverages Kubernetes to ensure data security across compute, network, and storage layers  
- All data and conversations are processed through the DCE LLM platform, ensuring sensitive data protection  

## Can I upload files for OpenClaw to analyze?

**Absolutely**

You can do this in the following ways:

1. Send files to OpenClaw via Feishu chat  
2. Upload and manage files through the DCE file management interface  

## OpenClaw instance creation failed

Please check:

1. Whether real-name verification is completed  
2. Whether your account balance is greater than the selected resource price  

## Feishu integration not working

A single Feishu application can only be connected to one OpenClaw instance at a time.  

If you have multiple OpenClaw instances, each one must use a separate App ID and App Secret.
