# Fedi UX Research: Prioritised Assumption Register
**Sequenced against product velocity and acquisition goals — March 2026**

---

## The Prioritisation Filter

The 16 assumptions in this register were not all created equal — and in an organisation where research is viewed as a potential drag on shipping, presenting them as a flat list is the wrong move. What follows reorders them against a single governing question:

**Which assumptions, if wrong, cost Fedi the most — and which can be answered fastest?**

The sequence below is explicitly designed to address the concern that research delays production. It leads with the governance assumptions that define *when research is done* (so the team never debates it again), then moves to the conversion assumptions that directly affect acquisition, then to the growth ceiling and retention questions, and parks the high-importance-but-not-blocking safety work for later cycles.

Each tier maps to the 30/60/90 plan. Nothing here requires a full research programme before shipping. The timeboxes are in the register.

---

## Tier 1 — First 30 Days: Answer "Does Research Delay Us?"

These are not user-facing assumptions. They are the operational foundation that determines whether research is seen as a function or a bottleneck. They need to land before anything else, because without them every subsequent study triggers a debate about timing.

### A16 — Roadmap alignment: in-flight vs shapeable
**Assumption:** Research can align to the roadmap — mitigating risk on in-flight work, de-risking shapeable bets before code is committed.

**Why first:** Without a shared map of what is already committed vs what is still being scoped, research has no defensible place in the timeline. This assumption establishes the framework for all subsequent prioritisation decisions.

**Key research questions:**
- What is committed vs shapeable in the next 6–12 weeks?
- Where can research reduce risk mid-flight without blocking delivery?
- What unlocks near-term decisions fastest?

**Timebox:** ~1 week

---

### A15 — Validated-enough thresholds agreed
**Assumption:** The team can agree on what "validated enough" looks like per decision type — so research has a clear finish line, not an open-ended mandate.

**Why first:** The fastest way to kill the perception that research delays shipping is to define, upfront, when it stops. One-way-door decisions (custody, recovery) require higher evidence bars. Reversible experiments do not. This assumption is answered in a workshop, not a study.

**Key research questions:**
- Which decisions need high confidence before shipping?
- Which can ship as experiments with monitoring?
- What metrics and thresholds constitute "validated enough"?

**Timebox:** ~1 week

---

## Tier 2 — Days 1–30: Acquisition and Conversion

These assumptions sit at the top of the funnel. If they are wrong, users do not acquire. Both are fast studies with immediately actionable outputs.

### A2 — Onboarding: first successful moment without help
**Assumption:** Users can reach their first successful moment — joining a federation and completing a send or receive — without needing a person to help them.

**Why now:** This is the most direct line to Obi's acquisition goal. Every user who drops out of onboarding before completing that first moment is a conversion failure. The study takes 1–2 weeks and produces specific, fixable friction points.

**Key research questions:**
- Where do users drop out or hesitate?
- What step triggers fear or confusion?
- What reassurance or reframing increases completion?

**Timebox:** 1–2 weeks

---

### A1 — Federation vs Community mental model understood
**Assumption:** Users understand the distinction between a federation and a community well enough to navigate the app correctly and route help-seeking appropriately.

**Why now:** This is the conceptual step before A2. Users who do not understand what a federation is — or who assume Fedi is primarily a chat or community app — will never meaningfully engage with the wallet setup. This assumption is also the upstream cause of the most common early drop-off risk.

**Key research questions:**
- What do users think a federation is vs a community?
- Where do they misroute actions or help-seeking as a result?
- What explanation or metaphor makes the distinction click?

**Timebox:** 5–7 days

---

## Tier 3 — Days 31–60: The Growth Ceiling

These assumptions determine whether Fedi can grow beyond its current community-dependent acquisition model. They do not block the immediate onboarding fix, but they are the research questions that determine whether the product can reach non-Bitcoin-literate, non-community-onboarded users.

### A13 — Universal vs local UX needs separated early
**Assumption:** It is possible to identify, early, which UX needs generalise across regions and which require localisation — so the team does not build universal defaults that fail specific markets.

**Why here:** Fedi's current user base is concentrated in communities that already understand Bitcoin and already have a local champion to contextualise the product. Reaching beyond that base requires knowing which onboarding and UX decisions are universal and which are locally specific.

**Key research questions:**
- What generalises across SE Asia, Africa, and LatAm?
- What must be localised and cannot be abstracted?
- What is the minimum regional sample needed to tell the difference?

