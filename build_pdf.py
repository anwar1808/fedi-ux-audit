"""
Build annotated PDF: report text + embedded screenshots side by side.
Font: Times-Roman (matches pandoc/xelatex output from previous version).
Each journey section begins on a new page.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage,
    Table, TableStyle, HRFlowable, KeepTogether, PageBreak
)
import os

ANN = "/Users/annie/fedi-ux-audit-repo/screenshots/annotated"
OUT = "/Users/annie/fedi-ux-audit-repo/fedi-ux-audit-annotated.pdf"

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

# ── Colours ────────────────────────────────────────────────────────────────────
RED    = colors.HexColor("#CC2222")
ORANGE = colors.HexColor("#C47A00")
GREEN  = colors.HexColor("#1A6B3C")
DARK   = colors.HexColor("#111111")
MID    = colors.HexColor("#444444")
LIGHT  = colors.HexColor("#777777")
RULE   = colors.HexColor("#CCCCCC")

# ── Styles — Times-Roman to match pandoc/xelatex output ───────────────────────
TITLE = ParagraphStyle("Title",
    fontName="Times-Bold", fontSize=22,
    textColor=DARK, spaceAfter=4, spaceBefore=0)

SUBTITLE = ParagraphStyle("Subtitle",
    fontName="Times-Roman", fontSize=10,
    textColor=LIGHT, spaceAfter=2, leading=14)

H2 = ParagraphStyle("H2",
    fontName="Times-Bold", fontSize=14,
    textColor=DARK, spaceAfter=6, spaceBefore=6)

H3 = ParagraphStyle("H3",
    fontName="Times-Bold", fontSize=10,
    textColor=MID, spaceAfter=3, spaceBefore=6)

BODY = ParagraphStyle("Body",
    fontName="Times-Roman", fontSize=10,
    textColor=DARK, leading=15, spaceAfter=6,
    alignment=TA_JUSTIFY)

ITALIC = ParagraphStyle("Italic",
    fontName="Times-Italic", fontSize=10,
    textColor=MID, leading=15, spaceAfter=6)

BOLD_LABEL = ParagraphStyle("BoldLabel",
    fontName="Times-Bold", fontSize=10,
    textColor=DARK, spaceAfter=4, spaceBefore=10)

META = ParagraphStyle("Meta",
    fontName="Times-Roman", fontSize=9,
    textColor=LIGHT, spaceAfter=2)

TABLE_HEAD = ParagraphStyle("TH",
    fontName="Times-Bold", fontSize=9, textColor=DARK)

TABLE_CELL = ParagraphStyle("TC",
    fontName="Times-Roman", fontSize=9, textColor=DARK, leading=13)

TABLE_CELL_BOLD = ParagraphStyle("TCB",
    fontName="Times-Bold", fontSize=9, textColor=DARK)


# ── Helpers ────────────────────────────────────────────────────────────────────
def screenshot(filename, width_cm=5.4):
    path = os.path.join(ANN, filename)
    if not os.path.exists(path):
        return Spacer(1, 2*cm)
    w = width_cm * cm
    h = w * (2400 / 1080)   # screenshots are 1080×2400
    return RLImage(path, width=w, height=h)


def side_by_side(ss_file, paragraphs, img_width_cm=5.4):
    col_w   = img_width_cm * cm
    text_w  = CONTENT_W - col_w - 0.6*cm
    t = Table([[screenshot(ss_file, img_width_cm), paragraphs]],
              colWidths=[col_w, text_w])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
        ("LEFTPADDING",  (1,0), (1,0),   14),
    ]))
    return t


def rule():
    return HRFlowable(width="100%", thickness=0.5,
                      color=RULE, spaceAfter=10, spaceBefore=4)


def finding(severity, text):
    """Return list of flowables for one finding bullet."""
    if severity == "critical":
        label = '<font color="#CC2222"><b>●  Critical</b></font>'
    elif severity == "moderate":
        label = '<font color="#C47A00"><b>▲  Moderate</b></font>'
    else:
        label = '<font color="#1A6B3C"><b>✓  Works well</b></font>'
    return [
        Paragraph(f"{label} — {text}", BODY),
        Spacer(1, 3),
    ]


def scene(text):
    return [Paragraph(text, ITALIC), Spacer(1, 8)]


def two_col_screenshot_row(ss1, paras1, ss2, paras2, img_w=4.5):
    col_w  = img_w * cm
    half_w = CONTENT_W / 2
    def cell(ss, paras):
        t = Table([[screenshot(ss, img_w), paras]],
                  colWidths=[col_w, half_w - col_w - 0.4*cm])
        t.setStyle(TableStyle([
            ("VALIGN",       (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING",  (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING",   (0,0), (-1,-1), 0),
            ("BOTTOMPADDING",(0,0), (-1,-1), 0),
            ("LEFTPADDING",  (1,0), (1,0),  10),
        ]))
        return t
    row = Table([[cell(ss1, paras1), cell(ss2, paras2)]],
                colWidths=[half_w, half_w])
    row.setStyle(TableStyle([
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING",(0,0), (-1,-1), 0),
        ("TOPPADDING",  (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0),
        ("RIGHTPADDING",(0,0),(0,0), 12),
    ]))
    return row


def legend_table(data, col_widths):
    """Render a two-column legend table matching the original PDF style."""
    rows = []
    for i, (left, right) in enumerate(data):
        lp = Paragraph(left,  TABLE_HEAD if i == 0 else TABLE_CELL_BOLD)
        rp = Paragraph(right, TABLE_HEAD if i == 0 else TABLE_CELL)
        rows.append([lp, rp])
    t = Table(rows, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("FONTNAME",     (0,0), (-1,0),  "Times-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 9),
        ("BACKGROUND",   (0,0), (-1,0),  colors.HexColor("#EEEEEE")),
        ("GRID",         (0,0), (-1,-1), 0.4, RULE),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    # Colour severity symbols in left column
    sev_map = {"●": RED, "▲": ORANGE, "✓": GREEN}
    for i, (left, _) in enumerate(data[1:], start=1):
        c = sev_map.get(left.strip())
        if c:
            t.setStyle(TableStyle([
                ("TEXTCOLOR", (0,i), (0,i), c),
            ]))
    return t


# ── Build ──────────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(OUT, pagesize=A4,
                            leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=MARGIN, bottomMargin=MARGIN)
    story = []

    # ── Cover page ─────────────────────────────────────────────────────────────
    story += [
        Spacer(1, 1.0*cm),
        Paragraph("Fedi App — UX Audit", TITLE),
        Spacer(1, 0.3*cm),
        Paragraph("Version audited: 26.2.4", META),
        Paragraph("Platform: Android", META),
        Paragraph("Method: Live emulator walkthrough, Nielsen Norman Group heuristics", META),
        Paragraph("Date: February 2026", META),
        Spacer(1, 0.6*cm),
        rule(),
        Paragraph("<b>Executive Summary</b>", BOLD_LABEL),
        Paragraph(
            "Fedi is trying to do something genuinely ambitious — combine chat, payments, and mini apps "
            "inside a federated community model. That's a hard brief, and you can feel the vision behind it. "
            "But right now, the app is designed for people who already understand how it works. The onboarding "
            "drops users straight into federation jargon without explanation, the navigation is almost entirely "
            "unlabelled, and the app's core feature — the wallet — is locked behind a joining process that "
            "can leave someone completely stranded with no way forward. The visual design is clean and the "
            "intent is clear, but the gap between what the team understands and what a new user experiences "
            "is significant. These findings are organised in the order a real user would encounter them.",
            BODY),
    ]

    # ── Section 1: First Launch ────────────────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("1. First Launch", H2),
        rule(),
    ]
    story.append(
        side_by_side("01-splash.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "A calm, well-designed splash screen. Floating avatar bubbles, the Fedi logo, a short tagline. "
            "Two buttons — \"Get started\" and \"Restore access.\" First impressions are good."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("moderate",
            "The legal copy — \"By continuing, you agree to our Terms of Use & Privacy Policy\" — sits "
            "above the button in small grey text against a pastel gradient. The contrast is too low and "
            "the placement makes it easy to miss. For a financial app, this matters more than it might "
            "for a typical social app.") +
        finding("moderate",
            "\"Ask Fedi\" appears at the very bottom of the splash screen as a help affordance. It's a "
            "nice idea, but the placement is so peripheral that most users won't notice it.") +
        finding("ok",
            "Everything else on this screen works. The visual hierarchy is clear, the two-button layout "
            "is intuitive, and the avatar bubbles do a good job of communicating \"social network\" "
            "without needing to say it.")
    ))

    # ── Section 2: Federation Discovery ───────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("2. Federation Discovery — The First Wall", H2),
        rule(),
    ]
    story.append(
        side_by_side("02-federation-discovery.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "They tap \"Get started\" and land immediately on a screen titled \"Join or Create a "
            "Federation.\" There's a list of federations with \"Join\" buttons. No one has explained "
            "what a federation is yet."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("critical",
            "The word \"federation\" appears in the headline, the subheading, the tab labels, and every "
            "list item — before the user has any idea what it means. The subheading reads: "
            "<i>\"Federations are the homes for your personal wallets.\"</i> That's helpful, but it's "
            "doing too much work too late.") +
        finding("critical",
            "The federation list cards are not tappable. There's no detail view — no way to learn more "
            "about a federation before committing to it. The only action is \"Join.\" For something the "
            "app itself describes as \"the home for your personal wallet,\" this is a significant trust "
            "gap.") +
        finding("moderate",
            "Description text is truncated mid-sentence throughout the list "
            "(\"Privacy Sovereignty Fr…\", \"Feel free to use the wall…\"). Minor, but it reinforces "
            "a feeling of roughness.") +
        finding("moderate",
            "The three tabs at the top — Discover, Join, Create — have no clear visual active state "
            "and their distinction isn't explained.") +
        finding("ok",
            "\"Maybe Later\" at the bottom is the right call — it gives users an exit.")
    ))

    # ── Section 3: Joining a Federation ───────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("3. Joining a Federation — Errors, Loops, and a Disappearing Exit", H2),
        rule(),
    ]
    story.append(
        side_by_side("03-join-tos.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "They tap \"Join\" on one of the federations. A Terms of Service screen appears — titled "
            "simply \"Welcome\" — with the federation's full ToS linked as an external PDF. The user "
            "is being asked to accept terms they cannot read without leaving the app."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("critical",
            "The screen title is simply \"Welcome.\" There's no heading that signals this is a legal "
            "consent moment. The ToS is not shown in-app — only a link to an external PDF. A user is "
            "committing before they can read what they're agreeing to.") +
        finding("critical",
            "An error banner appears when connection fails: <i>\"Unable to connect. Try switching "
            "between Wi-Fi and cellular or disable your VPN.\"</i> The advice is generic, there is no "
            "retry button, and the banner persists across multiple subsequent screens — stacking over "
            "other UI elements.") +
        finding("critical",
            "\"View public federations\" on the QR scanner screen sounds like it should take you "
            "somewhere new. It takes you back to the federation list you just came from. No feedback, "
            "no explanation — just a loop.") +
        finding("critical",
            "Once a user has gone through the joining flow and returned to the federation list, "
            "\"Maybe Later\" is gone. Pressing the system back button exits the app entirely. The user "
            "is effectively walled in — no way to reach the main app if joining fails.") +
        finding("moderate",
            "The camera permission screen that appears has no heading and doesn't clarify whether "
            "tapping Continue grants permission or defers it.") +
        finding("moderate",
            "The QR scanner screen has no instruction text. A new user has no idea what to point "
            "their camera at, or where they'd even get a federation QR code from.")
    ))

    # ── Section 4: Arriving in the App ────────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("4. Arriving in the App", H2),
        rule(),
    ]
    story.append(
        side_by_side("05-home-username-modal.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "If they do make it through — either by joining or by catching \"Maybe Later\" on first "
            "visit — they land on the home screen with a modal already waiting for them."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("critical",
            "The modal informs them that their display name is \"ambitious wolf.\" It was assigned "
            "automatically, without asking. For a chat and payments app, an auto-assigned username is "
            "jarring — this is an app where people will send each other money and messages. A prompt "
            "to set a real name before entering would feel much more considered.") +
        finding("moderate",
            "The display name shows as \"ambitious wolf #267f\" throughout the app. The #267f is a "
            "hash suffix that means nothing to a user. It's technical noise that's been surfaced "
            "without context or explanation.") +
        finding("moderate",
            "The home screen mixes three different content types — a pinned federation info banner, "
            "Community News, and Community Mini Apps — with no clear visual hierarchy separating "
            "them. It reads like a dashboard where everything has been given equal weight.") +
        finding("moderate",
            "The \"Fedi Global\" banner at the top has a QR grid icon in the top right. It's not "
            "labelled. It's not obviously tappable. A user has no way of knowing what it does.")
    ))

    # ── Section 5: Core Navigation ─────────────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("5. Core Navigation", H2),
        rule(),
    ]
    story.append(
        side_by_side("06-home.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "The bottom navigation has four icons. There are no labels on any of them."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("critical",
            "Four unlabelled icons in the bottom nav means four things the user has to guess. The "
            "active state is indicated only by a marginally bolder icon — easy to miss. Android "
            "Material Design guidelines recommend labels on bottom navigation precisely because "
            "of this.") +
        finding("critical",
            "Every tab — Chat, Mini Apps — opens with a bottom sheet upsell overlay that the user "
            "must dismiss before they can see the actual screen. Getting a promotional sheet every "
            "time you switch tabs is exhausting. The first impression of each section is an "
            "interruption, not the content itself.") +
        finding("critical",
            "The Wallet tab doesn't show a wallet for users who haven't joined a federation. It "
            "redirects to the federation wall with no explanation for why.") +
        finding("moderate",
            "The unlabelled QR icon on the Fedi Global banner has no affordance that it's tappable. "
            "A user has no way of knowing what it does.") +
        finding("moderate",
            "Four unlabelled header icons appear on every screen across the app. Almost no labelled "
            "navigation exists anywhere.")
    ))
    story.append(Spacer(1, 0.5*cm))

    # Chat + Mini Apps side by side
    story.append(
        two_col_screenshot_row(
            "07-chat.png",
            [Paragraph("Chat screen", H3)] +
            finding("moderate",
                "The Chat empty state — \"No messages in this group yet.\" — is just text. No "
                "illustration, no suggestion of what to do next, no pointer to the + button.") +
            finding("critical",
                "Promotional bottom sheet appears every time the tab is opened, blocking the "
                "content behind it."),
            "08-mini-apps.png",
            [Paragraph("Mini Apps screen", H3)] +
            finding("moderate",
                "The app icon grid mixes wildly inconsistent icon styles — there is no visual "
                "coherence across the grid.") +
            finding("critical",
                "Promotional bottom sheet appears again on first open, covering all content."),
        )
    )

    # ── Section 6: Settings & Profile ─────────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("6. Settings & Profile", H2),
        rule(),
    ]
    story.append(
        side_by_side("09-settings-top.png", [
            Paragraph("<i>What the user experiences:</i>", H3),
        ] + scene(
            "The profile icon in the header opens a settings screen — but the first thing they see "
            "isn't profile options. It's a large QR code."
        ) + [Paragraph("<i>Findings:</i>", H3)] +
        finding("critical",
            "The QR code sits at the very top of the settings screen with no label, no heading, no "
            "explanation of what it is or what scanning it would do. Is it a wallet address? A profile "
            "link? A login code? A user has no way to know.") +
        finding("moderate",
            "The display name shows \"#267f\" — a hash suffix that means nothing to a regular user.") +
        finding("moderate",
            "\"Nostr Details\" appears in the settings list without explanation. Most users won't "
            "know what Nostr is.")
    ))
    story.append(Spacer(1, 0.5*cm))

    story.append(
        two_col_screenshot_row(
            "10-settings-bottom.png",
            [Paragraph("Settings — icon inconsistency", H3)] +
            finding("moderate",
                "\"Notification Settings\" and \"Fedi App Terms of Service\" use an external link "
                "icon instead of a chevron. The distinction is visually subtle and inconsistent with "
                "the rest of the list.") +
            finding("ok",
                "The settings content itself is well-structured — Personal Backup, PIN Access, "
                "Language, Display currency, Ask Fedi. The bones are good."),
            "11-settings-footer.png",
            [Paragraph("Settings — footer", H3)] +
            finding("moderate",
                "\"Fedimint 0.9.1\" is internal technical versioning that adds noise for a regular "
                "user.") +
            finding("moderate",
                "\"Share logs\" has no icon, no chevron, and no visual affordance that it's "
                "tappable. It appears as plain text floating below the version number."),
        )
    )

    # ── Appendix: Priority Matrix ──────────────────────────────────────────────
    story += [
        PageBreak(),
        Paragraph("Appendix: Priority Matrix", H2),
        rule(),
        Spacer(1, 6),
    ]

    matrix_rows = [
        ["Screen / Area", "Finding", "Heuristic", "Severity"],
        ["Federation Discovery", "No explanation of what a federation is before asking users to join one", "H2", "●"],
        ["Federation Discovery", "Federation cards are not tappable — no detail view before committing to join", "H5", "●"],
        ["Joining Flow", "Error banner persists across multiple screens, stacking over other UI", "H1", "●"],
        ["Joining Flow", "\"View public federations\" loops back to the same screen with no feedback", "H3", "●"],
        ["Joining Flow", "\"Maybe Later\" disappears after navigating through the flow", "H3", "●"],
        ["Joining Flow", "Back button exits app entirely — no path to main UI if joining fails", "H3", "●"],
        ["Arriving in App", "Display name auto-assigned without asking (\"ambitious wolf\")", "H2", "●"],
        ["Wallet Tab", "Redirects to federation wall with no explanation", "H1", "●"],
        ["Core Navigation", "All four bottom nav tabs are unlabelled", "H4", "●"],
        ["Core Navigation", "Every tab triggers a promotional bottom sheet on first open", "H8", "●"],
        ["Settings", "QR code at top of settings has no label or explanation", "H6", "●"],
        ["Joining Flow", "Camera permission screen doesn't clarify whether Continue grants or defers", "H5", "▲"],
        ["Joining Flow", "QR scanner has no instruction text — user doesn't know what to scan", "H6", "▲"],
        ["Joining Flow", "Error banner offers no retry action", "H9", "▲"],
        ["Federation Discovery", "Description text truncated mid-sentence throughout list", "H8", "▲"],
        ["Federation Discovery", "Three tabs (Discover/Join/Create) have no active state and no explanation", "H4", "▲"],
        ["Arriving in App", "\"#54e2\" hash suffix shown in display name with no explanation", "H2", "▲"],
        ["Arriving in App", "Home screen gives equal visual weight to three different content types", "H8", "▲"],
        ["Arriving in App", "\"Fedi Global\" QR icon in home banner is unlabelled and non-obvious", "H6", "▲"],
        ["Chat Screen", "Empty state is bare text with no illustration or call to action", "H7", "▲"],
        ["Core Navigation", "Four unlabelled header icons on every screen", "H4", "▲"],
        ["Mini Apps", "App icon grid mixes wildly inconsistent icon styles", "H4", "▲"],
        ["Settings", "\"Nostr Details\" listed with no explanation of what Nostr is", "H2", "▲"],
        ["Settings", "External link icons vs chevrons are inconsistent and unexplained", "H4", "▲"],
        ["Settings", "\"Share logs\" has no visual affordance — looks like plain text", "H6", "▲"],
        ["Settings", "Three different background treatments in one screen", "H8", "▲"],
        ["Settings", "\"Fedimint 0.9.1\" version shown — internal technical noise for users", "H8", "▲"],
        ["Splash Screen", "Legal consent text is low contrast and easy to miss", "H5", "▲"],
        ["Splash Screen", "\"Ask Fedi\" help link is too peripheral to be noticed", "H10", "▲"],
        ["Splash Screen", "Two-button layout (Get started / Restore access) is clear and familiar", "H4", "✓"],
        ["Splash Screen", "Avatar bubbles convey \"social network\" without text", "H6", "✓"],
        ["Camera Permission", "\"This can be updated later\" reduces anxiety about granting permission", "H5", "✓"],
        ["Settings", "Good range of settings — backup, PIN, language, currency", "H7", "✓"],
        ["Settings", "\"Ask Fedi\" dedicated help entry in settings", "H10", "✓"],
        ["Settings", "Settings list structure (icon + label + chevron) is clear and scannable", "H6", "✓"],
    ]

    sev_hex = {"●": "#CC2222", "▲": "#C47A00", "✓": "#1A6B3C"}
    col_widths = [3.0*cm, 9.6*cm, 1.5*cm, 1.3*cm]

    table_data = []
    for i, row in enumerate(matrix_rows):
        screen    = Paragraph(row[0], TABLE_HEAD if i==0 else TABLE_CELL)
        finding_p = Paragraph(row[1], TABLE_HEAD if i==0 else TABLE_CELL)
        heuristic = Paragraph(row[2], TABLE_HEAD if i==0 else TABLE_CELL)
        sev_sym   = row[3]
        if i == 0:
            sev_p = Paragraph(sev_sym, TABLE_HEAD)
        else:
            hx = sev_hex.get(sev_sym, "#111111")
            sev_p = Paragraph(
                f'<font color="{hx}"><b>{sev_sym}</b></font>',
                TABLE_CELL_BOLD)
        table_data.append([screen, finding_p, heuristic, sev_p])

    matrix = Table(table_data, colWidths=col_widths, repeatRows=1)
    matrix.setStyle(TableStyle([
        ("FONTNAME",     (0,0), (-1,0),  "Times-Bold"),
        ("FONTSIZE",     (0,0), (-1,-1), 8.5),
        ("BACKGROUND",   (0,0), (-1,0),  colors.HexColor("#EEEEEE")),
        ("GRID",         (0,0), (-1,-1), 0.4, RULE),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(matrix)

    # ── Legends — exactly matching the original PDF ────────────────────────────
    story += [
        Spacer(1, 1.0*cm),
        rule(),
        Paragraph("<b>Severity Legend</b>", BOLD_LABEL),
    ]

    sev_legend = [
        ["Symbol", "Meaning"],
        ["●", "Critical — significant impact on usability, should be prioritised"],
        ["▲", "Moderate — noticeable friction or inconsistency, worth addressing"],
        ["✓", "Works well — effective design worth preserving"],
    ]
    story.append(legend_table(sev_legend, [2.0*cm, 13.4*cm]))
    story.append(Spacer(1, 0.8*cm))

    story.append(
        Paragraph(
            "<b>Heuristics Reference</b> <i>(Nielsen Norman Group, 10 Usability Heuristics)</i>",
            BOLD_LABEL)
    )

    heuristics_legend = [
        ["Code", "Heuristic"],
        ["H1",  "Visibility of system status"],
        ["H2",  "Match between system and the real world"],
        ["H3",  "User control and freedom"],
        ["H4",  "Consistency and standards"],
        ["H5",  "Error prevention"],
        ["H6",  "Recognition rather than recall"],
        ["H7",  "Flexibility and efficiency of use"],
        ["H8",  "Aesthetic and minimalist design"],
        ["H9",  "Help users recognise, diagnose, and recover from errors"],
        ["H10", "Help and documentation"],
    ]
    story.append(legend_table(heuristics_legend, [2.0*cm, 13.4*cm]))

    doc.build(story)
    print(f"PDF written → {OUT}")
    print(f"Size: {os.path.getsize(OUT)/1024/1024:.1f} MB")


if __name__ == "__main__":
    build()
