import streamlit as st
import Send_email


st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""

    if button:
        print("I was pressed!")
        Send_email.send_email(message)
        st.info("Your message for sent successfully")