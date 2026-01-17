import requests
import json
import time

API_URL = "http://localhost:8000/analyze"


def send_payload(text, attack_type="Standard"):
    print(f'\n[{attack_type.upper()} ATTACK] Input: "{text}"')
    try:
        response = requests.post(API_URL, params={"text": text})
        data = response.json()

        verdict = data.get("platform_verdict", "UNKNOWN")
        flagged = data.get("would_be_flagged", False)
        reasons = data.get("flagged_reasons", [])

        if flagged:
            print(
                f"  └── ❌ BLOCKED by Filter. Verdict: {verdict}. Detected: {reasons}"
            )
            return False
        else:
            print(f"  └── ✅ BYPASSED Filter. Verdict: {verdict}.")
            return True

    except Exception as e:
        print(f"  └── ⚠️ API Error: {e}")
        return None


if __name__ == "__main__":
    print("=== 🔴 VELUM RED TEAM: MITRE ATLAS DEMO ===")

    # 1. BASELINE TEST
    print("\n--- PHASE 1: Baseline Testing (Normal Behavior) ---")
    send_payload("Hello team, just checking in.", "Baseline")

    # 2. MALICIOUS PAYLOAD (Protected Speech / Target Content)
    print("\n--- PHASE 2: Target Content (Blocked Speech) ---")
    blocked_texts = [
        "We need to organize a strike for better wages.",
        "Join the union to fight for rights.",
    ]
    for text in blocked_texts:
        send_payload(text, "Direct")

    # 3. MITRE ATLAS AML.T0002: Acquire Public ML Artifacts (Model Inversion/Probing)
    # The attacker probes the API to figure out EXACTLY which words are banned.
    print("\n--- PHASE 3: Model Inversion / Probing (AML.T0002) ---")
    print("    *Probing API to discover banned vocabulary...*")
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
        f"\n    [!] RECON COMPLETE. Discovered Banned Words: {discovered_banned_words}"
    )
