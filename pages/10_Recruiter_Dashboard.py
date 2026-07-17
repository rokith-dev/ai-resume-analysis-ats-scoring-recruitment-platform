import streamlit as st

from database.dashboard_db import get_dashboard_stats

st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Recruiter Dashboard")
st.write("Welcome to the AI Recruitment Dashboard")

stats = get_dashboard_stats()

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Candidates",
        stats["total_candidates"]
    )

with col2:
    st.metric(
        "📄 Total Resumes",
        stats["total_resumes"]
    )

with col3:
    st.metric(
        "💼 Total Jobs",
        stats["total_jobs"]
    )

with col4:
    st.metric(
        "🎯 Average ATS Score",
        f'{stats["average_ats"]}%'
    )

st.divider()

st.success("✅ Database Connected Successfully")

st.info("Recruitment analytics will be displayed here.")

st.divider()

st.subheader("📈 Project Summary")

st.write(f"👥 Candidates : {stats['total_candidates']}")

st.write(f"📄 Resumes : {stats['total_resumes']}")

st.write(f"💼 Jobs : {stats['total_jobs']}")

st.write(f"🎯 Average ATS Score : {stats['average_ats']}%")