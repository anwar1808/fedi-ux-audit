# User Research at Fedi: Strategic Assessment & Recommendations
**Anwar Abdulhaqq — March 2026**


## The Short Version

Fedi's growth goals are clear: acquire users quickly, and make the product sticky enough that they stay. The onboarding experience is where both goals are either won or lost — it is the first moment a new user decides whether Fedi is worth their trust.

Fedi recently completed a study to evaluate three onboarding flows for the wallet experience. The study produced a clear directional signal: the majority of participants preferred a simplified flow that gives users a meaningful choice before asking them to commit. That signal is credible and worth acting on.

But the more important story is not which flow won. It is what this study reveals about how Fedi currently approaches user research — and what is possible if that approach is upgraded. The onboarding flow problem is real, but it sits inside a larger set of acquisition and retention challenges that a single flow study cannot address. This report covers both.


## What the Research Tells Us

The study asked 13 participants — a mix of internal team members, power users, and community leaders across LatAm, Africa, and Asia — to evaluate three onboarding designs and share their preferences.

The finding is consistent: most participants preferred a flow that presents a simple, clear choice upfront (auto-select or manual wallet setup) rather than either overwhelming them with options immediately or pre-selecting a provider before they have any context. The reasoning participants gave — across different regions and user types — was grounded in real dynamics: clarity, trust, and the feeling of having chosen rather than been pushed.

One piece of context worth noting: Option A in this study is not a novel concept — it is Fedi's current live onboarding flow. The majority of participants, particularly internal team members and community power users, had already encountered it before the study. The fact that Option B was preferred over something participants already knew and had used makes that preference a stronger signal than it might initially appear. Choosing the new over the familiar — without being primed to do so — suggests the preference reflects genuine usability improvement, not novelty.

These themes hold up under scrutiny. Terminology confusion ("wallet provider," "federation," "auto-select") is a real and consistent barrier — and notably, "provider" does not just confuse users, it actively alienates privacy-conscious ones by evoking internet service providers and data tracking. Participants across multiple sessions converged on "wallet" as the term that works. Cognitive overload at the point of first decision is a real problem. The relationship between perceived consent and trust is a real UX dynamic — and one that matters especially for a product targeting communities that have historical reasons to be sceptical of financial systems that act on their behalf without asking.

The research points in a clear direction. It is a good starting point.


## What the Research Cannot Tell Us

The study captures what people *say* they prefer. It does not capture what they *do*.

There is a well-documented gap between stated preference and actual behaviour in product research — and it is wider in fintech than almost anywhere else. A user in a moderated session with a researcher watching them navigate a prototype is not the same as a user in Jakarta or Nairobi downloading an app for the first time, alone, with patchy connectivity, and no one to ask for help.

The study also has structural limitations that a more experienced research practitioner would design out: all three flows were shown in the same fixed order across every session, which likely inflated preference for the option shown last. More than half the participants were internal team members, who understand federations, trust the organisation, and cannot fully simulate what it feels like to encounter these concepts for the first time. And because Option A is the current live app, the study was not comparing three equally unfamiliar concepts — it was comparing two new designs against something many participants already used daily, without acknowledging that asymmetry in how findings were interpreted. These are not criticisms of the people who ran the sessions — they are design problems in the study itself, and they are fixable.

The result is a signal. A strong enough signal to act on, but not strong enough to close the conversation. The right response is to move forward with the leading option while building in the kind of behavioural testing that confirms — or challenges — what the attitudinal study suggested.

There is also a deeper problem this study does not address: users who never reach the onboarding flow at all. The current product assumes that the person downloading the app already understands that a wallet is the gateway to everything Fedi can do. That assumption does not hold for all users. Some arrive thinking Fedi is primarily a community or messaging platform and never meaningfully engage with the wallet setup. Optimising the onboarding flow is valuable — but it is a solution to a step users have already reached. Understanding why users stall before that step, or why they download the app but don't convert, is a different and equally important research question.


## The Bigger Pattern

