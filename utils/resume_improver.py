from utils.groq_client import generate_response


def improve_resume(resume_text):
    """
    Improve an existing resume using AI.
    """

    prompt = f"""
You are a professional ATS Resume Expert and Career Coach.

Your task is to improve the following resume.

Rules:

- Do NOT add fake information.
- Do NOT add fake projects.
- Do NOT add fake skills.
- Improve grammar.
- Improve wording.
- Improve professionalism.
- Improve ATS compatibility.
- Use action verbs.
- Keep all original information.

Return the improved resume in Markdown format.

Resume:

{resume_text}
"""

    improved_resume = generate_response(prompt)

    return improved_resume