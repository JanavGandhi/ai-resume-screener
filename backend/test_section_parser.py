from extract import extract_pdf_text
from section_parser import split_sections

if __name__ == "__main__":
    text = extract_pdf_text("resume.pdf")
    sections = split_sections(text)

    for name, content in sections.items():
        print(f"\n--- {name.upper()} ---")
        print(content[:500])
