import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.resume_parser import extract_skills
from utils.jd_parser import extract_required_skills
from utils.matching_engine import calculate_match_score

st.set_page_config(
    page_title="Resume Matching",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 Resume Matching")

st.write("Upload a Resume and a Job Description to compare their skills.")

# -----------------------------
# Upload Files
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"],
        key="resume"
    )

with col2:
    jd_file = st.file_uploader(
        "💼 Upload Job Description",
        type=["pdf"],
        key="jd"
    )

# -----------------------------
# Compare
# -----------------------------

if resume_file and jd_file:

    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_required_skills(jd_text)

    result = calculate_match_score(
        resume_skills,
        jd_skills
    )

    st.divider()

    st.subheader("📊 Match Score")

    st.metric(
        "Overall Match",
        f"{result['score']}%"
    )

    st.progress(result["score"] / 100)

    st.divider()

    left, right = st.columns(2)

    # -----------------------------
    # Matched Skills
    # -----------------------------

    with left:

        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.success(skill.title())
        else:
            st.warning("No matched skills.")

    # -----------------------------
    # Missing Skills
    # -----------------------------

    with right:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.error(skill.title())
        else:
            st.success("No missing skills.")