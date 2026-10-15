def analyze_resume(resume_text, skills):
    """Provide transparent, rule-based resume feedback without requiring an API key."""
    words = resume_text.split()
    suggestions = []
    if len(words) < 120:
        suggestions.append("Add more relevant detail about projects, education, and technical experience.")
    if not skills:
        suggestions.append("Add a clearly labelled Skills section using specific tools and technologies.")
    if not any(term in resume_text.lower() for term in ["project", "projects"]):
        suggestions.append("Include 2–3 projects with your role, tools used, and measurable outcomes.")
    if not any(term in resume_text.lower() for term in ["experience", "internship", "work"]):
        suggestions.append("Add internship, work, volunteering, or practical project experience where applicable.")
    if not any(term in resume_text.lower() for term in ["education", "degree", "b.tech", "bachelor"]):
        suggestions.append("Make your education and current degree easy to find.")
    if not suggestions:
        suggestions.append("Keep formatting consistent and tailor the resume keywords to each job description.")
    return {
        "word_count": len(words),
        "skill_count": len(skills),
        "suggestions": suggestions,
        "note": "This is automated guidance, not a hiring decision. Review all recommendations before using them."
    }
