import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64

st.set_page_config(
    page_title="Remaining useful life Prediction in Batteries",
    page_icon=":guardsman:", layout="wide"
)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("menu.jpg") 
img2 = get_img_as_base64("cover.jpg")    

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img2}");
background-size: 190%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)
model_file = "Models/Battery.pkl"
model = pickle.load(open(model_file, "rb"))

def predict(inputs):
    prediction = model.predict(inputs)
    return prediction[0]

st.title("Remaining useful life Prediction in Batteries")
cycle = st.number_input('Please enter the cycle value')
st.write('The given cycle value is ', cycle)
ambient_temperature = st.number_input('Please enter the Ambient Temparature')
st.write('The given Ambient Temparature value is ', ambient_temperature)
voltage_measured = st.number_input('Please enter the Measured Voltage Value')
st.write('The given Measured Voltage Value is ', voltage_measured)
current_measured = st.number_input('Please enter the Measured Current Value')
st.write('The given Measured Current Value is ', current_measured)
temperature_measured = st.number_input('Please enter the Measured Temparature value')
st.write('The given Measured Temparature value is ', temperature_measured)
current_load = st.number_input('Please enter the Current load value')
st.write('The given Current load value is ', current_load)
voltage_load = st.number_input('Please enter the Voltage Load Value')
st.write('The given Axial Voltage Load Value is ', voltage_load)
time = st.number_input('Please enter the time value')
st.write('The given time value is ', time)
inputs = pd.DataFrame({'cycle':[cycle],'ambient_temperature':[ambient_temperature],'voltage_measured':[voltage_measured],'current_measured':[current_measured],'temperature_measured':[temperature_measured],'current_load':[current_load],'voltage_load':[voltage_load],'time':[time]})

# Create a button to trigger the prediction
if st.button('Predict'):
    prediction = predict(inputs)
    pre = prediction
    res = round(pre, 2)
    st.write('The Predicted Capacity of the battery is',res)



