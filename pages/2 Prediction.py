import pandas as pd
import numpy as np
import random
import pickle
import streamlit as st
df = pd.read_csv('Walmart_cleaned.csv')
st.set_page_config(layout = 'wide' , page_title = 'Prediction')

st.markdown("""
    <div style="padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); text-align: center;">
        <h1 style="color: #1f77b4;">Weekly Sales</h1>
        <p>This App To Predict Sales in Walmart Store</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    store = st.selectbox('Select Store', df.store.unique())
with col2:
    holiday = st.selectbox('Select Holiday Flag', df.holiday_flag.unique())

col3, col4 = st.columns(2)

with col3:
    temperature = st.selectbox('Select Temperature', df.temperature.unique())
with col4:
    fuel = st.selectbox('Select Fuel Price', df.fuel_price.unique())

col5, col6 = st.columns(2)

with col5:
    month = st.selectbox('Select Month', df.month.unique())
with col6:
    day = st.selectbox('Select Day', df.day.unique())

col7, col8 = st.columns(2)

with col7:
    cpi = st.selectbox('Select Cpi', df.cpi.unique().round(2))
with col8:
    unemployment = st.selectbox('Select Unemployment', df.unemployment.unique())


year = st.selectbox('Select Year', df.year.unique())



with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

if st.button('Predict'):
    new_data = pd.DataFrame([[store, holiday, temperature, fuel, cpi, unemployment, year, month, day]], columns=['store', 'holiday_flag', 'temperature', 'fuel_price','cpi', 'unemployment', 'year','month', 'day'],dtype='object')
    prediction = model.predict(new_data)

    st.write(f'The predicted Sales In Week {prediction}.round(2)')
