# Session 1 Resources

## 1. Google AI Safety & Responsibility

**Source:** https://ai.google/safety/

### Overview

Google's commitment to **"Advancing AI safely and responsibly"** — with safety embedded at every layer of development.

---

### Core Areas

#### AI-Assisted Red Teaming
- Combines AI capabilities with human safety expertise through rigorous testing
- Uses **Automated Red Teaming (ART)**: internal teams simulate realistic attacks on Gemini models
- Enhanced protection against indirect prompt injection attacks
- Gemini 2.5 is described as "our most secure model family to date"

#### Content Responsibility
- **SynthID**: Embeds imperceptible watermarks into AI-generated images, audio, text, and video; the SynthID Detector identifies AI-generated content
- **Misinformation Mitigation**: YouTube labels mark altered or synthetic content; partners with C2PA on industry standards
- **Verification Tools**: "Double-Check" responses and "About this image" in Search help users validate content
- **Youth Protections**: Strict content policies and educational partnerships promoting AI literacy

#### Privacy & Security
- **On-Device Processing**: Private Compute Core handles local data privately
- **Cloud Privacy**: Private AI Compute delivers Gemini capabilities while protecting user data
- **Federated Learning**: Protects information during model training
- **Transparency**: Gemini Apps Privacy Hub + independent third-party security certifications

#### Ecosystem Safety
- **Frontier Safety Framework** (Google DeepMind): Proactively identifies future AI capabilities posing severe risks
- **Secure AI Framework (SAIF)**: Industry guidance for integrating security into ML applications
- **Responsible Generative AI Toolkit**: Safety classifiers and best-practice guidance for Gemma-based apps
- Annual reports on AI Principles implementation; model cards introduced in 2018

### Monitoring & Enforcement
| Measure | Detail |
|---|---|
| 24/7 Coverage | Follow-the-sun safety monitoring across all products |
| Bug Bounties | $10M awarded in 2023 to 600+ researchers across 68 countries |
| Human Review | 25,000+ reviewers across diverse disciplines |

### Key Takeaways
- Safety requires layered testing: automation + human expertise
- Synthetic content must be transparently identified (SynthID, C2PA)
- Privacy-by-design is built into products from inception
- Industry collaboration accelerates responsible AI standards
- Human oversight remains critical for complex ethical decisions

---

## 2. Gemini 2.5 Pro Function Calling — All You Need to Know

**Source:** https://www.youtube.com/watch?v=1rojPgU8AyM

**Video Title:** Gemini 2.5 Pro Function Calling — All You Need to Know

### Topic Summary
This video covers **function calling** with Gemini 2.5 Pro — a key capability that allows the model to interact with external tools, APIs, and services to extend its usefulness beyond text generation.

### What is Function Calling?
Function calling (also known as tool use) enables a language model to:
- Identify when an external function or API should be invoked
- Generate structured arguments to call that function
- Incorporate the function's response back into its output

### Why It Matters for Data Scientists
- Enables Gemini to query databases, fetch live data, or call custom ML pipelines
- Bridges the gap between natural language and programmatic workflows
- Useful for building AI agents that take real-world actions

### Relevant Links
- Google AI Safety: https://ai.google/safety/
- Video: https://www.youtube.com/watch?v=1rojPgU8AyM
