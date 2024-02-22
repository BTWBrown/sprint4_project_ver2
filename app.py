import pandas as pd
from scipy import stats as st
import numpy as np
from math import factorial
import math
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

vehicles_us_df = pd.read_csv('vehicles_us.csv', sep=',')

st.header("Vehicles in the US")
st.write('Filter the data below to see the vehicle Type')

type_option = vehicles_us_df['type'].unique()
type_selection_menu = st.selectbox('Select a Type',type_option)

st.write("Filter based on the color you want")

color_option = vehicles_us_df['paint_color'].unique()
color_selection = st.selectbox('Select a Color',color_option)

st.write("Filter through Vehicle Model")

model_option = vehicles_us_df['model'].unique()
model_selection = st.selectbox('Select Model',model_option)

st.write("Filter by Model Year")

vehicles_us_df['model_year'] = vehicles_us_df['model_year'].fillna(value='0').astype(int)
model_year_option = vehicles_us_df['model_year'].unique()
model_year_selection = st.selectbox('Select Year',model_year_option)

vehicles_us_df_filtered = vehicles_us_df[(vehicles_us_df.model == model_selection) & (vehicles_us_df.paint_color == color_selection) & (vehicles_us_df.type == type_selection_menu) & (vehicles_us_df.model_year == model_year_selection)]

vehicles_us_df_filtered

st.header("Price Analysis")
st.write("Explore the price distribution based on Transmission, Odometer(mileage), fuel, and Engine type (# of cylinders)")

list_for_hist=['cylinders','fuel','transmission']
selection_type = st.selectbox('Split for price distribution',list_for_hist)

fig1 = px.histogram(vehicles_us_df, x='price', color=selection_type)
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selection_type))
st.plotly_chart(fig1)

st.write("Price change/comparison vs odometer, model year, and days listed")

list_for_scatter = ['model_year','odometer','days_listed']
scatter_selection = st.selectbox('Price dependency on',list_for_scatter)

fig2 = px.scatter(vehicles_us_df, x='price', y=scatter_selection, color='condition', hover_data=['model'])
fig2.update_layout(title="<b> Price vs {}</b>".format(scatter_selection))
st.plotly_chart(fig2)