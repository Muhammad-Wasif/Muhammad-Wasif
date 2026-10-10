import os
import re

assets_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"

def read_svg(name):
    with open(os.path.join(assets_dir, name), "r", encoding="utf-8") as f:
        return f.read()

def write_svg(name, content):
    with open(os.path.join(assets_dir, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {name}: {len(content)} bytes")

# -------------------------------------------------------------
# 1. HERO.SVG
# -------------------------------------------------------------
hero = read_svg("hero.svg")

# Aurora: blue -> emerald green
hero = hero.replace('stop-color="#8bc6ff"', 'stop-color="#6ee7b7"')
hero = hero.replace('stop-color="#247bff"', 'stop-color="#10b981"')
hero = hero.replace('stop-color="#1240bd"', 'stop-color="#047857"')

# Hairline & Foil: blue -> green, red -> white
hero = hero.replace('stop-color="#ff354f"', 'stop-color="#ffffff"')
hero = hero.replace('stop-color="#1266ed"', 'stop-color="#059669"')
hero = hero.replace('stop-color="#ff1c3f"', 'stop-color="#ffffff"')
hero = hero.replace('stop-color="#76afff"', 'stop-color="#34d399"')
hero = hero.replace('stop-color="#d2ecff"', 'stop-color="#a7f3d0"')

# Chevron accent marks & badge
hero = hero.replace('fill="#247bff"', 'fill="#10b981"')
hero = hero.replace('stroke="#247bff"', 'stroke="#10b981"')
hero = hero.replace('stroke="#2d527b"', 'stroke="#1b4d3e"')

write_svg("hero.svg", hero)

# -------------------------------------------------------------
# 2. ABOUT-LIFE.SVG
# -------------------------------------------------------------
about = read_svg("about-life.svg")

about = about.replace('stop-color="#8bc6ff"', 'stop-color="#6ee7b7"')
about = about.replace('stop-color="#247bff"', 'stop-color="#10b981"')
about = about.replace('stop-color="#1240bd"', 'stop-color="#047857"')
about = about.replace('stop-color="#ff354f"', 'stop-color="#ffffff"')
about = about.replace('stop-color="#1266ed"', 'stop-color="#059669"')
about = about.replace('stop-color="#ff1c3f"', 'stop-color="#ffffff"')
about = about.replace('stop-color="#76afff"', 'stop-color="#34d399"')
about = about.replace('stop-color="#d2ecff"', 'stop-color="#a7f3d0"')

# Replace blue accents with green (#10b981), red accents with white (#ffffff)
about = about.replace('fill="#247bff"', 'fill="#10b981"')
about = about.replace('stroke="#247bff"', 'stroke="#10b981"')
about = about.replace('fill="#ff354f"', 'fill="#ffffff"')
about = about.replace('stroke="#ff354f"', 'stroke="#ffffff"')

write_svg("about-life.svg", about)

# -------------------------------------------------------------
# 3. STACK.SVG
# -------------------------------------------------------------
stack = read_svg("stack.svg")

stack = stack.replace('stop-color="#8bc6ff"', 'stop-color="#6ee7b7"')
stack = stack.replace('stop-color="#247bff"', 'stop-color="#10b981"')
stack = stack.replace('stop-color="#1240bd"', 'stop-color="#047857"')
stack = stack.replace('stop-color="#ff354f"', 'stop-color="#ffffff"')
stack = stack.replace('stop-color="#1266ed"', 'stop-color="#059669"')
stack = stack.replace('stop-color="#ff1c3f"', 'stop-color="#ffffff"')
stack = stack.replace('stop-color="#76afff"', 'stop-color="#34d399"')
stack = stack.replace('stop-color="#d2ecff"', 'stop-color="#a7f3d0"')

stack = stack.replace('fill="#247bff"', 'fill="#10b981"')
stack = stack.replace('stroke="#247bff"', 'stroke="#10b981"')
stack = stack.replace('fill="#ff354f"', 'fill="#ffffff"')
stack = stack.replace('stroke="#ff354f"', 'stroke="#ffffff"')

write_svg("stack.svg", stack)

# -------------------------------------------------------------
# 4. ID-DASHBOARD.SVG
# -------------------------------------------------------------
idd = read_svg("id-dashboard.svg")

idd = idd.replace('stop-color="#8bc6ff"', 'stop-color="#6ee7b7"')
idd = idd.replace('stop-color="#247bff"', 'stop-color="#10b981"')
idd = idd.replace('stop-color="#1240bd"', 'stop-color="#047857"')
idd = idd.replace('stop-color="#ff354f"', 'stop-color="#ffffff"')
idd = idd.replace('stop-color="#1266ed"', 'stop-color="#059669"')
idd = idd.replace('stop-color="#ff1c3f"', 'stop-color="#ffffff"')
idd = idd.replace('stop-color="#76afff"', 'stop-color="#34d399"')
idd = idd.replace('stop-color="#d2ecff"', 'stop-color="#a7f3d0"')

# Animated border around badge photo:
idd = idd.replace('stroke="#8cc3ff"', 'stroke="#6ee7b7"')

# Number "12517" in badge:
idd = idd.replace('fill="#247bff" style="fill:#247bff"', 'fill="#10b981" style="fill:#10b981"')

# "BS DATA SCIENCE" pill:
idd = idd.replace('<rect x="126" y="450" width="128" height="28" rx="5" fill="#247bff" stroke="none" />',
                  '<rect x="126" y="450" width="128" height="28" rx="5" fill="#10b981" stroke="none" />')

# Badge top stripe (was red):
idd = idd.replace('<rect x="95" y="193" width="346" height="7" rx="3" fill="#ff354f" stroke="none" />',
                  '<rect x="95" y="193" width="346" height="7" rx="3" fill="#ffffff" stroke="none" />')

# Counters:
# Metric 1: DATA & AI (was red #ff354f -> now white #ffffff)
idd = re.sub(r'fill="#ff354f" style="fill:#ff354f"', 'fill="#ffffff" style="fill:#ffffff"', idd)
# Metric 2 & 3: REPOSITORIES and COMMITS (was blue #73b0ff -> now mint #34d399)
idd = re.sub(r'fill="#73b0ff" style="fill:#73b0ff"', 'fill="#34d399" style="fill:#34d399"', idd)

# Star in featured repos header (was #ff354f -> now white #ffffff):
idd = idd.replace('stroke="#ff354f"', 'stroke="#ffffff"')

# Featured repo progress bars:
idd = re.sub(r'(<rect x="520" y="\d+" width="[^"]+" height="12" rx="3" fill=")#247bff(")',
             r'\g<1>#10b981\2', idd)

# NOW pill at bottom:
# Background was red #ff354f -> now white #ffffff, text was #f2f5ff -> now #070b16 (high-contrast dark on white)
idd = idd.replace('<rect x="537" y="652" width="76" height="28" rx="5" fill="#ff354f" stroke="none" />',
                  '<rect x="537" y="652" width="76" height="28" rx="5" fill="#ffffff" stroke="none" />')
idd = idd.replace('<text x="549" y="671" font-size="10" fill="#f2f5ff" style="fill:#f2f5ff" class="mono" letter-spacing="1">NOW</text>',
                  '<text x="549" y="671" font-size="10" fill="#070b16" style="fill:#070b16; font-weight:700" class="mono" letter-spacing="1">NOW</text>')

# Background watermark "THE":
idd = idd.replace('fill="#11264a" style="fill:#11264a"', 'fill="#0d3a27" style="fill:#0d3a27"')

write_svg("id-dashboard.svg", idd)

# -------------------------------------------------------------
# 5. CONNECT.SVG
# -------------------------------------------------------------
conn = read_svg("connect.svg")

# Palette replacements:
conn = conn.replace('stop-color="#8bc6ff"', 'stop-color="#6ee7b7"')
conn = conn.replace('stop-color="#247bff"', 'stop-color="#10b981"')
conn = conn.replace('stop-color="#1240bd"', 'stop-color="#047857"')
conn = conn.replace('stop-color="#ff354f"', 'stop-color="#ffffff"')
conn = conn.replace('stop-color="#1266ed"', 'stop-color="#059669"')
conn = conn.replace('stop-color="#ff1c3f"', 'stop-color="#ffffff"')
conn = conn.replace('stop-color="#76afff"', 'stop-color="#34d399"')
conn = conn.replace('stop-color="#d2ecff"', 'stop-color="#a7f3d0"')

# Slashes top right:
conn = re.sub(r'(<path d="M11\d\d 91l9 0 -7 18h-9Z" fill=")#ff354f("/>)',
              r'\g<1>#ffffff\2', conn)

# Watermark "CONNECT.":
conn = conn.replace('fill="#183b6e" style="fill:#183b6e"', 'fill="#0d3a27" style="fill:#0d3a27"')

# CSS injection for hover interactivity
hover_css = """
<style>
  .card-link { cursor: pointer; text-decoration: none; }
  .card-group { transition: all 0.25s ease; }
  .card-group-green:hover .card-bg { stroke: #10b981 !important; fill: #0f261f !important; }
  .card-group-white:hover .card-bg { stroke: #ffffff !important; fill: #1c2636 !important; }
  .card-group:hover .nudge { transform: translate(6px, 0); }
  .nudge { transition: transform 0.25s ease; }
</style>
"""

# Insert hover CSS before </defs>
conn = conn.replace('</defs>', hover_css + '</defs>')

# Construct the 4 Interactive Link Cards
discord_path = "M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"
linkedin_path = "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"
gmail_path = "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"

card1_xml = f'''<a href="https://www.linkedin.com/in/muhammad-wasif-310324398/" xlink:href="https://www.linkedin.com/in/muhammad-wasif-310324398/" target="_blank" rel="noopener noreferrer" class="card-link" style="cursor:pointer;text-decoration:none;"><g class="card-group card-group-green"><rect x="507" y="148" width="647" height="86" rx="10" fill="#101c30" stroke="#1c4738" pointer-events="all" class="card-bg" style="cursor:pointer;"/><rect x="507" y="148" width="4" height="86" rx="2" fill="#10b981" stroke="none" pointer-events="none"/><g transform="translate(530 174) scale(1.3333333333333333)" fill="#10b981" pointer-events="none"><path d="{linkedin_path}"/></g><text x="584" y="185" font-size="31" class="" pointer-events="none">LinkedIn</text><text x="585" y="210" font-size="12" fill="#8facd4" style="fill:#8facd4" class="mono" pointer-events="none">Connect &amp; exchange ideas</text><g class="nudge" pointer-events="none"><g transform="translate(1100 178) scale(1.1)" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18 M15 6l6 6-6 6"/></g></g></g></a>'''

card2_xml = f'''<a href="mailto:wasifalibhatti12517@gmail.com" xlink:href="mailto:wasifalibhatti12517@gmail.com" target="_blank" rel="noopener noreferrer" class="card-link" style="cursor:pointer;text-decoration:none;"><g class="card-group card-group-white"><rect x="507" y="255" width="647" height="86" rx="10" fill="#101c30" stroke="#334155" pointer-events="all" class="card-bg" style="cursor:pointer;"/><rect x="507" y="255" width="4" height="86" rx="2" fill="#ffffff" stroke="none" pointer-events="none"/><g transform="translate(530 281) scale(1.3333333333333333)" fill="#ffffff" pointer-events="none"><path d="{gmail_path}"/></g><text x="584" y="292" font-size="31" class="" pointer-events="none">Gmail</text><text x="585" y="317" font-size="12" fill="#8facd4" style="fill:#8facd4" class="mono" pointer-events="none">wasifalibhatti12517@gmail.com</text><g class="nudge" pointer-events="none"><g transform="translate(1100 285) scale(1.1)" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18 M15 6l6 6-6 6"/></g></g></g></a>'''

card3_xml = f'''<a href="https://discord.com/users/1222455872668827669" xlink:href="https://discord.com/users/1222455872668827669" target="_blank" rel="noopener noreferrer" class="card-link" style="cursor:pointer;text-decoration:none;"><g class="card-group card-group-green"><rect x="507" y="362" width="647" height="86" rx="10" fill="#101c30" stroke="#1c4738" pointer-events="all" class="card-bg" style="cursor:pointer;"/><rect x="507" y="362" width="4" height="86" rx="2" fill="#10b981" stroke="none" pointer-events="none"/><g transform="translate(530 388) scale(1.3333333333333333)" fill="#10b981" pointer-events="none"><path d="{discord_path}"/></g><text x="584" y="399" font-size="31" class="" pointer-events="none">Discord</text><text x="585" y="424" font-size="12" fill="#8facd4" style="fill:#8facd4" class="mono" pointer-events="none">Chat &amp; collaborate on Discord</text><g class="nudge" pointer-events="none"><g transform="translate(1100 392) scale(1.1)" fill="none" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18 M15 6l6 6-6 6"/></g></g></g></a>'''

card4_xml = '''<a href="https://majorweb.netlify.app/" xlink:href="https://majorweb.netlify.app/" target="_blank" rel="noopener noreferrer" class="card-link" style="cursor:pointer;text-decoration:none;"><g class="card-group card-group-white"><rect x="507" y="469" width="647" height="86" rx="10" fill="#101c30" stroke="#334155" pointer-events="all" class="card-bg" style="cursor:pointer;"/><rect x="507" y="469" width="4" height="86" rx="2" fill="#ffffff" stroke="none" pointer-events="none"/><g transform="translate(530 495) scale(1.3333333333333333)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" pointer-events="none"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></g><text x="584" y="506" font-size="31" class="" pointer-events="none">Portfolio</text><text x="585" y="531" font-size="12" fill="#8facd4" style="fill:#8facd4" class="mono" pointer-events="none">majorweb.netlify.app</text><g class="nudge" pointer-events="none"><g transform="translate(1100 499) scale(1.1)" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18 M15 6l6 6-6 6"/></g></g></g></a>'''

# Replace all 4 old <a> cards with the new cards
old_cards_pattern = r'<a href="https://www\.linkedin\.com[^>]+>[\s\S]*?</a>\s*<a href="mailto:wasif[^>]+>[\s\S]*?</a>\s*<a href="https://github\.com[^>]+>[\s\S]*?</a>\s*<a href="https://majorweb[^>]+>[\s\S]*?</a>'

new_cards_block = f"{card1_xml}\n{card2_xml}\n{card3_xml}\n{card4_xml}"

if re.search(old_cards_pattern, conn):
    conn = re.sub(old_cards_pattern, new_cards_block, conn)
    print("Replaced all 4 cards in connect.svg successfully!")
else:
    print("Warning: regex did not match old cards in connect.svg, investigating...")

write_svg("connect.svg", conn)

print("\nALL SVGS UPDATED WITH GREEN/WHITE PALETTE AND INTERACTIVITY!")
