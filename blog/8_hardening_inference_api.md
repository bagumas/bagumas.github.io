# ⚙️ Hardening ML Inference — Securing Models & APIs

A practical walkthrough of securing an inference system using Flask, Docker, Nginx, and AES encryption.

## 🧱 Architecture Layers
1. **Model Encryption:** AES-256 at rest.
2. **API Key Enforcement:** validate every request header.
3. **OAuth2 Authentication:** GitHub login for web access.
4. **Network Isolation:** internal-only service_api.
5. **Secrets Management:** .env-based configuration.

**Stack:** Flask, Docker Compose, AES, Authlib, Nginx.

**Lesson:** Security *is* part of production readiness.

---
#DevSecOps #MLSecurity #AIEngineering
