import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import plotly.graph_objects as go
import plotly.express as px

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
df_bikes = pd.read_sql(sql='select * from edinburgh_bikes LIMIT 10000', con=engine)
selected_columns = ['start_station_latitude','start_station_longitude']
df_temp = df_bikes[selected_columns]
df_temp = df_temp.sample(frac=0.5)

st.title("Moje první appka")

page = st.sidebar.radio("Select page", ["Mapa", "Thomson"])

if page == "Mapa":
	st.write("Mapa používání sdílených kol v Edinburghu")
	fig = px.scatter_mapbox(df_temp,lat='start_station_latitude', lon='start_station_longitude')
	fig.update_layout(mapbox_style="open-street-map")
	fig.show()
		
if page == "Thomson":
	st.write("Toto je Thomson")