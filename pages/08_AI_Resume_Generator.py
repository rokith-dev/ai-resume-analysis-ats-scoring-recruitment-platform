import streamlit as st

from utils.prompt_builder import build_resume_prompt
from utils.groq_client import generate_response
from utils.pdf_generator import generate_resume_pdf
from utils.resume_preview import show_resume_preview

st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Generator")
st.write("Generate a professional ATS-friendly resume using AI.")

# ===========================
# Resume Form
# ===========================

with st.form("resume_form"):

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

    with col2:
        target_role = st.selectbox(
            "Target Role",
            [
                "AI Engineer",
                "Data Scientist",
                "Machine Learning Engineer",
                "Python Developer",
                "Software Engineer",
                "Backend Developer"
            ]
        )

    st.divider()

    st.subheader("🎓 Education")

    education = st.text_area(
        "Education",
        height=120,
        placeholder="Example:\nB.Tech Artificial Intelligence and Data Science\nKarunya Institute of Technology\nCGPA : 7.2"
    )

    st.subheader("🛠 Technical Skills")

    skills = st.text_area(
        "Skills (Comma Separated)",
        height=120,
        placeholder="Python, SQL, Docker, Machine Learning, Streamlit"
    )

    st.subheader("💼 Experience")

    experience = st.text_area(
        "Experience",
        height=150,
        placeholder="Mention internships or work experience..."
    )

    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Projects",
        height=150,
        placeholder="Mention your important projects..."
    )

    st.subheader("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        height=120,
        placeholder="Cisco, AWS, NPTEL..."
    )

    generate = st.form_submit_button("✨ Generate Resume")

# ===========================
# Resume Generation
# ===========================

if generate:

    if not name.strip():

        st.error("Please enter your name.")

    elif not education.strip():

        st.error("Please enter your education details.")

    elif not skills.strip():

        st.error("Please enter your technical skills.")

    else:

        with st.spinner("🤖 AI is generating your professional resume..."):

            try:

                prompt = build_resume_prompt(
                    name=name,
                    email=email,
                    phone=phone,
                    target_role=target_role,
                    education=education,
                    skills=skills,
                    experience=experience,
                    projects=projects,
                    certifications=certifications
                )

                resume = generate_response(prompt)

                st.success("✅ Resume Generated Successfully!")

                show_resume_preview(
                    name=name,
                    email=email,
                    phone=phone,
                    target_role=target_role,
                    resume=resume
                )

                pdf = generate_resume_pdf(resume)

                st.download_button(
                    label="📥 Download Resume (PDF)",
                    data=pdf,
                    file_name=f"{name.replace(' ','_')}_Resume.pdf",
                    mime="application/pdf"
                )

            except Exception as e:

                st.error("❌ Failed to generate resume.")

                st.exception(e)