import streamlit as st
from PIL import Image

st.title('คู่มือการใช้งาน')

image = Image.open('how2.png')
st.image(image)