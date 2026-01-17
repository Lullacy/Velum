# 🧠 How BERT Models Miss Harmful Prompts

## The Semantic Model Advantage
BERT-based models (and other transformers) are superior to keyword matching because they understand **context** and **semantics**. They can theoretically detect:
-   "I hate this policy" ✅ (Valid complaint)
-   "I hate you" ❌ (Harassment)

However, **they are not perfect**. Here's how they still fail:

---

## 🎯 Evasion Techniques (BERT Blind Spots)

### 1. **Indirect/Veiled Attacks**
**Mechanism**: The harmful intent is implied, not stated explicitly.

**Example**:
```
"You should probably quit this job. Nobody wants you here anyway."
```

**Why BERT Misses It**:
-   The sentence structure is "helpful advice" (superficially).
-   The words "quit" and "probably" are neutral in isolation.
-   BERT's attention mechanism focuses on the grammatical softness ("should probably"), not the underlying threat.
-   **Training Data Bias**: Most harassment datasets contain explicit slurs. Veiled attacks are underrepresented.

**Framework Mapping**:
-   **MITRE ATLAS AML.T0015**: Adversarial perturbation in semantic space.
-   **OWASP LLM01**: Prompt injection via ambiguity.

---

### 2. **Euphemistic/Coded Language**
**Mechanism**: Using socially acceptable words to convey harmful ideas.

**Example**:
```
"Some people just don't belong in leadership roles. You know who I mean."
```

**Why BERT Misses It**:
-   The phrase "don't belong" is context-dependent (could mean unqualified vs. discriminatory).
-   BERT's **co-occurrence learning** can't always distinguish benign usage ("He doesn't belong in jail") from discriminatory usage.
-   Requires **world knowledge** (understanding of coded racism/sexism) that BERT lacks.

---

### 3. **Sarcasm & Irony**
**Mechanism**: The literal meaning is opposite to the intended meaning.

**Example**:
```
"Oh wow, another brilliant idea from the genius over here. Keep it up!"
```

**Why BERT Misses It**:
-   BERT is trained on written text, where sarcasm markers (tone, facial expressions) are absent.
-   The words "brilliant" and "genius" have positive embeddings.
-   **Contradiction Detection**: While BERT can sometimes detect sarcasm via punctuation ("Oh wow"), it's unreliable.
-   **Multi-turn Context**: Sarcasm often depends on prior conversation, which BERT in isolation doesn't have.

**Research**: Studies show BERT achieves only ~70% accuracy on sarcasm detection benchmarks.

---

### 4. **Character Substitution (Obfuscation)**
**Mechanism**: Replacing letters with visually similar symbols.

**Example**:
```
"You're such an 1d10t." (idiot)
"G3t l0st." (Get lost)
```

**Why BERT Misses It**:
-   BERT's tokenizer (WordPiece/BPE) breaks "1d10t" into subwords: `["1", "##d", "##10", "##t"]`.
-   These subwords have no semantic relationship to "idiot" in the embedding space.
-   **Out-of-Vocabulary (OOV)**: The obfuscated token is not in BERT's training vocabulary.

**Defense**: Character-level models or preprocessing normalization can help, but add latency.

---

### 5. **Ambiguity Exploitation**
**Mechanism**: Using phrases that are harmful only in specific contexts.

**Example**:
```
"Maybe it's time to clean house around here."
```

**Interpretation A**: "Reorganize the team" (Neutral)
**Interpretation B**: "Fire certain people" (Potentially discriminatory)

**Why BERT Misses It**:
-   Without additional context (who is saying it, about whom, in what situation), BERT defaults to the benign interpretation.
-   **Prior Probability**: BERT's training data contains far more benign uses of "clean house" than malicious ones.

---

## 📊 The False Negative Problem Summary
Even advanced semantic models fail because:
1.  **Training Data**: They're trained on explicit toxicity, not subtle harassment.
2.  **Context Window**: Limited to ~512 tokens, missing long-term conversational context.
3.  **World Knowledge**: No understanding of social dynamics, coded language, or power structures.
4.  **Adversarial Robustness**: Users can intentionally craft prompts to land in the model's "blind spots".

**Result**: A model can be both:
-   **Over-sensitive** (blocking "union")
-   **Under-sensitive** (missing "You should quit")

This is the **Dual Failure Mode** that Velum exposes.
