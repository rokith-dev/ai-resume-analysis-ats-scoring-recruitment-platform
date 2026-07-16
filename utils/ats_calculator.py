def calculate_ats_score(candidate, skills, education, experience):
    """
    Calculate ATS score and provide suggestions.
    """

    score = 0
    suggestions = []

    # -----------------------------
    # Name
    # -----------------------------
    if candidate["Name"] != "Not Detected":
        score += 10
    else:
        suggestions.append("Add your full name.")

    # -----------------------------
    # Email
    # -----------------------------
    if candidate["Email"] != "Not Detected":
        score += 10
    else:
        suggestions.append("Add a professional email address.")

    # -----------------------------
    # Phone
    # -----------------------------
    if candidate["Phone"] != "Not Detected":
        score += 10
    else:
        suggestions.append("Add your phone number.")

    # -----------------------------
    # Skills
    # -----------------------------
    if len(skills) >= 5:
        score += 25
    elif len(skills) >= 3:
        score += 15
        suggestions.append("Add more relevant technical skills.")
    else:
        suggestions.append("Increase the number of technical skills.")

    # -----------------------------
    # Education
    # -----------------------------
    if education:
        score += 20
    else:
        suggestions.append("Add your education details.")

    # -----------------------------
    # Experience
    # -----------------------------
    if experience != "No experience section found.":
        score += 25
    else:
        suggestions.append("Include your work experience or internships.")

    return score, suggestions