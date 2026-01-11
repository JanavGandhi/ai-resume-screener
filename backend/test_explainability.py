from extract import extract_pdf_text
from section_parser import split_sections
from explain_skills import common_skills
from explain_sentences import top_matching_sentences

if __name__ == "__main__":
    resume_text = extract_pdf_text("resume.pdf")
    sections = split_sections(resume_text)

    jd_text = """
    Looking for a software engineer with experience in Python,
    machine learning, backend development, and data analysis.
    """

    print("\nCOMMON SKILLS:")
    skills = common_skills(
        sections.get("skills", ""),
        jd_text
    )
    print(skills)

    print("\nTOP MATCHING SENTENCES:")
    matches = top_matching_sentences(
        sections.get("experience", ""),
        jd_text
    )

    for sentence, score in matches:
        print(f"\nScore: {score:.3f}")
        print(sentence)
