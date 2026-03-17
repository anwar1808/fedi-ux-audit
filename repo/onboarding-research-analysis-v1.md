# Fedi Wallet Onboarding: UX Research Analysis
**Independent Review — March 2026**
**For: Head of Product & UX / Chris Vázquez**

---

## 1. Context & Purpose

This document provides an independent analysis of the moderated usability study conducted between March 5–9, 2026, evaluating three proposed onboarding flows for the Fedi wallet experience. The study was designed and run by Chris Vázquez, with one additional session conducted by this reviewer. The goal of this analysis is not to relitigate the research, but to examine the methodology critically, validate the findings against the raw session data, and frame what the results can and cannot responsibly tell us as the team moves forward.

Fedi occupies a genuinely difficult UX challenge. Its core product concept — the federation — has no widely-understood analogue in everyday financial experience. Users must choose a custodian before they can do anything, but most will arrive with no frame of reference for what a federation is, why it matters, or how to evaluate one. Onboarding is therefore not just a flow problem; it is a mental model problem. The research was right to focus here. The question is whether the method used is capable of answering it.

---

## 2. Methodology Review

### 2.1 Study Design: Attitudinal, Not Behavioural

This study is, by design, entirely **attitudinal** — it captures what participants *say* they prefer, not what they *do* when navigating the product under real conditions. Participants were shown three Figma prototype flows in sequence, asked to walk through each one, and then asked to rank and explain their preferences.

According to Nielsen Norman Group's research methodology framework, attitudinal research is best suited to:

- Exploring mental models and how users think about a concept
- Capturing emotional responses — trust, confusion, fear, confidence
- Generating hypotheses about user behaviour for future testing

It is less well-suited to:

- Predicting what users will actually do
- Measuring task completion speed or error rates
- Understanding behaviour under real conditions, without a moderator, on a personal device

For a product like Fedi — where trust, privacy, and financial safety are load-bearing values — the gap between stated preference and actual behaviour is likely to be significant. Participants in a moderated session are aware they are being observed. They are more considered, more articulate, and more patient than a user downloading the app on their phone while distracted. Social desirability bias operates in both directions: participants may overstate their confidence and understate their confusion.

That said, attitudinal research conducted at this stage is appropriate and valuable. It surfaced consistent themes around terminology, cognitive load, and consent dynamics that are worth acting on. The findings should be read as **directional signals** — strong enough to inform a working hypothesis, not strong enough to close one.

### 2.2 Pros and Cons of Attitudinal Research in Fedi's Context

**Where this approach worked:**

- Well-suited to exploring the terminology problem — "federation," "wallet provider," "auto-select" — language that needs testing before anything else can be evaluated
- Captured emotional responses (trust, fear, confusion) that matter enormously for a financial product targeting communities with limited prior exposure to digital custody tools
- Surfaced mental model mismatches early and cheaply — e.g. "provider" carrying ISP-style surveillance connotations (Marius), or federation language feeling politically loaded in some regional contexts
- Appropriate for early-stage comparative concept evaluation

**Where attitudinal research falls short for this use case:**

- Cannot tell us how quickly users actually complete onboarding without a facilitator present
- Cannot tell us where users drop off, hesitate, or abandon in a real environment
- Cannot tell us whether users who said they preferred Option B would complete it faster or more successfully in an unmoderated setting
- Cannot validate whether the trust and consent dynamics observed verbally translate into actual behaviour at the moment of commitment — signing a ToS, accepting a federation, funding a wallet

**What good research looks like next:** Complement attitudinal findings with behavioural methods — unmoderated task testing, time-on-task measurement, and drop-off analysis in beta — as Option B is developed. The attitudinal study has done its job by pointing in a direction. Behavioural research confirms whether the direction is right.

### 2.3 Presentation Order Bias — An Unacknowledged Confound

One of the most significant methodological issues identified from reviewing the raw session transcripts is one that does not appear in the research notes: **all sessions run by the primary interviewer used the same fixed presentation order.**

- **Link 1 (shown first):** Option C — auto pre-selected provider, scroll to accept ToS
- **Link 2 (shown second):** Option A — current flow (Discover / Join / Create)
- **Link 3 (shown last):** Option B — empty state, auto-select or manual choice

**Option B was shown last in every session.** This creates three compounding effects well-documented in research methodology:

