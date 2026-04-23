from function.function import *
import streamlit as st
from loader import page_icon


st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inputs
from app.input import app
input_data =  app()

# Prediction
from app.predict import app
app(input_data)