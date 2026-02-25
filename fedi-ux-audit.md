# Fedi App — UX Audit
**Version audited:** 26.2.4
**Platform:** Android
**Method:** Live emulator walkthrough, Nielsen Norman Group heuristics
**Date:** February 2026

---

## Executive Summary

Fedi is trying to do something genuinely ambitious — combine chat, payments, and mini apps inside a federated community model. That's a hard brief, and you can feel the vision behind it. But right now, the app is designed for people who already understand how it works. The onboarding drops users straight into federation jargon without explanation, the navigation is almost entirely unlabelled, and the app's core feature — the wallet — is locked behind a joining process that can leave someone completely stranded with no way forward. The visual design is clean and the intent is clear, but the gap between what the team understands and what a new user experiences is significant. These findings are organised in the order a real user would encounter them.

---

## 1. First Launch

**What the user experiences:**
A calm, well-designed splash screen. Floating avatar bubbles, the Fedi logo, a short tagline. Two buttons — "Get started" and "Restore access." First impressions are good.

**Findings:**

- The legal copy — "By continuing, you agree to our Terms of Use & Privacy Policy" — sits above the button in small grey text against a pastel gradient. The contrast is too low and the placement makes it easy to miss. For a financial app, this matters more than it might for a typical social app. ⚠️

- "Ask Fedi" appears at the very bottom of the splash screen as a help affordance. It's a nice idea, but the placement is so peripheral that most users won't notice it. ⚠️

- Everything else on this screen works. The visual hierarchy is clear, the two-button layout is intuitive, and the avatar bubbles do a good job of communicating "social network" without needing to say it. ✅

---

## 2. Federation Discovery — The First Wall

**What the user experiences:**
They tap "Get started" and land immediately on a screen titled "Join or Create a Federation." There's a list of federations with "Join" buttons. No one has explained what a federation is yet.

**Findings:**

- The word "federation" appears in the headline, the subheading, the tab labels, and every list item — before the user has any idea what it means. The subheading reads: *"Federations are the homes for your personal wallets."* That's helpful, but it's doing too much work too late. By the time a confused user reads it, they've already felt lost. 🔴

- The federation list cards are not tappable. There's no detail view — no way to learn more about a federation before committing to it. The only action is "Join." For something that the app itself describes as "the home for your personal wallet," this is a significant trust gap. 🔴

- Description text is truncated mid-sentence throughout the list ("Privacy Sovereignty Fr…", "Feel free to use the wall…"). This is minor but it reinforces a feeling of roughness. ⚠️

- The three tabs at the top — Discover, Join, Create — have no clear visual active state and their distinction isn't explained. ⚠️

- "Maybe Later" at the bottom is the right call — it gives users an exit. ✅

---

## 3. Joining a Federation — Errors, Loops, and a Disappearing Exit

**What the user experiences:**
They tap "Join" on one of the federations. Things start to go wrong here, and they don't obviously recover.

**Findings:**

- An error banner appears immediately: *"Unable to connect. Try switching between Wi-Fi and cellular or disable your VPN."* This is technically accurate, but the advice is generic and there's no retry button in the banner itself. The user is left to figure out next steps on their own. 🔴

- The error banner is never dismissed. It persists through multiple subsequent screens — including the camera permission screen and the QR scanner — stacking on top of other UI elements. This is a state management issue more than a design one, but the user experience is of a broken app. 🔴

- After the error, the app moves to a camera permission request screen. The transition is unexplained — there's no heading, no "here's what's happening" moment. The user is simply looking at a camera icon and some feature bullets with a "Continue" button. It's not clear whether tapping Continue grants permission or defers it. ⚠️

- The QR scanner screen that follows has no instruction text. A new user has no idea what to point their camera at, or where they'd even get a federation QR code from. ⚠️

- "View public federations" on the scanner screen sounds like it should take you somewhere new. It takes you back to the federation list you just came from. No feedback, no explanation — just a loop. 🔴

