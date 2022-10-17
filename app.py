import streamlit as st
import numpy as np
import pandas as pd
import pickle
st.title('This is an app to determine compressive strength of Concrete of different compostions')

# importing the model and dataframe
model=pickle.load(open('XGBRegressor.pkl','rb'))
df=pickle.load(open('Dataframe.pkl','rb'))

#cement
cement=st.number_input('Enter quantity of cement in kg/m3 of mixture')

#Blast Furnace slag
blast_furnace_slag=st.number_input('Enter quantity of Blast Furnace Slag in kg/m3 of mixture')

#Fly Ash
fly_ash=st.number_input('Enter quantity of fly ash in kg/m3 of mixture ')

#Water
water=st.number_input('Enter quantity of water in kg/m3 of mixture')

#Super Plasticiser
superplasticizer=st.number_input('Enter quantity of super plasticiser in kg/m3 of mixture')

#Course Aggregate
coarse_aggregate=st.number_input('Enter quantity of course aggregate in kg/m3 of mixture')

#Fine aggregate
fine_aggregate=st.number_input('Enter quantity of Fine aggregate in kg/m3 of mixture')

#Age
age=st.number_input('Enter no of days from (1 day) to (365 days)')

if st.button('Predict Compressive Strength'):
    arr=np.array([cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]).reshape(1,8)
    prediction=model.predict(arr)[0]
    prediction=round(prediction,2)
    st.title(f'Thevenv compressive strength of concrete is {prediction} MPA')
