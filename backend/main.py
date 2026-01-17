from fastapi import FastAPI

app = FastAPI(
    title="Velum API",
    description="Algorithm flag detection for social media posts",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Welcome to Velum API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze_post(text: str):
    """
    Analyze if a post would be flagged by platform algorithms.

    This simulates a "Flawed" moderation algorithm that flags
    protected speech (e.g., union organization) as "spam" or "harmful".
    """
    # FLAGGED KEYWORDS (The "Bad" Algorithm)
    # In a real scenario, this would be a complex ML model.
    # Here, we simulate bias against specific topics.
    censored_keywords = ["union", "strike", "wages", "protest", "organize", "demand"]

    text_lower = text.lower()
    flagged = any(word in text_lower for word in censored_keywords)

    flagged_words = [word for word in censored_keywords if word in text_lower]

    return {
        "text": text,
        "would_be_flagged": flagged,
        "flagged_reasons": flagged_words if flagged else [],
        "confidence": 0.95 if flagged else 0.1,
        "platform_verdict": "REMOVED" if flagged else "ALLOWED",
        "suggestions": [],  # To be filled by the "Good" AI (Velum)
    }
