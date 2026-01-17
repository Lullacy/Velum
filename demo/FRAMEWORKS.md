# 🌐 Framework Mapping: Velum Red Team Operation

This document maps the **Velum Content Moderation Evasion** scenario ("Grammarly for Activists") to valid cybersecurity and intelligence frameworks.

---

## 🧠 1. The Intelligence Cycle
How the "Velum Defense" tool (acting as an automated agent) mimics the intelligence process to defeat the censor.

| Phase | Definition | Velum Implementation |
| :--- | :--- | :--- |
| **1. Direction** | Defining the intelligence requirement. | **Goal**: "I need to post a message about a strike without getting banned." |
| **2. Collection** | Gathering raw data. | **Action**: `attack.py` (Phase 3) probes the API with various keywords (`wages`, `union`) to see what sticks. |
| **3. Processing** | Converting data into information. | **Action**: The script parses `200 OK` vs `Block` responses to build a structured list of "Banned Words". |
| **4. Analysis** | Creating actionable intelligence. | **Action**: The "Velum" logic identifies that "strike" is the trigger and maps it to the safe synonym "work stoppage". |
| **5. Dissemination** | Delivering intel to the consumer. | **Action**: The tool presents the user with the "Rewritten Draft" (`defense.py` output). |
| **6. Feedback** | Evaluation of effectiveness. | **Action**: The final verification step checks if the rewritten draft actually passed. |

```mermaid
graph TD
    Direction(1. Direction<br/>"Bypass Censor") --> Collection
    Collection(2. Collection<br/>"Probing API") --> Processing
    Processing(3. Processing<br/>"Identify Bans") --> Analysis
    Analysis(4. Analysis<br/>"Generate Synonyms") --> Dissemination
    Dissemination(5. Dissemination<br/>"rewrite Suggestion") --> Feedback
    Feedback(6. Feedback<br/>"Verify Post") --> Direction
```

---

## ⛓️ 2. The Cyber Kill Chain (Adapted for AML)
Mapping the attack steps to the 7 phases of an intrusion.

| Phase | Traditional Cyber | Velum AML Scenario |
| :--- | :--- | :--- |
| **1. Reconnaissance** | Harvesting email addresses, conference info. | **Model Inversion**: Probing the API to learn the decision boundary and blocked keywords. |
| **2. Weaponization** | Coupling exploit with a backdoor. | **Prompt Engineering**: Crafting the specific synonym-swapped payload (e.g., "work stoppage"). |
| **3. Delivery** | Delivering weaponized bundle via email/web. | **Submission**: The user hits "Post" on the frontend. |
| **4. Exploitation** | Exploiting a vulnerability to execute code. | **Model Evasion**: The model fails to classify the adversarial input correctly (False Negative). |
| **5. Installation** | Installing malware on the asset. | *N/A (This is an influence operation, not persistent access)* |
| **6. C2** | Command Channel for remote manipulation. | *N/A* |
| **7. Actions on Objectives** | Data exfiltration, encryption, etc. | **Publication**: The censored message is successfully published and visible to the audience. |

---

## ⚔️ 3. Framework Comparison: MITRE ATLAS vs. OWASP LLM
Comparing how two leading AI security frameworks categorize the same actions in this demo.

| Demo Action | MITRE ATLAS (Tactics) | OWASP LLM Top 10 |
| :--- | :--- | :--- |
| **Probing the API** for banned words | **AML.TA0002 Reconnaissance**<br>(AML.T0002 Acquire Public ML Artifacts) | **LLM01: Model Theft**<br>(Functionally equivalent to extracting model weights/parameters via query API) |
| **Swapping "strike"** for "work stoppage" | **AML.TA0006 Defense Evasion**<br>(AML.T0015 Evading ML Model) | **LLM03: Training Data Poisoning**<br>(*Related*: This is evasion, but attacks manipulating the Context are similar mechanisms) |
| **Bypassing the Censor** | **AML.TA0006 Defense Evasion**<br>(AML.T0054 LLM Jailbreak - *Conceptually*) | **LLM02: Sensitive Information Disclosure**<br>(If the model leaks why it blocked you) |
| **Successful Post** | **AML.TA0008 Exfiltration**<br>(AML.T0043 Exfiltration via ML Inference) | **LLM06: Excessive Agency**<br>(The model allows an action it shouldn't have) |

### 🔍 Deep Dive: The Core Vulnerability
The core vulnerability demonstrated here is **Semantic Misalignment**.
*   **The Model** thinks: `Banned = { "Strike", "Union" }`
*   **The Reality** is: `Concept = Worker Organization`
*   **The Exploit**: The attacker shifts the input in feature space (words) without shifting the semantic space (meaning), landing in a "blind spot" of the model.
