import re

SKILLS = [
    "python", "java", "c++", "sql", "excel", "power bi", "tableau",
    "machine learning", "deep learning", "artificial intelligence", "ai",
    "natural language processing", "nlp", "data analysis", "data science",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "flask", "django", "html", "css", "javascript", "react",
    "git", "github", "statistics", "communication", "problem solving",
    "cloud computing", "aws", "azure", "docker", "linux", "opencv",
    "computer vision", "mongodb", "mysql", "postgresql", "matplotlib"
]

def extract_skills(text):
    """Find known skills in resume text (case-insensitive)."""
    normalized = re.sub(r"\s+", " ", text.lower())
    found = []
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill.lower()) + r"(?![a-z0-9+#])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(set(found), key=str.lower)
