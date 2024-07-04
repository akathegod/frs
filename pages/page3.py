import streamlit as st 
import pickle 
import yaml 
import pandas as pd

# Load YAML config
cfg = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)
PKL_PATH = cfg['PATH']["PKL_PATH"]
st.set_page_config(layout="wide")

# Function to create sidebar
from navigation import make_sidebar
make_sidebar()

# Load database from pickle
with open(PKL_PATH, 'rb') as file:
    database = pickle.load(file)

# Define columns for layout
Index, Id, Name, Image = st.columns([0.5, 0.5, 3, 3])

# Iterate through database items and display
for idx, person in database.items():
    with Index:
        st.write(idx)
    with Id: 
        st.write(person['id'])
    with Name:     
        st.write(person['name'])
    with Image:     
        # Display image with custom CSS
        st.markdown(f'<style>.stImage > img {{ max-width: 200px; }}</style>', unsafe_allow_html=True)
        st.markdown(f'<div class="stImage"><img src="{person["image"]}" width="200"></div>', unsafe_allow_html=True)

