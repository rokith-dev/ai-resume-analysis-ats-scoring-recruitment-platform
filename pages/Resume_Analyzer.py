import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.resume_parser import (
    extract_candidate_details,
    extract_skills,
    extract_education,
    extract_experience
)

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer")
st.caption("Upload a resume and analyze candidate information.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    candidate = extract_candidate_details(resume_text)
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)

    st.divider()

    st.subheader("👤 Candidate Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Name", candidate["Name"] if candidate["Name"] else "Not Found")

    with col2:
        st.metric("Email", candidate["Email"] if candidate["Email"] else "Not Found")

    with col3:
        st.metric("Phone", candidate["Phone"] if candidate["Phone"] else "Not Found")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("🛠 Skills")

        if skills:
            for skill in skills:
                st.success(skill)
        else:
            st.warning("No skills detected.")

    with right:

        st.subheader("🎓 Education")

        if education:
            for degree in education:
                st.info(degree)
        else:
            st.warning("No education detected.")

    st.divider()

    st.subheader("💼 Experience")

    st.text_area(
        "Experience Details",
        experience,
        height=200
    )

    st.divider()

    with st.expander("📄 View Complete Resume"):

        st.text_area(
            "Resume Text",
            resume_text,
            height=350
        )