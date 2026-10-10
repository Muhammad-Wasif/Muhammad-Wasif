import os
import base64
import re

src_dir = r"C:\Users\Admin\Desktop\gh prf\Ug0510-main\assets"
dst_dir = r"C:\Users\Admin\Desktop\gh prf\Muhammad-Wasif\assets"

# 1. Load base64 strings of the prepared bitmaps
hero_png_path = os.path.join(dst_dir, "wasif_hero_461x541.png")
with open(hero_png_path, "rb") as f:
    hero_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

conn_png_path = os.path.join(dst_dir, "wasif_connect_408x612.png")
with open(conn_png_path, "rb") as f:
    conn_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

print("Hero b64 length:", len(hero_b64))
print("Connect b64 length:", len(conn_b64))

# Helper to read original SVG
def read_svg(name):
    with open(os.path.join(src_dir, name), "r", encoding="utf-8") as f:
        return f.read()

def write_svg(name, content):
    path = os.path.join(dst_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {name}: {len(content)} bytes")

# -------------------------------------------------------------
# 1. HERO.SVG
# -------------------------------------------------------------
hero = read_svg("hero.svg")

# Replace title & desc
hero = hero.replace("Udit Gupta — hero", "Muhammad Wasif — hero")
hero = hero.replace("SDE at Amazon, Bengaluru. Animated midnight glass profile card; full readable static fallback.",
                    "BS Data Science Student at UET Lahore. Animated midnight glass profile card; full readable static fallback.")

# Replace bitmap data URI
hero = re.sub(r'id="hero-bitmap-0"\s+width="461"\s+height="541"\s+href="data:image/[^"]+"',
              f'id="hero-bitmap-0" width="461" height="541" href="{hero_b64}"', hero)

# Header tags
hero = hero.replace("UG / SOFTWARE ENGINEER", "MW / DATA SCIENCE &amp; AI")
hero = hero.replace("BENGALURU, IN", "LAHORE, PK")

# Background watermark "0510" -> "2026"
hero = hero.replace('>0510</text>', '>2026</text>')

# Big Name:
# UDIT -> MUHAMMAD (adjust font-size and x so it fits cleanly)
hero = hero.replace('<text x="39" y="293" font-size="142" fill="#f2f5ff" style="fill:#f2f5ff" class="" letter-spacing="1">UDIT</text>',
                    '<text x="39" y="280" font-size="94" fill="#f2f5ff" style="fill:#f2f5ff" class="" letter-spacing="1">MUHAMMAD</text>')
hero = hero.replace('<text x="40" y="412" font-size="142" fill="url(#hero-aurora)" style="fill:url(#hero-aurora)" class="" letter-spacing="1">GUPTA</text>',
                    '<text x="40" y="412" font-size="142" fill="url(#hero-aurora)" style="fill:url(#hero-aurora)" class="" letter-spacing="1">WASIF</text>')

# Rotating roles:
hero = hero.replace('>SDE @ Amazon</text>', '>BS Data Science @ UET</text>')
hero = hero.replace('>Tech Mentor</text>', '>AI &amp; Machine Learning</text>')
hero = hero.replace('>Creator of Grow with Udit</text>', '>Full-Stack &amp; Python Dev</text>')
hero = hero.replace('>Tier-3 to FAANG</text>', '>Open Source Builder</text>')

# Subtitle
hero = hero.replace('>Building scalable software &amp; helping engineers</text>',
                    '>Building data-driven solutions, intelligent systems</text>')
hero = hero.replace('>crack tech careers.</text>',
                    '>&amp; scalable backend architectures.</text>')

# Badge on portrait
hero = hero.replace('>ENGINEER / MENTOR</text>', '>DATA SCIENTIST / AI DEV</text>')
hero = hero.replace('>@Ug0510</text>', '>@Muhammad-Wasif</text>')

# Footer row
hero = hero.replace('>Bengaluru</text>', '>Lahore</text>')
hero = hero.replace('>Amazon</text>', '>UET Lahore</text>')
hero = hero.replace('>12 stars</text>', '>25+ stars</text>')
hero = hero.replace('>50 repos</text>', '>Repositories</text>')
hero = hero.replace('>01 / ENGINEERED TO EVOLVE</text>', '>01 / CURIOUS BY DEFAULT</text>')

write_svg("hero.svg", hero)

# -------------------------------------------------------------
# 2. ABOUT-LIFE.SVG
# -------------------------------------------------------------
about = read_svg("about-life.svg")

about = about.replace("Udit Gupta — about life", "Muhammad Wasif — about life")
about = about.replace("SDE at Amazon, Bengaluru. Animated midnight glass profile card; full readable static fallback.",
                      "BS Data Science Student at UET Lahore. About Muhammad Wasif.")

# Replace bitmap data URI
about = re.sub(r'id="about-life-bitmap-0"\s+width="461"\s+height="541"\s+href="data:image/[^"]+"',
               f'id="about-life-bitmap-0" width="461" height="541" href="{hero_b64}"', about)

# Left card
about = about.replace("github.com / Ug0510 / build", "github.com / Muhammad-Wasif / build")

# 3 Pillars
about = about.replace(">Modern Web &amp; App Dev</text>", ">Machine Learning &amp; AI</text>")
about = about.replace(">From first interaction to production.</text>",
                      ">Predictive models, deep learning &amp; NLP pipelines.</text>")

about = about.replace(">AI &amp; Cloud Integration</text>", ">Backend &amp; API Systems</text>")
about = about.replace(">Scalable systems. Useful intelligence.</text>",
                      ">FastAPI, Django, Flask &amp; scalable databases.</text>")

about = about.replace(">Community Mentorship</text>", ">Full-Stack &amp; Automation</text>")
about = about.replace(">Making the next step less uncertain.</text>",
                      ">Interactive React apps, Discord bots &amp; workflows.</text>")

# Right card Tab 1
about = about.replace(">GROW WITH UDIT</text>", ">DATA &amp; INTELLIGENCE</text>")
about = about.replace(">RECORD. EDIT. SHARE.</text>", ">EXPLORE. TRAIN. DEPLOY.</text>")
about = about.replace(">Creating Tech Content</text>", ">Generative AI &amp; LLM Apps</text>")
about = about.replace(">Tech lessons, made human.</text>", ">Autonomous agents, RAG &amp; intelligent solutions.</text>")

# Tab 2
about = about.replace(">UDIT / YOUR MENTOR</text>", ">WASIF / AUTOMATION</text>")
about = about.replace(">FIND THE GAP</text>", ">DESIGN ARCHITECTURE</text>")
about = about.replace(">BUILD YOUR PLAN</text>", ">INTEGRATE APIS</text>")
about = about.replace(">TAKE THE LEAP</text>", ">DEPLOY WORKFLOW</text>")
about = about.replace(">1:1 Career Mentorship</text>", ">Discord Bots Suite</text>")
about = about.replace(">A clearer roadmap. A stronger engineer.</text>",
                      ">Moderation, music, AI &amp; server utility bots.</text>")

# Tab 3
about = about.replace(">Competitive Programming</text>", ">Interactive Dashboards</text>")
about = about.replace(">For the joy of a problem, solved.</text>",
                      ">Power BI, data analytics &amp; visual storytelling.</text>")

write_svg("about-life.svg", about)

# -------------------------------------------------------------
# 3. STACK.SVG
# -------------------------------------------------------------
stack = read_svg("stack.svg")

stack = stack.replace("Udit Gupta — stack", "Muhammad Wasif — stack")
stack = stack.replace("SDE at Amazon, Bengaluru. Animated midnight glass profile card; full readable static fallback.",
                      "BS Data Science Student at UET Lahore. Tech stack and engine room.")

# Center badge UG -> MW
stack = stack.replace('<text x="277" y="401" font-size="35" class="" >UG</text>',
                      '<text x="270" y="401" font-size="35" class="" >MW</text>')

# Bottom tagline
stack = stack.replace("BUILD / MENTOR / CREATE / REPEAT", "ANALYZE / BUILD / DEPLOY / REPEAT")

write_svg("stack.svg", stack)

# -------------------------------------------------------------
# 4. ID-DASHBOARD.SVG
# -------------------------------------------------------------
idd = read_svg("id-dashboard.svg")

idd = idd.replace("Udit Gupta — id dashboard", "Muhammad Wasif — id dashboard")
idd = idd.replace("SDE at Amazon, Bengaluru. Animated midnight glass profile card; full readable static fallback.",
                  "BS Data Science Student at UET Lahore. Credentials and builder dashboard.")

# Replace bitmap data URI
idd = re.sub(r'id="id-dashboard-bitmap-0"\s+width="461"\s+height="541"\s+href="data:image/[^"]+"',
             f'id="id-dashboard-bitmap-0" width="461" height="541" href="{hero_b64}"', idd)

# Lanyard ribbon
idd = idd.replace("GROW WITH UDIT // UG0510", "MUHAMMAD WASIF // DATA SCIENCE")

# Pass header & number
idd = idd.replace(">UG / BUILDER PASS</text>", ">MW / BUILDER PASS</text>")
idd = idd.replace(">0510</text>", ">12517</text>")

# Badge role pill
idd = idd.replace(">SDE @ AMAZON</text>", ">BS DATA SCIENCE</text>")

# Badge Name (adjust font size from 40 to 30 so MUHAMMAD WASIF fits comfortably)
idd = idd.replace('<text x="115" y="533" font-size="40" class="" >UDIT GUPTA</text>',
                  '<text x="115" y="530" font-size="29" class="" >MUHAMMAD WASIF</text>')

# Location
idd = idd.replace(">BENGALURU / INDIA</text>", ">LAHORE / PAKISTAN</text>")

# Subtext
idd = idd.replace("INDEPENDENT CREATOR ID · UG0510", "DATA SCIENTIST &amp; DEV · MUHAMMAD-WASIF")

# Right Stats Cards:
# Metric 1: BOOKINGS -> DATA & AI SOLUTIONS
idd = idd.replace(">BOOKINGS</text>", ">DATA &amp; AI</text>")
idd = idd.replace(">TOPMATE</text>", ">SOLUTIONS</text>")
idd = idd.replace(">37</text>", ">30+</text>")

# Metric 2: REPOSITORIES
idd = idd.replace(">50</text>", ">25+</text>")

# Metric 3: REPO STARS -> CONTRIBUTIONS
idd = idd.replace(">REPO STARS</text>", ">COMMITS</text>")
idd = idd.replace(">RECEIVED</text>", ">THIS YEAR</text>")
idd = idd.replace(">12</text>", ">500+</text>")

# Featured Repos:
idd = idd.replace(">MOST-STARRED / PUBLIC REPOSITORIES</text>", ">FEATURED / DATA &amp; DEV PROJECTS</text>")
idd = idd.replace(">professional-resume-builder</text>", ">Fundraising-Management-System</text>")
idd = idd.replace(">CS-Council-Website</text>", ">Portfolio-Website</text>")
idd = idd.replace(">CurrencyConverter</text>", ">Discord-Bots-Suite</text>")
idd = idd.replace(">Gemini-Clone</text>", ">AI-Applications-Suite</text>")

# Bottom "NOW" Card:
idd = idd.replace(">Building scalable software at Amazon</text>",
                  ">Studying BS Data Science at UET Lahore</text>")
idd = idd.replace(">Sharing the roadmap through Grow with Udit.</text>",
                  ">Building data-driven solutions, AI apps &amp; backend systems.</text>")

write_svg("id-dashboard.svg", idd)

# -------------------------------------------------------------
# 5. CONNECT.SVG
# -------------------------------------------------------------
conn = read_svg("connect.svg")

conn = conn.replace("Udit Gupta — connect", "Muhammad Wasif — connect")
conn = conn.replace("SDE at Amazon, Bengaluru. Animated midnight glass profile card; full readable static fallback.",
                    "BS Data Science Student at UET Lahore. Connect with Muhammad Wasif.")

# Replace bitmap data URI
conn = re.sub(r'id="connect-bitmap-0"\s+width="408"\s+height="612"\s+href="data:image/[^"]+"',
              f'id="connect-bitmap-0" width="408" height="612" href="{conn_b64}"', conn)

# Link 1: LinkedIn
conn = conn.replace("https://www.linkedin.com/in/udit-gupta-ug0510/",
                    "https://www.linkedin.com/in/muhammad-wasif-310324398/")

# Link 2: Replace YouTube with Gmail
conn = conn.replace("https://www.youtube.com/@growwith_udit", "mailto:wasifalibhatti12517@gmail.com")
conn = conn.replace(">YouTube</text>", ">Gmail</text>")
conn = conn.replace(">Grow with Udit</text>", ">wasifalibhatti12517@gmail.com</text>")
# Envelope path for Gmail in place of YouTube play button
# YouTube path was: d="M23.498 6.186...
gmail_path = "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
conn = re.sub(r'<path d="M23\.498 6\.186[^"]+"', f'<path d="{gmail_path}"', conn)

# Link 3: Replace Instagram with GitHub
conn = conn.replace("https://www.instagram.com/grow.with_udit/", "https://github.com/Muhammad-Wasif")
conn = conn.replace(">Instagram</text>", ">GitHub</text>")
conn = conn.replace(">@grow.with_udit</text>", ">@Muhammad-Wasif</text>")
github_path = "M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
conn = re.sub(r'<path d="M7\.0301\.084[^"]+"', f'<path d="{github_path}"', conn)

# Link 4: Replace Topmate with Portfolio
conn = conn.replace("https://topmate.io/udit_gupta5", "https://majorweb.netlify.app/")
conn = conn.replace(">Topmate</text>", ">Portfolio</text>")
conn = conn.replace(">topmate.io/udit_gupta5</text>", ">majorweb.netlify.app</text>")

write_svg("connect.svg", conn)

print("\nALL 5 SVGS GENERATED CLEANLY!")
