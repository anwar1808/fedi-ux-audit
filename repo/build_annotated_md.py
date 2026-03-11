"""
Generate fedi-ux-audit-annotated.md — pandoc markdown with raw LaTeX blocks.
Each section is a single raw block (title + rule + content) so LaTeX
cannot break between the heading and its content. Sections flow naturally;
a section will push to the next page only if there isn't room for it.
"""
import subprocess, os

ANN = "/Users/annie/Annie-Claude/fedi-ux-audit/repo/screenshots/annotated"
MD  = "/Users/annie/Annie-Claude/fedi-ux-audit/repo/fedi-ux-audit-annotated.md"
PDF = "/Users/annie/Annie-Claude/fedi-ux-audit/repo/fedi-ux-audit-annotated.pdf"
HDR = "/tmp/latex-header-annotated.tex"

HEADER = r"""
\usepackage{xcolor}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{float}
\usepackage{parskip}
\setlength{\parskip}{6pt}
\setlength{\parindent}{0pt}
"""

# ── Helpers ────────────────────────────────────────────────────────────────────
def img(filename):
    return os.path.join(ANN, filename)

def raw(latex):
    return f"\n```{{=latex}}\n{latex}\n```\n"

def finding(severity, text):
    sym = {"critical": r"\textcolor{red}{$\bullet$}",
           "moderate": r"\textcolor{orange}{$\triangle$}",
           "ok":       r"\textcolor{teal}{$\checkmark$}"}[severity]
    text = text.replace("%", r"\%").replace("_", r"\_")
    return f"\\noindent {sym}\\enskip {text}\\par\\smallskip\n"

def scene(text):
    return f"\\textit{{{text}}}\\par\\medskip\n"

def subhead(text):
    return f"\\textbf{{{text}}}\\par\\smallskip\n"

def vsep():
    """Vertical separator between sections — suggests (but doesn't force) a page break."""
    return raw(r"\par\vspace{1.4em}\pagebreak[3]")

def section_block(number, title, screenshot, content_latex, img_frac=0.40):
    """
    One unified LaTeX block: heading + rule + two-column layout.
    \\filbreak moves the whole thing to a new page if it doesn't fit.
    \\nopagebreak[4] after the rule makes it impossible to break between
    the heading and the screenshot content.
    """
    text_frac = round(0.97 - img_frac, 2)
    heading = (
        f"\\filbreak\n"
        f"\\vspace{{1.2em}}\n"
        f"{{\\large\\bfseries {number}.\\enspace {title}}}\\par\\smallskip\n"
        f"\\noindent\\rule{{\\textwidth}}{{0.4pt}}\n"
        f"\\nopagebreak[4]\\par\\medskip\\nopagebreak[4]\n"
    )
    cols = (
        f"\\noindent\n"
        f"\\begin{{minipage}}[t]{{{img_frac}\\textwidth}}\n"
        f"  \\includegraphics[width=\\linewidth]{{{img(screenshot)}}}\n"
        f"\\end{{minipage}}%\n"
        f"\\hfill\n"
        f"\\begin{{minipage}}[t]{{{text_frac}\\textwidth}}\n"
        f"  \\setlength{{\\parskip}}{{4pt}}\n"
        f"{content_latex}"
        f"\\end{{minipage}}\n"
    )
    return raw(heading + cols)

def two_col_pair(ss1, content1, ss2, content2, img_frac=0.32):
    """Two screenshots side by side, each with findings."""
    text_frac = round(0.48 - img_frac, 2)
    def half(ss, content):
        return (
            f"  \\begin{{minipage}}[t]{{{img_frac}\\textwidth}}\n"
            f"    \\includegraphics[width=\\linewidth]{{{img(ss)}}}\n"
            f"  \\end{{minipage}}%\n"
            f"  \\hspace{{0.5em}}\n"
            f"  \\begin{{minipage}}[t]{{{text_frac}\\textwidth}}\n"
            f"    \\setlength{{\\parskip}}{{4pt}}\n"
            f"{content}"
            f"  \\end{{minipage}}\n"
        )
    return raw(
        f"\\par\\medskip\n"
        f"\\noindent\n"
        f"\\begin{{minipage}}[t]{{0.49\\textwidth}}\n"
        + half(ss1, content1) +
        f"\\end{{minipage}}%\n"
        f"\\hfill\n"
        f"\\begin{{minipage}}[t]{{0.49\\textwidth}}\n"
        + half(ss2, content2) +
        f"\\end{{minipage}}\n"
    )


