# -*- coding: utf-8 -*-
"""Translate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rUC9eFHjnx1YYIopjyPaVKtFMwpiTaxs
"""

from google.cloud import translate_v2 as translate
import os
import json
from dotenv import load_dotenv

load_dotenv()

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not credentials_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set in .env file")

"""# Path to service account JSON key"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

"""# Initializing the Google Translate client"""

translate_client = translate.Client()

"""# Indian languages supported by Google Translate"""

target_languages = {
    'as': 'Assamese',
    'bn': 'Bengali',
    'bho': 'Bhojpuri',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'kn': 'Kannada',
    'kok': 'Konkani',
    'mai': 'Maithili',
    'ml': 'Malayalam',
    'mni-Mtei': 'Manipuri',
    'mr': 'Marathi',
    'or': 'Odia',
    'pa': 'Punjabi',
    'sa': 'Sanskrit',
    'sd': 'Sindhi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ur': 'Urdu',
}

"""# Input Text"""

with open("input.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    summary = data.get("summary", "")
    lang_code = data.get("language", "").strip()

if lang_code not in target_languages:
    raise ValueError(f"Invalid language code: {lang_code}")

"""# Result"""

result = translate_client.translate(summary, target_language=lang_code)

output_data = {
    "original_text": summary,
    "translated_text": result["translatedText"],
    "language": target_languages[lang_code]
}

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)

print(f"Translation saved to output.json")

