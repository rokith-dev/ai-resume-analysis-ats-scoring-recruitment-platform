import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.resume_parser import (
    extract_candidate_details,
    extract_skills
)

st.title("📄 Resume Analyzer")

st.write("Upload a PDF resume to analyze candidate details.")

uploaded_file = st.file_uploader(
    "Choose a Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Extract Candidate Information
    candidate = extract_candidate_details(resume_text)

    # Extract Skills
    skills = extract_skills(resume_text)

    # -----------------------------
    # Candidate Information
    # -----------------------------

    st.subheader("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name:**", candidate["Name"])
        st.write("**Email:**", candidate["Email"])

    with col2:
        st.write("**Phone:**", candidate["Phone"])

    # -----------------------------
    # Skills
    # -----------------------------

    st.divider()

    st.subheader("🛠 Skills")

    if skills:
        st.success(", ".join(skills))
    else:
        st.warning("No skills detected.")

    # -----------------------------
    # Resume Text
    # -----------------------------

    st.divider()

    st.subheader("📄 Resume Text")

    st.text_area(
        "Extracted Resume",
        resume_text,
        height=400
    )