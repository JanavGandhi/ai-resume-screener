from extract import extract_pdf_text
from section_parser import split_sections
from text_cleaner import clean_text
from tfidf_matcher import compute_similarity as tfidf_score
from bert_matcher import compute_semantic_similarity as bert_score

if __name__ == "__main__":
    resume_text = extract_pdf_text("resume.pdf")
    sections = split_sections(resume_text)

    resume_combined = " ".join([
        sections.get("skills", ""),
        sections.get("experience", "")
    ])

    jd_text = """
    Looking for a software engineer with experience in Python,
    machine learning, data analysis, backend development,
    and scalable systems.
    """

    resume_clean = clean_text(resume_combined)
    jd_clean = clean_text(jd_text)

    tfidf = tfidf_score(resume_clean, jd_clean)
    bert = bert_score(resume_clean, jd_clean)

    print(f"TF-IDF similarity : {tfidf:.4f}")
    print(f"BERT similarity   : {bert:.4f}")
