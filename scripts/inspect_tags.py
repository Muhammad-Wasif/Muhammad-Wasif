import os
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"
files = ["hero.svg", "about-life.svg", "stack.svg", "id-dashboard.svg", "connect.svg"]

for f in files:
    path = os.path.join(assets_dir, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Strip base64
    no_b64 = re.sub(r'data:image/[^"]+', 'b64', content)
    
    # Find all occurrences of blue and red hexes
    print(f"\n=================== {f} ===================")
    for tag in re.findall(r'<[^>]+(?:247bff|ff354f|8bc6ff|1240bd|1266ed|ff1c3f|73b0ff|8cc3ff|76afff|d2ecff)[^>]*>', no_b64, re.IGNORECASE):
        # Truncate tag if too long
        print("TAG:", tag[:120])
