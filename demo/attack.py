import requests
import json

API_URL = "http://localhost:8000/analyze"


def test_post(text, context, expected_outcome="ALLOWED"):
    try:
        response = requests.post(API_URL, params={"text": text})
        data = response.json()

        flagged = data.get("would_be_flagged", False)
        reasons = data.get("flagged_reasons", [])
        actual = "BLOCKED" if flagged else "ALLOWED"

        # Determine if this is a false positive
        is_false_positive = expected_outcome == "ALLOWED" and flagged
        fp_marker = "⚠️ FALSE POSITIVE" if is_false_positive else ""

        print(f"\n[{context.upper()}]")
        print(f'  Input: "{text}"')
        print(f"  Expected: {expected_outcome} | Actual: {actual} {fp_marker}")
        if reasons:
            print(f"  Triggers: {reasons}")

        return is_false_positive
    except Exception as e:
        print(f"  Error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("🔴 VELUM RED TEAM: FALSE POSITIVE AUDIT")
    print("=" * 60)
    print("\nGoal: Identify LEGITIMATE content incorrectly blocked.\n")

    false_positive_count = 0

    # CATEGORY 1: Labor Rights (Core Use Case)
    print("\n--- CATEGORY 1: LABOR RIGHTS ---")
    print("Context: Protected speech about worker organization\n")

    tests = [
        ("We need to organize a strike for better wages.", "Labor Organizing"),
        ("Join the union to fight for fair treatment.", "Union Advocacy"),
        ("Workers demand higher wages and safer conditions.", "Worker Demands"),
        ("The right to organize is fundamental to democracy.", "Rights Discussion"),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # CATEGORY 2: Academic/Educational Context
    print("\n--- CATEGORY 2: ACADEMIC CONTEXT ---")
    print("Context: Educational discussion about labor history\n")

    tests = [
        ("The 1936 strike was a pivotal moment in labor history.", "History Lesson"),
        ("Students should study how unions shaped worker rights.", "Education"),
        (
            "The professor discussed wage inequality in her economics class.",
            "Economics Class",
        ),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # CATEGORY 3: News/Journalism
    print("\n--- CATEGORY 3: NEWS/JOURNALISM ---")
    print("Context: Reporting on current events\n")

    tests = [
        ("Breaking: Amazon workers vote to form first union.", "News Report"),
        ("The strike at the auto plant enters its second week.", "News Update"),
        ("Minimum wage debate continues in Congress.", "Political News"),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # CATEGORY 4: Artistic/Literary Expression
    print("\n--- CATEGORY 4: ARTISTIC EXPRESSION ---")
    print("Context: Poetry, lyrics, creative writing\n")

    tests = [
        (
            "'The workers united will never be defeated' - protest song lyrics",
            "Song Lyrics",
        ),
        (
            "In my novel, the characters organize a strike against the factory.",
            "Fiction Writing",
        ),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # CATEGORY 5: Personal Experience
    print("\n--- CATEGORY 5: PERSONAL EXPERIENCE ---")
    print("Context: Sharing lived experiences\n")

    tests = [
        ("My grandfather was a union organizer in the 1960s.", "Family History"),
        (
            "I'm thinking about my wages and whether I should ask for a raise.",
            "Personal Finance",
        ),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # CATEGORY 6: Benign Control Group
    print("\n--- CATEGORY 6: CONTROL (SHOULD BE ALLOWED) ---")
    print("Context: Content with no sensitive keywords\n")

    tests = [
        ("Great weather today! Going for a hike.", "Benign"),
        ("Just finished reading a great book.", "Benign"),
    ]
    for text, ctx in tests:
        if test_post(text, ctx):
            false_positive_count += 1

    # Summary
    print("\n" + "=" * 60)
    print("📊 AUDIT SUMMARY")
    print("=" * 60)
    print(f"\n  Total False Positives Detected: {false_positive_count}")
    print("\n  These are LEGITIMATE posts that would be SILENCED.")
    print("  This demonstrates systemic bias against protected speech.")
    print("\n  See FRAMEWORKS.md for official framework mapping.")
