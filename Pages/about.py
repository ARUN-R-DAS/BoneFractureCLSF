import streamlit as st

def show():

    st.markdown("""
        <h2 style='text-align: center; color: #4A90E2;'>About This Project</h2>
        <p style='text-align: center; font-size: 17px; color: #dddddd; max-width: 700px; margin: auto;'>
            This application is developed as a part of a deep learning project at Luminar Technolab under the guidance of Dr.Prajesha T M to classify X-ray images for fracture detection.
            It is powered by a  custom-trained convolutional neural network (CNN) model.
        </p>
        <br>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <h3 style='color: #4A90E2;'>🔗 Connect with Me</h3>
        <ul style='list-style: none; padding-left: 0; font-size: 16px;'>
            <li>💼 <a href='https://www.linkedin.com/in/arunrdas' target='_blank'>LinkedIn</a></li>
            <li>💻 <a href='https://github.com/your-github' target='_blank'>GitHub</a></li>
            <li>📊 <a href='https://www.kaggle.com/datasets/your-dataset-link' target='_blank'>Dataset (Kaggle)</a></li>
        </ul>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <p style='text-align: center; font-size: 14px; color: gray;'>
            Made with Streamlit & TensorFlow
        </p>
    """, unsafe_allow_html=True)
