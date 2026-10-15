import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect, url_for
from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.job_recommender import recommend_jobs
from utils.job_matcher import match_resume_with_jd
from utils.analyzer import analyze_resume

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-for-production")
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {"pdf"}
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        flash("Please choose a PDF resume.")
        return redirect(url_for("home"))
    file = request.files["resume"]
    if not file or file.filename == "":
        flash("Please choose a PDF resume.")
        return redirect(url_for("home"))
    if not allowed_file(file.filename):
        flash("Only PDF resumes are supported.")
        return redirect(url_for("home"))

    safe_name = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], safe_name)
    file.save(path)
    try:
        resume_text = extract_text(path)
    except Exception as exc:
        flash(f"Could not read this PDF: {exc}")
        return redirect(url_for("home"))
    finally:
        # Uploaded resumes are processed locally and removed after processing.
        if os.path.exists(path):
            try:
                os.remove(path)
            except OSError:
                pass

    if not resume_text.strip():
        flash("No readable text found. Please upload a text-based PDF, not a scanned image.")
        return redirect(url_for("home"))

    skills = extract_skills(resume_text)
    job_description = request.form.get("job_description", "").strip()
    job_results = recommend_jobs(skills)
    jd_result = match_resume_with_jd(resume_text, job_description) if job_description else None
    feedback = analyze_resume(resume_text, skills)
    return render_template(
        "results.html",
        filename=safe_name,
        skills=skills,
        jobs=job_results,
        jd_result=jd_result,
        feedback=feedback,
        resume_preview=resume_text[:2500],
    )

@app.errorhandler(413)
def too_large(_error):
    flash("File is too large. Maximum upload size is 5 MB.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
