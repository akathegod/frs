import streamlit as st 
from navigation import make_sidebar
import cv2
import yaml 
import pickle 
from utils import submitNew, get_info_from_id, deleteOne
import numpy as np

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


make_sidebar()


#st.set_page_config(layout="wide")
st.title("Lost Person!")
st.write("Please fill the details!")

menu = ["Adding"]
choice = st.sidebar.selectbox("Options",menu)
if choice == "Adding":
    name = st.text_input("Full Name of the Missing Person!",placeholder='Enter name')
    id = st.text_input("ID",placeholder='Enter id')
    #Create 2 options: Upload image or use webcam
    #If upload image is selected, show a file uploader
    #If use webcam is selected, show a button to start webcam
    upload = st.radio("Upload image or use webcam",("Upload","Webcam"))
    if upload == "Upload":
        uploaded_image = st.file_uploader("Upload",type=['jpg','png','jpeg'])
        if uploaded_image is not None:
            st.image(uploaded_image)
            submit_btn = st.button("Submit",key="submit_btn")
            if submit_btn:
                if name == "" or id == "":
                    st.error("Please enter name and ID")
                else:
                    ret = submitNew(name, id, uploaded_image)
                    if ret == 1: 
                        st.success("Missing Person Added")
                    elif ret == 0: 
                        st.error("Missing Person ID already exists")
                    elif ret == -1: 
                        st.error("There is no face in the picture")
    elif upload == "Webcam":
        img_file_buffer = st.camera_input("Take a picture")
        submit_btn = st.button("Submit",key="submit_btn")
        if img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            bytes_data = img_file_buffer.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            if submit_btn: 
                if name == "" or id == "":
                    st.error("Please enter name and ID")
                else:
                    ret = submitNew(name, id, cv2_img)
                    if ret == 1: 
                        st.success("Missing Person Added")
                    elif ret == 0: 
                        st.error("Missing Person ID already exists")
                    elif ret == -1: 
                        st.error("There is no face in the picture")

                
