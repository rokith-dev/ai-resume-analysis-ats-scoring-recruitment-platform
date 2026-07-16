from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class ResumeRenderer:
    """
    Render a resume using an HTML template.
    """

    def __init__(self, template_name="ats"):

        template_folder = Path(
            f"resume_builder/templates/{template_name}"
        )

        self.env = Environment(
            loader=FileSystemLoader(template_folder)
        )

        self.template = self.env.get_template("template.html")

    def render(
        self,
        personal_info,
        sections
    ):

        return self.template.render(

            name=personal_info["name"],

            email=personal_info["email"],

            phone=personal_info["phone"],

            linkedin=personal_info.get("linkedin", ""),

            github=personal_info.get("github", ""),

            target_role=personal_info["target_role"],

            summary=sections["summary"],

            skills=sections["skills"],

            experience=sections["experience"],

            projects=sections["projects"],

            education=sections["education"],

            certifications=sections["certifications"],

            strengths=sections["strengths"]

        )