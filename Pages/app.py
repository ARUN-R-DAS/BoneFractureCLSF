import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
from skimage.io import imread
from skimage.transform import resize


def main():
    model = load_model("C:\_PROJECTS\BoneFractureCLSF\model.keras")

    st.header('Detect Fracture')

    #File Uploader
    uploaded_file = st.file_uploader("Upload an image",type=['jpg','png','jpeg'])

    if uploaded_file is not None:
        if st.button("Predict"):
            try:
                # image = Image.open(uploaded_file)
                image = imread(uploaded_file)
                img = resize(image,(150,150,1))
                img2 = resize(img,(1,150,150,1))
                st.image(img,caption='Uploaded Image')
                pred = model.predict(img2)
                ind = pred.argmax()
                if ind:
                    st.success("Fractured")
                else:
                    st.success("Not fractured")
            except Exception as e:
                print(e)


    st.markdown("## ")

    c1,c2,c3 = st.columns([1,3,1], gap="large", vertical_alignment="center", border=True)
    with c2:
        st.markdown("""
        <h4 style='font-size:25px; color:#4A90E2; padding-left:45px;'>
                    Rate your Experience
        </h4>
        """, unsafe_allow_html=True)

        a1,a2 = st.columns([0.18,0.5])
        with a2:
            selected = st.feedback('stars')


    if selected != None: 
        if selected < 2:
            st.markdown("""
            <div style='background-color:#E46A2A; padding:15px; text-align:center; border-radius:8px; color:white; font-size:18px;'>
                    Sorry the app didn't meet expectations. 😞
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                "<div style='text-align:center;'>Please share your experience and how this page could be improved.</div>",
                unsafe_allow_html=True
            )
            suggestion = st.text_area("share your experience")
            if st.button("Submit"):
                st.success("Thank you for your feedback!")

        elif selected < 3:
            st.markdown("""
            <div style='background-color:#0080FF; padding:15px; text-align:center; border-radius:8px; color:white; font-size:18px;'>
                    Thanks for the feedback!
            </div>
            """, unsafe_allow_html=True)
            st.markdown(
                "<div style='text-align:center;'>Open to suggestions — feel free to mention what could be better.</div>",
                unsafe_allow_html=True
            )
            suggestion = st.text_area("share your experience")
            if st.button("Submit"):
                st.success("Thank you for your feedback!")

        elif selected < 4:
            st.markdown("""
            <div style='background-color:#00b102; padding:15px; text-align:center; border-radius:8px; color:white; font-size:18px;'>
                    Glad you found it useful! 😊
            </div>
            """, unsafe_allow_html=True)

        else:
            st.balloons()
            st.markdown("""
            <div style='background-color:#00b102; padding:15px; text-align:center; border-radius:8px; color:white; font-size:18px;'>
                    Awesome! ⭐⭐⭐⭐⭐ Really appreciate the support!
            </div>
            """, unsafe_allow_html=True)