1. **Recency effect:** The most recently seen option is most salient at the point of comparison and ranking
2. **Contrast effect:** After experiencing Option C (information-heavy, potentially overwhelming) and Option A (multiple layers of choice), Option B's simplicity is amplified by comparison — more so than if it had been evaluated first or second
3. **Learning effect:** Participants became progressively more fluent with the Figma prototype across each demo. By the third flow, they could navigate it more naturally — which systematically benefited Option B

There is a further complication: **Option A is the current live flow.** Most participants — all internal users, all power users, and all community leaders — had already used it before the study began. This means the study was not presenting three equally unfamiliar stimuli. It was asking participants to compare two genuinely new designs (C and B) against a flow they already knew well. Option A carried the full weight of prior experience — both its familiarity and its accumulated frustrations. This is not inherently a flaw, but it needed to be acknowledged in the research design and factored into how results are interpreted. It was not.

The session conducted by this reviewer used a different order (C → B → A). The participant — Kanda, a community manager who works with Fedi daily across 40 city meetups — preferred Option A, which was shown last in his session. Kanda's familiarity with Fedi is the more compelling explanation for his preference (see Section 4.2), and his session cannot be used as proof of the order effect. But the directional consistency is worth noting: in both orderings, the option shown last was the one preferred.

This does not invalidate Option B as the leading candidate. The qualitative themes give genuine explanatory weight to why participants preferred it. But the study as designed cannot rule out presentation order as a contributing factor to the strength of that preference.

**Recommendation for future studies:** Counterbalance presentation order across participants — rotate which option is shown first, second, and third. This is standard practice in comparative concept testing and eliminates order effects from the results.

### 2.4 Prototype Fidelity and Session Quality

Several sessions were affected by conditions that limited the quality of data collected:

- **Connectivity issues (Bitcoinshagga):** The session transcript is largely incoherent due to severe connection problems throughout. The detailed feedback attributed to this participant in the research notes cannot be independently verified from the raw transcript. This session's data should be treated with caution and not given equal weight to sessions where the interaction was clean.
- **Screen display issues (Lorena):** Significant time at the start of the session was spent troubleshooting a compressed Figma view that prevented Lorena from scrolling through Option C's ToS content — the specific interaction being evaluated in that flow.
- **Prototype orientation (multiple sessions):** Several participants initially attempted to navigate the Figma file using its frame controls rather than interacting with the prototype as they would the real app. One participant initially believed they were inside the live Fedi application. Brief reorientation was needed across multiple sessions. Since Option C was shown first in every session, early navigation friction disproportionately affected impressions of Option C.

**A note on AI-generated transcription:** Session notes were generated using an AI transcription and summarisation tool. While useful for rapid documentation, AI-generated meeting summaries carry inherent accuracy limitations. During this review, at least one confirmed instance was identified where the AI summary misidentified which flow a participant ultimately preferred — contradicting what was clearly stated in the underlying transcript. The research notes (compiled separately) caught this in most cases, but it is a useful reminder that AI-generated summaries should be reviewed against raw transcripts before being treated as the record of a session. This is a tool limitation, not a critique of the process — and it is an argument for always preserving and reviewing the underlying transcript wherever possible.

---

## 3. Participant Sample

### 3.1 Internal User Overrepresentation

Of the 13 participants included in this study, **7 are internal users** — Fedi team members or council members with direct knowledge of and investment in the product. That represents **54% of the sample**.

This is a meaningful concern. Internal users are not representative of Fedi's target audience in several structural ways:

- They understand what a federation is. Most real new users will not.
- They have baseline trust in the organisation. New users in emerging markets — particularly those with prior negative experiences with financial institutions — may be significantly more sceptical of anything that looks like custody.
- They carry implicit investment in the product's direction, which shapes how they engage with design decisions even when trying to be neutral.
- Their mental models are calibrated to the existing product, making it structurally harder for them to experience a new flow as a genuine first-time user would.

This was visible in the transcripts. Dea acknowledged mid-session: *"I think I maybe maybe I am biased. Maybe I got used to this this method."* Ray prefaced his feedback with *"I'm so used to setting up new wallets"* before projecting a new user perspective. These are honest acknowledgements of a problem that cannot be resolved by asking internal participants to try harder to think like a stranger.

**The likely management response:** *"But they're close to the community — they understand our users better than an outsider would."*

