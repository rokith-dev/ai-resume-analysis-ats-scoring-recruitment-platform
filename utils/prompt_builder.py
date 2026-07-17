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

    return f"""
You are an expert ATS Resume Writer.

Create a professional ATS-friendly resume.

Rules:

- Do NOT invent information.
- Improve grammar.
- Improve wording.
- Use professional language.
- Keep it ATS-friendly.
- Return the resume in Markdown.

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

Return exactly in this format:

# {name}

## {target_role}

Email: {email}

Phone: {phone}

# Professional Summary

Write a professional summary.

# Technical Skills

- Skill 1
- Skill 2

# Projects

Project Name

Description

# Experience

...

# Education

...

# Certifications

...
"""