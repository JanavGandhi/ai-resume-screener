from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from .extract import extract_pdf_text
from .section_parser import split_sections
from .text_cleaner import clean_text
from .tfidf_matcher import compute_similarity as tfidf_score
from .bert_matcher import compute_semantic_similarity as bert_score
from .explain_skills import common_skills
from .explain_sentences import top_matching_sentences

import numpy as np

def to_float(x):
    if isinstance(x, np.generic):
        return float(x)
    return x



app = FastAPI(title="AI Resume Screener")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class JobDescription(BaseModel):
    text: str

@app.post("/analyze-resume")
async def analyze_resume(
    jd_text: str = Form(...),
    resume: UploadFile = File(...)
):
    # Save uploaded resume temporarily
    file_path = f"data/{resume.filename}"
    with open(file_path, "wb") as f:
        f.write(await resume.read())

    # Extract resume text
    resume_text = extract_pdf_text(resume.filename)
    sections = split_sections(resume_text)

    resume_combined = " ".join([
        sections.get("skills", ""),
        sections.get("experience", "")
    ])

    resume_clean = clean_text(resume_combined)
    jd_clean = clean_text(jd_text)

    tfidf = tfidf_score(resume_clean, jd_clean)
    bert = bert_score(resume_clean, jd_clean)

    skills = common_skills(sections.get("skills", ""), jd_text)
    top_sentences = top_matching_sentences(
        sections.get("experience", ""),
        jd_text
    )

    return {
        "tfidf_score": to_float(round(tfidf, 4)),
        "bert_score": to_float(round(bert, 4)),
        "common_skills": list(skills),
        "top_sentences": [
            {
                "sentence": s,
                "score": to_float(round(sc, 3))
            }
            for s, sc in top_sentences
        ]
    }
