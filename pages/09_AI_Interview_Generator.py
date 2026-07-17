import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.interview_generator import generate_interview_questions

from database.candidate_db import add_candidate
from database.interview_db import save_question

from utils.resume_parser import extract_candidate_details

st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Question Generator")

st.write(
    "Upload a resume and generate AI-powered interview questions."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    candidate = extract_candidate_details(resume_text)

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

    if st.button("🎤 Generate Interview Questions"):

        with st.spinner("Generating Interview Questions..."):

            questions = generate_interview_questions(
                resume_text
            )

        candidate_id = add_candidate(

            candidate.get("Name", "Unknown"),

            candidate.get("Email", ""),

            candidate.get("Phone", ""),

            "Interview Candidate"

        )

        sections = questions.split("#")

        current_category = "General"

        for section in sections:

            section = section.strip()

            if not section:
                continue

            lines = section.split("\n")

            current_category = lines[0].strip()

            for question in lines[1:]:

                question = question.strip()

                if question:

                    save_question(

                        candidate_id,

                        question,

                        current_category

                    )

        st.success("✅ Interview Questions Generated Successfully!")

        st.divider()

        st.markdown(questions)

        st.download_button(

            label="📥 Download Questions",

            data=questions,

            file_name="Interview_Questions.md",

            mime="text/markdown"

        )