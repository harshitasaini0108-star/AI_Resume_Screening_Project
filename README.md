# AI Resume Screening & Job Recommendation System

A Python Flask-based web application that analyzes PDF resumes, identifies technical skills, recommends relevant job roles, and compares a candidate's resume with a job description.

**Built with Python, Flask, pypdf, scikit-learn, HTML, and CSS.**

[View Repository](https://github.com/harshitasaini0108-star/AI_Resume_Screening_Project)

## Overview

The AI Resume Screening & Job Recommendation System is an educational AIML project designed to simplify basic resume analysis. It extracts text from PDF resumes, identifies skills using a predefined keyword dictionary, recommends relevant job roles, and provides suggestions to improve resume content.

The application also compares a resume with a job description using TF-IDF vectorization, cosine similarity, and known-skill overlap.

## Features

- **PDF Resume Upload:** Upload text-based PDF resumes up to 5 MB.
- **Resume Text Extraction:** Extract readable text using pypdf.
- **Skill Detection:** Identify technical skills using a predefined keyword dictionary.
- **Job Role Recommendations:** Suggest relevant roles based on skill overlap.
- **Job Description Matching:** Compare resume content with a job description using TF-IDF cosine similarity and known-skill overlap.
- **Resume Improvement Suggestions:** Generate rule-based suggestions to improve resume content.
- **Web Interface:** Simple, responsive interface built with Flask, HTML, and CSS.
- **Temporary File Handling:** Uploaded PDF files are removed after processing.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| pypdf | PDF text extraction |
| scikit-learn | TF-IDF vectorization and cosine similarity |
| HTML | Web page structure |
| CSS | Styling and responsive layout |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
AI_Resume_Screening_Project/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── results.html
├── uploads/
│   └── .gitkeep
└── utils/
    ├── __init__.py
    ├── analyzer.py
    ├── job_matcher.py
    ├── job_recommender.py
    ├── pdf_reader.py
    └── skill_extractor.py
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git
- A web browser

### 1. Clone the repository

```bash
git clone https://github.com/harshitasaini0108-star/AI_Resume_Screening_Project.git
```

### 2. Navigate to the project directory

```bash
cd AI_Resume_Screening_Project
```

### 3. Create a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

**Windows:**

```powershell
py -m pip install -r requirements.txt
```

**macOS/Linux:**

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run the application

**Windows:**

```powershell
py app.py
```

**macOS/Linux:**

```bash
python3 app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

Keep the terminal running while using the application.

## How It Works

1. Upload a text-based PDF resume.
2. The application extracts text from the PDF.
3. The skill extractor identifies matching skills from its predefined dictionary.
4. The job recommender suggests roles based on detected skills.
5. If a job description is provided, the matcher calculates text similarity and known-skill overlap.
6. The analyzer displays results and rule-based improvement suggestions.

## Limitations

- Scanned or image-only PDFs are not supported because OCR is not implemented.
- Skill detection depends on a predefined keyword dictionary and may miss synonyms or unlisted skills.
- Job-role recommendations depend on the skills and role data defined in the application.
- Similarity scores are not hiring probabilities or guarantees of job suitability.
- Resume improvement suggestions are rule-based; the current version does not call an external LLM or paid AI API.
- The project is an educational prototype and should not be used as the sole basis for hiring decisions.

## Future Enhancements

- Add OCR support for scanned resumes.
- Expand the skill dictionary and job-role dataset.
- Add automated tests and improved error handling.
- Introduce an optional LLM integration using secure server-side configuration.
- Add an admin dashboard and CSV export.
- Deploy the application to a public hosting platform.

## Security and Privacy

- Do not commit API keys, `.env` files, personal resumes, or private candidate information.
- Use synthetic or sample resumes for demonstrations.
- Review `.gitignore` before committing changes.
- Process candidate data responsibly and follow applicable privacy requirements.

## Author

**Harshita Saini**

GitHub: [@harshitasaini0108-star](https://github.com/harshitasaini0108-star)

## Disclaimer

This project was developed for educational and learning purposes. It demonstrates basic resume parsing, keyword-based skill extraction, job-role recommendations, and text similarity techniques. Results should be reviewed by a human and should not be treated as automated hiring decisions.
