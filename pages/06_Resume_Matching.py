import streamlit as st

from utils.pdf_reader import extract_text_from_pdf

from utils.resume_parser import (
    extract_skills,
    extract_education,
    extract_experience
)

from utils.jd_parser import (
    extract_required_skills,
    extract_required_education,
    extract_required_experience
)

from utils.matching_engine import calculate_match_score

st.set_page_config(
    page_title="Resume Matching",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 Resume Matching Engine")

st.write("Compare a Resume with a Job Description.")

# -----------------------------------
# Upload Files
# -----------------------------------

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

# -----------------------------------
# Compare
# -----------------------------------

if resume_file and jd_file:

    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    resume_skills = extract_skills(resume_text)
    resume_education = extract_education(resume_text)
    resume_experience = extract_experience(resume_text)

    jd_skills = extract_required_skills(jd_text)
    jd_education = extract_required_education(jd_text)
    jd_experience = extract_required_experience(jd_text)

    result = calculate_match_score(
        resume_skills,
        jd_skills,
        resume_education,
        jd_education,
        resume_experience,
        jd_experience
    )

    st.divider()

    # -----------------------------------
    # Overall Score
    # -----------------------------------

    st.subheader("📊 Overall Match")

    st.metric(
        "Overall Score",
        f"{result['overall_score']}%"
    )

    st.progress(result["overall_score"] / 100)

    st.success(result["recommendation"])

    st.divider()

    # -----------------------------------
    # Individual Scores
    # -----------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "📈 Skill Score",
            f"{result['skill_score']} / 60"
        )

    with c2:
        st.metric(
            "🎓 Education Score",
            f"{result['education_score']} / 20"
        )

    with c3:
        st.metric(
            "💼 Experience Score",
            f"{result['experience_score']} / 20"
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.success(skill.title())
        else:
            st.warning("No matched skills.")

    with right:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.error(skill.title())
        else:
            st.success("No missing skills.")