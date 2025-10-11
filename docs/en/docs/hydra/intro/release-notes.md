# LLM Studio Release Notes

This page lists the release notes for LLM Studio, helping you understand version evolution and feature changes.

*[hydra]: Internal codename for DaoCloud's LLM Studio

## 2025-08-07

### v0.8.0

**Admin Console**

* **Added** model list display
* **Added** support for bulk importing models from URL address information
* **Added** support for creating models
* **Added** MaaS model list display
* **Added** support for adding MaaS models
* **Added** support for adding multiple upstream endpoint configurations
* **Added** support for rate limiting at the **apikey** level
* **Added** support for rate limiting at the **Workspace** level
* **Added** support for defining multiple sets of rate-limiting rules
* **Added** support for **round-robin load balancing**
* **Added** model deployment management list display
* **Added** support for configuring multiple sets of model parameters
* **Added** support for deploying models with **vLLM**

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
