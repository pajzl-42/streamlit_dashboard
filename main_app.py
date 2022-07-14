import streamlit as st

st.title("Moje první appka")
st.write("Toto je moje první aplikace, další řádky budou super cool")

page = st.sidebar.radio("Select page", ["Test", "Thomson"])

if page == "Test":
	st.write("Toto je moje první aplikace, další řádky budou super cool")
	
if page == "Thomson":
	st.write("Toto je Thomson")