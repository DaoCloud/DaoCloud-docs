# Platform engineering, API platforms and intelligent agents dominate innovation at KubeCon Paris

> GUEST COLUMN BY JASON BLOOMBERG from [siliconangle.com](https://siliconangle.com/2024/03/23/platform-engineering-api-platforms-intelligent-agents-dominate-innovation-kubecon-paris/)

The sizzle at this past week’s [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)
in Paris was all about Kubernetes-based infrastructure for generative artificial intelligence. The steak, in contrast, was all about platforms.

I attend conferences such as KubeCon to uncover particularly innovative vendors who are pushing the boundaries of their respective technologies.
Since is my seventh article for SiliconANGLE covering this flagship open-source conference, my goal was to uncover vendors I hadn’t spoken to before.

![Post of KubeCon EU](./images/KubeConEU1.jpg)

Here are six such innovators – plus one former client whose recent acquisition makes them deserving of inclusion on this exclusive list.

## Next-generation observability with intelligent agents

Observability is all about the data, and wherever you find data these days, you find large language models or LLMs,
the technology behind generative AI.

Most observability vendors are slapping LLMs on their solutions to give them natural language chat interfaces –
useful, but not particularly revolutionary.

[Robusta Dev Ltd.](https://home.robusta.dev/), in contrast, uses LLMs to implement observability-based intelligent agents:
autonomous pieces of software that can not only uncover root causes of operational issues, but also take action to remediate them.

Robusta’s agents approach their tasks iteratively, adjusting dynamically to shifting data.
As a result, Robusta is particularly well-suited to resolving issues in dynamic cloud native deployments.

## Internal developer platforms: Two Extremes

Platform engineering was a hot topic at KubeCon, second only to AI on the buzz meter.
Vendors support enterprise platform engineering efforts with internal developer platforms.
What an IDP product offering actually looks like, however, can vary dramatically from one vendor to another.

The central question: How opinionated should the IDP on offer be? Is it better to let the customer decide
the best way to build and use their IDP, or should the IDP vendor instill best practices into the platform?

At one extreme: [MIA srl](https://mia-platform.eu/), aka Mia-Platform. Mia-Platform offers a platform for
building IDPs, empowering platform engineers to choose from a multitude of open-source or commercial tools
when constructing their own IDPs.

Mia then focuses on providing a consistent user interface, streamlining the developer experience across the software lifecycle.
Mia’s flexibility enables platform engineering teams to incorporate legacy tooling as they modernize their infrastructure to cloud native.

At the opposite extreme is [Kapeta Inc](https://kapeta.com/). Kapeta sells an opinionated IDP – prebuilt for quick deployment.
Given other IDPs can take years to deploy, this highly opinionated approach has obvious advantages.
Unlike less opinionated offerings, Kapeta offers rapid time-to-value.

Once platform engineers have deployed the Kapeta platform, they can tweak the tools it connects to via Kapeta’s plugin architecture.
Kapeta is thus able to balance the value of an opinionated IDP with the flexibility necessary to adjust it to each customer’s needs.

## Enterprise Kubernetes platform for days 0, 1 and 2

Day 0 refers to the planning phase of cloud-native infrastructure deployment.
Given the complexity of the Kubernetes ecosystem, simply coming up with a plan of attack is an onerous task.

Day 1 means the initial deployment of Kubernetes and all its associated add-ons,
while day 2 refers to full production of multiple Kubernetes clusters, often in hybrid multicloud environments.

Few vendors other than long-term market incumbents have the wherewithal to support all three days.
[DaoCloud Network Technology Co. Ltd.](https://www.daocloud.io/en/), however, has plunged into the deep end.

DaoCloud offers a layered enterprise Kubernetes platform solution. It provides a day 0 platform that
adds an app store and application delivery capabilities to its cloud-native community edition foundation.
These capabilities include CI/CD pipelines and GitOps support.

On top of this day 0 offering, DaoCloud’s advanced offering adds microservice governance and observability.
The full enterprise premium edition layers on multicloud orchestration and real-time data services.

The result is an end-to-end cloud native platform that can meet the needs of the most complex of enterprise scenarios.

## Next-generation API platforms featuring GraphQL support

Earlier generations of application programming interface gateways and management platforms handle the
security and availability of APIs on an individual basis, leaving it up to the developer of the
consuming application to know which APIs to access and when.

The current generation leverages the power of GraphQL to combine APIs, connecting them to a data graph that
enables the front-end developer to specify the data they want rather than the specific API.

[Tyk Technologies Ltd.](https://tyk.io/) offers a universal data graph that unifies multiple APIs into
a single GraphQL API endpoint. Tyk provides both an API gateway as well as a developer portal,
leveraging an all open-source technology base to deliver high-performance API capabilities.

[Apollo Graph Inc.](https://www.apollographql.com/) also leverages GraphQL to implement JOIN-like combinations of APIs.
They offer a query planner that works in an analogous way to traditional relational database SQL interpreters,
giving developers the ability to build business-centric APIs that abstract the underlying application endpoints.

Via this abstraction, Apollo gives front-end developers the ability to maintain the business context of
underlying data without the need to deal with the protocols or parameters of the back-end APIs.

## Environment-centric approach to the Kubernetes application lifecycle

I worked briefly with [Octopus Deploy Pty. Ltd.](https://octopus.com/) in its early startup days,
but the company has come so far in the intervening years that it deserves a spot in this article.

The vendor’s most recent news is its acquisition of [CodeFresh, Inc.](https://codefresh.io/),
the purveyor of a leading CI/CD platform and the champion of the popular Argo open-source CD tool.

Octopus Deploy places CI/CD into the context of individual environments, for example dev, staging and production.
Each of these environments might comprise elements in different clouds, perhaps incorporating different infrastructure components or Kubernetes clusters.

It abstracts out all such details, giving developers and DevOps engineers the ability to move workloads
from one environment to another without having to worry about the messy details.
Rolling back to a previous environment is also dead simple with Octopus.

Octopus supports other environments for other situations, for example, edge computing.
On the edge, companies may define specific environments by geography (“push this code to California”)
or by business context (“push this code to all refineries”).

## Kubernetes has crossed the chasm

Management thought leader Geoffrey Moore famously described the chasm between early adopters and the early majority users of a given technology.
Early adopters are willing to try immature technologies to obtain early-mover advantages.
The early majority, in contrast, simply want to get their jobs done.

The 12,000-strong crowd at KubeCon was generally more interested in solving their business problems than
worrying about being early movers, a clear sign that Kubernetes — and the more mature components of its ecosystem —
have reached early-majority status.

For innovators such as the vendors in this article, this chasm crossing raises the bar.
Offerings must clearly address recognized enterprise challenges or buyers won’t bite. It’s time to get down to business.

_Jason Bloomberg is managing director of Intellyx. (Disclosure: Octopus Deploy is a former Intellyx customer. None of the other organizations mentioned in this article is an Intellyx customer. The CNCF covered the author’s travel expenses at KubeCon, a standard industry practice.)_

> Photo: Mark Albertson/SiliconANGLE
