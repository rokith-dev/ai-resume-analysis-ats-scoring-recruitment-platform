from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)


def generate_resume_pdf(resume_text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        fontSize=22,
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=15,
        textColor=colors.darkblue,
        spaceBefore=15,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=11,
        leading=18,
        spaceAfter=8,
    )

    story = []

    lines = resume_text.split("\n")

    first_heading = False

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):

            text = line.replace("# ", "")

            if not first_heading:
                story.append(Paragraph(text, title_style))
                first_heading = True

            else:

                story.append(HRFlowable(width="100%", color=colors.grey))

                story.append(Spacer(1, 8))

                story.append(
                    Paragraph(
                        text,
                        heading_style
                    )
                )

        elif line.startswith("## "):

            story.append(
                Paragraph(
                    line.replace("## ", ""),
                    heading_style,
                )
            )

        elif line.startswith("- "):

            bullet = "• " + line.replace("- ", "")

            story.append(
                Paragraph(
                    bullet,
                    body_style,
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    body_style,
                )
            )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf