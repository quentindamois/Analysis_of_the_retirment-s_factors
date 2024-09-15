import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Welcome_to_my_Dashboard",
    page_icon=":mag:",
)


st.sidebar.success("Select a page above.")


st.sidebar.markdown("About me")
st.sidebar.link_button("Github", url="https://github.com/quentindamois")
st.sidebar.link_button("LinkedIn", url="www.linkedin.com/in/quentin-damois-6756a7222")
st.title("Quentin DAMOIS's Dashbord")

image = Image.open('CV-IMG_5875-75.jpg')
st.image(image, caption='me')



st.markdown("welcome to my dashboard")
st.markdown("I am a student at Efrei in ING 2 DAI")