# ── Document ───────────────────────────────────────────────────────────────────
def build_md():
    p = []

    # YAML front matter
    p.append("""\
---
title: "Fedi App — UX Audit"
date: "February 2026"
geometry: margin=1.2in
fontsize: 11pt
linestretch: 1.4
colorlinks: true
linkcolor: blue
---
""")

    # Preamble
    p.append("""\
**Version audited:** 26.2.4 · **Platform:** Android · **Method:** Live emulator walkthrough, Nielsen Norman Group heuristics

---

## Executive Summary

Fedi is trying to do something genuinely ambitious — combine chat, payments, and mini apps inside a federated community model. That's a hard brief, and you can feel the vision behind it. But right now, the app is designed for people who already understand how it works. The onboarding drops users straight into federation jargon without explanation, the navigation is almost entirely unlabelled, and the app's core feature — the wallet — is locked behind a joining process that can leave someone completely stranded with no way forward. The visual design is clean and the intent is clear, but the gap between what the team understands and what a new user experiences is significant. These findings are organised in the order a real user would encounter them.

""")

    # ── Section 1 ──────────────────────────────────────────────────────────────
    p.append(section_block("1", "First Launch", "01-splash.png",
        scene("A calm, well-designed splash screen. Floating avatar bubbles, the Fedi logo, "
              "a short tagline. Two buttons --- \"Get started\" and \"Restore access.\" "
              "First impressions are good.") +
        subhead("Findings:") +
        finding("moderate",
            "The legal copy --- \"By continuing, you agree to our Terms of Use \\& Privacy "
            "Policy\" --- sits above the button in small grey text against a pastel gradient. "
            "The contrast is too low and the placement makes it easy to miss. For a financial "
            "app, this matters more than it might for a typical social app.") +
        finding("moderate",
            "\"Ask Fedi\" appears at the very bottom as a help affordance. It's a nice idea, "
            "but the placement is so peripheral that most users won't notice it.") +
        finding("ok",
            "Everything else on this screen works. Clear visual hierarchy, intuitive two-button "
            "layout, and the avatar bubbles communicate \"social network\" without needing to "
            "say it.")
    ))

    # ── Section 2 ──────────────────────────────────────────────────────────────
    p.append(section_block("2", "Federation Discovery --- The First Wall",
        "02-federation-discovery.png",
        scene("They tap \"Get started\" and land on a screen titled \"Join or Create a "
              "Federation.\" There's a list of federations with \"Join\" buttons. No one has "
              "explained what a federation is yet.") +
        subhead("Findings:") +
        finding("critical",
            "The word \"federation\" appears in the headline, subheading, tab labels, and every "
            "list item --- before the user has any idea what it means. The subheading is "
            "helpful but it's doing too much work too late.") +
        finding("critical",
            "Federation list cards are not tappable. There's no detail view --- no way to learn "
            "more before committing to join. For something described as \"the home for your "
            "personal wallet,\" this is a significant trust gap.") +
        finding("moderate",
            "Description text is truncated mid-sentence throughout the list "
            "(\"Privacy Sovereignty Fr\\ldots\"). Minor, but it reinforces roughness.") +
        finding("moderate",
            "The three tabs --- Discover, Join, Create --- have no clear active state and "
            "their distinction isn't explained.") +
        finding("ok",
            "\"Maybe Later\" at the bottom is the right call --- it gives users an exit.")
    ))

    # ── Section 3 ──────────────────────────────────────────────────────────────
    p.append(section_block("3", "Joining a Federation --- Errors, Loops, and a Disappearing Exit",
        "03-join-tos.png",
        scene("They tap \"Join\" on one of the federations. A Terms of Service screen appears "
              "--- titled simply \"Welcome\" --- with the full ToS linked as an external PDF. "
              "The user is asked to accept terms they cannot read without leaving the app.") +
        subhead("Findings:") +
        finding("critical",
            "The screen title is simply \"Welcome.\" There's no signal this is a legal consent "
            "moment. The ToS is not shown in-app --- only a link to an external PDF.") +
        finding("critical",
            "An error banner appears when connection fails: \\textit{\"Unable to connect. Try "
            "switching between Wi-Fi and cellular...\"} The advice is generic, there is no "
            "retry button, and the banner persists across multiple subsequent screens.") +
        finding("critical",
            "\"View public federations\" on the QR scanner screen sounds like it takes you "
            "somewhere new. It takes you back to the list you just came from --- just a loop.") +
        finding("critical",
            "Once through the joining flow, \"Maybe Later\" disappears. Pressing the system "
            "back button exits the app entirely. If joining fails, the user is walled in.") +
        finding("moderate",
            "The camera permission screen doesn't clarify whether tapping Continue grants "
            "permission or defers it.") +
        finding("moderate",
            "The QR scanner has no instruction text. A new user has no idea what to point "
            "their camera at, or where they'd get a federation QR code from.")
    ))

    # ── Section 4 ──────────────────────────────────────────────────────────────
    p.append(section_block("4", "Arriving in the App", "05-home-username-modal.png",
        scene("If they make it through --- either by joining or by catching \"Maybe Later\" "
              "on first visit --- they land on the home screen with a modal already waiting.") +
        subhead("Findings:") +
        finding("critical",
            "The modal tells them their display name is \"ambitious wolf\" --- assigned "
            "automatically, without asking. For a chat and payments app, this is jarring. "
            "A prompt to set a real name before entering would feel far more considered.") +
        finding("moderate",
            "The display name shows as \"ambitious wolf \\#267f\" throughout the app. The "
            "\\#267f suffix is a hash that means nothing to a user --- technical noise "
            "surfaced without context or explanation.") +
        finding("moderate",
            "The home screen mixes three different content types --- a pinned federation "
            "banner, Community News, and Community Mini Apps --- with no clear visual "
            "hierarchy separating them. Everything has equal weight.") +
        finding("moderate",
            "The \"Fedi Global\" banner has an unlabelled QR grid icon. It's not obviously "
            "tappable and a user has no way of knowing what it does.")
    ))

    # ── Section 5 ──────────────────────────────────────────────────────────────
    p.append(section_block("5", "Core Navigation", "06-home.png",
        scene("The bottom navigation has four icons. There are no labels on any of them.") +
        subhead("Findings:") +
        finding("critical",
            "Four unlabelled icons in the bottom nav means four things the user has to guess. "
            "The active state is indicated only by a marginally bolder icon. Android Material "
            "Design guidelines recommend labels precisely because of this.") +
        finding("critical",
            "Every tab opens with a bottom sheet upsell overlay the user must dismiss before "
            "seeing the actual screen. Getting an interruption every time you switch tabs is "
            "exhausting --- the first impression of each section is a promotion, not content.") +
        finding("critical",
            "The Wallet tab doesn't show a wallet for users who haven't joined a federation. "
            "It redirects to the federation wall with no explanation.") +
        finding("moderate",
            "The unlabelled QR icon on the Fedi Global banner has no affordance that it's "
            "tappable.") +
        finding("moderate",
            "Four unlabelled header icons appear on every screen. Almost no labelled "
            "navigation exists anywhere in the app.")
    ))

    p.append(two_col_pair(
        "07-chat.png",
        subhead("Chat screen") +
        finding("moderate",
            "The empty state --- \"No messages in this group yet.\" --- is bare text. "
            "No illustration, no suggestion of what to do next.") +
        finding("critical",
            "Promotional bottom sheet appears every time the tab is opened, blocking content."),
        "08-mini-apps.png",
        subhead("Mini Apps screen") +
        finding("moderate",
            "The icon grid mixes wildly inconsistent icon styles --- no visual coherence.") +
        finding("critical",
            "Promotional bottom sheet appears again on first open, covering all content.")
    ))

    # ── Section 6 ──────────────────────────────────────────────────────────────
    p.append(section_block("6", "Settings \\& Profile", "09-settings-top.png",
        scene("The profile icon opens a settings screen --- but the first thing they see "
              "isn't profile options. It's a large QR code.") +
        subhead("Findings:") +
        finding("critical",
            "The QR code sits at the very top with no label, no heading, no explanation of "
            "what it is or what scanning it would do. Wallet address? Profile link? Login "
            "code? A user has no way to know.") +
        finding("moderate",
            "The display name shows \"\\#267f\" --- a hash suffix that means nothing to a "
            "regular user.") +
        finding("moderate",
            "\"Nostr Details\" appears in the settings list without explanation. Most users "
            "won't know what Nostr is.") +
        finding("ok",
            "The settings content itself is well-structured --- Personal Backup, PIN Access, "
            "Language, Display currency, Ask Fedi. The bones are good.")
    ))

    p.append(two_col_pair(
        "10-settings-bottom.png",
        subhead("Icon inconsistency") +
        finding("moderate",
            "\"Notification Settings\" and \"Fedi App Terms of Service\" use an external link "
            "icon instead of a chevron. Subtle and inconsistent with the rest of the list.") +
        finding("ok",
            "The settings list structure --- icon + label + chevron --- is otherwise clear "
            "and scannable."),
        "11-settings-footer.png",
        subhead("Settings footer") +
        finding("moderate",
            "\"Fedimint 0.9.1\" is internal technical versioning --- noise for a regular user.") +
        finding("moderate",
            "\"Share logs\" has no icon, no chevron, no visual affordance that it's tappable. "
            "It appears as plain text floating below the version number.")
    ))

    # ── Appendix ───────────────────────────────────────────────────────────────
    p.append("\n---\n\n## Appendix: Priority Matrix\n\n")
    p.append("""\
| Screen / Area | Finding | Heuristic | Severity |
|---|---|---|---|
| Federation Discovery | No explanation of what a federation is before asking users to join one | H2 | $\\bullet$ |
| Federation Discovery | Federation cards are not tappable — no detail view before committing to join | H5 | $\\bullet$ |
| Joining Flow | Error banner persists across multiple screens, stacking over other UI | H1 | $\\bullet$ |
| Joining Flow | "View public federations" loops back to the same screen with no feedback | H3 | $\\bullet$ |
| Joining Flow | "Maybe Later" disappears after navigating through the flow | H3 | $\\bullet$ |
| Joining Flow | Back button exits app entirely — no path to main UI if joining fails | H3 | $\\bullet$ |
| Arriving in App | Display name auto-assigned without asking ("ambitious wolf") | H2 | $\\bullet$ |
| Wallet Tab | Redirects to federation wall with no explanation | H1 | $\\bullet$ |
| Core Navigation | All four bottom nav tabs are unlabelled | H4 | $\\bullet$ |
| Core Navigation | Every tab triggers a promotional bottom sheet on first open | H8 | $\\bullet$ |
| Settings | QR code at top of settings has no label or explanation | H6 | $\\bullet$ |
| Joining Flow | Camera permission screen doesn't clarify whether Continue grants or defers | H5 | $\\triangle$ |
| Joining Flow | QR scanner has no instruction text — user doesn't know what to scan | H6 | $\\triangle$ |
| Joining Flow | Error banner offers no retry action | H9 | $\\triangle$ |
| Federation Discovery | Description text truncated mid-sentence throughout list | H8 | $\\triangle$ |
| Federation Discovery | Three tabs have no active state and no explanation | H4 | $\\triangle$ |
| Arriving in App | "#54e2" hash suffix shown in display name with no explanation | H2 | $\\triangle$ |
| Arriving in App | Home screen gives equal visual weight to three different content types | H8 | $\\triangle$ |
| Arriving in App | "Fedi Global" QR icon in home banner is unlabelled and non-obvious | H6 | $\\triangle$ |
| Chat Screen | Empty state is bare text with no illustration or call to action | H7 | $\\triangle$ |
| Core Navigation | Four unlabelled header icons on every screen | H4 | $\\triangle$ |
| Mini Apps | App icon grid mixes wildly inconsistent icon styles | H4 | $\\triangle$ |
| Settings | "Nostr Details" listed with no explanation of what Nostr is | H2 | $\\triangle$ |
| Settings | External link icons vs chevrons are inconsistent and unexplained | H4 | $\\triangle$ |
| Settings | "Share logs" has no visual affordance — looks like plain text | H6 | $\\triangle$ |
| Settings | Three different background treatments in one screen | H8 | $\\triangle$ |
| Settings | "Fedimint 0.9.1" version shown — internal technical noise for users | H8 | $\\triangle$ |
| Splash Screen | Legal consent text is low contrast and easy to miss | H5 | $\\triangle$ |
| Splash Screen | "Ask Fedi" help link is too peripheral to be noticed | H10 | $\\triangle$ |
| Splash Screen | Two-button layout (Get started / Restore access) is clear and familiar | H4 | $\\checkmark$ |
| Splash Screen | Avatar bubbles convey "social network" without text | H6 | $\\checkmark$ |
| Camera Permission | "This can be updated later" reduces anxiety about granting permission | H5 | $\\checkmark$ |
| Settings | Good range of settings — backup, PIN, language, currency | H7 | $\\checkmark$ |
| Settings | "Ask Fedi" dedicated help entry in settings | H10 | $\\checkmark$ |
| Settings | Settings list structure (icon + label + chevron) is clear and scannable | H6 | $\\checkmark$ |

""")

    # ── Legends ────────────────────────────────────────────────────────────────
    p.append("---\n\n**Severity Legend**\n\n")
    p.append("""\
| Symbol | Meaning |
|---|---|
| $\\bullet$ | Critical — significant impact on usability, should be prioritised |
| $\\triangle$ | Moderate — noticeable friction or inconsistency, worth addressing |
| $\\checkmark$ | Works well — effective design worth preserving |

""")
    p.append("**Heuristics Reference** *(Nielsen Norman Group, 10 Usability Heuristics)*\n\n")
    p.append("""\
| Code | Heuristic |
|---|---|
| H1 | Visibility of system status |
| H2 | Match between system and the real world |
| H3 | User control and freedom |
| H4 | Consistency and standards |
| H5 | Error prevention |
| H6 | Recognition rather than recall |
| H7 | Flexibility and efficiency of use |
| H8 | Aesthetic and minimalist design |
| H9 | Help users recognise, diagnose, and recover from errors |
| H10 | Help and documentation |
""")

    return "".join(p)


def compile_pdf(md_path, pdf_path, hdr_path):
    cmd = [
        "pandoc", md_path,
        "--pdf-engine=/usr/local/texlive/2025basic/bin/universal-darwin/xelatex",
        f"-H{hdr_path}",
        "-V", "geometry:margin=1.2in",
        "-V", "fontsize=11pt",
        "-V", "linestretch=1.4",
        "-V", "colorlinks=true",
        "-V", "linkcolor=blue",
        "-o", pdf_path,
    ]
    print("Running pandoc/xelatex…")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("STDERR:", result.stderr[-3000:])
    else:
        size = os.path.getsize(pdf_path) / 1024 / 1024
        print(f"PDF written → {pdf_path}  ({size:.1f} MB)")


if __name__ == "__main__":
    with open(HDR, "w") as f:
        f.write(HEADER)

    md = build_md()
    with open(MD, "w") as f:
        f.write(md)
    print(f"Markdown written → {MD}")

    compile_pdf(MD, PDF, HDR)
