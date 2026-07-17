import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.ats_scoring import calculate_ats_score
from utils.resume_parser import extract_candidate_details

from database.candidate_db import add_candidate
from database.ats_db import save_ats_result

st.set_page_config(
    page_title="ATS Resume Scoring",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 ATS Resume Scoring")
st.write("Upload a resume and compare it with a Job Description.")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

uploaded_jd = st.file_uploader(
    "Upload Job Description (PDF)",
    type=["pdf"],
    key="jd_pdf"
)

if uploaded_resume and uploaded_jd:

    resume_text = extract_text_from_pdf(uploaded_resume)

    candidate = extract_candidate_details(resume_text)

    score, missing_keywords = calculate_ats_score(
        resume_text,
        job_description
    )

    candidate_id = add_candidate(
        name=candidate.get("Name", "Unknown"),
        email=candidate.get("Email", ""),
        phone=candidate.get("Phone", ""),
        target_role="Not Specified"
    )

    save_ats_result(
        candidate_id,
        score,
        ", ".join(missing_keywords)
    )

    st.success("✅ ATS Analysis Completed")

    st.metric(
        "ATS Score",
        f"{score}%"
    )

    st.progress(min(int(score), 100))

    st.divider()

    st.subheader("❌ Missing Keywords")

    if missing_keywords:

        for keyword in missing_keywords:

            st.error(keyword)

    else:

        st.success("No Missing Keywords")

    st.divider()

    st.subheader("💡 Recommendation")

    if score >= 80:

        st.success(
            "Excellent ATS Compatibility."
        )

    elif score >= 60:

        st.warning(
            "Good resume. Add missing keywords to improve ATS score."
        )

    else:

        st.error(
            "Resume needs improvement. Add more relevant skills and keywords."
        )