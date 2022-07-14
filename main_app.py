import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
query = 'SELECT * FROM covid19_basic ORDER BY date DESC LIMIT 10'
df = pd.read_sql(sql=query, con=engine)

st.title("Moje první appka")

page = st.sidebar.radio("Select page", ["Test", "Thomson"])

if page == "Test":
	st.write("Toto je moje první aplikace, další řádky budou super cool")
	
if page == "Thomson":
	st.write("Toto je Thomson")