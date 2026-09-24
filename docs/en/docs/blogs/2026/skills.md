# Demystifying Agent Skills: Why They Work — Until They Don't

When it comes to agents, "skills" is an unavoidable word.

Simply put, it means packaging various operational experiences into reusable "skill packs" that an agent can call on demand while executing tasks — it sounds great.

But few people ask a more fundamental question:

**Why are skills useful at all? Is it just "store experience and retrieve it later" — that simple?**

Researchers from Princeton, Stanford, and UC San Diego recently published a paper, [Demystifying Agent Skills](https://arxiv.org/html/2608.14036v1), dedicated to this exact question.

They ran 8,135 controlled experiments, analyzed 240 complete trajectories, and finally distilled three major categories and twelve skill-effect patterns. The conclusion is quite counterintuitive.

![Skill vs. Workflow Memory Experiment Pipeline](./images/skills-pipeline.png)

The figure above shows their core experimental design: the same piece of historical experience is fed to the agent in two forms — "raw trajectory" and "distilled skill" — and then they compare which performs better on the same task. All experiments run in a fixed Docker environment to ensure fairness.

## Key Finding: Skills Rely on "Anchoring," Not "Knowledge"

The most surprising finding of the study is this: the reason skills are useful **is mainly not that they supplement new knowledge, but that they provide "procedural anchoring."**

The data tells the story: 65.7% of skill utility comes from procedural anchoring, while genuine "knowledge injection" accounts for only 4.5%. The rest is auxiliary effects such as execution-layer correction and context compression.

What does that mean? Here's an analogy: an agent doing a task is like a novice walking a maze. It's not dumb — its reasoning is fine — but at every step it may stray, take a detour, or hit a wall.

The role of a skill is not to give it a map full of knowledge points, but to put up signposts at the key forks of the maze: go left first, then straight, turn right at the third intersection, and if it doesn't work, back up and try another path.

Put simply, a skill doesn't make the agent smarter; it makes it steadier.

## Why "Steady" Matters More Than "Smart"

Many people think an agent falls short because the model isn't smart enough. But in real tool-use scenarios, failures are mostly not an intelligence problem — they are repeated trial-and-error at the execution level.

For example, the environment is misconfigured and it takes three tries to find the right dependency version; the command argument is wrong and it loops back and forth; the output format doesn't match the validator and it keeps changing things; the tool-call order is reversed and the earlier work was wasted; or it even forgets to verify and only discovers the result is wrong at the very end.

Each of these alone is small, but piled together they mean massive Token waste, timeout failures, and even going off in the wrong direction.

The study compared two approaches — "injecting the raw trajectory directly (workflow memory)" versus "distilling it into a skill" — and concluded that skills improve on workflow memory by an average of 6.06 percentage points.

The reason is intuitive: the raw trajectory, while containing the correct answer, is also mixed with a lot of exploration noise, failed branches, and redundant processes — and this noise actually interferes with the agent, even leading it astray.

What a skill does is distill the "useful steps" out of the "noisy process," turning them into a reusable execution scaffold.

![Skill Taxonomy Distribution](./images/skills-taxonomy.png)

This figure is quite intuitive. Three groups compared: on the left is the bare agent (Raw), in the middle is the one fed the raw trajectory directly (Workflow Memory), and on the right is the one given the distilled skill (Skill).

At a glance, the dark green in the right Skill group (skill-guided success) is much higher than the other two, and the blue-toned execution failures are visibly fewer. This is the visual evidence of procedural anchoring.

## What Real Skills Look Like

This may still feel a bit abstract, so let me give a few examples of skills we are using internally, and you'll feel what "procedural anchoring" really means.

### Troubleshooting Pod Issues Without Random Guessing

Anyone working in cloud native knows that a crashed Pod is a daily event. But troubleshooting is where people differ enormously.

A beginner might immediately run `kubectl logs`, stare at logs for a long time without a clue, then run describe, and if that fails, go to the node to check kubelet — and after half an hour of fussing, find it was just an image pull failure. We've all done that. An experienced engineer is different: they start with `describe` to look at Events, and nine times out of ten can spot the root cause at a glance.

What a skill does is solidify that senior engineer's "muscle memory": look at Events first, then probes, then logs, and finally drill down to the node. What to look at each step, what counts as abnormal, and which signals are most easily ignored — all spelled out clearly.

The result is that the agent no longer pokes around like a beginner; it follows the process and finds the root cause by the fastest path.

### Image Optimization: No Need to Start From Scratch Every Time

Another skill we use heavily is Dockerfile optimization.

This is neither particularly hard nor particularly easy. You might say the agent doesn't know multi-stage builds? Of course it does. But when it actually writes one, it still makes all kinds of mistakes:

putting cache cleanup in a separate RUN makes the cleanup useless; putting `COPY . .` at the front causes all dependencies to reinstall on every code change; blindly using alpine and then hitting musl compatibility issues…

These are pitfalls you learn after stepping in once. But the agent hits them "for the first time" every time.

The role of a skill is to flag these pitfalls in advance. Like an experienced driver guiding a novice through mountain roads — which curve is dangerous, which stretch is prone to rockfall — a heads-up in advance. No need to fall yourself every time to learn the lesson.

### Token Cost Analysis: From Month-End Bill Shock to Real-Time Control

There's also a skill closely related to the Token Factory — Token cost analysis.

Many teams using LLMs start with "just get it running first," and at month-end they're shocked by the bill: how did we spend so much? Then they start cutting usage by gut feeling.

But cost optimization actually has a method: first break down usage by application and team to find the Top-N consuming scenarios, then see which tasks can be replaced by smaller models, and finally set up budget alerts. Following this process usually cuts 30%–50% of wasted consumption without hurting the business.

The skill hard-codes this analysis path, so the agent doesn't have to explore "how to reduce cost" from scratch — it just follows the steps, and no data to check, metric to compare, or suggestion to produce is missed.

## What a Skill File Looks Like

Having said all this, what does a skill file actually look like? Here's the simplest example — taking a web screenshot.

Without a skill, when the agent needs to take a screenshot, it might fumble with what tool to use, how to write the parameters, whether to scroll the page, and waste quite a while. With a skill it's different — just follow it:

```markdown title="SKILL.md"
# Web Screenshot Skill

## When to use

When you need to take a screenshot of a web page.

## How to do it

1. Use `navigate()` to open the target web page and wait for it to finish loading
2. Use `setViewport()` to set the window size (default 1280x800)
3. Use `screenshot(fullPage=true)` to capture the full page and save it as a PNG

## Pitfalls to avoid

- Don't capture before loading finishes, or you'll get a blank image
- Don't forget `fullPage=true`, otherwise only the first screen is captured
- Close any pop-ups first, otherwise they'll block the content

## What counts as done well

The screenshot file exists, the content is complete, and the layout is normal.
```

That's all there is to it. A skill, four things: when to use it, how to do it, what pitfalls to avoid, and what counts as done well.

Does the agent not know what a screenshot is? Of course it does. What it lacks is "what to do first, what to do second, which parameters are easy to get wrong, which pitfalls someone has already fallen into before" — the structure that turns knowledge into action.

This is exactly what the paper says: 65.7% of skill utility comes from procedural anchoring. The knowledge is already there; what's missing is the execution path that strings the knowledge together.

## The Skill Ceiling: Retrieval Is the Real Bottleneck

But skills are not a silver bullet.

One data point in the paper is quite surprising: as the skill pool grows from 5 to 100, the precision of actually effective usage drops from 29.6% straight down to 3.3%.

![Retrieval Precision Drops as Skill Pool Grows](./images/skills-retrieval.png)

Look at this figure — the three curves have a large gap: the top blue line is offline retrieval accuracy, which looks decent; the middle orange line is the agent's own skill-selection accuracy, also okay; the bottom green line, which drops the steepest, is the proportion that **selected the right one and actually made it work**.

From 30% down to 3% — a brutal fall.

| Skill pool size | Actual usage precision |
|---|---|
| 5 skills | 29.6% |
| 20 skills | ~15% |
| 50 skills | ~7% |
| 100 skills | 3.3% |

What does this mean? The more skills there are, the harder it is for the agent to pick the right one at the right time. Retrieval is the true bottleneck of the skill system.

More interestingly, the study also found that "precise retrieval" and "task success" are not simply positively correlated:

- Selecting the right skill does not guarantee task success — the skill may be invoked superficially, or may be insufficient to solve a deep execution-level bottleneck
- Selecting the wrong skill does not guarantee task failure — a related, non-exact-matched skill can still provide useful procedural support

So the design of a skill system should not fixate on the offline metric of "retrieval accuracy," but pay more attention to the actual effect of downstream execution.

## From Token Factory to Agent Skills: Two Loops of AI Efficiency

When it comes to efficiency, there are actually two layers, which map exactly to the two things DaoCloud is working on.

**One layer is on the compute supply side — the Token Factory.**

Traditional compute is renting GPUs; you pay whether they're idle or not. The Token Factory is different — it bills by the Tokens actually consumed, paying only for what you use.

DaoCloud's d.run AI operating system does exactly this — upgrading the intelligent computing center from piling up hardware to a high-yield Token Factory, using scheduling, optimization, and fine-grained operations to make every kilowatt-hour and every GPU produce more effective Tokens.

**One layer is on the inference consumption side — Agent Skills.**

For the same task, an agent with skills takes fewer detours, hits fewer pitfalls, and naturally consumes fewer Tokens. Procedural anchoring, simply put, uses experience to reduce blind fumbling, making every Token count.

One up, one down — that's the complete answer to AI efficiency:

| Efficiency dimension | Representative capability | Core goal |
|---|---|---|
| Supply-side efficiency | Token Factory | More Tokens per unit of compute |
| Consumption-side efficiency | Agent Skills | More tasks per Token |

Only by combining the two can we truly build a complete efficiency loop from compute to application.

## The Future of Skills: From Experience Distillation to Self-Evolution

There's one point in the paper I quite agree with: the maturity of a skill system is not about accumulating more and more, but about being able to reliably generate, retrieve, and apply them.

It roughly goes through these stages:

| Stage | Characteristic | Key capability |
|---|---|---|
| Manual authoring | Skills are manually written and maintained by experts | Standardized format, version management |
| Experience distillation | Automatically extract skills from successful trajectories | Trajectory analysis, pattern recognition, quality assessment |
| Adaptive invocation | Agent flexibly selects and combines skills based on context | Precise retrieval, context adaptation, failure fallback |
| Self-evolution | Agent automatically discovers, generates, and optimizes skills | Autonomous learning, skill iteration, effect loop |

The industry as a whole is still near the second step — moving from manually writing skills toward automatically distilling experience. The hurdle of retrieval hasn't been crossed yet, and there's still a long way to go.

## Conclusion: The Essence of Skills Is "Fewer Detours"

Finally, back to the opening question: why are skills useful after all?

Not because the agent learned new knowledge, but because someone organized "mistakes made, pitfalls stepped in, paths that worked" into a path that can be walked directly.

The essence of a skill is fewer detours.

On one side, the Token Factory makes compute supply more efficient; on the other, Agent Skills make inference consumption more precise — one up, one down, and the story of AI efficiency has only just begun.

## References

- [Demystifying Agent Skills: Why They Work—Until They Don't](https://arxiv.org/abs/2608.14036): original arXiv paper
- [Token Factory: In the AI Era, How to Measure a Team's Real Productivity?](./token-factory.md): a research productivity measurement system for the AI era
- [DaoCloud d.run AI Operating System](https://www.daocloud.io/): an enterprise-grade service platform connecting compute, models, and applications
