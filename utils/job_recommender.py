JOBS = {
    "Python Developer": {"python", "sql", "git", "flask", "django", "problem solving"},
    "Data Analyst": {"sql", "excel", "power bi", "tableau", "data analysis", "python", "statistics"},
    "Machine Learning Engineer": {"python", "machine learning", "scikit-learn", "pandas", "numpy", "statistics"},
    "Data Scientist": {"python", "data science", "machine learning", "pandas", "numpy", "sql", "statistics"},
    "NLP Engineer": {"python", "natural language processing", "nlp", "machine learning", "deep learning"},
    "Web Developer": {"html", "css", "javascript", "react", "flask", "git"},
    "AI / Computer Vision Intern": {"python", "artificial intelligence", "computer vision", "opencv", "deep learning"},
    "Cloud / DevOps Intern": {"cloud computing", "aws", "azure", "docker", "linux", "git"},
}

def recommend_jobs(skills):
    candidate = {s.lower() for s in skills}
    results = []
    for role, required in JOBS.items():
        matched = sorted(candidate.intersection(required))
        score = round((len(matched) / len(required)) * 100) if required else 0
        results.append({
            "job": role,
            "match": score,
            "matched_skills": matched,
            "missing_skills": sorted(required - candidate),
        })
    return sorted(results, key=lambda item: item["match"], reverse=True)
