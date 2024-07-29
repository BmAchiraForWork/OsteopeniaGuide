import streamlit as st
from PIL import Image

# Set the title of the Streamlit app
st.title('คู่มือการใช้งาน')

# Loop through the image names and display each one
for i in range(1, 10):
    image_path = f'how{i}.png'
    image = Image.open(image_path)
    st.image(image)
