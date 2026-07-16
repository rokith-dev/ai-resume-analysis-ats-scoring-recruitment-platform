import streamlit as st

from utils.pdf_reader import extract_text_from_pdf

from utils.resume_parser import (
    extract_candidate_details,
    extract_skills,
    extract_education,
    extract_experience
)

from utils.ats_calculator import calculate_ats_score


st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ATS Resume Analyzer")

st.write("Upload your resume and check its ATS score.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    candidate = extract_candidate_details(resume_text)

    skills = extract_skills(resume_text)

    education = extract_education(resume_text)

    experience = extract_experience(resume_text)

    score, suggestions = calculate_ats_score(
        candidate,
        skills,
        education,
        experience
    )

    st.divider()

    st.subheader("📊 ATS Score")

    st.metric(
        label="Overall Score",
        value=f"{score}/100"
    )

    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent ATS Resume ✅")

    elif score >= 60:
        st.warning("Good Resume - Can be Improved")

    else:
        st.error("Poor ATS Score")

    st.divider()

    st.subheader("💡 Suggestions")

    if suggestions:

        for suggestion in suggestions:

            st.write("✔", suggestion)

    else:

        st.success("No suggestions. Your resume looks good!")