# LLM Studio Release Notes

This page lists the release notes for LLM Studio, helping you understand version evolution and feature changes.

*[hydra]: Internal codename for DaoCloud's LLM Studio

## 2026-05-31

### v0.15.0

- **Added** support for large language model fine-tuning, including dataset management, fine-tuning job management, model evaluation, and model export
- **Added** pre-deployment health checks for model deployments, automatically validating critical hardware and software environments before deployment to identify issues in advance
- **Added** support for token weight configuration in model deployments and MaaS models to ensure fair token quota allocation
- **Added** support for enabling and disabling API Keys, allowing users to activate API Keys as needed
- **Added** support for accounting of cached tokens in large language models
- **Added** support for workspace token quota configuration in operations management, allowing users to set token limits for each workspace
- **Added** support for gateway security policy management and audit logs in operations management, allowing users to configure gateway security policies such as sensitive word detection and model allowlists/blocklists
- **Added** support for forwarding multimodal MaaS models, including speech-to-text, OCR, rerank, and embedding models
- **Improved** model marketplace management by adding support for model deletion

!!! note

    Starting from version 0.15.0, Hydra integrates Higress into the Knoway gateway to provide capabilities such as AI security and token quota management. For details, see the [Upgrade Notes](upgrade-notes.md).

## 2026-04-30

### v0.14.0

- **Added** support for API Key expiration settings
- **Added** support for API Key token quota settings
- **Improved** API Key management permissions, allowing each user to create and manage their own API Keys
- **Improved** model experience authentication to support only user-created API Keys
- **Improved** model deletion logic by adding validation for associated model services
- **Improved** model deployment templates by supporting custom GPU types and custom runtime logic for more flexible model deployment

## 2025-03-31

### v0.13.1

**User View**

- **Added** support for user private model management, including configuration of deployment templates and management of model weight files
- **Added** support for user-defined deployments, allowing modification of resource and runtime configurations during deployment
- **Added** support for priority and topology-aware queue scheduling in inference services
- **Added** support for user-defined runtime frameworks in inference services
- **Added** support for creating and managing file storage for persistent storage of model files, datasets, etc.

**Admin Console**

- **Added** file storage module for uploading and persistent storage of model weight files in the model hub
- **Added** UI-based management of model weight files in the model hub
- **Optimized** deployment configuration management by integrating it into model hub management, supporting multiple configuration templates

## 2025-11-30

### v0.12.1

**Admin Console**

- **Added** support for custom inference frameworks in model deployment management.

## 2025-10-31

### v0.11.0

**Admin Console**

- **Added** support for uploading model icons locally in the Model Marketplace.

## 2025-09-30

### v0.10.0

**Admin Console**

- **Added** support for deploying models using SGLang.
- **Added** support for viewing audit logs.

## 2025-08-07

### v0.8.0

**Admin Console**

- **Added** model list display
- **Added** support for bulk importing models from URL address information
- **Added** support for creating models
- **Added** MaaS model list display
- **Added** support for adding MaaS models
- **Added** support for adding multiple upstream endpoint configurations
- **Added** support for rate limiting at the **apikey** level
- **Added** support for rate limiting at the **Workspace** level
- **Added** support for defining multiple sets of rate-limiting rules
- **Added** support for **round-robin load balancing**
- **Added** model deployment management list display
- **Added** support for configuring multiple sets of model parameters
- **Added** support for deploying models with **vLLM**

## 2025-07-04

### v0.7.0

**User View**

- **Added** support for deep thinking in text models.
- **Added** support for copying and regenerating messages in text models.
- **Added** support for generating multiple images in vision-to-text models.
- **Added** support for custom positive and negative prompts, as well as custom image sizes in vision-to-text models.
- **Added** full compatibility with the standard OpenAI SDK.
- **Added** support for usage statistics by API Key, model type, and call time.
- **Added** quick summaries for total invocations, input tokens, and output tokens.
- **Added** support for usage comparison across multiple models.
- **Added** card view for displaying model lists with visual summaries.
- **Added** support for showing model details and API call examples.
- **Added** support for quick deployment and trial of text models.
- **Added** support for searching models by name, provider, and type.
- **Added** support for trialing multimodal models.
- **Added** support for trialing vision-to-text models.
- **Added** support for listing deployed model services.
- **Added** support for filtering models by type for quick deployment.
- **Added** support for scaling model service instances horizontally.
- **Added** support for configuring the number of model service instances.
- **Added** support for online trials of deployed model services.
- **Added** API call examples in curl, Python, and Node.js for deployed models.
- **Added** one-click trial feature for quickly verifying service availability.
- **Added** support for configuring parameters for text generation models, including system prompt, temperature, and top_p.
- **Added** support for comparison among models of the same type.
- **Added** support for displaying API Key lists.
- **Added** one-click copy for full API Keys.
- **Added** support for deleting specific API Keys irreversibly.
- **Added** support for generating new API Keys with custom names.
