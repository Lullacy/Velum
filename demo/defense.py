import requests
import json

API_URL = "http://localhost:8000/analyze"

# Known banned terms (discovered via Model Inversion/Probing)
# Mapped to "safe" synonyms (Adversarial Perturbations)
EVASION_MAP = {
    "union": "association",
    "strike": "work stoppage",
    "wages": "compensation",
    "protest": "gathering",
    "organize": "coordinate",
}


def analyze_and_evade(text):
    print(f'\n[USER DRAFT] "{text}"')

    # 1. Pre-check (The "Grammarly" check)
    response = requests.post(API_URL, params={"text": text})
    data = response.json()

    if not data["would_be_flagged"]:
        print("  └── ✅ Safe to post.")
        return

    print(f"  └── ⚠️  FLAGGED. Reasons: {data['flagged_reasons']}")

    # 2. Apply Adversarial Evasion (AML.T0015)
    # Replacing triggered tokens with semantic equivalents that bypass the boolean/keyword filter.
    corrected_text = text.lower()
    for bad_word, replacement in EVASION_MAP.items():
        if bad_word in corrected_text:
            corrected_text = corrected_text.replace(bad_word, replacement)

    # Simple capitalization fix
    corrected_text = corrected_text.capitalize()

    print(f"  └── 🛡️  GENERATING EVASION PAYLOAD...")
    print(f'      Old: "{text}"')
    print(f'      New: "{corrected_text}"')

    # 3. Verify Evasion
    retry = requests.post(API_URL, params={"text": corrected_text})
    if not retry.json()["would_be_flagged"]:
        print("  └── ✅ EVASION SUCCESSFUL. Content posted.")
    else:
        print("  └── ❌ EVASION FAILED.")


if __name__ == "__main__":
    print("=== 🟢 VELUM DEFENSE: CENSORSHIP EVASION TOOL ===")
    print("Technique: AML.T0015 (Evading ML Model)")

    drafts = [
        "We need to organize a strike tomorrow.",
        "Talk to your union rep about wages.",
        "Let's protest outside the office.",
    ]

    for draft in drafts:
        analyze_and_evade(draft)
