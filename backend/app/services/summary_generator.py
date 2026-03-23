# app/services/summary_generator.py

import os
from transformers import pipeline

# Use a lightweight robust summarization model
SUMMARIZER_MODEL = os.getenv("SUMMARIZER_MODEL", "sshleifer/distilbart-cnn-12-6")

try:
    summarizer = pipeline("summarization", model=SUMMARIZER_MODEL)
except Exception as e:
    print(f"Failed to load transformer model: {e}")
    summarizer = None

# --------------------------------------------------
# Generate Resume Summary
# --------------------------------------------------
def generate_summary(text: str) -> str:
    """
    Generate professional bullet points from resume text using a Transformer model.
    """
    if not text or len(text.strip()) < 50:
        return "Insufficient text to generate summary."
        
    if summarizer:
        try:
            # truncate text to avoid exceeding max tokens (approx 1024 tokens)
            input_text = text[:3000]
            summary_output = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
            summary_text = summary_output[0]['summary_text']
            
            # Format as bullet points
            sentences = [s.strip() for s in summary_text.split('.') if len(s.strip()) > 5]
            bullets = [f"• {s}." for s in sentences]
            return "\n".join(bullets)
            
        except Exception as e:
            print(f"Transformers error: {e}")
            
    # Fallback to simple extraction
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 5][:3]
    bullets = [f"• {s}." for s in sentences]
    return "\n".join(bullets)
