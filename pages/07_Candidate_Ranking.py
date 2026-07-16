import streamlit as st
import pandas as pd

from utils.pdf_reader import extract_text_from_pdf
from utils.resume_parser import (
    extract_candidate_details,
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
from utils.ranking_engine import rank_candidates

st.set_page_config(
    page_title="Candidate Ranking",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Candidate Ranking")

st.write("Upload one Job Description and multiple resumes.")

jd_file = st.file_uploader(
    "📄 Upload Job Description",
    type=["pdf"]
)

resume_files = st.file_uploader(
    "📄 Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if jd_file and resume_files:

    jd_text = extract_text_from_pdf(jd_file)

    jd_skills = extract_required_skills(jd_text)
    jd_education = extract_required_education(jd_text)
    jd_experience = extract_required_experience(jd_text)

    candidates = []

    for resume in resume_files:

        resume_text = extract_text_from_pdf(resume)

        candidate = extract_candidate_details(resume_text)

        result = calculate_match_score(
            extract_skills(resume_text),
            jd_skills,
            extract_education(resume_text),
            jd_education,
            extract_experience(resume_text),
            jd_experience
        )

        candidates.append({

            "Candidate": candidate["Name"],

            "Overall Score": result["overall_score"],

            "Recommendation": result["recommendation"]

        })

    ranked = rank_candidates(candidates)

    st.divider()

    st.subheader("🏆 Candidate Ranking")

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    for candidate in ranked:

        medal = medals.get(candidate["Rank"], "🏅")

        st.markdown(f"## {medal} Rank {candidate['Rank']}")

        col1, col2 = st.columns([3, 1])

        with col1:

            st.write(f"### 👤 {candidate['Candidate']}")

            st.progress(candidate["Overall Score"] / 100)

        with col2:

            st.metric(
                "Score",
                f"{candidate['Overall Score']}%"
            )

        st.success(candidate["Recommendation"])

        st.divider()

    df = pd.DataFrame(ranked)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Ranking Report",

        csv,

        "candidate_ranking.csv",

        "text/csv"
    )