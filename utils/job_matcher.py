import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skill_extractor import extract_skills

def match_resume_with_jd(resume_text, job_description):
    """Compare resume and job description using TF-IDF cosine similarity + skill overlap."""
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))
    matched = sorted(resume_skills.intersection(jd_skills))
    missing = sorted(jd_skills - resume_skills)

    try:
        matrix = TfidfVectorizer(stop_words="english").fit_transform([resume_text, job_description])
        similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100
    except ValueError:
        similarity = 0.0

    if jd_skills:
        skill_score = (len(matched) / len(jd_skills)) * 100
        score = round(0.6 * similarity + 0.4 * skill_score)
    else:
        score = round(similarity)
    return {
        "match_percentage": max(0, min(100, score)),
        "text_similarity": round(similarity),
        "matched_skills": matched,
        "missing_skills": missing,
    }
