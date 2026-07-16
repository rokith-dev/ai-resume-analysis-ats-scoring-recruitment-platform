def build_resume_prompt(
    name,
    email,
    phone,
    target_role,
    education,
    skills,
    experience,
    projects,
    certifications
):
    """
    Build a prompt for AI Resume Generation.
    """

    prompt = f"""
You are an expert Resume Writer.

Generate a professional ATS-friendly resume.

Candidate Information

Name: {name}

Email: {email}

Phone: {phone}

Target Role: {target_role}

Education:
{education}

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Certifications:
{certifications}

Instructions

1. Write a professional summary.
2. Improve project descriptions.
3. Improve experience descriptions.
4. Highlight technical skills.
5. Keep the resume ATS-friendly.
6. Use professional formatting.
7. Do not invent information.
"""

    return prompt