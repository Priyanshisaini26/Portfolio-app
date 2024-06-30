import streamlit as st
import smtplib, ssl
import pandas

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "priyanshisaini2603@gmail.com"
    password = "zssptpxqvcxtjbaq"

    receiver = "priyanshisaini2603@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username)
        server.sendmail(username, receiver, message)


st.header("Contact me")
df = pandas.read_csv(r"Project\topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")

    option = st.selectbox("What topic do you want to discuss",
                          df["topic"],
                          index=None,)
    st.write("You selected:", option)
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your message was sent successfully!!! :)")
