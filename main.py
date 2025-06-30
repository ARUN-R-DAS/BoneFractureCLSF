from streamlit_option_menu import option_menu
import streamlit as st
from Pages import home, app, about

st.markdown("""
    <style>
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background: linear-gradient(-45deg, #4b0082, #1B1B1B, #000080);
        background-size: 600% 600%;
        animation: gradientBG 10s linear infinite;
    }
    </style>
""", unsafe_allow_html=True)




st.set_page_config(initial_sidebar_state="collapsed")
selected = option_menu(
    menu_title="",
    options=["Overview", "Detect Fracture", "Connect"],
    icons=["info-circle", "activity", "person-lines-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Overview":
    home.show()
elif selected == "Detect Fracture":
    app.main()
elif selected == "Connect":
    about.show()

