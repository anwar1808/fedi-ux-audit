"""
Annotate Fedi UX audit screenshots with red circles and arrows.
Outputs to screenshots/annotated/
"""
from PIL import Image, ImageDraw
import math, os

OUT_DIR = "/Users/annie/Annie-Claude/fedi-ux-audit/repo/screenshots/annotated"
IN_DIR  = "/Users/annie/Annie-Claude/fedi-ux-audit/repo/screenshots"
os.makedirs(OUT_DIR, exist_ok=True)

RED = (220, 30, 30)
W = 10   # line width for circles/rects
AW = 10  # arrow line width

def circle(draw, cx, cy, rx, ry):
    draw.ellipse([(cx-rx, cy-ry), (cx+rx, cy+ry)], outline=RED, width=W)

def rect(draw, x1, y1, x2, y2):
    draw.rectangle([(x1, y1), (x2, y2)], outline=RED, width=W)

def arrow(draw, x1, y1, x2, y2, size=40):
    draw.line([(x1, y1), (x2, y2)], fill=RED, width=AW)
    angle = math.atan2(y2 - y1, x2 - x1)
    for da in (-math.pi/6, math.pi/6):
        ax = x2 - size * math.cos(angle + da)
        ay = y2 - size * math.sin(angle + da)
        draw.polygon([(x2, y2), (int(ax), int(ay)),
                      (int(x2 - size*0.6*math.cos(angle)),
                       int(y2 - size*0.6*math.sin(angle)))], fill=RED)

# ── 01 Splash ──────────────────────────────────────────────────────────────────
def annotate_01():
    img = Image.open(f"{IN_DIR}/01-splash.png").copy()
    d = ImageDraw.Draw(img)
    # Legal consent text — low contrast, easy to miss
    rect(d, 180, 1740, 900, 1870)
    arrow(d, 980, 1640, 860, 1755, size=45)
    # "Ask Fedi" — too peripheral at very bottom
    rect(d, 555, 2200, 790, 2290)
    img.save(f"{OUT_DIR}/01-splash.png")
    print("01-splash.png done")

# ── 02 Federation Discovery ────────────────────────────────────────────────────
def annotate_02():
    img = Image.open(f"{IN_DIR}/02-federation-discovery.png").copy()
    d = ImageDraw.Draw(img)
    # Jargon headline — "Wallets need Federations" / "Join or Create a Federation"
    rect(d, 40, 60, 1040, 290)
    # Tabs with no clear active state
    rect(d, 40, 295, 1040, 400)
    # Truncated description on first card (approx y=445–495)
    arrow(d, 1000, 360, 850, 460, size=40)
    rect(d, 190, 440, 880, 500)
    img.save(f"{OUT_DIR}/02-federation-discovery.png")
    print("02-federation-discovery.png done")

# ── 03 Join ToS ───────────────────────────────────────────────────────────────
def annotate_03():
    img = Image.open(f"{IN_DIR}/03-join-tos.png").copy()
    d = ImageDraw.Draw(img)
    # Minimal description — no actual ToS content shown in-app
    rect(d, 60, 650, 1020, 820)
    # External PDF link — ToS not readable in-app
    rect(d, 60, 2210, 1020, 2340)
    arrow(d, 540, 2130, 540, 2205, size=40)
    img.save(f"{OUT_DIR}/03-join-tos.png")
    print("03-join-tos.png done")

# ── 05 Home — username modal ───────────────────────────────────────────────────
def annotate_05():
    img = Image.open(f"{IN_DIR}/05-home-username-modal.png").copy()
    d = ImageDraw.Draw(img)
    # Auto-assigned display name
    rect(d, 230, 1120, 850, 1260)
    arrow(d, 150, 1000, 310, 1130, size=45)
    img.save(f"{OUT_DIR}/05-home-username-modal.png")
    print("05-home-username-modal.png done")

