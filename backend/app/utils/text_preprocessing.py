# app/utils/text_preprocessing.py

import re
import string

# --------------------------------------------------
# Clean Text
# --------------------------------------------------
def clean_text(text: str) -> str:
    """
    Lowercase, remove extra spaces, special characters
    """
    text = text.lower()
    text = text.strip()
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # remove punctuation
    return text


# --------------------------------------------------
# Tokenize text
# --------------------------------------------------
def tokenize_text(text: str) -> list[str]:
    """
    Split text into words
    """
    cleaned = clean_text(text)
    return cleaned.split()
