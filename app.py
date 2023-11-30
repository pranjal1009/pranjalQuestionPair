import streamlit as st
import helper
import pickle
from PIL import Image


model = pickle.load(open('model.pkl','rb'))

st.header('Hi! From MITAOE :smiley: ')
st.header('Duplicate Question Pairs')

image = Image.open('mitaoe-logo-2.png')
image = image.resize((250,250))
st.image(image)

st.subheader('Group Members:')
st.text('Pranjal Patil')
st.text('Rachi Wasnik')
st.text('Isha Chatap')

st.divider()

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.subheader('Questions are :rainbow[Duplicate]')
    else:
        st.subheader('Questions are :rainbow[Not Duplicate]')
