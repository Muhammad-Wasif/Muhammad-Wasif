import os
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"
svgs = ['hero.svg', 'about-life.svg', 'stack.svg', 'id-dashboard.svg', 'connect.svg']

blue_shades = ['#247bff', '#1266ed', '#8bc6ff', '#73b0ff', '#8cc3ff', '#76afff', '#d2ecff', '#183b6e', '#11264a', '#294e79', '#2d527b', '#28558b', '#28476d', '#2c5b96', '#101c30', '#101c31', '#132842', '#0b1b33']
red_shades = ['#ff354f', '#ff1c3f', '#e44332', '#ff4d6d']

for s in svgs:
    path = os.path.join(assets_dir, s)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n==================== {s} ====================")
    for color in ['#247bff', '#ff354f', '#1266ed', '#ff1c3f', '#73b0ff', '#8cc3ff', '#183b6e', '#ff4d6d', '#11264a']:
        c_lower = color.lower()
        matches = [m.start() for m in re.finditer(re.escape(c_lower), content.lower())]
        if matches:
            print(f"  {color}: {len(matches)} occurrences")
            # show one sample context
            idx = matches[0]
            snippet = content[max(0, idx-40):min(len(content), idx+50)].replace('\n', ' ')
            print(f"    sample: {snippet}")
