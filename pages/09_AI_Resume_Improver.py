import streamlit as st
import pdfplumber

from utils.resume_improver import improve_resume
from utils.pdf_generator import generate_resume_pdf

st.set_page_config(
    page_title="AI Resume Improver",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Improver")
st.write("Upload your existing resume and let AI improve it for ATS compatibility.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📃 Extracted Resume")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    if st.button("🤖 Improve Resume"):

        with st.spinner("Improving your resume..."):

            improved_resume = improve_resume(resume_text)

        st.success("✅ Resume Improved Successfully!")

        st.subheader("✨ Improved Resume")

        st.markdown(improved_resume)

        pdf = generate_resume_pdf(improved_resume)

        st.download_button(
            "📥 Download Improved Resume",
            pdf,
            file_name="Improved_Resume.pdf",
            mime="application/pdf"
        )