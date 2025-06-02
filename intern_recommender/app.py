import streamlit as st
from recommender import load_data, recommend_domains

st.title("Internship Domain Recommender")
students, domains = load_data()

name = st.selectbox("Select your name", students['name'])
if st.button("Recommend"):
    recs = recommend_domains(name, students, domains)
    st.write("Recommended Internship Domains:")
    st.table(recs)