What this study reflects is a wider dynamic that many product teams encounter: research gets done reactively, under time pressure, to resolve a decision that has already been partially made. The question being asked is "which of these three options should we build?" rather than "what does a user in this context actually need, and have we designed for it?"

That is not a criticism of intent. It is a description of what happens when research is treated as a deliverable rather than a discipline — when the goal is to produce an answer rather than to reduce uncertainty.

The engineering and product tension that has driven this study is a symptom of the same pattern. When teams disagree about the right direction and there is no systematic research infrastructure to generate shared evidence, opinions fill the gap. Research becomes a tiebreaker rather than a foundation. It gets commissioned when a stalemate needs resolving, not before the decisions that create stalemates are made.

There are two further dimensions to this pattern that are worth naming directly.

The first is a **feature-based rather than needs-based product culture**. The current approach tends to start from: "we have version A — is version B or C better?" That is a valid question, but it is the second question, not the first. The first question is: what does a user in this context actually need to feel confident setting up a wallet? Answering that question first changes what gets built and in what order. Without research infrastructure to answer it, the team will continue to be productive at building things — but with less certainty that they are building the right things.

The second is what might be called a **community-dependent acquisition ceiling**. Fedi's current user base has grown largely through existing Bitcoin community networks. That is a genuine strength — community-onboarded users arrive with context, trust, and support that organic downloads cannot replicate. But it also means that the product has been designed, tested, and iterated primarily for an audience that already understands Bitcoin and already has a community reason to use Fedi. Feedback from community leaders in Asia confirms this clearly: it is difficult to explain why someone *outside* an existing community should download Fedi at all. For growth goals that require reaching beyond that core network, the product needs to work for users who arrive with no prior context — and currently, it is not clear that it does. Research is the mechanism for understanding what those users need, and for building a product experience that earns their trust without relying on a community interpreter to do it for you.

The assumption that research delays production is contradicted by the companies that move fastest. The businesses that have dominated their categories — in Bitcoin, crypto, and beyond — did not win by shipping features faster. They won by shipping the *right* features, because they understood their users before writing a line of code.

In the Bitcoin and crypto space, Coinbase's dominance was not a function of superior technology — every major exchange had comparable infrastructure. It was a function of UX investment. Brian Armstrong understood that the barrier to crypto adoption was experiential, not technical. The "Simple/Advanced" toggle that made Coinbase accessible to non-technical users was not a product decision made in a vacuum — it was the output of understanding that two fundamentally different user types were arriving at the same front door. Block's Cash App, shaped by Jack Dorsey's background as a product designer, consistently outperformed technically comparable competitors on the strength of experience design alone — lower friction, clearer mental models, and a send flow that felt intuitive to users who had never touched a financial app before.

The same pattern holds in the wider industry. Stripe did not win the payments infrastructure market because their technology was superior to Braintree or Authorize.net. They won because Patrick Collison understood what developers actually experienced — the hours lost to poorly documented APIs, the friction of integration, the lack of clarity at the point of failure — and built against that understanding. Airbnb's growth inflection came not from a new feature but from founders going door-to-door to photograph hosts' homes, because they understood that the blocker to adoption was trust, not technology.

The principle is the same in every case: research does not delay production — it de-risks engineering. Every week of development spent building a feature that users do not understand, do not trust, or do not need is engineering capacity that research would have protected. The cost of building the wrong thing is always greater than the cost of the study that would have prevented it. And when research is embedded early — before the build begins rather than after it ships — it directly drives revenue: faster decisions, fewer costly pivots, higher activation rates, and a product that earns loyalty because it earns trust before it asks for commitment.

This is a solvable problem. But solving it requires treating research as a strategic function, not a project-by-project service.


## The Analogy That Fits

In Bitcoin custody, there is a useful distinction between an **auditor** and a **custody architect**.

An auditor tells you the current state of a wallet — what's in it, whether the keys are intact, whether the last transaction checks out. It is a snapshot. Useful, necessary, but backward-looking. Think Armanino / Sparrow verification tools, etc. — Armanino signed off on FTX's proof of reserves shortly before the collapse. The audit was technically accurate: it showed exactly what was in the wallets at that moment. It missed everything that mattered, because auditing the current state tells you nothing about whether the system around it is sound.

