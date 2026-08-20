import streamlit as st
from PIL import Image

st.title("HOLA !!! mi Nombre es Miguelato ")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Imagen.open('Juan_imagen_10.jpg')
st.image(image, caption='Interfaces multimodales')
