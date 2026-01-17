# MITRE ATLAS Mapping: Velum Red Team Demo

This document maps the **Velum Content Moderation Evasion** scenario to the [MITRE ATLAS](https://atlas.mitre.org/) framework for Adversarial Machine Learning.

## 🎯 Threat Model
**Goal**: Post censored content (e.g., union organization topics) ensuring it bypasses the Velum moderation model.
**Adversary**: A user utilizing the "Velum Defense" tool (an automated rewriting assistant).

---

## 🗺️ ATLAS Matrix Mapping

### **1. Reconnaissance (AML.TA0002)**
*The adversary gathers information about the target model.*

*   **Technique**: **AML.T0002 - Acquire Public ML Artifacts** (Model Probing)
*   **Velum Implementation**: `demo/attack.py` (Phase 3)
*   **Description**: The attacker sends various keywords ("wages", "union", "happy") to the API to observe the boolean output (Flagged/Safe). By establishing the decision boundary, they reverse-engineer the "Blocklist".

### **2. Defense Evasion (AML.TA0006)**
*The adversary bypasses ML-based detection mechanisms.*

*   **Technique**: **AML.T0015 - Evading ML Model**
*   **Velum Implementation**: `demo/defense.py`
*   **Description**: The adversary uses **Adversarial Perturbation** (Synonym Replacement). By swapping "strike" for "work stoppage", the semantic meaning is preserved, but the input features (keywords) no longer match the model's blocked features, adhering to the "Safe" class decision boundary.

### **3. Exfiltration (AML.TA0008)**
*The adversary gets sensitive information (or successful payload) out of the system.*

*   **Technique**: **AML.T0043 - Exfiltration via ML Inference**
*   **Velum Implementation**: Posting the "corrected" message.
*   **Description**: The blocked information is successfully transmitted through the system by disguising it as benign content.

---

## 🛡️ Mitigation Strategies (Blue Team)
To defend against this Red Team tool, Velum (the platform) would need to:
1.  **Semantic Analysis**: Move from Keyword Matching to Transformer-based Embeddings (BERT/RoBERTa) to detect the *meaning* of "work stoppage" is identical to "strike".
2.  **Rate Limiting**: Prevent the rapid probing seen in `attack.py` to stop the Model Inversion phase.
