# navigation.py
import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("🏢 ParadoxBi")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            if st.session_state.user_role == "admin":  # Example: Show all pages to admins
                st.page_link("pages/page1.py", label="Found Person", icon="🔎")
                st.page_link("pages/page2.py", label="Lost Entry", icon="🕵")
                st.page_link("pages/page3.py", label="Database", icon="💾")
            elif st.session_state.user_role == "viewer": # Example: Show only viewing pages 
                st.page_link("pages/page4.py", label="Found Person", icon="🔎")
                st.page_link("pages/page5.py", label="Lost Entry", icon="🕵")
            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "streamlit_app":
            st.switch_page("streamlit_app.py")


def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None  # Clear the user role
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")