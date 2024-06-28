import streamlit as st

st.set_page_config(layout='wide')

col1, col2, = st.columns(2)

with col1:
    st.image("images/myphoto.jpg", width=400)

with col2:
    st.title("Priyanshi Saini")
    content = """
    Hi, I am Priyanshi! a dedicated data science student. I have a master's degree in data science.
     Passionate about harnessing 
    data to drive insights, I have developed projects leveraging Python’s capabilities in data analysis, visualization,
     and machine learning
    """
    st.info(content)

content2 = """
Below you can find of the apps I have built in python. Feel free to contact me!
"""
st.write(content2)