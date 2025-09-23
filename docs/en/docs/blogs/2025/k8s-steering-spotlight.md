# Spotlight on the Kubernetes Steering Committee

> Original from [k8s.dev](https://www.kubernetes.dev/blog/2025/09/22/k8s-steering-spotlight-2025/)

_This interview was conducted in August 2024, and due to the dynamic nature of the Steering
Committee membership and election process it might not represent the actual composition accurately.
The topics covered are, however, overwhelmingly relevant to understand its scope of work. As we
approach the Steering Committee elections, it provides useful insights into the workings of the
Committee._

The [Kubernetes Steering Committee](https://github.com/kubernetes/steering) is the backbone of the
Kubernetes project, ensuring that its vibrant community and governance structures operate smoothly
and effectively. While the technical brilliance of Kubernetes is often spotlighted through its
[Special Interest Groups (SIGs) and Working Groups (WGs)](https://github.com/kubernetes/community),
the unsung heroes quietly steering the ship are the members of the Steering Committee. They tackle
complex organizational challenges, empower contributors, and foster the thriving open source
ecosystem that Kubernetes is celebrated for.

But what does it really take to lead one of the world’s largest open source communities? What are
the hidden challenges, and what drives these individuals to dedicate their time and effort to such
an impactful role? In this exclusive conversation, we sit down with current Steering Committee (SC)
members --- Ben, Nabarun, Paco, Patrick, and Maciej --- to uncover the rewarding, and sometimes
demanding, realities of steering Kubernetes. From their personal journeys and motivations to the
committee’s vital responsibilities and future outlook, this Spotlight offers a rare
behind-the-scenes glimpse into the people who keep Kubernetes on course.

## Introductions

**Sandipan: Can you tell us a little bit about yourself?**

**Ben**: Hi, I’m [Benjamin Elder](https://www.linkedin.com/in/bentheelder/), also known as
BenTheElder. I started in Kubernetes as a Google Summer of Code student in 2015 and have been
working at Google in the space since 2017. I have contributed a lot to many areas but especially
build, CI, test tooling, etc. My favorite project so far was building
[KIND](https://kind.sigs.k8s.io/). I have been on the release team, a chair of [SIG
Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md), and currently a
tech lead of SIG Testing and [SIG K8s Infra](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md).

**Nabarun**: Hi, I am [Nabarun](https://www.linkedin.com/in/palnabarun/) from India. I have been
working on Kubernetes since 2019. I have been contributing across multiple areas in Kubernetes: [SIG
ContribEx](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md) (where I am
also a chair), [API
Machinery](https://github.com/kubernetes/community/blob/master/sig-k8s-infra/README.md),
[Architecture](https://github.com/kubernetes/community/blob/master/sig-architecture/README.md), and
[SIG Release](https://github.com/kubernetes/community/blob/master/sig-release/README.md), where I
contributed to several releases including being the Release Team Lead of [Kubernetes 1.21](https://kubernetes.io/blog/2021/04/08/kubernetes-1-21-release-announcement/).

**Paco**: I am [Paco](https://www.linkedin.com/in/pacoxu2020/) from China. I worked as an open
source team lead in DaoCloud, Shanghai. In the community, I participate mainly in
[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/),
[SIG Node](https://github.com/kubernetes/community/blob/master/sig-node/README.md) and [SIG
Testing](https://github.com/kubernetes/community/blob/master/sig-testing/README.md). Besides, I
helped in KCD China and was co-chair of the recent
[KubeCon+CloudNativeCon China 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-open-source-summit-ai-dev-china/)
in Hong Kong.

**Patrick**: Hello! I’m [Patrick](https://www.linkedin.com/in/patrickohly/). I’ve contributed to Kubernetes since 2018.
I started in [SIG Storage](https://github.com/kubernetes/community/blob/master/sig-storage/README.md) and then
got involved in more and more areas. Nowadays, I am a SIG Testing tech lead, logging infrastructure maintainer, organizer of the 
[Structured Logging](https://github.com/kubernetes/community/tree/master/wg-structured-logging) and 
[Device Management](https://github.com/kubernetes/community/tree/master/wg-device-management) working groups, contributor in 
[SIG Scheduling](https://github.com/kubernetes/community/blob/master/sig-scheduling/README.md), and of course member of the Steering Committee. 
My main focus area currently is 
[Dynamic Resource Allocation (DRA)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/), a new API for accelerators.

**Maciej**: Hey, my name is [Maciej](https://www.linkedin.com/in/maciejszulik/) and I've been working on Kubernetes
since late 2014 in various areas, including controllers, apiserver and kubectl. Aside from being part of the Steering Committee,
I’m also helping guide [SIG CLI](https://github.com/kubernetes/community/blob/master/sig-cli/README.md),
[SIG Apps](https://github.com/kubernetes/community/blob/master/sig-apps/README.md) and
[WG Batch](https://github.com/kubernetes/community/blob/master/wg-batch/README.md). 

## About the Steering Committee

**Sandipan: What does Steering do?**

**Ben:** The charter is the definitive answer, but I see Steering as helping resolve
Kubernetes-organization-level "people problems" (as opposed to technical problems), such as
clarifying project governance and liaising with the Cloud Native Computing Foundation (for example,
to request additional resources and support) and other CNCF projects.

**Maciej**: Our
[charter](https://github.com/kubernetes/steering/blob/main/charter.md#direct-responsibilities-of-the-steering-committee)
nicely describes all the responsibilities. In short, we make sure the project runs smoothly by
supporting our maintainers and contributors in their daily tasks.

**Patrick**: Ideally, we don’t do anything 😀 All of the day-to-day business has been delegated to
SIGs and WGs. Steering gets involved when something pops up where it isn’t obvious who should handle
it or when conflicts need to be resolved.

**Sandipan: And how is Steering different from SIGs?

**Ben**: From a governance perspective: Steering delegates all of the ownership of subprojects to
the SIGs and/or committees (_Security Response_, _Code Of Conduct_, etc.). They’re very different.
The SIGs own pieces of the project, and Steering handles some of the overarching people and policy
issues. You’ll find all of the software development, releasing, communications and documentation
work happening in the SIGs and committees.

**Maciej**: SIGs or WGs are primarily concerned with the technical direction of a particular area in
Kubernetes. Steering, on the other hand, is primarily concerned with ensuring all the SIGs, WGs, and
most importantly maintainers have everything they need to run the project smoothly. This includes
anything from ensuring financing of our CI systems, through governance structures and policies all
the way to supporting individual maintainers in various inquiries.

**Sandipan: You've mentioned projects, could you give us an example of a project Steering has worked
on recently?

**Ben**: We’ve been discussing the logistics to sync a better definition of the project’s official
maintainers to the CNCF, which are used, for example, to vote for the [Technical Oversight
Committee](https://www.cncf.io/people/technical-oversight-committee/) (TOC). Currently that list is
the Steering Committee, with SIG Contributor Experience and Infra + Release leads having access to
the CNCF service desk. This isn’t well standardized yet across CNCF projects but I think it’s
important.

**Maciej**: For the past year I’ve been sitting on the SC, I believe the majority of tasks we’ve
been involved in were around providing letters supporting visa applications. Also, like every year,
we’ve been helping all the SIGs and WGs with their annual reports.

**Patrick**: Apparently it has been a quiet year since Maciej and I joined the Steering Committee at
the end of 2023. That’s exactly how it should be.

**Sandipan: Do you have any examples of projects that came to Steering, which you then redirected to
SIGs?**

**Ben**: We often get requests for test/build related resources that we redirect to SIG K8s Infra +
SIG Testing, or more specifically about releasing for subprojects that we redirect to SIG K8s Infra
/ SIG Release.

## The road to the Steering Committee

**Sandipan: What motivated you to be part of the Steering Committee? What has your journey been
like?**

**Ben**: I had a few people reach out and prompt me to run, but I was motivated by my passion for
this community and the project. I think we have something really special going here and I care
deeply about the ongoing success. I’ve been involved in this space my whole career and while there’s
always rough edges, this community has been really supportive and I hope we can keep it that way.

**Paco**: After my journey to the [Kubernetes Contributor Summit EU
2023](https://www.kubernetes.dev/events/2023/kcseu/), I met and chatted with many maintainers and
members there, and attended the steering AMA there for the first time as there hadn’t been a
contributor summit in China since 2019, and I started to connect with contributors in China to make
it later the year. Through conversations at KCS EU and with local contributors, I realized that it
is quite important to make it easy to start a contributor journey for APAC contributors and want to
attract more contributors to the community. Then, I was elected just after the
[KCS CN 2023](https://www.kubernetes.dev/events/2023/kcscn/).

**Patrick**: I had done a lot of technical work, of which some affects and (hopefully) benefits all
contributors to Kubernetes (linting and testing) and users (better log output). I saw joining the
Steering Committee as an opportunity to help also with the organizational aspects of running a big
open source project.

**Maciej**: I’ve been going through the idea of running for SC for a while now. My biggest drive was
conversations with various members of our community. Eventually last year, I decided to follow their
advice, and got elected :-)

**Sandipan: What is your favorite part of being part of Steering?**

**Ben**: When we get to help contributors directly. For example, sometimes extensive contributors
reach out for an official letter from Steering explaining their contribution and its value for visa
support. When we get to just purely help out Kubernetes contributors, that’s my favorite part.

**Patrick**: It’s a good place to learn more about how the project is actually run, directly from
the other great people who are doing it.

**Maciej**: The same thing as with the project --- it’s always the people that surround us, that give
us opportunities to collaborate and create something interesting and exciting.

**Sandipan: What do you think is most challenging about being part of Steering?**

**Ben**: I think we’ve all spent a lot of time grappling with the sustainability issues in the
project and not having a single great answer to solve them. A lot of people are working on these
problems but we have limited time and resources. We’ve officially delegated most of this (for
example, to SIGs Contributor Experience and K8s Infra), but I think we all still consider it very
important and deserving of more time and energy, yet we only have so much and the answers are not
obvious. The balancing act is hard.

**Paco**: Sustainability of contributors and maintainers is one of the most challenging aspects to
me. I am constantly advocating for OSS users and employers to join the community. Community is a
place that developers can learn from each other, discuss issues they encounter, and share their
experience or solutions. Ensuring everyone in the community to feel supported and valued is crucial
for the long-term health of the project.

**Patrick**: There is documentation about how things are done, but it’s not exhaustive. There are
parts which are intentionally not documented, perhaps because they cannot be public, change too
often, or simply need to be handled on a case-by-case basis. Luckily we have overlapping terms, so
there is an opportunity to learn from more experienced members. We also have a list of former
members and they are happy to respond to questions if needed.

**Maciej**: The unknown unknowns :-) After I got elected to SC I’ve tried to talk to various folks
from current and past SC. The biggest challenge that came from all those discussions is that no
matter how hard you try and what you prepare for, there will always be something new that none of
the previous SC had to deal with, so far.

**Sandipan: For folks who might want to run for Steering in the future, what are the most important
things you think they should know?**

**Ben**: A lot of what Steering does is "interrupt driven"... something comes up and needs resolution
– Make sure you’re committed and prepared to set aside the time. Otherwise I hope you think calmly
about issues and listen to our community with empathy.

**Paco**: This is a quote from the survey to all previous SCs: we should make sure that "everyone’s
voice was heard and respected" from Clayton. For the community, the most important part is about the
people here.

**Maciej**: Once you decide to run and get elected, make sure to reserve a constant time per week
for your Steering duties. There will be times when nothing will need to happen, and others when you
will overflow so reserving that timeframe will ensure consistency in you being a Steering member.

## Conclusion

Behind every successful open source project is a group of dedicated people who ensure things run
smoothly, and the Kubernetes Steering Committee does just that. They work quietly but effectively,
tackling challenges, supporting contributors, and ensuring the community remains inclusive and
vibrant.

What makes them stand out is their focus on people --- empowering contributors, resolving governance
issues, and creating an environment where innovation can thrive. It’s not always easy, but as
they’ve shared, it’s deeply rewarding.

Whether you’re a long-time contributor or thinking about getting involved, the Kubernetes community
is open to you. At its heart, Kubernetes is about more than just technology --- it’s about the people
who make it all happen. There’s always room for one more voice to help shape the future.