- **The most critical finding in this section:** Once a user has gone through the joining flow and returned to the federation list, "Maybe Later" is gone. It doesn't come back. Pressing the system back button exits the app entirely to the home screen. The user is effectively walled in — they cannot reach the main app without successfully joining a federation, and if the connection fails, they have no path forward. 🔴

---

## 4. Arriving in the App

**What the user experiences:**
If they do make it through — either by joining or by catching "Maybe Later" on first visit — they land on the home screen with a modal already waiting for them.

**Findings:**

- The modal informs them that their display name is "curious seahorse." It was assigned automatically, without asking. For a chat and payments app, an auto-assigned username is jarring — this is an app where people will send each other money and messages. A prompt to set a real name before entering would feel much more considered. 🔴

- The display name shows as "curious seahorse #54e2" throughout the app. The `#54e2` is a hash suffix that means nothing to a user. It's technical noise that's been surfaced without context or explanation. ⚠️

- The home screen mixes three different content types — a pinned federation info banner, Community News, and Community Mini Apps — with no clear visual hierarchy separating them. It reads like a dashboard where everything has been given equal weight. ⚠️

- The "Fedi Global" banner at the top has a QR grid icon in the top right. It's not labelled. It's not obviously tappable. A user has no way of knowing what it does. ⚠️

---

## 5. Core Navigation

**What the user experiences:**
The bottom navigation has four icons. There are no labels on any of them.

**Findings:**

- Four unlabelled icons in the bottom nav means four things the user has to guess. The active state is indicated only by a marginally bolder icon — easy to miss. Android Material Design guidelines recommend labels on bottom navigation precisely because of this. 🔴

- Every tab — Chat, Mini Apps — opens with a bottom sheet upsell overlay that the user must dismiss before they can see the actual screen. Getting a promotional sheet every time you switch tabs is exhausting. It also means the first impression of each section is an interruption, not the content itself. 🔴

- The Wallet tab doesn't show a wallet. It redirects to the federation wall. There is no explanation for why. A user who skipped federation joining and is now tapping the Wallet tab has no idea they'd end up back at onboarding. 🔴

- The Chat screen's empty state — "No messages in this group yet." — is just text. There's no illustration, no suggestion of what to do next, no pointer to the + button in the header. The screen is mostly white space. ⚠️

- The header in every section has four icons with no labels. Across the whole app, there is almost no labelled navigation anywhere. Everything is icon-only. ⚠️

---

## 6. Settings & Profile

**What the user experiences:**
The profile icon in the header opens a settings screen — but the first thing they see isn't profile options. It's a large QR code.

**Findings:**

- The QR code sits at the very top of the settings screen with no label, no heading, no explanation of what it is or what scanning it would do. Is it a wallet address? A profile link? A login code? A user has no way to know. 🔴

- Below the QR code there's a URL and a Share button. This is more context, but it's still not explained in plain language. ⚠️

- "Nostr Details" appears in the settings list without explanation. Most users won't know what Nostr is. ⚠️

- Two items — "Notification Settings" and "Fedi App Terms of Service" — use an external link icon instead of a chevron, indicating they open outside the app. The distinction is visually subtle and inconsistent with the rest of the list. ⚠️

- "Share logs" at the bottom of the screen has no icon, no chevron, and no visual affordance that it's a tappable element. It appears as plain text floating below the version number. ⚠️

- The settings list sits on a light blue background card, the Communities section is on white, and the version footer is on another light blue card. Three different background treatments in one scroll, no clear reason for any of them. ⚠️

- The settings content itself is well-structured and covers the right ground — Personal Backup, PIN Access, Language, Display currency, and a dedicated Ask Fedi help entry. The bones are good. ✅

- Version information is shown at the bottom, which is helpful for support. But "Fedimint 0.9.1" is internal technical versioning that adds noise for a regular user. ⚠️

---

## Appendix: Priority Matrix

