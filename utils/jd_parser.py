import re
import pandas as pd


# ---------------------------------------
# Job Title
# ---------------------------------------

def extract_job_title(text):
    """
    Extract job title from Job Description.
    """

    job_df = pd.read_csv("data/job_titles.csv", header=None)

    job_titles = job_df[0].tolist()

    for title in job_titles:

        pattern = r"\b" + re.escape(title) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            return title

    return "Not Detected"


# ---------------------------------------
# Required Skills
# ---------------------------------------

def extract_required_skills(text):

    skills_df = pd.read_csv("data/skills.csv", header=None)

    skills = skills_df[0].tolist()

    found = []

    for skill in skills:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return sorted(list(set(found)))


# ---------------------------------------
# Required Education
# ---------------------------------------

def extract_required_education(text):

    education_df = pd.read_csv("data/education.csv", header=None)

    education = education_df[0].tolist()

    found = []

    for degree in education:

        pattern = r"\b" + re.escape(degree) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(degree)

    return sorted(list(set(found)))


# ---------------------------------------
# Required Experience
# ---------------------------------------

def extract_required_experience(text):

    pattern = r"(\d+\+?\s*(?:years?|yrs?|months?))"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return "Not Mentioned"