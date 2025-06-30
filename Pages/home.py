import streamlit as st

def show():

    st.header("Bone Fracture Detection from X-rays")
    st.write("""
    Welcome to the Bone Fracture Detection app! 
             
    This project leverages deep learning to assist in the early and accurate detection of bone fractures from X-ray images. 

    Upload your X-ray images and the AI model will analyze them to predict the presence of fractures. 

    Get started by navigating to the 'Detect Fracture' tab!
    """)
