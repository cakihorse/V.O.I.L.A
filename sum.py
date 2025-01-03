from transformers import pipeline
import re

def summarize(text: str, max: int) -> str:
    # Charger le pipeline de résumé avec un modèle pré-entraîné
    summarizer = pipeline("summarization", model="./bart_finetuned_courses")

    TEXT = text

    # Découper le texte en phrases
    sentences = re.split(r'(?<=[.!?])\s+', TEXT)  # Découpe en fonction des points, points d'exclamation, etc.

    # Grouper les phrases en segments d'une longueur maximale
    segments = []
    current_segment = ""
    for sentence in sentences:
        if len(current_segment) + len(sentence) < 500:
            current_segment += " " + sentence
        else:
            segments.append(current_segment.strip())
            current_segment = sentence
    if current_segment:
        segments.append(current_segment.strip())

    # Résumer chaque segment
    resumes = [summarizer(segment, max_length=max, min_length=25, do_sample=False)[0]['summary_text'] for segment in
               segments]

    # Joindre les résumés
    final_resume = " ".join(resumes)
    return final_resume
