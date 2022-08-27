import streamlit as st
import pandas as pd 
import numpy as np 
import pickle 
import cv2
from PIL import Image

st.set_page_config(
     page_title="Digit Recognizer")

with open('W1','rb') as f:
  W1= pickle.load(f)

with open('W2','rb') as f:
  W2= pickle.load(f)

with open('b1','rb') as f:
  b1= pickle.load(f)

with open('b2','rb') as f:
  b2= pickle.load(f)

#forward
def ReLU(Z):
    return np.maximum(0, Z)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A

def get_predictions(A2):
    return np.argmax(A2, 0)

def forward_prop(W1, b1, W2, b2, X):    
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

#make prediction
def make_predictions(W1, b1, W2, b2, X):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    probability = np.amax(A2) * 100
    return predictions, probability
    

st.header('Digit Recognizer')
uploadfile = st.file_uploader("Upload the digit image you want to test:")

if uploadfile is not None:
    
    img = Image.open(uploadfile)
    img_array = np.array(img)

    # cv2.imwrite('out.png')
    # image =cv2.imread('out.png')

    resized_img=cv2.resize(img_array,(28,28))
    gray=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
    ret,fimg=cv2.threshold(blur,250,255,cv2.THRESH_BINARY_INV)
    input_img=fimg.flatten()
    input_img=np.reshape(input_img,(784,1))
    input_img=input_img/255

    predictions, probability=make_predictions(W1,b1,W2,b2,input_img)
    result=predictions
    st.write("Your image:")
    st.image(uploadfile)
    
    if result==[0]:
     st.markdown(f'<h1 style="font-size:24px;">Result:0</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[1]:
     st.markdown(f'<h1 style="font-size:24px;">Result:1</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[2]:
     st.markdown(f'<h1 style="font-size:24px;">Result:2</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[3]:
     st.markdown(f'<h1 style="font-size:24px;">Result:3</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[4]:
     st.markdown(f'<h1 style="font-size:24px;">Result:4</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[5]:
     st.markdown(f'<h1 style="font-size:24px;">Result:5</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[6]:
     st.markdown(f'<h1 style="font-size:24px;">Result:6</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[7]:
     st.markdown(f'<h1 style="font-size:24px;">Result:7</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[8]:
     st.markdown(f'<h1 style="font-size:24px;">Result:8</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    elif result==[9]:
     st.markdown(f'<h1 style="font-size:24px;">Result:9</h1>', unsafe_allow_html=True)
     st.write("Confidence:",probability)
    else:
     st.markdown(f'<h1 style="font-size:30px; color:red">No Result</h1>', unsafe_allow_html=True)

else:
    st.write("You should upload file")
