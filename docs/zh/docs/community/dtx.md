# DataTunerX

![DTX Logo](https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/logo/Logo_DataTunerX%20-%20Horizontal%20-%20Color%20Light.png#gh-dark-mode-only)
![DTX Logo](https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/logo/Logo_DataTunerX%20-%20Horizontal%20-%20Color%20Dark.png#gh-light-mode-only)

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)
![release](https://img.shields.io/badge/version-0.1.0-blue)
![fine-tuning](https://img.shields.io/badge/fine--tuning-8B3E3)

**DataTunerX（DTX）** 设计为与分布式计算框架集成的云原生解决方案。利用可扩展的 **GPU** 资源，它是一个专为高效微调 **LLMs** 而构建的平台，重点放在实用性上。其核心优势在于促进批量微调任务，使用户能够在单个 **实验** 中同时进行多个任务。 **DTX** 包含了数据集管理、超参数控制、微调工作流、模型管理、模型评估、模型比较推断和模块化插件系统等基本功能。

**技术栈** ：

**DTX** 基于云原生原则构建，采用包含不同 **自定义资源定义（CRDs）** 和 **控制器** 逻辑的各种[运算符](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-operator)。主要使用 **Go** 进行开发，实现利用[operator-sdk](https://github.com/operator-framework/operator-sdk)工具包。在[Kubernetes（K8s）](https://github.com/kubernetes/kubernetes)环境中运行， **DTX** 依赖于 **CRD** 开发和管理的运算符模式。此外， **DTX** 与[kuberay](https://github.com/ray-project/kuberay)集成，以利用分布式执行和推断能力。

**状态** ：

**v0.1.0** - 早期开发阶段。有关最近更新的详细信息，请参阅[CHANGELOG](CHANGELOG.md)。

**快速演示和更多文档** ：

- 演示

    <div align="center">
          <a href="https://www.youtube.com/watch?v=NvOzKj67oRQ">
            <img src="https://img.youtube.com/vi/NvOzKj67oRQ/maxresdefault.jpg" style="width:50%;">
          </a>
    </div>

- [文档](https://github.com/DataTunerX/datatunerx-controller)（即将推出）

    **屏幕截图** ：

    ![DTX屏幕截图](https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/screenshot/Job_Details.png)

## DTX 能做什么？ 💪

**DTX** 为用户提供了一套功能强大的功能，旨在高效微调大型语言模型。了解使 **DTX** 成为一个多功能平台的功能：

### 数据集管理 🗄️

通过支持 **S3** 协议（ **http** 即将推出）和本地数据集上传，轻松管理数据集。数据集以测试、验证和训练等拆分方式组织。此外，特征映射增强了微调作业的灵活性。

<div align="center">
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/datasetplugindark.png" alt="FineTune" width="30%" height="30%" />
</div>

### 微调实验 🧪

通过创建多个微调作业进行微调实验。每个作业可以使用不同的 llms、数据集和超参数。通过实验的评估单元对微调模型进行统一评估，以识别微调结果。

<div align="center">
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/finetunedark.png" alt="FineTune" width="30%" />
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/finetunejobdark.png" alt="FineTuneJob" width="30%" />
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/finetuneexdark.png" alt="FineTuneExperiment" width="30%" />
</div>

### 作业洞察 📊

深入了解实验中每个微调作业。探索作业详细信息、日志和度量可视化，包括学习率趋势、训练损失等。

### 模型存储库 🗃️

将 LLMs 存储在模型存储库中，便于有效管理和部署推断服务。

<div align="center">
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/evaldark.png" alt="FineTune" width="50%" height="70%" />
</div>

### 超参数组管理 🧰

利用丰富的参数配置系统，支持多样化的参数和基于模板的区分。

## 推断服务 🚀

部署多个模型的推断服务，便于直观比较和选择表现最佳的模型。

## 插件系统 🧩

利用数据集和评估单元的插件系统，使用户能够集成专门的数据集和评估方法，以满足其独特需求。

## 更多即将推出 🤹‍♀️

**DTX** 提供了一套全面的工具，确保您在微调任务过程中能够灵活和高效地使用功能。探索每个功能，根据您的特定需求定制微调任务。

## 为什么选择 DTX？ 🤔

**DTX** 是微调大型语言模型的首选选择，提供独特的优势，解决自然语言处理中的关键挑战：

### 优化资源利用 🚀

**高效 GPU 集成：** 与分布式计算框架无缝集成，确保在资源受限环境中充分利用可扩展的 GPU 资源。

### 流畅批量微调 🔄

**并发任务执行：** 擅长批量微调，能够同时执行多个任务，增强工作流效率和整体生产力。

<div align="center">
  <img src="https://raw.githubusercontent.com/DataTunerX/datatunerx-controller/main/assets/design/batchdark.png" alt="FineTuneExperiment" width="60%" />
</div>

### 丰富的功能集满足各种需求 🧰

**多样能力：** 从数据集管理到模型管理， **DTX** 提供了一套全面的功能集，满足多样化的微调需求。

### 简化实验降低门槛 🧪

**用户友好的实验：** 让用户轻松进行拥有不同模型、数据集和超参数的微调实验。这降低了对具有不同技能水平的用户的入门门槛。

总之， **DTX** 在资源优化、数据管理、工作流效率和可访问性等方面有针对性地解决了挑战，使其成为高效自然语言处理任务的理想解决方案。

## 参考资料 🙌

- [GitHub 上的 DataTunerX 存储库](https://github.com/DataTunerX/datatunerx)
- [Ray 项目](https://ray.io/)：一个开源的分布式计算框架，可以轻松扩展和并行化应用程序。
- [KubeRay](https://github.com/kuberay/kuberay)：Ray 与 Kubernetes 的集成，实现在 Kubernetes 集群上高效的分布式计算。
- [Operator SDK](https://sdk.operatorframework.io/)：用于构建 Kubernetes 运算符的工具包，这些运算符是自动化管理 Kubernetes 集群中自定义资源的应用程序。
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)：一个易于使用的 llm 微调框架。

欢迎探索这些项目，深入了解可能影响或启发本项目的技术和概念。