This is a reasonable point that deserves a direct answer. Proximity to a community is genuinely valuable. It provides cultural context, language intuition, and on-the-ground operational empathy that external researchers cannot replicate quickly. But proximity is not equivalence. A team member who knows what a federation is, has used the product for months, and has a professional stake in its success is structurally different from a community member in Lagos or Jakarta who just downloaded the app because a friend mentioned it.

The former can *imagine* the latter's experience. They cannot *be* it.

For a product whose primary onboarding challenge is precisely the concepts that internal users already understand — federation selection, wallet custody, provider terminology — this distinction is especially consequential. The more appropriate role for internal participants in this kind of research is as **subject matter informants**: experts on the ecosystem, the community, and the product's intent. Not as proxies for end users.

The external participants in this study — Jodom, Collins, Marius, Kanda, and with caveats Bitcoinshagga — carry more evidentiary weight as signals of genuine new user behaviour. Their data should be read with that in mind.

### 3.2 Sample Size and What It Means for Qualitative Research

Fourteen participants is a reasonable size for qualitative usability research. Nielsen Norman Group's longstanding guidance is that approximately five participants are sufficient to surface the majority of usability issues in a formative study — not because small samples are ideal, but because qualitative research is not attempting to prove frequency, it is attempting to find themes and patterns.

**Statistical significance does not apply here.** Statistical significance is a concept from quantitative research — it tells you whether a numerical result is likely to be real rather than a product of random variation. It requires large samples, controlled conditions, and a hypothesis being tested. This study has none of those things, and it was not designed to.

What "9 out of 12 preferred Option B" gives you is a **directional pattern** — consistent enough, and grounded in enough explanatory reasoning from participants, to justify treating it as a working hypothesis. It is not proof. It does not close the question. It opens the next one: does this stated preference translate into better real-world task performance?

The more important question is not the count, but the quality and diversity of participants generating it. On that measure, this study is weaker than the headline preference vote suggests: the distribution looks different when external participants are weighted more heavily than internal ones, and presentation order effects reduce the confidence we can place in the magnitude of Option B's apparent lead.

---

## 4. Thematic Analysis

The following themes were identified through independent review of raw session transcripts (J, Modibe, Dea, Ray, Jodom, Francisco, Lorena, Collins, Bitcoinshagga, Phil, Renata, Marius) and research notes for the session without an available transcript (Kanda). Themes are presented in order of consistency and strength of evidence.

### Theme 1: Terminology is the primary barrier — across all user types

The language of "wallet provider," "federation," and "auto-selected provider" was flagged as confusing in virtually every session. The nature of that confusion differed by user type, which is itself instructive:

- **External participants and community leaders** (Kanda, Collins, Marius): Confusion is genuine — these participants do not know what the terms mean in this context. Kanda expected "Ask Fedi" to be an AI chatbot in Bahasa Indonesia. Collins suggested reducing everything to "set up your wallet." Marius connected "provider" to ISPs and data tracking — a strongly negative association with direct implications for a privacy-first product. In his own words: *"It feels more that it's mine and that it's private if I only hear the word 'your wallet' instead of selecting a provider."*
- **Internal users** (Dea, Lorena, Modibe, Renata): Confusion is projected — they understand the concepts but recognise the language will fail with actual users. Dea referenced a design crit in Austin where exactly the same issue surfaced, suggesting this is not a new finding. Renata flagged "provider" as something that *"feels too institutional"* and could *"frighten a potential guardian user"* — she proposed simpler language like *"choose my own wallet"* as a direct replacement for "manually select provider."
- **Power users and product stakeholders** (J, Jodom, Phil Gomes): Specific negative connotations emerged. J felt "wallet provider" implied a third-party intermediary or broker. Jodom noted the language was opaque for something requiring a trust decision. Phil Gomes — reviewing from a product stakeholder perspective — preferred "wallet service" or "wallet service provider" over "federation" for new user clarity, while flagging concerns about regulatory proximity to terms like "money transmitter."

The consistent signal across all groups: **"wallet" is the word people understand**. "Provider," "federation," and their variants need to either be replaced or contextualised before the user is asked to act on them. Notably, the terminology concern was not just about confusion — for privacy-conscious users in particular, "provider" carries active negative connotations (surveillance, tracking, third-party control) that work against the trust Fedi is trying to build.

