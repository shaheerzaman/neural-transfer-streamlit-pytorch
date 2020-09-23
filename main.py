import streamlit as st
from PIL import Image
import os

import style

st.title('Pytorch style transfer')

img = st.sidebar.selectbox(
    'Select Image', 
    ('amber.jpg', 'dog.jpg')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = 'saved_models/' + style_name + '.pth'
input_image = 'images/content-images/' + img
print(input_image)
output_image = 'images/output-images/' + style_name + '-' + img

st.write('### Source image:')
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button('stylize')
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)
    
    st.write('### output image:')
    image = Image.open(output_image)
    st.image(image, width=400)