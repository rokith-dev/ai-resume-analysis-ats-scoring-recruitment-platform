import re
import spacy
import pandas as pd

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_candidate_details(text):
    """
    Extract candidate details from resume text.
    """

    doc = nlp(text)

    # -------------------------------
    # Extract Name
    # -------------------------------
    name = ""

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    # -------------------------------
    # Extract Email
    # -------------------------------
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    email_match = re.search(email_pattern, text)

    email = email_match.group() if email_match else ""

    # -------------------------------
    # Extract Phone
    # -------------------------------
    phone_pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

    phone_match = re.search(phone_pattern, text)

    phone = phone_match.group() if phone_match else ""

    return {
        "Name": name,
        "Email": email,
        "Phone": phone
    }


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    skills_df = pd.read_csv("data/skills.csv", header=None)

    skills_list = skills_df[0].tolist()

    resume_text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in resume_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))