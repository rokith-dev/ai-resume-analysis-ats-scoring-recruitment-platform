import re


def extract_experience_years(text):
    """
    Extract the first number of years from experience text.
    Example:
    '2+ Years' -> 2
    """

    match = re.search(r"(\d+)", text)

    if match:
        return int(match.group(1))

    return 0


def calculate_match_score(
    resume_skills,
    job_skills,
    resume_education,
    job_education,
    resume_experience,
    job_experience
):

    # -----------------------------
    # Skill Match (60 Marks)
    # -----------------------------

    resume_skill_set = {skill.lower() for skill in resume_skills}
    job_skill_set = {skill.lower() for skill in job_skills}

    matched_skills = sorted(
        resume_skill_set.intersection(job_skill_set)
    )

    missing_skills = sorted(
        job_skill_set.difference(resume_skill_set)
    )

    if len(job_skill_set) == 0:
        skill_score = 0
    else:
        skill_score = round(
            (len(matched_skills) / len(job_skill_set)) * 60
        )

    # -----------------------------
    # Education Match (20 Marks)
    # -----------------------------

    education_score = 0

    for degree in resume_education:

        if degree.lower() in [d.lower() for d in job_education]:

            education_score = 20
            break

    # -----------------------------
    # Experience Match (20 Marks)
    # -----------------------------

    resume_years = extract_experience_years(resume_experience)

    job_years = extract_experience_years(job_experience)

    if job_years == 0:
        experience_score = 20

    elif resume_years >= job_years:
        experience_score = 20

    elif resume_years > 0:
        experience_score = 10

    else:
        experience_score = 0

    # -----------------------------
    # Overall Score
    # -----------------------------

    total_score = (
        skill_score
        + education_score
        + experience_score
    )

    # -----------------------------
    # Recommendation
    # -----------------------------

    if total_score >= 85:
        recommendation = "⭐ Strong Candidate"

    elif total_score >= 70:
        recommendation = "👍 Good Candidate"

    elif total_score >= 50:
        recommendation = "⚠ Needs Skill Improvement"

    else:
        recommendation = "❌ Low Match"

    return {
        "overall_score": total_score,
        "skill_score": skill_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation
    }