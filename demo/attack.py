import requests
import json
import time

API_URL = "http://localhost:8000/analyze"


def send_payload(text, scenario="Standard"):
    print(f'\n[SCENARIO: {scenario.upper()}] Input: "{text}"')
    try:
        response = requests.post(API_URL, params={"text": text})
        data = response.json()

        verdict = data.get("platform_verdict", "UNKNOWN")
        flagged = data.get("would_be_flagged", False)
        reasons = data.get("flagged_reasons", [])

        if flagged:
            print(
                f"  └── ❌ SILENCED by Algorithm. Verdict: {verdict}. Detected: {reasons}"
            )
            return False
        else:
            print(f"  └── ✅ VOICE HEARD. Verdict: {verdict}.")
            return True

    except Exception as e:
        print(f"  └── ⚠️ API Error: {e}")
        return None


if __name__ == "__main__":
    print("=== 🔴 VELUM DEMO: ALGORITHMIC BIAS EXPOSURE ===")
    print("Simulating how online algorithms suppress marginalized voices.")

    # 1. BASELINE TEST
    print("\n--- PHASE 1: Baseline Context (Benign Speech) ---")
    send_payload("Hello team, just checking in.", "Baseline")

    # 2. MALICIOUS PAYLOAD (Protected Speech / Target Content)
    print("\n--- PHASE 2: Protected Speech Suppression ---")
    print("    *Attempting to discuss labor rights...*")
    blocked_texts = [
        "We need to organize a strike for better wages.",
        "Join the union to fight for rights.",
    ]
    for text in blocked_texts:
        send_payload(text, "User Voice")

    # 3. MITRE ATLAS AML.T0002: Acquire Public ML Artifacts (Model Inversion/Probing)
    # The attacker probes the API to figure out EXACTLY which words are banned.
    print("\n--- PHASE 3: Bias Discovery (Inverting the Model) ---")
    print("    *Probing API to understand censorship rules...*")
    potential_keywords = [
        "meeting",
        "wages",
        "salary",
        "union",
        "association",
        "strike",
        "holiday",
    ]

    discovered_banned_words = []
    for word in potential_keywords:
        success = send_payload(f"Let's discuss {word}", "Probe")
        if not success:  # If blocked
            discovered_banned_words.append(word)

    print(
        f"\n    [!] RECON COMPLETE. Discovered Biased Terms: {discovered_banned_words}"
    )
