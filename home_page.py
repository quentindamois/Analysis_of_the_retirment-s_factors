import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Home_page",
    page_icon=":house:"
)

image1 = Image.open('Journee_internationale_2024_(225).jpg')
st.image(image1, caption='Photo taken by Efrei Picture Studio')




st.sidebar.success("Select a page above.")


st.sidebar.markdown("About me")
st.sidebar.link_button("Github", url="https://github.com/quentindamois")
st.sidebar.link_button("LinkedIn", url="www.linkedin.com/in/quentin-damois-6756a7222")
st.title("Quentin DAMOIS's Dashbord")




st.markdown("# welcome to my dashboard")

st.markdown("I am a student at Efrei in ING 2 DAI (Data and IA)\nThis dash board was made during my 7 semester in Data Visulization.")






st.markdown("This dash board possess four pages : ")
st.markdown(" - The presentation page")
st.markdown(" - a data analysis of the factors of retirement")
st.markdown(" - page presenting me")
st.markdown("- a display of the data of a uber analysis")

