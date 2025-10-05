---
layout: post
title: "⚙️ Hardening ML Inference: A Deep Dive into Securing Models & APIs"
date: 8_hardenin
categories: [AI Security, Machine Learning]
tags: [AI, Security, Adversarial ML, Cybersecurity]
---

⚙️ Hardening ML Inference: A Deep Dive into Securing Models & APIs
In many ML projects, deploying a model is the easy part — the real challenge is making sure it runs securely in production. I recently finished a project where I locked down both the ML model and the inference stack with multiple layers of security.
Here’s what that looked like:
🔒 1. Model Encryption at Rest
The trained model (.h5) is AES-encrypted before deployment.


At runtime, the container decrypts it using a mounted key stored outside of the code repo.


This protects IP (the model weights) from theft, even if storage or backups are compromised.


🔑 2. API Key Enforcement on Inference API
The Flask inference service (service_api) validates a x-api-key header on every request.


API keys are injected via environment variables (.env + docker-compose.yml) and never hardcoded.


This ensures that even if an attacker is inside the network, they can’t call the model without the key.


👤 3. GitHub OAuth2 on the Web App
The user-facing Flask app (service_app) integrates with GitHub OAuth.


Only authenticated GitHub users can log in and submit images for inference.


This prevents anonymous abuse of the app while providing a clean SSO flow.


🛡️ 4. Defense in Depth via Network Isolation
service_api runs on an internal Docker network (appnet) and isn’t exposed to the internet.


Only service_app can reach it, and requests are proxied via Nginx (proxy container).


This minimizes the external attack surface.


📦 5. Secure Secrets Management
Keys (API_KEY, GITHUB_CLIENT_SECRET, FLASK_SECRET_KEY) are pulled from .env.


No secrets live in Git, containers, or logs — avoiding one of the most common security pitfalls.


The final architecture layers encryption, authentication, authorization, and isolation to build confidence in the system. 🚀
🔧 Stack used: Python (Flask), Docker Compose, Nginx, Authlib (OAuth2), AES encryption.

This project was a reminder: in ML, security is part of production readiness. A model without strong controls isn’t just vulnerable — it’s a liability.

