import streamlit as st
from email_generator import generate_email
from utils import create_prompt
import json
import os

st.set_page_config(layout="wide", page_title="A/B Email Tester")
st.markdown("<h1 style='font-size: 2.5rem;'>📧 A/B Email Testing App</h1>", unsafe_allow_html=True)

# Custom footer branding
st.markdown("""
<hr style="margin-top: 20px; margin-bottom: 10px;">
<div style="text-align: center; padding: 10px; font-size: 14px; color: gray;">
  <span style="font-weight: bold; font-size: 16px;">🚘</span> 
  <span style="font-family: 'Segoe UI', sans-serif;">Developed by <strong style="color:#19c37d;">Harshit Sharma</strong></span>
</div>
""", unsafe_allow_html=True)

# Sidebar - Previous Results
st.sidebar.header("📊 Previous Results")

if os.path.exists("results.json"):
    with open("results.json", "r") as f:
        results = json.load(f)
        if results:
            for i, r in enumerate(reversed(results[-5:])):  # Show last 5
                st.sidebar.markdown(f"**{i+1}. {r['name']}** ({r['style']})")
                st.sidebar.markdown(f"• Location: {r['location']}")
                st.sidebar.markdown(f"• Choice: _{r['choice']}_")
                with st.sidebar.expander("📨 Email A Preview"):
                    st.markdown(r["email_a"], unsafe_allow_html=True)
                with st.sidebar.expander("📨 Email B Preview"):
                    st.markdown(r["email_b"], unsafe_allow_html=True)
                st.sidebar.markdown("---")
        else:
            st.sidebar.info("No results yet.")
else:
    st.sidebar.info("No results found.")

# Email generation form
with st.form("email_form"):
    name = st.text_input("Name")
    location = st.text_input("Location")
    interests = st.text_area("Interests (comma-separated)")
    service_description = st.text_area("Service Description", value="A car dealership that offers car selling, reselling, servicing, legal paperwork help, and technical support.")
    style = st.selectbox("Communication Style", ["Professional", "Funny", "Critical", "Friendly", "Inspirational"])
    submitted = st.form_submit_button("Generate Emails")

if submitted:
    with st.spinner("Generating Emails..."):
        prompt_a = create_prompt(name, location, interests, style, "A", service_description)
        prompt_b = create_prompt(name, location, interests, style, "B", service_description)
        email_a = generate_email(prompt_a)
        email_b = generate_email(prompt_b)

        # Save generated content to session state
        st.session_state.email_a = email_a
        st.session_state.email_b = email_b
        st.session_state.name = name
        st.session_state.location = location
        st.session_state.interests = interests
        st.session_state.service_description = service_description
        st.session_state.style = style
        st.session_state.preview_a = False
        st.session_state.preview_b = False

# Display emails if they exist in session state
if "email_a" in st.session_state and "email_b" in st.session_state:
    st.subheader("Compare the Two Emails")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✉️ Email A")
        st.markdown(st.session_state.email_a, unsafe_allow_html=True)
        if st.button("📬 Preview Email A"):
            st.session_state.preview_a = True

    with col2:
        st.markdown("### ✉️ Email B")
        st.markdown(st.session_state.email_b, unsafe_allow_html=True)
        if st.button("📬 Preview Email B"):
            st.session_state.preview_b = True

    # Styled email preview popups
    if st.session_state.get("preview_a"):
        with st.expander("📧 Email A Preview", expanded=True):
            st.markdown(f"""
            <div style='background-color:#fff;border:1px solid #ddd;padding:20px;border-radius:8px;max-width:600px;margin:auto;font-family:Arial;line-height:1.5'>
                {st.session_state.email_a}
            </div>
            """, unsafe_allow_html=True)

    if st.session_state.get("preview_b"):
        with st.expander("📧 Email B Preview", expanded=True):
            st.markdown(f"""
            <div style='background-color:#fff;border:1px solid #ddd;padding:20px;border-radius:8px;max-width:600px;margin:auto;font-family:Arial;line-height:1.5'>
                {st.session_state.email_b}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Which version do you prefer?")
    choice = st.radio("Your choice:", ["Email A", "Email B", "It's a tie"])

    if st.button("Submit Choice"):
        result = {
            "name": st.session_state.name,
            "location": st.session_state.location,
            "interests": st.session_state.interests,
            "style": st.session_state.style,
            "email_a": st.session_state.email_a,
            "email_b": st.session_state.email_b,
            "choice": choice
        }

        if not os.path.exists("results.json"):
            with open("results.json", "w") as f:
                json.dump([], f)

        with open("results.json", "r+") as f:
            data = json.load(f)
            data.append(result)
            f.seek(0)
            json.dump(data, f, indent=2)

        st.success("Your choice has been recorded!")
