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
        background-image: url("https://img.freepik.com/premium-vector/binary-matrix-code-background_6735-815.jpg");
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
