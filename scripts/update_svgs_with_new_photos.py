import os
import base64
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"

def load_b64(filename):
    path = os.path.join(assets_dir, filename)
    with open(path, "rb") as f:
        data = f.read()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")

print("Loading bitmaps...")
badge_b64 = load_b64("wasif_id_badge_612x470.png")
hero_b64  = load_b64("wasif_hero_922x1082.png")
conn_b64  = load_b64("megumi_connect_816x1224.png")

print(f"Badge b64: {len(badge_b64)} chars")
print(f"Hero b64:  {len(hero_b64)} chars")
print(f"Conn b64:  {len(conn_b64)} chars")

# ==============================================================
# 1. Update HERO.SVG
# ==============================================================
hero_path = os.path.join(assets_dir, "hero.svg")
with open(hero_path, "r", encoding="utf-8") as f:
    hero = f.read()

# Replace bitmap href
hero = re.sub(
    r'(<image id="hero-bitmap-0"\s+width="461"\s+height="541"\s+href=")[^"]+(")',
    r'\g<1>' + hero_b64 + r'\2',
    hero
)

with open(hero_path, "w", encoding="utf-8") as f:
    f.write(hero)
print("Updated hero.svg")

# ==============================================================
# 2. Update ABOUT-LIFE.SVG
# ==============================================================
about_path = os.path.join(assets_dir, "about-life.svg")
with open(about_path, "r", encoding="utf-8") as f:
    about = f.read()

about = re.sub(
    r'(<image id="about-life-bitmap-0"\s+width="461"\s+height="541"\s+href=")[^"]+(")',
    r'\g<1>' + hero_b64 + r'\2',
    about
)

with open(about_path, "w", encoding="utf-8") as f:
    f.write(about)
print("Updated about-life.svg")

# ==============================================================
# 3. Update ID-DASHBOARD.SVG
# ==============================================================
idd_path = os.path.join(assets_dir, "id-dashboard.svg")
with open(idd_path, "r", encoding="utf-8") as f:
    idd = f.read()

# Replace bitmap tag: update width="306" height="235" and href
idd = re.sub(
    r'<image id="id-dashboard-bitmap-0"\s+width="[^"]+"\s+height="[^"]+"\s+href="[^"]+"',
    f'<image id="id-dashboard-bitmap-0" width="306" height="235" href="{badge_b64}"',
    idd
)

# Replace symbol viewBox
idd = re.sub(
    r'<symbol id="id-dashboard-raster-0"\s+viewBox="[^"]+"\s+preserveAspectRatio="xMidYMid meet">',
    r'<symbol id="id-dashboard-raster-0" viewBox="0 0 306 235" preserveAspectRatio="xMidYMid meet">',
    idd
)

# Replace inner svg containers inside badge photo
# Old: <svg x="143" y="235" width="269" height="316" viewBox="0 0 1158 1358" overflow="hidden"><use width="1158" height="1358" href="#id-dashboard-raster-0"/></svg>
# New: <svg x="115" y="253" width="306" height="235" viewBox="0 0 306 235" overflow="hidden"><use width="306" height="235" href="#id-dashboard-raster-0"/></svg>
old_badge_svg = '<svg x="143" y="235" width="269" height="316" viewBox="0 0 1158 1358" overflow="hidden"><use width="1158" height="1358" href="#id-dashboard-raster-0"/></svg>'
new_badge_svg = '<svg x="115" y="253" width="306" height="235" viewBox="0 0 306 235" overflow="hidden"><use width="306" height="235" href="#id-dashboard-raster-0"/></svg>'

count = idd.count(old_badge_svg)
print(f"Found {count} instances of old_badge_svg in id-dashboard.svg")
idd = idd.replace(old_badge_svg, new_badge_svg)

with open(idd_path, "w", encoding="utf-8") as f:
    f.write(idd)
print("Updated id-dashboard.svg")

# ==============================================================
# 4. Update CONNECT.SVG
# ==============================================================
conn_path = os.path.join(assets_dir, "connect.svg")
with open(conn_path, "r", encoding="utf-8") as f:
    conn = f.read()

conn = re.sub(
    r'(<image id="connect-bitmap-0"\s+width="408"\s+height="612"\s+href=")[^"]+(")',
    r'\g<1>' + conn_b64 + r'\2',
    conn
)

with open(conn_path, "w", encoding="utf-8") as f:
    f.write(conn)
print("Updated connect.svg")

print("\nALL SVGS UPDATED SUCCESSFULLY!")
