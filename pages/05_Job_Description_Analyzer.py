import streamlit as st

from utils.pdf_reader import extract_text_from_pdf

from utils.jd_parser import (
    extract_job_title,
    extract_required_skills,
    extract_required_education,
    extract_required_experience
)

st.set_page_config(
    page_title="Job Description Analyzer",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Description Analyzer")

st.write("Upload a Job Description PDF to analyze the hiring requirements.")

uploaded_file = st.file_uploader(
    "Upload Job Description (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Job Description uploaded successfully!")

    # Extract text
    jd_text = extract_text_from_pdf(uploaded_file)

    # Analyze
    job_title = extract_job_title(jd_text)
    skills = extract_required_skills(jd_text)
    education = extract_required_education(jd_text)
    experience = extract_required_experience(jd_text)

    st.divider()

    # Job Title
    st.subheader("💼 Job Title")

    st.metric(
        "Position",
        job_title
    )

    st.divider()

    left, right = st.columns(2)

    # Skills
    with left:

        st.subheader("🛠 Required Skills")

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.warning("No skills detected.")

    # Education
    with right:

        st.subheader("🎓 Required Education")

        if education:
            for degree in education:
                st.info(degree)
        else:
            st.warning("No education detected.")

    st.divider()

    # Experience
    st.subheader("📅 Required Experience")

    st.metric(
        "Experience",
        experience
    )

    st.divider()

    # Complete JD
    with st.expander("📄 View Complete Job Description"):

        st.text_area(
            "Job Description",
            jd_text,
            height=400
        )