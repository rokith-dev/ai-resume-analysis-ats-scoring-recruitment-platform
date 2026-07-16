def analyze_skill_gap(resume_skills: list[str], job_skills: list[str]) -> list[str]:
    return [skill for skill in job_skills if skill not in resume_skills]
