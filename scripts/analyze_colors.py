import os
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"
svgs = ['hero.svg', 'about-life.svg', 'stack.svg', 'id-dashboard.svg', 'connect.svg']

for s in svgs:
    path = os.path.join(assets_dir, s)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    grads = re.findall(r'<linearGradient id="([^"]+)"[\s\S]*?</linearGradient>', content)
    rad_grads = re.findall(r'<radialGradient id="([^"]+)"[\s\S]*?</radialGradient>', content)
    print(f"=== {s} ===")
    print(f"  linearGradients: {len(grads)}")
    for gid in grads:
        full = re.search(r'<linearGradient id="' + gid + r'"[\s\S]*?</linearGradient>', content).group(0)
        stops = re.findall(r'stop-color="([^"]+)"', full)
        print(f"    {gid}: {stops}")
    for gid in rad_grads:
        full = re.search(r'<radialGradient id="' + gid + r'"[\s\S]*?</radialGradient>', content).group(0)
        stops = re.findall(r'stop-color="([^"]+)"', full)
        print(f"    RADIAL {gid}: {stops}")
    
    # Also find all hex colors
    hexes = set(re.findall(r'#([0-9a-fA-F]{3,8})', content))
    print(f"  Unique colors count: {len(hexes)}")
