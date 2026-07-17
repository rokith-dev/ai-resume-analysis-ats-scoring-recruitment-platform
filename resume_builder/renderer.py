from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class ResumeRenderer:

    def __init__(self, template_name="ats"):

        template_path = Path(f"resume_templates/{template_name}")

        self.env = Environment(
            loader=FileSystemLoader(template_path)
        )

        self.template = self.env.get_template("template.html")

    def render(
        self,
        name,
        email,
        phone,
        target_role,
        summary,
        skills,
        projects,
        experience,
        education,
        certifications,
    ):

        html = self.template.render(

            name=name,

            email=email,

            phone=phone,

            target_role=target_role,

            summary=summary,

            skills=skills,

            projects=projects,

            experience=experience,

            education=education,

            certifications=certifications

        )

        return html