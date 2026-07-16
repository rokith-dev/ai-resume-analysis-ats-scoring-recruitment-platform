from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def render_ats_template(resume_data):
    """
    Render the ATS resume template with resume data.
    """

    template_path = Path("resume_templates/ats")

    env = Environment(
        loader=FileSystemLoader(template_path)
    )

    template = env.get_template("template.html")

    html = template.render(
        name=resume_data["name"],
        email=resume_data["email"],
        phone=resume_data["phone"],
        target_role=resume_data["target_role"],
        summary=resume_data["summary"],
        skills=resume_data["skills"],
        projects=resume_data["projects"],
        education=resume_data["education"],
        certifications=resume_data["certifications"]
    )

    return html