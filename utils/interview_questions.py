def generate_interview_questions(skills: list[str]) -> list[str]:
    return [f"Tell me about your experience with {skill}." for skill in skills]
