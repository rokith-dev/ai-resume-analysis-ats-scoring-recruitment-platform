import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Recruitment Platform",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.main-title{
    font-size:48px;
    font-weight:800;
    color:#2563EB;
    text-align:center;
}

.sub-title{
    font-size:20px;
    text-align:center;
    color:#555;
    margin-bottom:30px;
}

.feature-card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
    text-align:center;
    margin-bottom:20px;
    transition:0.3s;
}

.feature-card:hover{
    transform:translateY(-5px);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.markdown(
"""
<div class='main-title'>
🤖 AI Recruitment Platform
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
AI-Based Resume Analysis, ATS Scoring and Recruitment Platform
</div>
""",
unsafe_allow_html=True)

st.divider()

# -----------------------------
# About
# -----------------------------

st.markdown("## 🚀 About the Project")

st.write("""
This platform helps recruiters and candidates using Artificial Intelligence.

It provides resume analysis, ATS scoring, resume matching,
candidate ranking, AI resume generation,
AI interview question generation and recruitment analytics.
""")

st.divider()

# -----------------------------
# Features
# -----------------------------

st.markdown("## ✨ Platform Features")

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
<div class='feature-card'>

<h3>📄 Resume Analyzer</h3>

Analyze resumes and extract candidate information.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>🎯 ATS Scoring</h3>

Check ATS compatibility using AI.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>💼 Job Description</h3>

Analyze hiring requirements automatically.

</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class='feature-card'>

<h3>🤝 Resume Matching</h3>

Compare resumes with Job Descriptions.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>🏆 Candidate Ranking</h3>

Rank candidates based on AI scores.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>🤖 Resume Generator</h3>

Generate ATS-friendly professional resumes.

</div>
""",unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class='feature-card'>

<h3>✨ Resume Improver</h3>

Improve existing resumes using AI.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>🎤 Interview Generator</h3>

Generate personalized interview questions.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class='feature-card'>

<h3>📊 Recruiter Dashboard</h3>

View recruitment analytics and reports.

</div>
""",unsafe_allow_html=True)

st.divider()

# -----------------------------
# Technology
# -----------------------------

st.markdown("## 🛠 Technology Stack")

tech1,tech2,tech3,tech4=st.columns(4)

tech1.metric("Frontend","Streamlit")

tech2.metric("Backend","Python")

tech3.metric("Database","MySQL")

tech4.metric("AI Model","Groq Llama 3")

st.divider()

# -----------------------------
# Footer
# -----------------------------

st.markdown("""
<div class='footer'>

Made with ❤️ using Streamlit, Groq AI and MySQL

</div>
""",unsafe_allow_html=True)