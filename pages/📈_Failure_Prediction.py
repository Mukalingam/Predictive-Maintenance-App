import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64

st.set_page_config(
    page_title="Failure Prediction in Bearings",
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
background-size: 110%;
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
model_file = "Models/Failure.pkl"
model = pickle.load(open(model_file, "rb"))

def predict(inputs):
    prediction = model.predict(inputs)
    return prediction[0]

st.title("Failure Prediction in Bearings")

drive_end = st.number_input('Please enter the Drive End value of the Bearing')
st.write('The given Drive End value is ', drive_end)
axial_load = st.number_input('Please enter the Axial Load value on the Bearing')
st.write('The given Axial Load value is ', axial_load)
# Create a button to trigger the prediction
if st.button('Predict'):
    inputs = np.array([[drive_end,axial_load]])
    prediction = predict(inputs)
    if prediction == 1:
        st.error("The might be a Failure in the working of the Bearings as per the given values")
    else:
        st.success("The Bearings will not failure as per the above given values")    

