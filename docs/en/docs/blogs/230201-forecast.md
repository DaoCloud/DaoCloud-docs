# 2023 Cloud Native Predictions

![Head image](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/forecast01.png)

> By Chris Aniszczyk

I hope everyone had a wonderful holiday with their loved ones! CNCF recently published an [annual report](https://www.cncf.io/reports/cncf-annual-report-2022/) on all the work we accomplished last year.
I encourage everyone to take the time to read this report carefully, as we have spent a lot of time documenting all the amazing work the community has done. Also, it's been a few years since I posted my annual forecast, so I apologize for the delay and hope you enjoyed this year's list!

## Cloud native IDEs become the norm

Recently, GitHub Codespaces completed beta, and while we don't have a lot of public usage data from GitHub,
But there seems to be a lot of positive sentiment on Twitter. Additionally, GitPod closed its Series A round alongside other companies in the space that have raised impressive funding rounds.

I am 100% confident that ephemeral development workspaces and the time developers save when setting up workspaces will drive this technology to become the industry norm.
There's a reason you see companies like Uber, Shopify, Slack, Stripe using this form of development, with Codespace and Gitpod
Once the product becomes the norm, these best practices will spread to the rest of the industry.

Finally, Gitpod compiled a set of excellent [CDE3 (Cloud Development Environment, Cloud Development Environment)](https://www.gitpod.io/cde) principles,
I suggest you take a look. My views were also shared by the wonderful folks at Redmonk who wrote about "[The Year of the Cloud Development Environment](https://redmonk.com/jgovernor/2022/12/01/the-year-of-the-cloud- development-environment/)", which I recommend reading from an analyst perspective.

## FinOps goes mainstream and shifts left

A few years ago, the Linux Foundation helped establish the [FinOps Foundation](https://www.finops.org/blog/linux-foundation),
to foster innovation in this field. The FinOps Foundation is off to a great start, hosting the first [FinOpsX](https://x.finops.org/)
Conference to Launch [The State of FinOps Survey](https://data.finops.org/), and some great [introduction material](https://www.edx.org/course/introduction-to-finops).

Why is this a big year for FinOps? Cloud spending has increased significantly over the past few years and is becoming a large cost within organizations, sometimes on par with wages.

Additionally, you can combine FinOps employment trends with [Google Trends](https://trends.google.com/trends/explore?date=today%205-y&q=finops) to find where economic growth has reached an inflection point index.

Another benefit of all this market pressure is more standardization and open source options like [OpenCost](https://www.opencost.io/).
Cracking your cloud bill has traditionally been a difficult problem, compounded if you use multiple clouds (there is no open standard for cloud pricing and cost management covering all major clouds).

These market pressures combined with the global recession will increase FinOps practices in most organizations, not just high-tech Bay Area companies.
FinOps will become a bigger engineering problem than in the past, when engineering teams had free reign over cloud consumption.
You will see FinOps information transfer to developers and eventually become part of the pull request infrastructure.

Finally, cost management and FinOps will be part of observability solutions by default (for example, Datadog
Announcing the launch of [Cost Management Product](https://www.datadoghq.com/about/latest-news/press-releases/datadog-introduces-cloud-cost-management/)).
I expect a lot of consolidation in this space as well, with large legacy players entering the space through acquisitions.

## Open Source SBOM Everywhere

The U.S. government has enacted policies and laws to improve software security over the past few years, from a 2021 executive order to the most recent "America's Protecting Open Source Software Act,"
Covers countless security improvements. OpenSSF (Open Source Security Foundation, Open Source Security Foundation) has a good summary of the act,
And their [mobilization plan](https://openssf.org/oss-security-mobilization-plan/) on how to address open source security.

Additionally, just recently, the U.S. government passed a law making it mandatory for medical device manufacturers to produce SBOMs.

Inevitably, this trend will continue and impact open source software, with leading key projects like Kubernetes already producing SBOMs for consumption.
There may be some bumps in the road to mandating SBOM across all industries, but I personally think it's inevitable either through regulation or when the industry just matures.

There will also be many new open source innovations, startups, and projects in this space working on aggregating large amounts of this security information (see https://deps.dev for a simple example).
The projects I personally pay attention to are [GUAC](https://github.com/guacsec/guac), [Scorecard](https://github.com/ossf/scorecard),
[Sigstore](https://www.sigstore.dev/), [Witness](https://github.com/testifysec/witness), etc.

## GreenOps merged into FinOps

Sustainability is a hot topic, and those in the ESG field know how complex calculating the carbon footprint of cloud-based workloads can be. A recent [research](https://www.pwc.com/us/en/tech-effect/cloud/esg.html) by PwC found that,
“Sixty percent of business leaders in Fortune 1000 companies are using or planning to use the cloud to enhance ESG reporting, and 59 percent are using or planning to use the cloud to improve their ESG strategy.”

I believe that as we increase the efficiency of the cloud, there will be a case of Jevons' paradox here...Also, interesting research suggests that "the energy required to run the computers of the future global fleet of self-driving cars may generate as much energy as As much greenhouse gas emissions as all data centers in the world today."

In my opinion, GreenOps is a form of FinOps that focuses on the carbon footprint of cloud workloads. It is my hope that these communities will merge into one and collaborate on open specifications and standards in the field,
For example [extending OpenCost](https://github.com/opencost/opencost/issues/1011) to include carbon footprint information across clouds. There are many opportunities for open source collaboration across companies and industries.

## GitOps is maturing and entering peak production

Since Alexis Richardson first coined the term GitOps in 2017, things have changed dramatically in this space when it comes to the maturity of GitOps tools.
At CNCF, the Argo and Flux projects [recently graduated](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529234&idx=1&sn=8baa2faf2de26366ba86ed56de129aef&scene=21#wechat_redirect),
Shows the project's stability and mature governance as well as rapid adoption levels. In addition, they are also CNCF
[The project with the highest open source speed] in the ecosystem (https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529664&idx=1&sn=fbd001427d06e607e50d182bed913071&scene=21#wechat_redirect).

If you are interested in this field, I recommend you to participate in the above open source projects and join the CNCF [Open GitOps Working Group](https://opengitops.dev/).

## OpenTelemetry maturing

If you look at the latest open source project velocity data from the CNCF,
[OpenTelemetry ranks second](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247529664&idx=1&sn=fbd001427d06e607e50d182bed913071&scene=21#wechat_redirect),
Second only to Kubernetes, which is unbelievable for such a young project.

Over the past few years, almost every major modern observability vendor has worked on integrating OTel.
The OTel collector framework frees providers from the need to implement this functionality and makes life better for end users.
In 2023, you will not only see [many technologically advanced companies](https://github.blog/2021-05-26-why-and-how-github-is-adopting-opentelemetry/) adopting OTel, but also See traditional enterprise end users taking advantage of this technology.

## Backstage Developer Portal Maturity

The developer experience has always been a concern for organizations reaching a certain scale to increase engineering throughput. As more and more organizations start their cloud native journey, this becomes very important for most industries.
In my previous set of [predictions](https://www.aniszczyk.org/2021/01/19/cloud-native-predictions-for-2021-and-beyond/), it was mentioned that the "service catalog" would becomes a necessity, but it will be more than that.

In the CNCF community, Backstage is one of the few projects I've seen deployed in traditional enterprises even before adopting Kubernetes.
It's a bit unique in that regard, but it's really been used by traditional businesses like banks or [airlines](https://backstage.spotify.com/blog/adopter-spotlight/american-airlines-runway/),
and used by cutting-edge tech companies like Spotify. You can download it from their [ADOPTERS.md](https://github.com/backstage/backstage/blob/master/ADOPTERS.md)
See some crazy adoption in the project in the docs and in the BackstageCon video.

To take it to the next level, Backstage needs to solidify its API and continue to cultivate its plugin ecosystem, essentially becoming the "Jenkins" of the space.

Another interesting thing about Backstage and modern developer portals is that Gartner has even taken notice and started doing research in this space, which is always a sign of later maturity.

## WebAssembly Innovation + Enlightenment Slope

I firmly believe that WebAssembly (Wasm) will become the dominant form of computing in the near future, and it is exploring use cases beyond the browser, from the edge to server workloads.
I found this [article](https://sapphireventures.com/blog/whats-up-with-webassembly-computes-next-paradigm-shift/) by Sapphire Ventures on Wasm promises to be one of the better ones on the topic one.
From personal experience, I keep seeing Wasm popping up in more areas for future cloud native ecosystems, from the refactoring of the plugin system in Envoy,
Or projects like WasmCloud and WasmEdge. Also, even [Docker](https://www.docker.com/blog/docker-wasm-technical-preview/) also supports Wasm in the recent technical preview.

However, as Wasm use cases are discovered, the runtime matures, and the technology fully develops, there will be some growing pains. In terms of the hype cycle,
Wasm will be somewhere between the trough of disillusionment and the slope of enlightenment. While there are many positive reports about the potential of Wasm, when there are many like [WASI](https://wasi.dev/)
Implementing these things is a reality to face when moving parts like tail calls and tail calls are not fully supported.

Additionally, I think you'll see boutique cloud providers like Cloudflare and smaller startups paving the way for the technology to mature, with hyperscalers starting to offer their first Wasm-related products this year.

Finally, I want to be clear, I see a world where containers, Wasm, and even VMs will co-exist...even as we do in Docker
My friend [said the same](https://www.docker.com/blog/why-containers-and-webassembly-work-well-together/).

## Cost cutting in favor of boutique cloud (or any "super cloud")

Continuing with this year's theme of cost management, I believe that as organizations take a step back to assess their cloud usage, boutique cloud providers
(or any [supercloud](https://blog.cloudflare.com/welcome-to-the-supercloud-and-developer-week-2022/)) will benefit from this trend.
For an example of this trend in 2023, see Cloudflare
A recent [announcement](https://www.prnewswire.com/news-releases/palantir-announces-strategic-partnership-with-cloudflare-focused-on-cloud-cost-optimization-301717292.html)…”
Palantir Announces Strategic Partnership With Cloudflare Focusing On Cloud Cost Optimization" And How They're Bringing It To
[R2](https://www.cloudflare.com/press-releases/2022/cloudflare-makes-r2-storage-available-to-all/) product compared to S3 product.

These boutique cloud providers will position themselves to focus on cost optimization and customer service in this particular area. They will announce new acquisitions and products in this space, competing with the larger cloud.

## Kubernetes Has Its Linux-Style Maturity Moment

I can't make cloud native predictions without mentioning Kubernetes, can I! ? Just recently, I published an article about [2022 open source project velocity](https://mp.weixin.qq.com/s/-AbkMXTPdERsW0OFNPwvyw) inside and outside the cloud native ecosystem
Also adopted Kubernetes. Also, Kubernetes is running on every [Chick-fil-A](https://medium.com/chick-fil-atech/enterprise-restaurant-compute-f5e2fd63d20f)
Restaurants, there's even some edge-based computing for you! There are even people running Kubernetes on [orbital](https://www.suse.com/success/hypergiant/), and even in [space](https://www.youtube.com/watch?v=Yk6wRsckroA)!

When I say that Kubenetes is going through its Linux-style maturity moment, I mean that Linux was originally built for a specific hobbyist use case,
Then eventually the broader ecosystem expands to run on phones, cars, real-time systems, and more. The Kubernetes project is going through a similar evolution, with organizations extending Kubernetes,
to run in new types of environments that the project was not originally designed for, such as embedded devices. These new use cases push innovation back into the Kubernetes project and the wider ecosystem,
Just like what happens in Linux. The engine of open source innovation is ready, and will continue to be.

## Other predictions

- Generative AI will be legislated and cause friction in the open source community. Interesting questions around attribution, copyright, and compliance with open source foundation and company policies will be interesting
   (For example, some companies have banned the use of code generated by CoPilot). We've also seen lawsuits against CoPilot and even art copyright and Stable Diffusion in this space,
   This will only accelerate and possibly lead to changes in some copyright laws. Heather Meeker has an article on [copyright eating AI](https://heathermeeker.com/2023/01/19/is-copyright-eating-ai/)
   Great blog post and I highly recommend it to readers.
- VSCode will continue to grow and dominate the IDE space. It's a very active project, and Microsoft has done a good job of managing the community so far.
   If you look at the Stackoverflow survey or Top IDE index data, VSCode will become the mainstream IDE for almost all major programming languages
   (Not even counting its embedded use in Codespaces and Gitpod).
- RISC-V will mature as an open source community and be widely used in embedded and mobile domains. Just recently, Google announced that Android plans to support RISC-V as a "Tier 1" architecture,
   This means that in the near future, you will see RISC-V in Android. There are also geopolitical headwinds around the world that favor RISC-V adoption in certain regions.
- Open source innovation in the game engine industry is booming. The gaming industry is a bit different than the cloud native world... most AAA style development still happens on Windows machines, huge
   monorepo and proprietary game engines like Unity and Unreal. As [a16z said in 2016](https://a16z.com/2016/06/01/open-source-gaming-vr/)…
   We need more open source in the game field, and this is finally realized with the emergence of open source game engines such as Bevy, Godot, [O3DE](https://o3de.org/).
- OSPO is growing in industry and government due to increased regulatory and security concerns. I'm one of the co-founders of the TODO Group,
   The organization is home to the Open Source Program Office (OSPO) network, which I've seen grow in the high-tech industry.
   As more and more of the software we rely on is based on open source, organizations will need a strategic approach to managing innovation and security risks.
   Furthermore, EU governments started to [regulate OSPO](https://openforumeurope.org/wp-content/uploads/2022/06/The-OSPO-A-New-Tool-for-Digital-Government-2.pdf), Other countries will follow suit.

## Finally, happy 2023 and good luck

I always have some more predictions and trends to share, especially around end-user driven open source, eBPF, service mesh and securing the software supply chain,
But I'll be posting more in detail later in the year, a few predictions are enough to start the new year! Anyway, thanks for reading,
I hope to see you all at [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/),
And of course our [Europe KubeCon + CloudNativeCon] in Amsterdam in April 2023 (https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)
Large conference, registration is open!

---

**DaoCloud Company Profile**

DaoCloud is an innovative leader in the field of cloud native. Founded at the end of 2014, it has core technologies with independent intellectual property rights and is committed to creating an open cloud operating system to empower digital transformation of enterprises.
Product capabilities cover the entire life cycle of cloud native application development, delivery, and operation and maintenance, and provide multiple delivery methods such as public cloud, private cloud, and hybrid cloud. Since its establishment, the company has been involved in financial technology, advanced manufacturing, smart cars,
Retail outlets, urban brain and other fields have been deeply cultivated. Benchmark customers include Bank of Communications, Shanghai Pudong Development Bank, SAIC Motor, Dongfeng Motor, Haier Group, Watsons, Golden Arches (McDonald's), etc.
At present, the company has completed the D round of financing exceeding 100 million yuan, and is known as a quasi-unicorn enterprise in the technology field. The company has set up a number of branches and joint ventures in Beijing, Nanjing, Wuhan, Shenzhen and Chengdu.
The total number of employees exceeds 400. It is a high-tech enterprise in Shanghai, a "little giant of science and technology" in Shanghai, and a "specialized and special new" enterprise in Shanghai, and has been selected into the list of enterprises cultivated by the Science and Technology Innovation Board.

URL: www.daocloud.io

Email: info@daocloud.io

Tel: 400 002 6898