### Theme 2: Cognitive overload is the shared failure of Options A and C

Both Option A and Option C were described using a consistent cluster of language across participants: "overwhelming," "too much text," "too busy," "scary," "a lot." The overload manifested differently in each:

- **Option C** overwhelmed users at the point of consent. The ToS content appeared before users had any frame of reference for what they were agreeing to. Jodom was explicit: he felt "strongly urged" toward acceptance because the Accept button visually dominated the screen and the "Manually Select" option was buried. Lorena called the experience "scary" — she felt she was accepting something without understanding it.
- **Option A** overwhelmed users at the point of choice. The Discover / Join / Create taxonomy, presented without guidance on what distinguishes the options, forced users to evaluate alternatives they had no criteria for. Francisco recalled his fiancée's reaction to the current flow: *"She was like, 'Oh, which one should I use?'"* — a direct, unprompted observation of a genuine new user's response. Marius articulated the same dynamic precisely: *"If there are too many options, you can't decide — so you just do it later."* His description of Option B's "maybe later" path — abandoning the flow entirely rather than making a choice — is direct evidence of how decision overload manifests in real user behaviour.

A further nuance Marius introduced: the volume of options is not a problem equally for all user types. Non-technical users benefit most from auto-select — they want to press one button and have a working wallet. Power users are comfortable with manual selection and often prefer it. The design problem is not which mode to offer, but how to present the choice in a way that serves both without forcing the first group through an experience designed for the second. Option B's two-button architecture (auto-select or manual) addresses this directly; Option A does not.

### Theme 3: Consent and permission are more powerful than information volume

The most actionable design insight to emerge from the study — and one that was consistent across both internal and external participants — is that the *feeling of having chosen* matters more than the *amount of information provided*.

Option C gave users information before they had consented to receiving it. Option B asked users to make one simple choice first (auto-select or manual), then delivered the information. The same ToS content landed entirely differently depending on whether the user had opted into the journey.

Lorena: *"She already had the context that she was setting up a wallet from the initial splash screen, and she consented for the wallet to be auto-selected, so when the ToS page for the chosen federation came up, she felt very comfortable — knowing that Fedi would pick something that made sense for her."*

Collins: *"You 'already trust the system' because you freely indicated as such — it means you're asking for it versus something being done to you."*

Jodom: *"The auto-selected federation in Option B feels like it's coming at the right time because he freely chose Auto Select — so he's keen to accept the terms."*

This is a durable UX principle with particular resonance in Fedi's context. Communities targeted by Fedi — in LatAm, Africa, Southeast Asia — have often had negative experiences with financial systems that took action without meaningful consent. Designing onboarding around permission rather than information is not just good UX; it is aligned with Fedi's core values.

A related but distinct concern was surfaced in Renata Rodrigues's session: **the legal and accountability risk of auto-selection itself**. Renata raised the explicit concern that if the application automatically selects a federation for a user, that user may later blame the app if things go wrong with that federation. She noted that current users come largely through community onboarding and already carry goodwill toward the product — but as Fedi grows toward more organic, less community-mediated user acquisition, this dynamic changes. A user with no prior relationship to the brand who is silently assigned to a federation has a more credible grievance than one who chose. This is not just a UX consideration — it is a product liability framing that is worth escalating to legal and product leadership as the auto-select feature moves toward build.

### Theme 4: Tooltip and help content is effectively invisible

Across almost every session, participants did not interact with the tooltip / question mark icons — the primary in-flow mechanism for explaining unfamiliar terms. When pointed out by the interviewer, participants in several sessions found the content insufficient anyway (Dea: *"even the tooltip is like... I don't know"*; the tooltip text did not explain what a wallet provider actually is).

This is one of the few genuinely behavioural observations in the study — a moment where what participants *did* diverged from what the design assumed they would do. It is a strong signal that passive help mechanisms are not a reliable solution to the terminology problem. The language needs to work in the primary UI, not in tooltips that users don't notice and content that doesn't clarify enough when they do.

### Theme 5: Familiarity bias among power users and internal participants

Two participants who ranked Option A most highly — Ray and Kanda — are among the most product-familiar people in the study. Critically, Option A is the current live flow that both use in their day-to-day work.

