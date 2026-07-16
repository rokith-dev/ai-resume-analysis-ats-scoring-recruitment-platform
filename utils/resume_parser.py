import re
import pandas as pd


# ---------------------------------------
# Candidate Details
# ---------------------------------------

def extract_candidate_details(text):
    """
    Extract candidate name, email and phone number.
    """

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    name = ""

    ignore_words = [
        "summary",
        "technical skills",
        "education",
        "experience",
        "projects",
        "certifications",
        "additional information",
        "languages",
        "soft skills",
        "leadership",
        "volunteering",
        "objective"
    ]

    tech_words = [
        "python",
        "java",
        "sql",
        "docker",
        "aws",
        "tableau",
        "mysql",
        "streamlit",
        "artificial intelligence",
        "data science"
    ]

    for line in lines[:20]:

        lower_line = line.lower()

        # Ignore headings
        if lower_line in ignore_words:
            continue

        # Ignore email line
        if "@" in line:
            continue

        # Ignore phone numbers
        if any(char.isdigit() for char in line):
            continue

        # Ignore long sentences
        if len(line.split()) > 4:
            continue

        # Ignore technology names
        if lower_line in tech_words:
            continue

        # Ignore university names
        if "university" in lower_line:
            continue

        # Accept only alphabetic words
        if re.fullmatch(r"[A-Za-z ]+", line):

            name = line.title()
            break

    # -----------------------------
    # Email
    # -----------------------------

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    email_match = re.search(email_pattern, text)

    email = email_match.group() if email_match else "Not Detected"

    # -----------------------------
    # Phone
    # -----------------------------

    phone_pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

    phone_match = re.search(phone_pattern, text)

    phone = phone_match.group() if phone_match else "Not Detected"

    return {
        "Name": name if name else "Not Detected",
        "Email": email,
        "Phone": phone
    }


# ---------------------------------------
# Skills
# ---------------------------------------

def extract_skills(text):

    skills_df = pd.read_csv("data/skills.csv", header=None)

    skills = skills_df[0].tolist()

    found = []

    for skill in skills:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return sorted(list(set(found)))


# ---------------------------------------
# Education
# ---------------------------------------

def extract_education(text):

    education_df = pd.read_csv("data/education.csv", header=None)

    education = education_df[0].tolist()

    found = []

    for degree in education:

        pattern = r"\b" + re.escape(degree) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(degree)

    return sorted(list(set(found)))


# ---------------------------------------
# Experience
# ---------------------------------------

def extract_experience(text):

    patterns = [
        r"experience(.*?)(education|skills|projects|certifications|additional information|$)",
        r"work experience(.*?)(education|skills|projects|certifications|additional information|$)",
        r"professional experience(.*?)(education|skills|projects|certifications|additional information|$)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1).strip()

    return "No experience section found."