**Timebox:** Ongoing (begins in cycle 2)

---

### A14 — Segmentation: defaults differ by user type
**Assumption:** Western and Global South users need different default settings and education paths — but not a different product.

**Why here:** The onboarding study already surfaced this in miniature: Marius described non-technical users who want to press one button and have a working wallet, vs power users who want manual control. Getting defaults right for each segment without fragmenting the product is a design challenge that research can de-risk before the team commits to a single default.

**Key research questions:**
- Which steps in the flow differ most between segments?
- What defaults should adapt vs stay fixed?
- Where can a single flow use progressive disclosure to serve both?

**Timebox:** 1–2 weeks

---

### A10 — Concepts work across literacy levels and languages
**Assumption:** Key product concepts — federation, wallet, auto-select, custody — are comprehensible to users across varying digital and financial literacy levels and across the languages Fedi operates in.

**Why here:** This is the research question that determines whether the product can work without a community interpreter. If key terms fail comprehension for users without Bitcoin background, the growth ceiling is structural.

**Key research questions:**
- Which terms and concepts fail comprehension in target markets?
- What metaphors or framings work locally?
- Can users teach the concept back accurately after encountering it in the app?

**Timebox:** ~2 weeks

---

## Tier 4 — Days 31–60: Stickiness and Retention

These assumptions determine whether users who successfully onboard keep coming back. They are important for Obi's stickiness goal but secondary to getting users through the door.

### A7 — Mini apps drive weekly utility
**Assumption:** Mini apps provide enough recurring utility — without becoming clutter — to bring users back to the app week over week.

**Key research questions:**
- Which mini apps are core by region?
- How do users judge trustworthiness of a mini app?
- What is the minimum set of mini apps that creates a retention habit?

**Timebox:** ~2 weeks

---

### A8 — Paying in chat is clear
**Assumption:** Completing a payment within a chat flow is clear and reduces friction compared to switching to a separate wallet flow.

**Key research questions:**
- Do users correctly understand who is paying whom?
- What mistakes happen (wrong person, wrong amount)?
- Does the chat payment surface increase scam exposure?

**Timebox:** ~1 week

---

### A6 — Stable Balance understood
**Assumption:** Users understand what Stable Balance is, why it exists, and when to choose it over holding BTC.

**Key research questions:**
- Do users grasp what stays stable vs what changes?
- When do they choose stable vs BTC and is that the right call?
- Does Stable Balance create "two-money" confusion that increases cognitive load?

**Timebox:** 1–2 weeks

---

## Tier 5 — Days 60–90: Safety and Resilience

These are high-risk assumptions — several of them existentially so if Fedi ever loses a user's funds or exposes a user to coercion or scam. They are not optional. But they do not block acquisition, and scheduling them in cycle 3 allows the team to ship onboarding improvements while the safety research runs in parallel.

### A3 — Social Backup feels safe and socially acceptable
Who do users trust as guardians? What nightmare scenarios do they imagine (coercion, theft)? What trust cues are needed before they commit to a guardian setup?
**Timebox:** 1–2 weeks

### A4 — Recovery works under panic
Which recovery steps break under stress? What guardrails prevent irreversible loss? How do users verify that recovery succeeded?
**Timebox:** 1–2 weeks

### A5 — Offline payments usable and trusted
When is offline genuinely needed? What "pending / sync later" states are acceptable? How do disputes get resolved?
**Timebox:** 2–3 weeks

### A9 — Scam resistance without heavy friction
What are the top scam vectors per region? What level of friction is acceptable? What in-app education moments actually stick?
**Timebox:** 1–2 weeks

### A11 — Safe under device-sharing and social pressure
Do users share phones? What must be hidden by default? What threats exist from family or community members?
**Timebox:** 2–3 weeks

### A12 — Help and accountability are clear
Who do users blame when something goes wrong? What support path feels intuitive? What reduces support load on the team?
**Timebox:** 1–2 weeks

---

## What Is Not in This Register

One assumption is missing from the original deck that the onboarding research has since surfaced: **users may not know they need a wallet at all.** Some new users download Fedi believing it is primarily a community or messaging app, and never reach the wallet setup step. This is a pre-onboarding orientation problem — upstream of A2, and upstream of every other assumption in this register. It should be added as A0 and treated as a Tier 2 priority alongside A1 and A2.

---

*Prioritisation prepared March 2026. Assumption IDs correspond to the original Assumption Register v0.*
