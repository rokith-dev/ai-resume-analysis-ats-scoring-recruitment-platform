import json


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

    prompt = f"""
You are an expert ATS Resume Writer.

Generate ONLY valid JSON.

Do not return Markdown.
Do not return explanations.
Do not wrap the JSON inside code blocks.

Return exactly this structure:

{{
    "name":"",
    "email":"",
    "phone":"",
    "target_role":"",
    "summary":"",
    "skills":[],
    "projects":[
        {{
            "title":"",
            "description":""
        }}
    ],
    "education":[
        {{
            "degree":"",
            "institution":"",
            "cgpa":""
        }}
    ],
    "experience":[
        {{
            "company":"",
            "role":"",
            "duration":"",
            "description":""
        }}
    ],
    "certifications":[]
}}

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

Rewrite the information professionally.

Do not invent fake information.

Return JSON only.
"""

    return prompt