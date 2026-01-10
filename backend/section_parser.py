import re
from typing import Dict

SECTION_HEADERS = {
    "skills": [
        "skills", "technical skills", "key skills", "core competencies"
    ],
    "experience": [
        "experience", "work experience", "professional experience", "employment"
    ],
    "education": [
        "education", "academic background", "qualifications"
    ]
}

def normalize_text(text: str) -> str:
    # Normalize spacing and casing
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{2,}", "\n", text)
    return text.lower()

def find_section_indices(text: str) -> Dict[str, int]:
    indices = {}
    for section, headers in SECTION_HEADERS.items():
        for header in headers:
            pattern = rf"\b{re.escape(header)}\b"
            match = re.search(pattern, text)
            if match:
                indices[section] = match.start()
                break
    return indices

def split_sections(text: str) -> Dict[str, str]:
    normalized = normalize_text(text)
    indices = find_section_indices(normalized)

    # Sort sections by appearance order
    sorted_sections = sorted(indices.items(), key=lambda x: x[1])

    result = {key: "" for key in SECTION_HEADERS.keys()}

    for i, (section, start_idx) in enumerate(sorted_sections):
        end_idx = (
            sorted_sections[i + 1][1]
            if i + 1 < len(sorted_sections)
            else len(normalized)
        )
        result[section] = normalized[start_idx:end_idx].strip()

    return result
