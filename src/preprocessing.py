import re

def clean_text(text):
    text = text.lower()  # ✅ normalize case
    text = re.sub(r'[^a-z0-9\s]', ' ', text)  # ✅ remove symbols
    text = re.sub(r'\s+', ' ', text).strip()  # ✅ remove extra spaces
    return text