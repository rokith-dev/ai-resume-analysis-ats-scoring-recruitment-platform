import re


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS score based on keyword matching.
    """

    resume = resume_text.lower()
    jd = job_description.lower()

    # Extract words from job description
    keywords = set(re.findall(r"\b[a-zA-Z]{3,}\b", jd))

    if len(keywords) == 0:
        return 0, []

    matched = []

    for word in keywords:
        if word in resume:
            matched.append(word)

    score = round((len(matched) / len(keywords)) * 100, 2)

    missing = sorted(list(keywords - set(matched)))

    return score, missing