A custody architect designs the system that surrounds the wallet: the signing policy, the key management structure, the recovery path, the human protocols that determine what happens when something goes wrong. Think Jameson Lopp / Casa, etc. — people who catalogue every known way humans have lost Bitcoin and build systems designed to prevent it before it happens. Bitcoin is sound. But plenty of people have lost funds not because the protocol failed — it never does — but because nobody thought carefully enough about the human layer around it. The custody architecture is where experience, trust, and real-world behaviour matter most.

Commissioning one-off research studies when a decision needs making is auditing. It tells you the current state of user opinion and moves on. What Fedi needs — given where it is in its growth, the communities it is trying to serve, and the complexity of the concepts it is asking new users to navigate — is a custody architect for the user experience. Someone who designs the research infrastructure: what gets studied, when, how findings feed back into product decisions, and how that system evolves as the product does.

This is not a "research monkey" running studies purely on request; it is a research leader building the Product Intelligence Function of Fedi.


## What a Research-Led Approach Looks Like

The difference between reactive and embedded research is largely a matter of timing and structure.

**Reactive research** (current state): A design question needs an answer. A study is commissioned. Findings are delivered. The team acts on them or doesn't. The next decision starts the cycle again from scratch.

**Embedded research** (recommended state): Research is mapped to the product roadmap. Before a feature enters design, the relevant user questions have already been identified and, where possible, answered. Development teams are building on evidence rather than assumption. Post-launch, behavioural data feeds back into the next research cycle.

Concretely, this means building a **UX research roadmap** aligned to Fedi's product development calendar — identifying the 6–12 months of planned builds, mapping the user knowledge gaps associated with each, and scheduling the right type of research (generative, evaluative, or behavioural) at the right point in the build cycle.

For a product serving communities in emerging markets where digital financial literacy varies enormously, where multiple languages are in play, and where trust is hard-won and easily broken, this kind of intentional research infrastructure is not a luxury. It is how you build something that actually works for the people it is meant to serve — and how you know when to change course before a full build has been committed to.


## Recommended Next Steps

**Immediately:**
- Treat the current study's findings as a working hypothesis, not a verdict. Proceed with the preferred onboarding direction, but build in unmoderated task testing and behavioural metrics as the flow is developed.
- Establish a feedback loop between research and engineering — so that when behavioural data comes in, there is a clear process for incorporating it rather than re-opening design debates.

**Within 90 days:**
- Map the product roadmap against a set of open user questions — what do we not yet know about users that could affect the success of each planned build?
- Prioritise the top three research questions and design studies that address them *before* the associated builds begin.
- Increase the proportion of genuine new users — particularly in LatAm, Africa, and Southeast Asia — in any future research. Internal participants and power users have a role, but not as primary evidence.
- Commission a dedicated study on pre-onboarding orientation: what mental model do new users arrive with, do they understand the wallet's centrality to the app, and where do they stall or abandon before reaching the setup flow? This is the research question that sits upstream of the current study and speaks most directly to conversion.
- Begin mapping the standalone value proposition for users who arrive without community context — this is the research question that determines whether Fedi's growth ceiling is structural or addressable.

**Structurally:**
- Define what a research function at Fedi looks like: not a single study, but a practice. Who owns it, how it connects to product decisions, and how findings are documented and built upon over time.
- Invest in that function with the same seriousness applied to engineering infrastructure. The human layer of a financial product is as consequential as the technical layer — and just as dependent on systematic, rigorous attention.


## Closing Thought

The onboarding study is a good start. It asked the right questions, surfaced real themes, and produced a direction worth pursuing. The goal of this report is not to diminish that work — it is to show what becomes possible when it is part of a larger, more intentional research practice rather than a one-time exercise.

Fedi is building financial infrastructure for communities that have rarely been well-served by it. Getting the human experience right is not separate from that mission. It is the mission.

---

*Report prepared by Anwar Abdulhaqq, March 2026. Based on review of session transcripts, research notes, and study design documentation provided.*


\newpage

## Appendix A: Prioritised Research Agenda

The table below reorders the full assumption register against a single governing question: which assumptions, if wrong, cost Fedi the most — and which can be answered fastest? The sequence is designed explicitly to address the concern that research delays production. Tiers 1 and 2 are achievable within the first 30 days.

\rowcolors{2}{tblrowalt}{white}

| Tier | ID | Theme | Assumption | Why now | Timebox |
|------|----|-------|-----------|---------|---------|
| 1 | A16 | Roadmap | Research aligns to roadmap: in-flight vs shapeable | Establishes the shared framework that determines when research is "done" — without this, every study triggers a timing debate | ~1w |
| 1 | A15 | Governance | "Validated enough" thresholds can be agreed per decision type | Defines the finish line for research; answered in a workshop, not a study | ~1w |
| 2 | A1 | Core concepts | Federation vs Community is understood well enough to act correctly | The conceptual pre-step to onboarding — users who don't grasp the model never reach the wallet setup | 5–7d |
| 2 | A2 | Onboarding | Users reach first successful moment (join + receive/send) without help | Direct line to acquisition: every drop-off here is a conversion failure | 1–2w |
| 2 | A0* | Orientation | Users understand that a wallet is required to use Fedi | *Not in original register.* Users who arrive thinking Fedi is a chat app never engage with onboarding at all — this is upstream of A2 | 1w |
| 3 | A13 | Localisation | Universal vs local UX needs can be separated early | Determines whether the product can work without a community interpreter; key to breaking the community-dependent growth ceiling | Ongoing |
| 3 | A14 | Segmentation | Western vs Global South users need different defaults (not a different product) | Getting defaults right for different user types before the team commits to a single flow | 1–2w |
| 3 | A10 | Language | Key concepts work across literacy levels and languages | Whether terms like "federation" and "wallet provider" land for non-Bitcoin-literate users | ~2w |
| 4 | A7 | Mini Apps | Mini apps drive weekly utility without becoming clutter | What creates the habit that brings users back; secondary to getting them through the door | ~2w |
| 4 | A8 | Chat + money | Paying in chat is clear and reduces friction | Retention utility — but only valuable once onboarding works | ~1w |
| 4 | A6 | Volatility | Stable Balance is understood and reduces volatility anxiety | Financial feature comprehension; affects stickiness once wallet is active | 1–2w |
| 5 | A3 | Trust & custody | Social Backup feels safe + socially acceptable vs self-custody | High risk, but does not block acquisition; can run in parallel with Tier 3–4 | 1–2w |
| 5 | A4 | Recovery | In a panic moment, users can recover without catastrophic mistakes | Existentially important; not a day-one acquisition question | 1–2w |
| 5 | A5 | Connectivity | Offline payments are usable and trusted in real contexts | Regional and specific; important but not blocking | 2–3w |
| 5 | A9 | Safety | Users avoid common scams without UX becoming oppressive | Regional threat patterns; can run once core flows are stable | 1–2w |
| 5 | A11 | Privacy | App is safe under device-sharing and social pressure | Important for emerging market contexts; not a conversion question | 2–3w |
| 5 | A12 | Support | Users know where to get help and who is accountable | Reduces support load; follows activation research | 1–2w |

*A0 is not in the original assumption register. It has been identified as a gap from the onboarding study and added here as a Tier 2 priority.*

---

\newpage

## Appendix B: Assumption Register v0

Full register of assumptions, research questions, and study parameters across all 16 themes. Risk column: H = High, M = Medium.

\rowcolors{2}{tblrowalt}{white}

