import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
Our company stands at the forefront of the IT industry, offering unparalleled expertise in software 
development, cybersecurity, and cloud solutions. Our tailored strategies empower businesses to thrive in a digital
 landscape, ensuring robust performance and data security. With a focus on innovation and client-centricity, TechGenius
  Solutions is your premier partner for scalable, future-ready IT solutions.
"""
st.write(content)
st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("Project\data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("Project/images (2)/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("Project/images (2)/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("Project/images (2)/" + row["image"])
