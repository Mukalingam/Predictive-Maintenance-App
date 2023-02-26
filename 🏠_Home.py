import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components
import datetime
import base64

st.set_page_config(
    page_title="Predictive Maintenance App",
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
background-size: 160%;
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

thedate = datetime.date.today()
def run():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("""
    # Welcome to AI based Predictive Maintenance for City Infrastructure!
    """) 

    st.markdown(
        """
    This is an AI tool which can be integrated with the real time application in order to maintain the 
    predictive maintatnce which in turn saves the power.
    

    """
    )
    st.subheader("Introduction")
    st.write("This application is designed to help improve the efficiency and reliability of city infrastructure using predictive maintenance. Predictive maintenance is a technique that uses machine learning algorithms to predict when equipment is likely to fail, allowing for proactive maintenance and reducing the need for emergency repairs.")
    st.subheader("How it works")
    st.write("The predictive maintenance system uses machine learning algorithms to predict the remaining life of equipment based on input features such as age, usage, temperature, and pressure. The system is trained on a dataset of equipment data and makes predictions based on user input.")
    st.subheader("Benefits of Predictive Maintenance")
    st.write("- Reduced downtime")
    st.write("- Improved equipment lifespan")
    st.write("- Cost savings")
    st.write("- Saves Energy")
    
                                    
                                          
                            

if __name__ == "__main__":
    run()

