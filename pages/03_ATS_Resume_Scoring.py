import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.resume_parser import extract_candidate_details
from utils.ats_scoring import calculate_ats_score

from database.candidate_db import add_candidate
from database.ats_db import save_ats_result

st.set_page_config(
    page_title="ATS Resume Scoring",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 ATS Resume Scoring")
st.caption("Compare a Resume with a Job Description and calculate ATS compatibility.")

# ===========================
# Upload Files
# ===========================

col1, col2 = st.columns(2)

with col1:

    uploaded_resume = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    uploaded_jd = st.file_uploader(
        "💼 Upload Job Description (PDF)",
        type=["pdf"]
    )

# ===========================
# ATS Analysis
# ===========================

if uploaded_resume and uploaded_jd:

    # Extract Resume

    resume_text = extract_text_from_pdf(uploaded_resume)

    # Extract Job Description

    job_description = extract_text_from_pdf(uploaded_jd)

    # Candidate Details

    candidate = extract_candidate_details(resume_text)

    st.success("✅ Files Uploaded Successfully")

    st.divider()

    st.subheader("👤 Candidate Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Name",
            candidate["Name"] if candidate["Name"] else "Not Found"
        )

    with col2:

        st.metric(
            "Email",
            candidate["Email"] if candidate["Email"] else "Not Found"
        )

    with col3:

        st.metric(
            "Phone",
            candidate["Phone"] if candidate["Phone"] else "Not Found"
        )

    st.divider()

    # Calculate ATS Score

    score, missing_keywords = calculate_ats_score(
        resume_text,
        job_description
    )

    # Save Candidate

    candidate_id = add_candidate(

        name=candidate.get("Name", "Unknown"),

        email=candidate.get("Email", ""),

        phone=candidate.get("Phone", ""),

        target_role="Not Specified"

    )

    # Save ATS Result

    save_ats_result(

        candidate_id,

        score,

        ", ".join(missing_keywords)

    )

    # Display Score

    st.subheader("📊 ATS Score")

    st.metric(
        "Overall Score",
        f"{score}%"
    )

    st.progress(min(int(score), 100))

    st.divider()

    # Missing Keywords

    st.subheader("❌ Missing Keywords")

    if missing_keywords:

        cols = st.columns(3)

        for index, keyword in enumerate(missing_keywords):

            cols[index % 3].error(keyword)

    else:

        st.success("No Missing Keywords Found 🎉")

    st.divider()

    # Recommendation

    st.subheader("💡 Recommendation")

    if score >= 90:

        st.success(
            "Excellent! Your resume is highly ATS compatible."
        )

    elif score >= 75:

        st.info(
            "Good Resume. Add the missing keywords to improve further."
        )

    elif score >= 60:

        st.warning(
            "Average ATS Score. Update your skills and experience using the missing keywords."
        )

    else:

        st.error(
            "Low ATS Score. Your resume needs significant improvement to match this Job Description."
        )

    st.divider()

    with st.expander("📄 Resume Text"):

        st.text_area(
            "Resume",
            resume_text,
            height=300
        )

    with st.expander("💼 Job Description Text"):

        st.text_area(
            "Job Description",
            job_description,
            height=300
        )