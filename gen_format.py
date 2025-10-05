import os

titles = [
    ("3_evasion_attacks.md", "🔐 #3: Evasion Attacks — Fooling Deployed AI Models"),
]

for filename, title in titles:
    path = os.path.join("_posts", filename)
    if not os.path.exists(path):
        print(f"⚠️ Missing: {path}")
        continue
    with open(path, "r+", encoding="utf-8") as f:
        content = f.read()
        if content.startswith("---"):  # Skip if front matter already exists
            continue
        f.seek(0)
        f.write(f"""---
layout: post
title: "{title}"
date: {filename[:10]}
categories: [AI Security, Machine Learning]
tags: [AI, Security, Adversarial ML, Cybersecurity]
---

{content}
""")
    print(f"✅ Added front matter to {filename}")

