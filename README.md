# AI Resume Screening & Job Recommendation System

A student AIML project that extracts text from PDF resumes, detects technical skills, recommends relevant job roles, compares a resume with a job description, and provides basic resume improvement suggestions.

## Features

- Upload a text-based PDF resume (up to 5 MB)
- Extract PDF text using `pypdf`
- Detect skills using a transparent keyword dictionary
- Recommend job roles based on skill overlap
- Compare resume and job description using TF-IDF cosine similarity plus known-skill overlap
- Provide rule-based resume improvement suggestions
- Responsive Flask web interface
- Uploaded PDF is removed after processing

## Tech stack

- Python, Flask
- pypdf for PDF text extraction
- scikit-learn for TF-IDF and cosine similarity
- HTML and CSS for the interface

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\\Scripts\\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## GitHub safety

- Do not upload `.env`, API keys, personal resumes, or private candidate data.
- `.gitignore` excludes environment files and uploaded PDFs.
- Keep only synthetic/demo resumes in screenshots and demonstrations.

## Limitations

- Scanned/image-only PDFs need OCR, which is not included.
- Skill extraction uses a predefined keyword list and may miss synonyms.
- Role scores show skill overlap with this demo's role lists; they are not hiring probabilities.
- The analyzer gives rule-based suggestions and does not call a paid external AI API.
- This educational prototype should support human review, not make hiring decisions.

## Suggested future improvements

- OCR support for scanned resumes
- Admin dashboard and CSV export
- Expandable skill taxonomy and role dataset
- Optional LLM integration using a server-side environment variable
- Automated tests and deployment
