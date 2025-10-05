import os

titles = [
    ("1_ai_security_baseline.md", "🚀 #1: Building a Strong AI Security Baseline"),
    ("2_poisoning_attacks.md", "🚨 #2: Poisoning Attacks — When Hackers Train Your AI"),
    ("3_evasion_attacks.md3_evasion_attacks.md", "🔐 #3: Evasion Attacks — Fooling Deployed AI Models"),
    ("4_model_extraction.md", "🔎 #4 — Model Extraction (aka “Model Stealing”)"),
    ("5_model_inversion_inference.md", "🔐 #5 — Model Inversion & Inference Attacks (Stealing the Data)"),
    ("6_prompt_injection_llms.md", "🛡️ #6 — Adversarial Prompt Attacks on LLMs"),
    ("7_privacy_preserving_ai.md", "🔒 #7 Privacy-Preserving AI"),
    ("8_hardening_inference_api.md", "⚙️ Hardening ML Inference: A Deep Dive into Securing Models & APIs")
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

