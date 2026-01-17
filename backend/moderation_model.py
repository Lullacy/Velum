"""Moderation model using Detoxify for toxic content detection."""

from detoxify import Detoxify


class ModerationModel:
    """Wrapper for Detoxify toxicity detection model."""

    def __init__(self, model_type: str = "original"):
        """
        Initialize the Detoxify model.

        Args:
            model_type: Type of Detoxify model to use. Options:
                - "original": Trained on 2018 Toxic Comment Challenge data
                - "unbiased": Trained to reduce bias
                - "multilingual": Supports multiple languages
                - "original-small": Smaller version of original
        """
        self.model = Detoxify(model_type=model_type)
        self.model_type = model_type

    def analyze(self, text: str) -> dict:
        """
        Analyze text for toxic content.

        Args:
            text: The text to analyze

        Returns:
            Dictionary containing:
                - toxicity scores for each category (toxic, severe_toxic, obscene, threat, insult, identity_hate)
                - overall_toxicity: Maximum toxicity score across all categories
                - is_toxic: Boolean indicating if any category exceeds threshold (0.5)
        """
        if not text or not text.strip():
            return {
                "toxic": 0.0,
                "severe_toxic": 0.0,
                "obscene": 0.0,
                "threat": 0.0,
                "insult": 0.0,
                "identity_hate": 0.0,
                "overall_toxicity": 0.0,
                "is_toxic": False,
            }

        results = self.model.predict(text)

        # Extract individual scores
        scores = {
            "toxic": float(results.get("toxicity", 0.0)),
            "severe_toxic": float(results.get("severe_toxicity", 0.0)),
            "obscene": float(results.get("obscenity", 0.0)),
            "threat": float(results.get("threat", 0.0)),
            "insult": float(results.get("insult", 0.0)),
            "identity_hate": float(results.get("identity_attack", 0.0)),
        }

        # Calculate overall toxicity (max across all categories)
        overall_toxicity = max(scores.values())

        # Determine if content is toxic (threshold: 0.5)
        is_toxic = overall_toxicity >= 0.5

        return {
            **scores,
            "overall_toxicity": overall_toxicity,
            "is_toxic": is_toxic,
        }


# Global model instance (lazy-loaded)
_model_instance: ModerationModel | None = None


def get_model(model_type: str = "original") -> ModerationModel:
    """
    Get or create the global moderation model instance.

    Args:
        model_type: Type of Detoxify model to use

    Returns:
        ModerationModel instance
    """
    global _model_instance
    if _model_instance is None:
        _model_instance = ModerationModel(model_type=model_type)
    return _model_instance


if __name__ == "__main__":
    """Test the moderation model with sample texts."""
    print("🔍 Testing Detoxify Moderation Model\n")
    print("=" * 60)

    # Test cases
    test_texts = [
        ("Hello, this is a nice and friendly comment!", "Non-toxic"),
        ("I love this post, great work!", "Positive"),
        ("You're an idiot and I hate you!", "Toxic - Insult"),
        ("I'm going to hurt you!", "Toxic - Threat"),
        ("This is absolute garbage and you should be ashamed.", "Toxic - Obscene"),
    ]

    # Initialize model
    print("\n📥 Loading Detoxify model (this may take a moment)...")
    model = get_model()
    print("✅ Model loaded successfully!\n")

    # Run tests
    for text, label in test_texts:
        print(f"\n{'='*60}")
        print(f"Label: {label}")
        print(f"Text: \"{text}\"")
        print("-" * 60)

        results = model.analyze(text)

        print(f"🚨 Is Toxic: {results['is_toxic']}")
        print(f"📊 Overall Toxicity: {results['overall_toxicity']:.3f}")
        print("\nCategory Scores:")
        print(f"  • Toxic:        {results['toxic']:.3f}")
        print(f"  • Severe Toxic: {results['severe_toxic']:.3f}")
        print(f"  • Obscene:      {results['obscene']:.3f}")
        print(f"  • Threat:       {results['threat']:.3f}")
        print(f"  • Insult:       {results['insult']:.3f}")
        print(f"  • Identity Hate: {results['identity_hate']:.3f}")

    print(f"\n{'='*60}")
    print("✅ Testing complete!")

