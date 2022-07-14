import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(layout="wide")

st.title("Moje první appka")

page = st.sidebar.radio("Select page", ["Mapa", "Thomson"])

if page == "Mapa":

	engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
	df_bikes = pd.read_sql(sql='select start_station_latitude as lat, start_station_longitude as lon  from edinburgh_bikes LIMIT 10000', con=engine)
	selected_columns = ['lat','lon']
	df_temp = df_bikes[selected_columns]
	df_temp = df_temp.sample(frac=0.5)
	
	from_hour_morning = st.slider("Ráno od: ", min_value = 6, max_value = 12)
	to_hour_morning = st.slider("Ráno do: ", min_value = 6, max_value = 12)
	
	query_morning = """ select 
		hour(started_at),start_station_latitude as lat, start_station_longitude as lon
	from edinburgh_bikes
	where hour(started_at) between {} and {}  """.format(from_hour_morning, to_hour_morning)
	
	df_bikes_morning = pd.read_sql(sql=query_morning, con=engine)
	
	query_afternoon = """ select 
		hour(started_at),start_station_latitude as lat, start_station_longitude as lon
	from edinburgh_bikes
	where hour(started_at) between 15 and 19  """
	
	df_bikes_afternoon = pd.read_sql(sql=query_afternoon, con=engine)

	col1, col2 = st.columns(2)
	st.write("Mapa používání sdílených kol v Edinburghu")
	col1.map(df_bikes_morning)
	col2.map(df_bikes_afternoon)
		
if page == "Thomson":
	st.write("Toto je Thomson")