Ray is an internal council member who navigated Option A quickly precisely because he already knows it. He was not evaluating it as a new user — he was recognising it. He explicitly noted he would rank it first if it simply had less text — a conditional that assumes the user already knows what they are reading and just wants less of it. That is a power user's edit request, not a new user's experience.

Kanda manages Bitcoin communities across 40 city meetups and uses Fedi operationally on a regular basis. He valued having federation options and explanations upfront on a single screen — precisely the information architecture that works for someone who already understands federations, and that overwhelms someone who does not. As observed directly by this reviewer during his session, Kanda's preference was rooted in deep operational familiarity with the current flow, not an assessment of what a first-time user would find intuitive.

Both participants were effectively rating a product they already use. Their preference for Option A reflects satisfaction with the known, not evidence that Option A serves new users better. Neither finding invalidates their feedback — understanding how power users respond is genuinely useful context. But it must be labelled as such.

---

## 5. Preference Findings

Based on independent analysis of raw transcripts and research notes:

| Participant | Type | Preferred Option | Source |
|-------------|------|-----------------|--------|
| J | Power User | B | Transcript ✓ |
| Modibe | Internal | B | Transcript ✓ |
| Dea | Internal | B | Transcript ✓ |
| Ray | Internal | A | Transcript ✓ |
| Jodom | Power User | B | Transcript ✓ |
| Francisco | Internal | C | Transcript ✓ |
| Lorena | Internal | B | Transcript ✓ |
| Collins | Power User | B | Transcript ✓ |
| Bitcoinshagga | New User | B* | Notes only — data quality caveat |
| Phil | Internal | A | Transcript ✓ |
| Renata | Internal | B | Transcript ✓ |
| Marius | Power User | B | Transcript ✓ |
| Kanda | Power User | A | Notes — session run by this reviewer |

*Bitcoinshagga's session was significantly affected by connectivity issues. Preference cannot be independently verified from the transcript.

**Updated vote tally:** A=3, B=9, C=1 (across 13 participants, including Kanda's session which postdated the original tally)

**What this shows:** Option B has a clear plurality of stated preferences, with explanatory reasoning from participants that is consistent and grounded in genuine usability dynamics — cognitive load, consent, clarity of action path. The preference is credible.

One factor that strengthens the signal: Option A is the current live flow. Most participants had prior exposure to it before the study began. The fact that a majority still preferred Option B — a genuinely new design — over something they already knew is a more meaningful finding than a straight preference count suggests. Participants were not simply gravitating toward the familiar. They were choosing something new over the status quo.

**Where to hold it lightly:** The presentation order effect means the strength of Option B's preference count cannot be taken at face value. An independently conducted study with counterbalanced order and a higher proportion of external participants may show a smaller gap. The direction is sound. The magnitude is uncertain.

---

## 6. Forward Path

The results of this study are best understood as a **research hypothesis, not a research conclusion.**

Option B surfaces consistently as the preferred direction, for reasons grounded in real behavioural dynamics. That is enough to justify treating it as the leading candidate for development. It is not enough to treat the question as settled.

The appropriate path forward:

1. **Proceed with Option B as the working hypothesis** — but hold it as a hypothesis, not a mandate
2. **Build in behavioural validation checkpoints** as the flow is developed — unmoderated task testing, time-on-task, completion rates, and drop-off analysis in beta, with a meaningful proportion of genuine new users in target markets
3. **Counterbalance presentation order** in any future comparative testing
4. **Recruit more external participants** — specifically new users in LatAm, Africa, and Southeast Asia who have not been exposed to the product
5. **Remain open to pivoting** — if behavioural data contradicts the attitudinal preference, the right response is to adjust, not to defend the earlier finding

The broader opportunity here is to move away from last-minute research conducted under time pressure and toward a model where research is embedded earlier in the build cycle — asking the right questions before design decisions are made, not after. That kind of research infrastructure requires intentional investment, but it produces decisions made with confidence rather than ones made to break a stalemate.

---

*This analysis was conducted independently based on session transcripts provided and the research plan and notes shared. Raw transcripts were reviewed for all sessions except Kanda (research notes) and Bitcoinshagga (notes only — data quality caveat applies). Sessions for Phil Gomes (March 11), Renata Rodrigues (March 12), and Marius (March 15) were conducted after the original study period and reviewed on the basis of transcripts provided subsequently.*
