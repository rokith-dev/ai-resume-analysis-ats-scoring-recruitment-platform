import streamlit as st


def show_resume_preview(
    name,
    email,
    phone,
    target_role,
    resume
):

    st.markdown("---")

    st.markdown(
        f"""
# {name}

### {target_role}

📧 **{email}**

📱 **{phone}**
"""
    )

    st.markdown("---")

    st.markdown(resume)