| Screen / Area | Finding | Heuristic | Severity |
|---|---|---|---|
| Federation Discovery | No explanation of what a federation is before asking users to join one | H2 — Match with real world | 🔴 |
| Federation Discovery | Federation cards are not tappable — no detail view before committing to join | H5 — Error prevention | 🔴 |
| Joining Flow | Error banner persists across multiple screens, stacking over other UI | H1 — Visibility of system status | 🔴 |
| Joining Flow | "View public federations" loops back to the same screen with no feedback | H3 — User control & freedom | 🔴 |
| Joining Flow | "Maybe Later" disappears after navigating through the flow | H3 — User control & freedom | 🔴 |
| Joining Flow | Back button exits app entirely — no path to main UI if joining fails | H3 — User control & freedom | 🔴 |
| Arriving in App | Display name auto-assigned without asking ("curious seahorse") | H2 — Match with real world | 🔴 |
| Wallet Tab | Redirects to federation wall with no explanation | H1 — Visibility of system status | 🔴 |
| Core Navigation | All four bottom nav tabs are unlabelled | H4 — Consistency & standards | 🔴 |
| Core Navigation | Every tab triggers a promotional bottom sheet on first open | H8 — Aesthetic & minimalist design | 🔴 |
| Settings | QR code at top of settings has no label or explanation | H6 — Recognition over recall | 🔴 |
| Joining Flow | Camera permission screen doesn't clarify whether Continue grants or defers | H5 — Error prevention | ⚠️ |
| Joining Flow | QR scanner has no instruction text — user doesn't know what to scan | H6 — Recognition over recall | ⚠️ |
| Joining Flow | Error banner offers no retry action | H9 — Help users recover from errors | ⚠️ |
| Federation Discovery | Description text truncated mid-sentence throughout list | H8 — Aesthetic & minimalist design | ⚠️ |
| Federation Discovery | Three tabs (Discover/Join/Create) have no active state and no explanation | H4 — Consistency & standards | ⚠️ |
| Arriving in App | "#54e2" hash suffix shown in display name with no explanation | H2 — Match with real world | ⚠️ |
| Arriving in App | Home screen gives equal visual weight to three different content types | H8 — Aesthetic & minimalist design | ⚠️ |
| Arriving in App | "Fedi Global" QR icon in home banner is unlabelled and non-obvious | H6 — Recognition over recall | ⚠️ |
| Chat Screen | Empty state is bare text with no illustration or call to action | H7 — Flexibility & efficiency | ⚠️ |
| Core Navigation | Four unlabelled header icons on every screen | H4 — Consistency & standards | ⚠️ |
| Mini Apps | App icon grid mixes wildly inconsistent icon styles | H4 — Consistency & standards | ⚠️ |
| Settings | "Nostr Details" listed with no explanation of what Nostr is | H2 — Match with real world | ⚠️ |
| Settings | External link icons vs chevrons are inconsistent and unexplained | H4 — Consistency & standards | ⚠️ |
| Settings | "Share logs" has no visual affordance — looks like plain text | H6 — Recognition over recall | ⚠️ |
| Settings | Three different background treatments in one screen | H8 — Aesthetic & minimalist design | ⚠️ |
| Settings | "Fedimint 0.9.1" version shown — internal technical noise for users | H8 — Aesthetic & minimalist design | ⚠️ |
| Splash Screen | Legal consent text is low contrast and easy to miss | H5 — Error prevention | ⚠️ |
| Splash Screen | "Ask Fedi" help link is too peripheral to be noticed | H10 — Help & documentation | ⚠️ |
| Splash Screen | Two-button layout (Get started / Restore access) is clear and familiar | H4 — Consistency & standards | ✅ |
| Splash Screen | Avatar bubbles convey "social network" without text | H6 — Recognition over recall | ✅ |
| Camera Permission | "This can be updated later" reduces anxiety about granting permission | H5 — Error prevention | ✅ |
| Settings | Good range of settings — backup, PIN, language, currency | H7 — Flexibility & efficiency | ✅ |
| Settings | "Ask Fedi" dedicated help entry in settings | H10 — Help & documentation | ✅ |
| Settings | Settings list structure (icon + label + chevron) is clear and scannable | H6 — Recognition over recall | ✅ |
