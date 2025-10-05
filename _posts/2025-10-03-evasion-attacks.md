---
layout: post
title: "🔐 #3: Evasion Attacks — Fooling Deployed AI Models"
date: 2025-10-03
categories: [AI Security, Machine Learning]
tags: [AI, Security, Adversarial ML, Cybersecurity]
---

🔐 #3: Evasion Attacks — Fooling Deployed AI Models
In the third post of my 7-part series on securing AI systems, I dive into evasion attacks — how attackers manipulate inputs after deployment to bypass AI models and what organizations can do to defend against them.

🎯 What Are Evasion Attacks?
Evasion attacks occur during the inference stage — when an AI model is making predictions.
 The adversary crafts perturbed inputs designed to trick the model into misclassifying data, even though the changes are imperceptible to humans.
These attacks can cause:
Financial losses → e.g., bypassing fraud detection


Reputation damage → manipulated sentiment analysis


Safety risks → evading medical diagnostics or autonomous systems



🕵️ How Attackers Prepare
Before launching an evasion attack, adversaries often perform reconnaissance by:
Reviewing model cards & documentation


Using social engineering to gather details


Conducting dry-run probes against inference APIs


Leveraging transfer learning vulnerabilities from open-source base models



⚡ Common Evasion Techniques
1️⃣ Fast Gradient Sign Method (FGSM)
Generates one-step perturbations by adjusting each pixel in the direction that maximizes classification error.


Supported by Adversarial Robustness Toolkit (ART) via the FastGradientMethod class.


Uses an epsilon value to control perturbation strength.


2️⃣ Projected Gradient Descent (PGD)
An iterative version of FGSM: applies multiple, smaller updates for refined perturbations.


Implemented in ART’s ProjectedGradientDescent module.


3️⃣ Carlini & Wagner (C&W) Attack
Finds the smallest possible perturbation to cause targeted misclassification.


More stealthy than FGSM/PGD since it optimizes imperceptible changes.


4️⃣ NLP Evasion Attacks (Text-based models)
Uses frameworks like TextAttack and BERT to manipulate input text:


Example: Changing a negative review into a positive one without altering its semantic meaning.


Can also mislead Natural Language Inference (NLI) models by replacing words strategically.



🛡️ Defending Against Evasion Attacks
Adversarial Training → Retrain models with perturbed examples to improve robustness.


Input Preprocessing → Apply transformations like image cropping, rotation, and scaling to neutralize malicious perturbations.


Gradient Masking → Obscure gradient information by introducing Gaussian noise during training, making gradient-based attacks less effective.


Continuous Testing → Use tools like:


Adversarial Robustness Toolkit (ART) → Generate adversarial test cases.


TextAttack → Test NLP models for evasion vulnerabilities.



Bottom line:
 Evasion attacks are one of the most common AI threats today — especially against deployed models and inference APIs. By combining adversarial testing, robust training, and secure MLOps practices, organizations can significantly reduce risk.

💬 Over to you:
 Have you tested your models against evasion attacks yet? What frameworks or strategies have worked best in your environment?
#AISecurity #EvasionAttacks #MLOps #AdversarialML #Cybersecurity #MachineLearning