# ── 06 Home ───────────────────────────────────────────────────────────────────
def annotate_06():
    img = Image.open(f"{IN_DIR}/06-home.png").copy()
    d = ImageDraw.Draw(img)
    # Unlabelled bottom nav — 4 icons, no text
    rect(d, 0, 2130, 1080, 2360)
    arrow(d, 540, 2050, 540, 2125, size=45)
    # Unlabelled header icons (right side of header bar)
    rect(d, 700, 85, 1055, 195)
    # Unlabelled QR icon on Fedi Global banner
    circle(d, 905, 390, 65, 55)
    img.save(f"{OUT_DIR}/06-home.png")
    print("06-home.png done")

# ── 07 Chat ───────────────────────────────────────────────────────────────────
def annotate_07():
    img = Image.open(f"{IN_DIR}/07-chat.png").copy()
    d = ImageDraw.Draw(img)
    # Promotional bottom sheet — appears every time you open the tab
    rect(d, 0, 1360, 1080, 2100)
    arrow(d, 200, 1250, 200, 1355, size=45)
    # Bare empty state text above the sheet
    rect(d, 30, 370, 700, 445)
    img.save(f"{OUT_DIR}/07-chat.png")
    print("07-chat.png done")

# ── 08 Mini Apps ──────────────────────────────────────────────────────────────
def annotate_08():
    img = Image.open(f"{IN_DIR}/08-mini-apps.png").copy()
    d = ImageDraw.Draw(img)
    # Inconsistent icon styles across the grid
    rect(d, 0, 220, 1080, 1100)
    arrow(d, 1000, 140, 900, 225, size=40)
    # Promotional bottom sheet again
    rect(d, 0, 1360, 1080, 2100)
    img.save(f"{OUT_DIR}/08-mini-apps.png")
    print("08-mini-apps.png done")

# ── 09 Settings top ───────────────────────────────────────────────────────────
def annotate_09():
    img = Image.open(f"{IN_DIR}/09-settings-top.png").copy()
    d = ImageDraw.Draw(img)
    # QR code at top — no label or explanation (extends from ~y=90 to y=1130)
    rect(d, 50, 90, 1030, 1130)
    arrow(d, 120, 1200, 120, 1135, size=45)
    # "#267f" hash suffix in display name — [695,1263][818,1316]
    circle(d, 756, 1289, 140, 75)
    img.save(f"{OUT_DIR}/09-settings-top.png")
    print("09-settings-top.png done")

# ── 10 Settings — external link inconsistency ─────────────────────────────────
def annotate_10():
    img = Image.open(f"{IN_DIR}/10-settings-bottom.png").copy()
    d = ImageDraw.Draw(img)
    # External link icons on Notification Settings & Terms of Service
    # (vs chevrons used everywhere else)
    rect(d, 800, 740, 1040, 850)   # Notification Settings icon
    rect(d, 800, 850, 1040, 960)   # Terms of Service icon
    arrow(d, 1000, 650, 940, 745, size=40)
    img.save(f"{OUT_DIR}/10-settings-bottom.png")
    print("10-settings-bottom.png done")

# ── 11 Settings footer ────────────────────────────────────────────────────────
def annotate_11():
    img = Image.open(f"{IN_DIR}/11-settings-footer.png").copy()
    d = ImageDraw.Draw(img)
    # "Fedimint 0.9.1" — internal technical noise [371,2140][709,2186]
    rect(d, 330, 2120, 760, 2200)
    # "Share logs" — no visual affordance [451,2207][628,2253]
    rect(d, 390, 2185, 700, 2280)
    arrow(d, 900, 2050, 770, 2130, size=40)
    img.save(f"{OUT_DIR}/11-settings-footer.png")
    print("11-settings-footer.png done")

if __name__ == "__main__":
    annotate_01()
    annotate_02()
    annotate_03()
    annotate_05()
    annotate_06()
    annotate_07()
    annotate_08()
    annotate_09()
    annotate_10()
    annotate_11()
    print("\nAll annotations done.")