| ID | Theme | Assumption | Risk | Region | Decision it informs | Next study | Timebox |
|----|-------|-----------|------|--------|-------------------|-----------|---------|
| A1 | Core concepts | Federation vs Community is understood well enough to act correctly | H | Global | IA / labels / onboarding | Comprehension + task usability | 5–7d |
| A2 | Onboarding | Users reach first successful moment (join + receive/send) without help | H | Global | Onboarding defaults | Usability + funnel review | 1–2w |
| A3 | Trust & custody | Social Backup feels safe + socially acceptable vs self-custody | H | Regional | Recovery + messaging | Concept test + scenario probes | 1–2w |
| A4 | Recovery | In a panic moment, users can recover without catastrophic mistakes | H | Global | Safeguards + recovery UX | "Lost phone" drill usability | 1–2w |
| A5 | Connectivity | Offline payments are usable and trusted in real contexts | H | Regional | Offline states + disputes | Scenario test + field/diary | 2–3w |
| A6 | Volatility | Stable Balance is understood and reduces volatility anxiety | M/H | Regional | Balance UX + education | Comprehension + choice tasks | 1–2w |
| A7 | Mini Apps | Mini apps drive weekly utility without becoming clutter | M | Regional | Catalogue IA + prioritisation | JTBD + card sort | ~2w |
| A8 | Chat + money | Paying in chat is clear and reduces friction vs separate wallet flows | M | Global | Chat-pay UX | Usability + mis-send prevention | ~1w |
| A9 | Safety | Users avoid common scams without UX becoming oppressive | H | Regional | Warnings / guardrails | Threat patterns + rapid test | 1–2w |
| A10 | Language | Key concepts work across literacy levels and languages | H | Regional | Terminology + icons | Teach-back comprehension | ~2w |
| A11 | Privacy | App is safe under device-sharing and social pressure | H | Regional | Privacy defaults | Context interviews + prototype test | 2–3w |
| A12 | Support | Users know where to get help and who is accountable | M/H | Global | Support UX | Journey + support flow test | 1–2w |
| A13 | Localisation | Universal vs local UX needs can be separated early | H | Global | Localisation strategy | Comparative synthesis | Ongoing |
| A14 | Segmentation | Western vs Global South users need different defaults/education (not a different product) | M/H | Regional | Default settings | Comparative flow test | 1–2w |
| A15 | Governance | "Validated enough" thresholds can be agreed per decision type | H | Global | Shipping governance | Validation ladder workshop | ~1w |
| A16 | Roadmap | Research aligns to roadmap: mitigate in-flight work, de-risk shapeable bets | H | Global | Research roadmap | Roadmap intake + triage | ~1w |

**Research questions by theme**

*Core concepts (A1):* What do users think a federation is vs a community? Where do they misroute actions or help-seeking? What explanation makes the distinction click?

*Onboarding (A2):* Where do users drop out or hesitate? What step triggers fear or confusion? What reassurance increases completion?

*Trust & custody (A3):* Who do users trust as guardians? What nightmare scenarios do they imagine (coercion, theft)? What trust cues are needed before they commit?

*Recovery (A4):* Which steps break under stress? What guardrails prevent irreversible loss? How do users verify recovery succeeded?

*Connectivity (A5):* When is offline truly needed? What "pending / sync later" states are acceptable? How do disputes get resolved?

*Volatility (A6):* Do users grasp what stays stable vs what changes? When do they choose stable vs BTC? Does it add "two-money" confusion?

*Mini Apps (A7):* Which apps are core by region? How do users judge trustworthiness? What is the minimum set for retention?

*Chat + money (A8):* Do users understand payee and source? What mistakes happen (wrong person, wrong amount)? Does it increase scam surface?

*Safety (A9):* What are the top scam vectors per region? What friction is acceptable? What education moments stick?

*Language (A10):* Which terms fail comprehension? What metaphors work locally? Can users teach the concept back accurately?

*Privacy (A11):* Do people share phones? What must be hidden by default? What threats exist from family or community?

*Support (A12):* Who do users blame when something goes wrong? What support path feels intuitive? What reduces support load?

*Localisation (A13):* What generalises across regions? What must be localised? What is the minimum sample to tell the difference?

*Segmentation (A14):* Which steps differ most between user types? What defaults should adapt? Where can one flow use progressive disclosure to serve both?

*Governance (A15):* Which decisions need high confidence before shipping? Which can ship as experiments? What metrics and thresholds count as "validated enough"?

*Roadmap (A16):* What is committed vs shapeable in the next 6–12 weeks? Where can research reduce risk mid-flight? What unlocks near-term decisions fastest?

---
