import re
from typing import Dict, Tuple

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
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{2,}", "\n", text)
    return text.lower()

def find_section_indices(text: str) -> Dict[str, Tuple[int, str]]:
    """
    Returns:
        section -> (start_index, matched_header)
    """
    indices = {}

    for section, headers in SECTION_HEADERS.items():
        for header in headers:
            pattern = rf"^\s*{re.escape(header)}\s*$"
            match = re.search(pattern, text, re.MULTILINE)
            if match:
                indices[section] = (match.start(), header)
                break

    return indices

def remove_header(text: str, header: str) -> str:
    pattern = rf"^\s*{re.escape(header)}\s*$"
    return re.sub(pattern, "", text, count=1, flags=re.MULTILINE).strip()

def split_sections(text: str) -> Dict[str, str]:
    normalized = normalize_text(text)
    indices = find_section_indices(normalized)

    sorted_sections = sorted(
        indices.items(),
        key=lambda x: x[1][0]
    )

    result = {key: "" for key in SECTION_HEADERS.keys()}

    for i, (section, (start_idx, header)) in enumerate(sorted_sections):
        end_idx = (
            sorted_sections[i + 1][1][0]
            if i + 1 < len(sorted_sections)
            else len(normalized)
        )

        content = normalized[start_idx:end_idx]
        content = remove_header(content, header)
        result[section] = content.strip()

    return result
