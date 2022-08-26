import streamlit as st
import pandas as pd 
import numpy as np 

st.set_page_config(
     page_title="Digit Recognizer")

st.header('Digit Recognizer')
uploadfile = st.file_uploader("Upload the digit image you want to test:")

if uploadfile is not None:
    st.write("Your image:")
    st.image(uploadfile)
    st.markdown(f'<h1 style="font-size:24px;">{"Output: 4"}</h1>', unsafe_allow_html=True)

else:
    st.write("You should upload file")