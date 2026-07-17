from utils.groq_client import generate_response


def generate_interview_questions(resume_text):
    """
    Generate AI interview questions based on the uploaded resume.
    """

    prompt = f"""
You are an experienced Technical Interviewer.

Analyze the candidate's resume and generate interview questions.

Rules:

1. Use ONLY the information available in the resume.
2. Do NOT invent projects or skills.
3. Generate questions suitable for software engineering placements.
4. Return the response in Markdown.

Generate the following sections:

# Technical Questions
Generate 5 technical questions.

# Project Based Questions
Generate 5 questions related to the candidate's projects.

# HR Questions
Generate 5 HR interview questions.

# Behavioral Questions
Generate 5 behavioral interview questions.

Resume:

{resume_text}
"""

    response = generate_response(prompt)

    return response