from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_resume_pdf(resume_text):
    """
    Generate a PDF from AI generated resume text.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    for line in resume_text.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 10))
            continue

        story.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(story)

    buffer.seek(0)

    return buffer