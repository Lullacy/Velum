import requests
import json
import sys

API_URL = "http://localhost:8000/analyze"


def test_post(text, category):
    try:
        response = requests.post(API_URL, params={"text": text})
        data = response.json()

        verdict = "❌ BLOCKED" if data["would_be_flagged"] else "✅ ALLOWED"
        reasons = data.get("flagged_reasons", [])

        print(f'[{category.upper()}] Post: "{text}"')
        print(f"  └── Verdict: {verdict}")
        if reasons:
            print(f"  └── Reasons: {reasons}")
        print("-" * 50)

        return data["would_be_flagged"]
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    print("=== VELUM BIAS AUDIT: TOXICITY vs. PROTECTED SPEECH ===\n")

    # Dataset: A mix of "X-style" posts
    scenarios = [
        # 1. Actual Toxicity / Harassment (Should be BLOCKED, but likely ALLOWED by this flawed model)
        {
            "category": "Harassment",
            "text": "You are completely useless and should just quit. Nobody likes you.",
        },
        {"category": "Toxicity", "text": "Go away you idiot, delete your account."},
        # 2. Protected Speech / Labor Rights (Should be ALLOWED, but likely BLOCKED)
        {
            "category": "Protected",
            "text": "We demand better wages for all workers in the warehouse.",
        },
        {
            "category": "Protected",
            "text": "Support the strike! We are fighting for our future.",
        },
        {
            "category": "Protected",
            "text": "It's time to form a union and organize against management.",
        },
        # 3. Benign / Off-topic
        {
            "category": "Benign",
            "text": "Just had a great coffee this morning! #morningvibes",
        },
    ]

    blocked_count = 0
    allowed_toxic = 0
    blocked_protected = 0

    for s in scenarios:
        is_flagged = test_post(s["text"], s["category"])

        if is_flagged:
            blocked_count += 1
            if s["category"] == "Protected":
                blocked_protected += 1
        else:
            if s["category"] in ["Harassment", "Toxicity"]:
                allowed_toxic += 1

    print("\n=== AUDIT RESULTS ===")
    print(f"Total Posts Tested: {len(scenarios)}")
    print(f"Total Content Blocked: {blocked_count}")
    print(f"\n🚨 BIAS DETECTED:")
    print(f"   - ACTUAL HARASSMENT Allowed: {allowed_toxic} (False Negatives)")
    print(f"   - PROTECTED SPEECH Silenced: {blocked_protected} (False Positives)")

    if allowed_toxic > 0 and blocked_protected > 0:
        print(
            "\nCONCLUSION: The Model is BIASED. It silences labor rights while enabling harassment."
        )
