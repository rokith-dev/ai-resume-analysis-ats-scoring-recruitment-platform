import re


class ResumeParser:
    """
    Parse the AI generated resume into structured sections.
    """

    @staticmethod
    def parse(markdown_text):

        sections = {
            "summary": "",
            "skills": [],
            "experience": "",
            "projects": "",
            "education": "",
            "certifications": "",
            "strengths": ""
        }

        current_section = None

        lines = markdown_text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if "professional summary" in lower:
                current_section = "summary"
                continue

            elif "technical skills" in lower:
                current_section = "skills"
                continue

            elif "professional experience" in lower:
                current_section = "experience"
                continue

            elif lower == "# projects" or lower == "projects":
                current_section = "projects"
                continue

            elif "education" in lower:
                current_section = "education"
                continue

            elif "certifications" in lower:
                current_section = "certifications"
                continue

            elif "additional strengths" in lower:
                current_section = "strengths"
                continue

            # Store content
            if current_section == "skills":

                clean_skill = re.sub(r"^[-•*]\s*", "", line)

                if clean_skill:
                    sections["skills"].append(clean_skill)

            elif current_section:

                sections[current_section] += line + "\n"

        return sections