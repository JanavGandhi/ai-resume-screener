from extract import extract_pdf_text
from section_parser import split_sections
from text_cleaner import clean_text
from tfidf_matcher import compute_similarity

if __name__ == "__main__":
    resume_text = extract_pdf_text("resume.pdf")
    sections = split_sections(resume_text)

    resume_combined = " ".join([
        sections.get("skills","")+
        sections.get("experience","")

    ])

    jd_text = """
    Looking for a software engineer with experience in Python,
    machine learning, data analysis, and backend development.
    """

    score = compute_similarity(
        clean_text(resume_combined),
        clean_text(jd_text)
    )

    print(f"TF-IDF similarity score: {score:.4f}")
