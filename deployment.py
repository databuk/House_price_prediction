
import pandas as pd
import joblib
import numpy as np
import streamlit as st
from data_cleaner import clean_data

model = joblib.load('model.joblib')
def collect_user_input():
    bedroom = st.number_input('No of Bedrooms', min_value=0, max_value=20, value='min')
    fullbath = st.number_input('No of Bathrooms', min_value=0, max_value=10, value='min')
    lotarea= st.number_input('Area(sqft)', min_value=0, max_value=500000, value='min')
    age = st.number_input('How old is the house(years)?', min_value=0, max_value=200, value='min')
    location = st.selectbox('Location', options=['Urban', 'SubUrban', 'Rural'])

    input_data = pd.DataFrame(data= [[bedroom, fullbath, lotarea, location, age]],
        columns=['bedroom', 'fullbath', 'lotarea', 'location', 'age'])
    return input_data

st.title('House Price Prediction App')
st.write('Predict the price of an apartment')
input_data = collect_user_input()
if st.button('Predict'):
    with st.spinner('Calculating the price of an apartment'):
        prediction = model.predict(input_data)
        st.success(f'The apartment would cost around USD {int(prediction[0])}.')