def calculate_match_score(resume_skills, job_skills):
    """
    Compare resume skills with job description skills.
    """

    # Convert to lowercase for comparison
    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}

    # Find matched and missing skills
    matched = sorted(resume_set.intersection(job_set))
    missing = sorted(job_set.difference(resume_set))

    # Calculate score
    if len(job_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(job_set)) * 100)

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }