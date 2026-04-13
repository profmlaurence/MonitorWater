import kagglehub
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    # Download latest version
    path = kagglehub.dataset_download("adityakadiwal/water-potability")
    df = pd.read_csv(path + "/water_potability.csv")
    return df

def get_data_name():
    return "adityakadiwal/water-potability"

def get_data_info():
    return kagglehub.dataset_info(get_data_name())