import streamlit as st
from utils.pdf_reader import extract_text_from_pdf

st.title("📄 Resume Analyzer")

st.write("Upload a PDF resume to extract its text.")

uploaded_file = st.file_uploader(
    "Choose a Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )