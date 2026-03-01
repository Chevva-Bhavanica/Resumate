# app/services/summary_generator.py

from gensim.summarization import summarize

# --------------------------------------------------
# Generate Resume Summary
# --------------------------------------------------
def generate_summary(text: str, ratio: float = 0.2) -> str:
    """
    Summarize resume text.
    ratio: proportion of text to keep
    """
    try:
        summary = summarize(text, ratio=ratio)
        if not summary:
            # fallback to first 5 sentences
            summary = ". ".join(text.split(".")[:5])
    except Exception:
        summary = ". ".join(text.split(".")[:5])
    return summary
