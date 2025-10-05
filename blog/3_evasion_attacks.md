# 🎭 Evasion Attacks — Fooling Deployed Models

Adversaries craft perturbed inputs to deceive models during inference — causing misclassifications while appearing normal to humans.

## ⚡ Common Techniques
- **FGSM:** single-step perturbation.
- **PGD:** iterative refinement of perturbations.
- **C&W:** minimal, stealthy adversarial noise.
- **Text-based attacks:** NLP manipulation via TextAttack.

## 🛡️ Defenses
- Adversarial training with perturbed examples.
- Input preprocessing (resize, crop, normalize).
- Gradient masking with Gaussian noise.

**Bottom line:** Continuous adversarial testing is critical for deployed AI systems.

---
#AISecurity #EvasionAttacks #AdversarialML
