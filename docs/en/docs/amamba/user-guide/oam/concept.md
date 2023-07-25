# OAM Application Concept

The OAM (Open Application Model) application functionality is built on the open-source software [KubeVela](http://kubevela.net/en/docs/v1.2/), which abstracts and integrates Kubernetes resources as the top-level abstraction for application delivery.

An OAM application consists of one or more components and various operational actions, enabling standardized and efficient application delivery in a hybrid environment.

## Components

Components define the delivery and management form of an artifact or cloud service, and an application can include multiple components. It is recommended to have one main component (core business logic) and supplementary components (middleware with strong dependencies or dedicated operation components) in an application. For component type explanations, refer to the [Component Definition](http://kubevela.net/en/docs/v1.2/platform-engineers/oam/x-definition#component-definition).

Currently, the application dashboard in KubeVela comes with five built-in components: **Cron-Task, Daemon, K8s-Objects, Task, Webservice**. For specific parameter details of each component, refer to the [Built-in Component List](http://kubevela.net/en/docs/end-user/components/references).

## Traits

Traits are modular and pluggable operational capabilities that can be bound to deployable components at any time. Examples of operational traits include manual or automatic replica scaling, data persistence, setting gateway policies, and automatic DNS resolution. Users can obtain mature capabilities from the community or define their own traits.

Currently, the application dashboard in KubeVela comes with multiple built-in operational traits such as **Affinity, Annotations, Command, Container-Image, Cpuscaler**. For specific parameter details of operational traits, refer to the [Built-in Operational Traits List](http://kubevela.net/en/docs/end-user/traits/references).

## Customization

KubeVela allows for easy in-place customization and extension based on your requirements.

### Custom Components

The design goal of component definitions (ComponentDefinition) is to allow platform administrators to package any type of deployable artifact as a deliverable "component". Once defined, these types of components can be referenced, instantiated, and delivered by users in deployment plans (Applications).

For specific operations on custom components, refer to the official documentation: [Getting Started with Custom Components](http://kubevela.net/en/docs/v1.2/platform-engineers/components/custom-component).

### Custom Operational Traits

Trait definitions (TraitDefinition) provide a set of operational actions that can be selectively bound to components. These operational actions are usually provided by platform administrators as operational capabilities, providing a range of operations and strategies for the component, such as adding a load balancing strategy, routing strategy, or performing elastic scaling, blue-green deployment strategies, etc.

For specific operations on custom operational traits, refer to the official documentation: [Customize Operational Traits](http://kubevela.net/en/docs/v1.2/platform-engineers/traits/customize-trait).
