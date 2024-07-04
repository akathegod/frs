# mainapp.py
import streamlit as st
from time import sleep
from navigation import make_sidebar

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







# Placeholder for authentication - Replace with your logic!
def authenticate_user(username, password): 
    user_credentials = {
        "admin": {"password": "admin", "role": "admin"},
        "user": {"password": "user", "role": "viewer"}, 
    }
    if username in user_credentials and user_credentials[username]['password'] == password:
        return user_credentials[username]
    return None

make_sidebar()

st.title("Welcome to ParadoxBi 🏢")

st.write("Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    user_data = authenticate_user(username, password)  
    if user_data:
        st.session_state.logged_in = True
        st.session_state.user_role = user_data['role'] 
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/page4.py")
    else:
        st.error("Incorrect username or password") 
