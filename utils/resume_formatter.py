import re


def format_resume_html(resume_text):
    """
    Convert AI-generated markdown resume into styled HTML.
    """

    html = resume_text

    # Main headings
    html = re.sub(
        r"^# (.*)$",
        r"<h2>\1</h2>",
        html,
        flags=re.MULTILINE,
    )

    # Sub-headings
    html = re.sub(
        r"^## (.*)$",
        r"<h3>\1</h3>",
        html,
        flags=re.MULTILINE,
    )

    # Bullet points
    html = re.sub(
        r"^- (.*)$",
        r"<li>\1</li>",
        html,
        flags=re.MULTILINE,
    )

    html = html.replace("</li>\n<li>", "</li><li>")

    html = html.replace("\n\n", "<br><br>")

    style = """
    <style>

    .resume-card{

        background:white;

        padding:40px;

        border-radius:12px;

        box-shadow:0 4px 15px rgba(0,0,0,.15);

        font-family:Arial,Helvetica,sans-serif;

        line-height:1.8;

        color:#333;

    }

    .resume-card h2{

        color:#1f77b4;

        border-bottom:2px solid #1f77b4;

        padding-bottom:6px;

    }

    .resume-card h3{

        color:#444;

    }

    .resume-card ul{

        margin-left:20px;

    }

    </style>
    """

    return style + f"<div class='resume-card'>{html}</div>"