# Building, Operating, and Contributing to Open Source Documentation

This article introduces common methods for building open source sites, operational strategies, and experiences in attracting contributors.

## DaoCloud’s Self-Hosted and Donated Open Source Sites

This section lists some of DaoCloud’s open source projects and sites, both self-hosted and donated to the community.

### Self-Hosted Products

DaoCloud’s main products currently include the cloud-native operating system DCE 5.0 and the compute management platform d.run.

| Site | Description | Generator | Build Method | Repo |
|-----|-----|-------|---------|----------|
| [DCE 5.0](https://docs.daocloud.io) | A high-performance, scalable cloud-native OS. Its documentation source is fully open source | mkdocs-material | cloudflare/wrangler-action@v3 | https://github.com/DaoCloud/DaoCloud-docs |
| [d.run](https://docs.d.run) | AIGC integrated compute management, large model services, and operations platform. Documentation source fully open | mkdocs-material | cloudflare/wrangler-action@v3 | https://github.com/d-run/drun-docs |

### CNCF Sandbox

DaoCloud has donated and contributed the following projects to CNCF Sandbox:

| Site | Description | Generator | Build Method | Repo |
|-----|-----|-------|---------|----------|
| [Clusterpedia](https://clusterpedia.io/) | A tool to easily query all resources in containerized clusters | Hugo | gh-pages | https://github.com/clusterpedia-io/website |
| [HAMi](https://project-hami.io/) | Middleware for compute virtualization, supporting multiple GPU architectures | Docusaurus 3 | gh-pages | https://github.com/Project-HAMi/website |
| [HwameiStor](https://hwameistor.io/) | A cloud-native local storage solution | Docusaurus | gh-pages | https://github.com/hwameistor/hwameistor |
| [Kubean](https://kubean-io.github.io/kubean/) | Kubernetes platform installation tool based on Kubespray | MkDocs | gh-pages | https://github.com/kubean-io/kubean |
| [Merbridge](https://merbridge.io/) | A tool using eBPF to accelerate service mesh | Hugo | gh-pages | https://github.com/merbridge/merbridge |
| [Piraeus](https://piraeus.io/) | A cloud-native data warehouse | mkdocs-material | gh-pages | https://github.com/piraeusdatastore/piraeus |
| [Spiderpool](https://spidernet-io.github.io/spiderpool/) | Underlay and RDMA networking solution built on Kubernetes | mkdocs-material | gh-pages | https://github.com/spidernet-io/spiderpool |

### Other Ongoing Open Source Sites

Sites that have been open sourced by DaoCloud and are still under development:

| Site | Description | Generator | Build Method | Repo |
|-----|-----|-------|---------|----------|
| [CloudTTY](https://cloudtty.github.io/cloudtty/) | Web-based command line tool | Not specified | gh-pages | https://github.com/cloudtty/cloudtty |
| [EgressGateway](https://spidernet-io.github.io/egressgateway/) | Provides fixed Egress IP solutions | mkdocs-material | gh-pages | https://github.com/spidernet-io/egressgateway |
| [kdoctor](https://kdoctor-io.github.io/kdoctor/) | Kubernetes data plane testing component to actively probe cluster functionality and performance | mkdocs-material | gh-pages | https://github.com/kdoctor-io/kdoctor |
| [KLTS](https://klts.io/) | Provides long-term support for Kubernetes versions outside the community’s latest four releases | Hugo | gh-pages | https://github.com/klts-io |

## Popular Community Open Source Sites

| Site | Description | Generator | Build Method | Repo |
|-----|-----|-------|---------|----------|
| [k/website](https://kubernetes.io/) | CNCF community cornerstone, the starting point for cloud-native | Hugo | Netlify | https://github.com/kubernetes/website |
| [istio.io](https://istio.io/) | Currently the most popular service mesh | Hugo | Netlify | https://github.com/istio/istio.io |
| [opentelemetry.io](https://opentelemetry.io/) | Open source toolkit for collecting and exporting observability data from distributed systems | Hugo | Netlify | https://github.com/open-telemetry/opentelemetry.io |
| [vLLM](https://docs.vllm.ai/en/latest/) | Efficient open source library to accelerate large language model inference | Sphinx | Read the Docs | https://github.com/vllm-project/vllm |
| [Pytorch](https://pytorch.org/) | Star 87k, widely used deep learning framework, known for dynamic computation graphs and usability | Hugo | Not specified | https://github.com/pytorch/pytorch |
| [huggingface](https://huggingface.co/) | Star 140k, aggregates large language models worldwide | Docusaurus | .github/workflows | https://github.com/huggingface/transformers |
| [KWOK](https://kwok.sigs.k8s.io/) | Simulated testing project donated to kubernetes-sigs by DaoCloud | Hugo | Netlify | https://github.com/kubernetes-sigs/kwok |
| [Kueue](https://kueue.sigs.k8s.io/) | Kubernetes-native Job queue manager jointly maintained by DaoCloud and kubernetes-sigs | Hugo | Netlify | https://github.com/kubernetes-sigs/kueue |
| [LWS](https://github.com/kubernetes-sigs/lws) | Jointly maintained with kubernetes-sigs, fully compatible with vLLM, SGLang, etc., one-click deploy enterprise AI services | None | Netlify | https://github.com/kubernetes-sigs/lws |

### Static Site Generator Comparison

Some of the static site generators mentioned above:

| Project | Stars | Language | Initial Release | Size | Repo |
|---------|-------|---------|----------------|------|------|
| **Hugo** | 78.1k | Go | 2014 | Ultra-lightweight, very fast | [Hugo repo](https://github.com/gohugoio/hugo) |
| **MkDocs** | 19.9k | Python | 2014 | Lightweight | [MkDocs repo](https://github.com/mkdocs/mkdocs) |
| **Docusaurus** | 58.4k | React | 2017 | Medium, React-based | [Docusaurus repo](https://github.com/facebook/docusaurus) |
| **Sphinx** | 6.8k | Python | 2008 | Medium, feature-rich | [Sphinx repo](https://github.com/sphinx-doc/sphinx) |

### Build Method Comparison

| Build Method | Advantages | Disadvantages |
|--------------|------------|---------------|
| **GitHub Pages** | ✅ Free hosting for open source <br> ✅ Deep integration with GitHub, auto-deploy <br> ✅ Supports Jekyll, can render Markdown directly | ❌ Static only, limited functionality <br> ❌ Custom domain HTTPS needs manual setup <br> ❌ Limited CI/CD capabilities |
| **Netlify** | ✅ Full CI/CD support, build, preview, deploy in one <br> ✅ Integrates with Git repos, supports multiple generators <br> ✅ Serverless functions for dynamic logic | ❌ Free tier limited, paid if over quota <br> ❌ Build logs can be minimal for complex debugging <br> ❌ Extra DNS configuration needed for edge features |
| **Cloudflare Pages** | ✅ Global CDN, ideal for users in China <br> ✅ Built-in DDoS protection, high security <br> ✅ Supports Pages Functions and Workers | ❌ Free tier limited, advanced features require subscription <br> ❌ Build/deploy process more complex than Netlify <br> ❌ Some third-party plugin compatibility issues |

### Common Bots in Open Source Projects

On GitHub, bots are widely used for automation, CI/CD, code quality, and release management. Common bots:

| Category | Bot | Purpose |
|----------|-----|--------|
| **Code Quality & Lint** | GitHub Actions Bots | Run `black`, `flake8`, `eslint`, `prettier` to maintain code style |
| | LGTM Bot | Analyze code quality, detect potential security issues |
| | Codecov Bot | Check test coverage and provide PR coverage reports |
| | Prettier Bot | Automatically format JS, Markdown, etc. |
| **PR & Issue Management** | k8s-ci-robot (Prow) | Auto-manage PRs and CI/CD for Kubernetes and CNCF projects |
| | Stale Bot (probot-stale) | Auto-close long-inactive Issues/PRs |
| | CLAassistant Bot | Verify contributor CLA signatures |
| | welcome Bot (probot-welcome) | Greet first-time contributors |
| **Release Management** | Release Drafter | Auto-generate release notes and categorize PRs |
| | Semantic Release | Automatically manage versions and releases from commits |
| | Dependabot | Detect dependency updates and open PRs |
| **Security & Dependency Management** | Snyk Bot | Scan dependencies for security vulnerabilities |
| | GitHub Security Bot (Security Alerts) | Alerts for security vulnerabilities and recommended fixes |

Most bots are based on GitHub Actions or Prow, improving automation, code quality, and security.

## Open Source Site Operations

Strategies to attract contributors:

- [Mentor programs](https://contribute.cncf.io/about/mentoring/) to train contributors
- Offer trial access to products like d.run for active contributors
- Annual external contributor awards with [badges](https://www.credly.com/users/michael-yao0422/) or trial incentives
- Regular online/offline open source events to engage contributors, share knowledge, and expand networks

Documentation is a key way to expand open source influence. See [2024 China Open Source Annual Report](./open-source-report.md#35-2024-10) and [Analysis of DaoCloud as China’s Enterprise Dark Horse 2024](./open-source-report.md#36-2024-openrank-10).

![DaoCloud ranked 5th nationwide](https://hackmd.io/_uploads/rkA0CtQU1g.png)

## Open Source Contributions

Contributions extend beyond code to documentation, testing, feedback, etc. Major ways to contribute:

### Documentation Contributions

| Type | Action |
|------|--------|
| New documentation | Review Issues and Release notes to identify documentation needs |
| Fix errors | Correct typos, formatting, or outdated info via PR |
| Improve readability | Add examples, improve phrasing, enhance Markdown formatting |
| Localization | Participate in i18n, contribute multi-language docs (e.g., Kubernetes, Istio SIGs) |

### Community Interaction

| Type | Action |
|------|--------|
| **Answer questions** | Help in GitHub Discussions, Slack, forums, WeChat; contribute FAQs |
| **Organize/attend events** | Participate in online/offline conferences (KubeCon, Open Source Summit); host meetups/workshops |

### Contribution Rewards

To incentivize contributors:

- **Badges**: e.g., CNCF contributor recognition
- **T-shirts & swag**: given to active contributors
- **Mentor programs**: guidance for newcomers
- **Early access**: trial quotas for services like d.run

### Getting Started

| Step | Description |
|------|-------------|
| Choose a project | Explore CNCF Landscape, GitHub Trending, find projects matching your stack |
| Read contribution guides | Follow `CONTRIBUTING.md` instructions |
| Join the community | Subscribe to mailing lists, Slack/Discord, attend meetings |
| Start small | Contribute docs or small bug fixes first |
| Continue contributing | Build reputation, become long-term contributor or Maintainer |

Open source contribution boosts skills, expands networks, and opens career opportunities. Join the community to advance technology together!

**Final Note:** Open source documentation sites not only extend enterprise influence but also promote product and doc improvement. Transparent environments allow direct feedback, drive updates, and encourage contributions, keeping docs timely and useful. Active sites strengthen community engagement, user retention, and a healthy tech ecosystem. Continuous updates aligned with industry trends ensure long-term product competitiveness and influence.
