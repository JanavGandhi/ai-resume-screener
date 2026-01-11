import re
from typing import Set

# Simple normalization map (expandable)
SKILL_SYNONYMS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "backend": "backend development",
    "frontend": "frontend development"
}

def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()
    return SKILL_SYNONYMS.get(skill, skill)

def extract_skills(text: str) -> Set[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9,\s]", " ", text)

    raw_tokens = re.split(r",|\n|•", text)

    skills = set()
    for token in raw_tokens:
        token = token.strip()
        if len(token) < 2:
            continue
        skills.add(normalize_skill(token))

    return skills

def common_skills(resume_text: str, jd_text: str) -> Set[str]:
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    common = set()
    for r in resume_skills:
        for j in jd_skills:
            if r in j or j in r:
                common.add(r)

    return common
