import pickle
import streamlit as st
from streamlit_option_menu import option_menu

import os

diabetes_model_path = os.path.join("C:/Users/Vibhuti/Desktop/Multiple disease prediction/saved", "diabetes_saved_")
heart_disease_model_path = os.path.join("C:/Users/Vibhuti/Desktop/Multiple disease prediction/saved", "heart_disease_saved")

diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))

with st.sidebar:
    selected=option_menu("Multiple disease prediction system",
                         ["Diabetes prediction",
                         "Heart disease prediction"],
                         default_index=0)


if(selected=="Diabetes prediction"):
    st.title("Diabetes prediction using ML")


if(selected=="Heart disease prediction"):
    st.title("Heart disease prediction using ML")


