import os
import xml.etree.ElementTree as ET

svg_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"
files = ["hero.svg", "about-life.svg", "stack.svg", "id-dashboard.svg", "connect.svg"]

all_valid = True
for f in files:
    path = os.path.join(svg_dir, f)
    try:
        ET.parse(path)
        size_kb = os.path.getsize(path) / 1024
        print(f"[OK] {f} ({size_kb:.1f} KB) is perfectly valid XML!")
    except Exception as e:
        print(f"[ERROR] {f} XML error: {e}")
        all_valid = False

if all_valid:
    print("\nALL 5 SVGS ARE 100% SYNTACTICALLY VALID XML!")
