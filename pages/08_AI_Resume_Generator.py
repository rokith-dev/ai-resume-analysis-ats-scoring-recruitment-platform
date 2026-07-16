import streamlit as st

from utils.prompt_builder import build_resume_prompt
from utils.groq_client import generate_response
from utils.pdf_generator import generate_resume_pdf

st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Generator")
st.write("Generate a professional ATS-friendly resume using AI.")

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
        height=100
    )

    st.subheader("🛠 Skills")

    skills = st.text_area(
        "Skills (comma separated)",
        height=100
    )

    st.subheader("💼 Experience")

    experience = st.text_area(
        "Experience",
        height=120
    )

    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Projects",
        height=120
    )

    st.subheader("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        height=100
    )

    generate = st.form_submit_button("✨ Generate Resume")


if generate:

    # Basic validation
    if not name or not education or not skills:
        st.error("Please fill in at least Name, Education and Skills.")
    else:

        with st.spinner("🤖 AI is generating your ATS-friendly resume..."):

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

            try:
                resume = generate_response(prompt)

                st.success("✅ Resume Generated Successfully!")

                st.divider()

                st.subheader("📄 AI Generated Resume")

                st.markdown(resume)

                pdf_file = generate_resume_pdf(resume)

                st.download_button(
                    label="📥 Download Resume (PDF)",
                    data=pdf_file,
                    file_name=f"{name.replace(' ', '_')}_AI_Resume.pdf",
                    mime="application/pdf"
)

            except Exception as e:
                st.error("Failed to generate resume.")
                st.exception(e)