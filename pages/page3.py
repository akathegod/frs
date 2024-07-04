import streamlit as st 
from navigation import make_sidebar
import pickle 
import yaml 
import pandas as pd 

# code to hide the watermark using CSS

# #MainMenu to hide the burger menu at the top-right side
# footer to hide the ⁠ made with streamlit ⁠ mark
hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
	header {visibility: hidden;}
	#GithubIcon {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)


cfg = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)
PKL_PATH = cfg['PATH']["PKL_PATH"]
st.set_page_config(layout="wide")



make_sidebar()

#Load databse 
with open(PKL_PATH, 'rb') as file:
    database = pickle.load(file)

Index, Id, Name, Image  = st.columns([0.5,0.5,3,3])

for idx, person in database.items():
    with Index:
        st.write(idx)
    with Id: 
        st.write(person['id'])
    with Name:     
        st.write(person['name'])
    with Image:     
        st.image(person['image'],width=200)

