import streamlit as st
import pandas as pd 
import numpy as np 
import pickle 
#import cv2

st.set_page_config(
     page_title="Digit Recognizer")
st.markdown(
  f"""
    <style>
     .stApp {{
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRytWY61RnHQHu934tyjvpUOOIrVYdbN2falCZxMK62o60VxBK9JUoNoncVQmKxx_DKp5c&usqp=CAU");
        background-attachment: fixed;
        background-size: cover}}
     </style>
  """,
unsafe_allow_html=True)

st.header('Digit Recognizer')
uploadfile = st.file_uploader("Upload the digit image you want to test:")

if uploadfile is not None:
    st.write("Your image:")
    st.image(uploadfile)

else:
    st.write("You should upload file")
