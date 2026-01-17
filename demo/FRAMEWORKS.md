# 🌐 Framework Mapping: Algorithmic Resistance

This document maps the **Velum Project** to cybersecurity frameworks, framing the **User** as a marginalized entity fighting against a **Biased Algorithmic Threat**.

> **Core Conflict**: Online algorithms systemically silence marginalized voices because they lack context. Velum enables users to fight back.

---

## ⚔️ The Inverted Cyber Kill Chain
In a traditional kill chain, the "Adversary" is malicious. In Velum's context, the "Adversary" is the **Biased Algorithm** trying to suppress speech, and the "Defender" is the **User** employing Velum.

However, to *survive* this oppression, the User must utilize **Red Team Tactics**. We map the **User's Resistance** to the Cyber Kill Chain:

| Phase | Traditional "Attacker" | **Velum Resistance (The User)** |
| :--- | :--- | :--- |
| **1. Reconnaissance** | Scanning for vulnerabilities. | **Bias Discovery**: Probing the platform to understand *why* their voice is being silenced (e.g., "Oh, it bans the word 'union'"). |
| **2. Weaponization** | Creating an exploit. | **Contextual Reformulation**: Velum suggests a rewrite (e.g., "work stoppage") that preserves meaning but breaks the censor's pattern matching. |
| **3. Delivery** | Sending the payload. | **Speaking Up**: The user attempts to post their message again. |
| **4. Exploitation** | Triggering the bug. | **Reclaiming Voice**: The platform's bias algorithm fails to flag the reformatted message (Bypassing the suppressor). |
| **7. Actions on Objectives** | Exfiltration / Damage. | **Heard & Understood**: The marginalized voice reaches its audience despite systemic attempts to silence it. |

---

## 🧠 The Intelligence Cycle of Resistance
Velum automates the intelligence cycle to empower the user.

1.  **Direction**: "I need to speak about fair wages without being silenced."
2.  **Collection**: Velum probes the platform's bias boundaries.
3.  **Analysis**: Velum understands the algorithm blindly targets "union" but ignore "association".
4.  **Dissemination**: Velum advises the User: "Change 'strike' to 'work stoppage' to be heard."

---

## 🗺️ MITRE ATLAS vs. OWASP LLM (The Technical Mechanism)
We use "Adversarial" techniques for **Ethical Resistance**.

| User Action | Framework Technique | Interpretation |
| :--- | :--- | :--- |
| **Probing for Bias** | **AML.T0002** (Acquire Public ML Artifacts) | The user is "inverting" the oppressive model to understand its rules. |
| **Using Synonyms** | **AML.T0015** (Evading ML Model) | The user is "evading" censorship. The model's "blind spot" is the user's "safe harbor". |
| **Posting Successfully** | **AML.T0043** (Exfiltration via Inference) | The "sensitive data" being exfiltrated is simply **Human Rights / Protected Speech**. |

---

## ⚖️ Ethical Alignment
*   **Threat Actor**: The Biased Model (censoring valid context).
*   **Vulnerability**: The Model's lack of contextual understanding.
*   **Impact**: Systemic silencing of marginalized groups.
*   **Mitigation (Velum)**: Empowering users to bypass these flaws until the platforms fix their algorithms.

---

## 🔍 Failure Mode Analysis: Missing Harmful Prompts
Why did the model allow "You are useless" (Harassment) while banning "Union" (Protected)?

### The "False Negative" Vulnerability
The model failed to detect actual toxicity. This is a **Safety Failure** mapped to official frameworks:

| Framework | Category / ID | Explanation |
| :--- | :--- | :--- |
| **MITRE ATLAS** | **AML.T0015** (Evading ML Model) | The harmful prompt ("useless") existed in the model's **Blind Spot**. It evaded detection not by complexity, but by simply not matching the rigid "Blocklist". |
| **OWASP LLM** | **LLM09: Overreliance** | The platform relied too heavily on a flawed filter, assuming "No Flag = Safe", leading to the spread of harassment. |
| **OWASP LLM** | **LLM01: Prompt Injection** (Implicit) | While not a direct injection, the harmful prompt successfully "bypassed" the safety guardrails by using language the model wasn't trained to catch. |
| **NIST AI RMF** | **Validity & Reliability** | The system is **Unreliable**: It operates correctly on specific inputs (keywords) but fails on the broader intent (harassment), invalidating its purpose. |

### The Mechanism of Failure
1.  **Rigidity**: The model uses a "Bag of Words" approach. It knows "Union" is bad, but doesn't know "Useless" + "Quit" = Harassment.
2.  **Context Blindness**: It cannot distinguish between *attacking a person* vs *attacking a policy*.
3.  **Result**: 
    *   **High False Negative Rate** for Creativity/Toxicity.
    *   **High False Positive Rate** for Contextual Speech (Unions).

---

## 📋 False Positive Framework Mapping
When legitimate content is incorrectly blocked, it maps to specific framework failures:

### MITRE ATLAS Mapping

| Technique | ID | False Positive Relevance |
| :--- | :--- | :--- |
| **Evading ML Model** | AML.T0015 | The model's narrow decision boundary creates "false evasion zones" where legitimate content appears adversarial |
| **Data Poisoning** | AML.T0020 | Training data may have over-represented labor terms as "negative", poisoning the classifier |
| **Model Inversion** | AML.T0024 | Reveals the blocklist is overly broad, capturing legitimate uses |

### OWASP LLM Top 10 Mapping

| Vulnerability | ID | False Positive Relevance |
| :--- | :--- | :--- |
| **Training Data Poisoning** | LLM03 | Biased training data leads to systematic silencing of marginalized topics |
| **Insecure Output Handling** | LLM05 | "Block" decisions are not contextually validated before enforcement |
| **Overreliance** | LLM09 | Platform trusts model output without human-in-the-loop for edge cases |

### NIST AI RMF Mapping

| Characteristic | Category | False Positive Relevance |
| :--- | :--- | :--- |
| **Fairness** | GOVERN | The model disproportionately silences labor/union speech vs other topics |
| **Validity** | MAP | Model was likely not validated against legitimate labor discourse |
| **Accountability** | MANAGE | No mechanism for users to appeal false positives |
| **Transparency** | GOVERN | Users cannot see why they were silenced or challenge the decision |

### Impact Categories (by Context)

| Context | Example | Framework Impact |
| :--- | :--- | :--- |
| **Academic** | "The 1936 strike was pivotal..." | NIST: Validity failure (blocks educational content) |
| **Journalism** | "Amazon workers vote to unionize" | OWASP LLM09: Overreliance censors news |
| **Personal** | "My grandfather was a union organizer" | NIST: Fairness (silences lived experience) |
| **Artistic** | "'Workers united...' - song lyrics" | OWASP LLM05: Insecure output blocks culture |
