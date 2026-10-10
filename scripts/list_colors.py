import os
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"
svgs = ['hero.svg', 'about-life.svg', 'stack.svg', 'id-dashboard.svg', 'connect.svg']

color_counts = {}
for s in svgs:
    path = os.path.join(assets_dir, s)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Exclude base64 strings
    content_no_b64 = re.sub(r'data:image/[^"]+', '', content)
    hexes = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})', content_no_b64)
    for h in hexes:
        hl = '#' + h.lower()
        color_counts[hl] = color_counts.get(hl, 0) + 1

print("Total unique colors found:", len(color_counts))
for c, count in sorted(color_counts.items(), key=lambda x: -x[1]):
    print(f"  {c}: {count}")
