---
hide:
  - toc
---

# What Is LLM Studio

LLM Studio is a comprehensive AI model management solution designed for enterprise users. It addresses key challenges enterprises face when adopting large models, such as deployment complexity, model selection difficulties, stability issues, and potential security risks. By offering end-to-end lifecycle services—from model deployment to operational management—the platform helps enterprises and developers efficiently integrate and utilize large-scale AI capabilities, accelerating digital transformation and intelligent innovation.

**Key Features**

- One-Click Deployment and Simplified Operations

    - Dual Support for GUI and API: Offers an intuitive web interface and complete API endpoints
    - One-Click Model Deployment: Supports mainstream large models to go live within minutes
    - Dynamic Inference Backends: Compatible with multiple inference engines such as vLLM and SGLang
    - Real-Time Scaling: Flexibly adjust the number of instances based on business needs
    - Multi-Region Deployment: Choose deployment regions on demand for local services

- Traffic Management and Stability Assurance
    
    - Intelligent Traffic Strategy Engine: Multi-dimensional control based on weights, QPS limits, and more
    - Multi-Layer Rate Limiting:
        - Global Limiting: Controls overall platform load
        - API Key Limiting: Fine-grained control of access frequency per application
        - Tenant-Level Limiting: Independent traffic control for enterprise users
 
- Distributed Inference Capabilities

    - Multi-Node, Multi-GPU Deployment: Supports ultra-large parameter models such as DeepSeek and GLM
    - Heterogeneous GPU Support: Compatible with NVIDIA, Biren, Muxi, Ascend, and other GPUs
    - Load Balancing Strategies:
        - Round Robin: Even traffic distribution
        - Random: Quickly disperses requests
        - Weighted: Allocates traffic based on weights

- Accurate Billing and Statistics

    - Token-Level Accounting: Supports billing logic for mainstream large models
    - Multi-Dimensional Analytics:
        - Total calls, input/output token counts
        - Filters by API key, model type, and time

- Unified Multimodal Management

    - Model Marketplace: Showcases models for text, images, and more
    - Model Comparison Experience: Input once, receive responses from multiple models for comparison
    - API Call Examples: Provides rich demos and integration guides

## Standard View and Operations Management Logic

The platform enables unified management, trial, and rapid deployment of models through a combination of the “Operations Management View + Standard User View.” As shown below, the model usage process consists of **three steps + model file download**.

<!-- ![Platform Usage Process](../intro/images/OperationalLogic.png) -->

### 1️⃣ Model Marketplace Management: Add and Publish Models

- **Operations Management**:
    - Import or create models in **Model Marketplace Management**.
    - Once published, models are automatically synchronized to the user view.
- **Standard User View**:
    - Browse published models in the **Model Marketplace**, serving as the entry point for trials or deployments.

### 2️⃣ MaaS Model Management: Configure Model Trial Services

- **Operations Management**:
    - Set a model as a **MaaS model** and configure its trial runtime environment.
- **Standard User View**:
    - Access the **Model Trial** section to test configured models online without local deployment.

### 3️⃣ Model Deployment Management: Configure Deployment Parameters

- **Operations Management**:
    - Create deployment configuration files for resources and environments (e.g., GPU, memory, runtime framework) in **Model Deployment Management**.
- **Standard User View**:
    - Quickly complete deployment by selecting a model in the **Model Deployment** page.
    - Simplifies workflows without requiring manual input of complex parameters.
  
### 4️⃣ Model File Download: Foundation for Deployment

- Operations staff need to download model files to designated locations.
