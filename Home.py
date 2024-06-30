import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

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

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

