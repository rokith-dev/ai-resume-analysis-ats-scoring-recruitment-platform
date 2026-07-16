class ResumePromptBuilder:
    """
    Builds prompts for the AI Resume Generator.
    """

    @staticmethod
    def build(
        name,
        email,
        phone,
        target_role,
        education,
        skills,
        experience,
        projects,
        certifications,
    ):

        prompt = f"""
You are a Senior Resume Writer and ATS Optimization Expert.

Your task is to generate a professional ATS-friendly resume.

IMPORTANT RULES

1. Do NOT invent any information.
2. Only improve the wording.
3. Keep the resume professional.
4. Use concise bullet points.
5. Use powerful action verbs.
6. Tailor the resume for the target role.
7. Highlight technical skills.
8. Keep the resume ATS-friendly.
9. Return ONLY Markdown.
10. Use exactly the headings below.

Candidate Information

Name:
{name}

Email:
{email}

Phone:
{phone}

Target Role:
{target_role}

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

Return the resume using EXACTLY this structure.

# Professional Summary

Write a 4–5 line ATS-friendly summary.

# Technical Skills

Return as bullet points.

# Professional Experience

Improve the experience section.

# Projects

For every project include:

Project Name

• Description

• Technologies Used

• Key Achievement

# Education

Improve formatting.

# Certifications

Return as bullet points.

# Additional Strengths

Write 3–5 professional strengths suitable for the target role.

Return ONLY the resume.
"""

        return prompt