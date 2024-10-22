import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.graph_objects as go

import numpy as np

import plotly.express as pxex

import altair as alt

import seaborn as sns

st.set_page_config(page_title="Retirement Visualisation", page_icon=":older_man:")
st.markdown("# Data visualisation")
st.sidebar.header("Data visualisaiton")

st.sidebar.success("Select a page above.")


st.sidebar.markdown("About me")
st.sidebar.link_button("Github", url="https://github.com/quentindamois")
st.sidebar.link_button("LinkedIn", url="www.linkedin.com/in/quentin-damois-6756a7222")
st.title("Quentin DAMOIS's Dashbord")

st.markdown("Where I studied and worked.")
df_work_and_studied = pd.DataFrame(data={"name":["Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)", "Semester abroad at Concordia University", "Manual interns - June 2022", "Commercial internship - January 2023", "Technical Internship - November 2024 to March 2025"],"latitude":[48.788919667159, 45.494903083235265, 48.865683133066284, 48.89052395645421, 56.85463907044315],"longitude":[2.3637624080891126, -73.57795388215288, 1.7970965394315566, 2.3490770246054242, 14.83034541100049 ],"type":["Study", "Study", "Internship", "Internship", "Internship"]})


map_fig = st.map(data=df_work_and_studied, latitude= "latitude", longitude= "longitude")


with st.expander("How it is done"):
    st.code("""

st.markdown("Where I studied and worked.")
df_work_and_studied = pd.DataFrame(data={"name":["Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)", "Semester abroad at Concordia University", "Manual interns - June 2022", "Commercial internship - January 2023", "Technical Internship - November 2024 to March 2025"],"latitude":[48.788919667159, 45.494903083235265, 48.865683133066284, 48.89052395645421, 56.85463907044315],"longitude":[2.3637624080891126, -73.57795388215288, 1.7970965394315566, 2.3490770246054242, 14.83034541100049 ],"type":["Study", "Study", "Internship", "Internship", "Internship"]})


map_fig = st.map(data=df_work_and_studied, latitude= "latitude", longitude= "longitude")


""")

info = {"name":["Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)", "NLP certification - April 2024 - Skill4All", "Semester abroad at Concordia University in Montreal", "Highschool diploma - 2021 - Highschool Viollet Le Duc (Villiers-Saint-Frédéric-78)", "EXPLAIN project - June-July 2024", "Study of land registration - June-July 2024", "Mathematical modelling - May 2023", "Data base - April 2023", "Surveying users' needs - January-May 2024", "Graphs theory - mars 2024", "Transvers project - February-May 2023", "Commercial internship - January 2023", "Manual interns - June 2022", "Informatic", "English", "Story telling (June 2022)", "Membre of the Pandora (From 2021)", "Oral expression (From 2011 to 2018)", "Member of the association Asian EFREI (From 2022)", "interests"], "type":["Education", "Education", "Education", "Education", "Academic Projects", "Academic Projects", "Academic Projects", "Academic Projects", "Academic Projects", "Academic Projects", "Academic Projects", "Professional Experiences", "Professional Experiences", "Skills", "Skills", "Skills", "Centre of interests", "Centre of interests", "Centre of interests", "Centre of interests"]}

df_info = pd.DataFrame(data=info)


info_categorie = ["Education", "Academic Projects", "Professional Experiences", "Skills", "Centre of interests"]

fig2 = pxex.pie(values=[len(df_info[df_info["type"] == i]) for i in info_categorie], names=info_categorie)
st.plotly_chart(fig2)

with st.expander("How it is done"):
    st.code("""

df_info = pd.DataFrame(data=info)


info_categorie = ["Education", "Academic Projects", "Professional Experiences", "Skills", "Centre of interests"]

fig2 = pxex.pie(values=[len(df_info[df_info["type"] == i]) for i in info_categorie], names=info_categorie)
st.plotly_chart(fig2)


""")

axes = ["category", "name", "precision"]

dict_profil = {"category":[], "name":[], "precision":[]}

content = [["Education", "Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)", "Python algorithmics"],
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","statistics"],
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","probability"],
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","database"],
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","machine learning"],
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","cryptography"],	
["Education","Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)","cybersecurity"],
["Education","NLP certification - April 2024 - Skill4All","Training in Natural Language Processing"],
["Education","Semester abroad at Concordia University in Montreal","Java"],		
["Education","Semester abroad at Concordia University in Montreal","UML"],
["Education","Semester abroad at Concordia University in Montreal","Web programming"],
["Education","Semester abroad at Concordia University in Montreal","assembly language x86"],
["Education","Highschool diploma - 2021 - Highschool Viollet Le Duc (Villiers-Saint-Frédéric-78)","Speciality in Mathematics and Physics"],
["Education","Highschool diploma - 2021 - Highschool Viollet Le Duc (Villiers-Saint-Frédéric-78)","high school diploma"],
["Education","Highschool diploma - 2021 - Highschool Viollet Le Duc (Villiers-Saint-Frédéric-78)","with honours"],
["Academic Projects","EXPLAIN project - June-July 2024","Fine-tuned a distil bert for patent classification"],
["Academic Projects","EXPLAIN project - June-July 2024","Used the library transformers-interpret to explain the prediction"],
["Academic Projects","Study of land registration - June-July 2024","Cleaned and analysing a data frame containing information on 2023 land registration"],
["Academic Projects","Study of land registration - June-July 2024","Created supervised learning and non-supervised learning model"],
["Academic Projects","Mathematical modelling - May 2023","Created a mathematical model to observe the evolution of prey and predator populations"],
["Academic Projects","Mathematical modelling - May 2023","Used MATLAB"],
["Academic Projects","Data base - April 2023","Created a data base with MySQL Workbench"],
["Academic Projects","Data base - April 2023","Stored the data of football matches"],
["Academic Projects","Surveying users' needs - January-May 2024","Created an application to manage virtual queues"],
["Academic Projects","Surveying users' needs - January-May 2024","Studied potential users' needs: Processing and interpretation of the gathered data"],
["Academic Projects","Surveying users' needs - January-May 2024","Pitched our project to industry professionals: third place in the TechDay"],
["Academic Projects","Graphs theory - mars 2024","Coded in Python"],
["Academic Projects","Graphs theory - mars 2024","Object Oriented programming"],	
["Academic Projects","Graphs theory - mars 2024","Modelled graph for scheduling"],
["Academic Projects","Transvers project - February-May 2023","Web scrapping: Used stockx-API to gather a large amount of data from the internet (brand of shoes)"],
["Academic Projects","Transvers project - February-May 2023","Programmed a Marketplace to resell shoes."],
["Professional Experiences","Commercial internship - January 2023","Internship in Henri SELMER's showroom (manufacturing and selling of saxophones and clarinets)"],		
["Professional Experiences","Commercial internship - January 2023","Assisted customers"],
["Professional Experiences","Commercial internship - January 2023","Programmed a Marketplace to resell shoes."],		
["Professional Experiences","Manual internship - June 2022","Internship at SPAT G20 (Supermarket)."],
["Professional Experiences","Technical Internship - November 2024 to March 2025","Internship at Linnaeus universty DISA."],
["Skills","Informatic","Simulink"],
["Skills","Informatic","MATLAB"],
["Skills","Informatic","programming in Python"],
["Skills","Informatic","HTML"],
["Skills","Informatic","JavaScript"],		
["Skills","Informatic","Java"],		
["Skills","Informatic","C"],	
["Skills","Informatic","CSS"],
["Skills","Informatic","Mastering office (Word, Excel, PowerPoint, …)"],
["Skills","English","Fluent (TOEIC: 945)"],
["Skills","Story telling (June 2022)","Finalist in the contest “Fairytale and storyteller”: writing and reading a fairytale on tolerance and diversity."],
["Center of interests","Member of the Pandora (From 2021)","Meeting and discussions about video games on consoles."],
["Center of interests","Oral expression (From 2011 to 2018)","Acting in different theatre associations. Taking part in several plays."],
["Center of interests","Member of the association Asian EFREI (From 2022)","Meetings about the different Asian cultures."],
["Center of interests","interests","Visit of foreign countries and France's regions"],
["Center of interests","interests","Coding"],		
["Center of interests","interests","Video games"],		
["Center of interests","interests","History"],		
["Center of interests","interests","Software engineering"],		
["Center of interests","interests","Artificial intelligence"]]



for i in content:
    for j in range(len(i)):
        dict_profil[axes[j]].append(i[j])

df_profil = pd.DataFrame(dict_profil)

st.markdown("My experience")
fig3 = pxex.icicle(df_profil, path=[pxex.Constant("all"), "category", "name", "precision"])
st.plotly_chart(fig3)

with st.expander("How it is done"):
    st.code("""

for i in content:
    for j in range(len(i)):
        dict_profil[axes[j]].append(i[j])

df_profil = pd.DataFrame(dict_profil)

st.markdown()
fig3 = pxex.icicle(df_profil, path=[pxex.Constant("all"), "category", "name", "precision"])
st.plotly_chart(fig3)

""")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Education", "Academic Projects", "Professional Experiences", "Skills", "Centre of interests"])
with tab1:
    with st.expander("Master's degree - 2021-2024 - EFREI PARIS (Engineering school of Digital Technologies)"):
        for i in ("Python algorithmics\tstatistics\tprobability\tdatabase\tmachine learning\tcryptography\tcybersecurity".split("\t")):
            st.markdown(f" - {i}")
    with st.expander("NLP certification - April 2024 - Skill4All"):
        st.markdown(" - Training in Natural Language Processing")
    with st.expander("Semester abroad at Concordia University in Montreal"):
        for i in ("Java\tUML\tWeb programming\tassembly language x86".split("\t")):
            st.markdown(f" - {i}")
    with st.expander("Highschool diploma - 2021 - Highschool Viollet Le Duc (Villiers-Saint-Frédéric-78)"):
        st.markdown(" - Speciality in Mathematics and Physics")
        st.markdown(" - high school diploma ")
        st.markdown(" - with honours")

with tab2:
    with st.expander("EXPLAIN project - June-July 2024"):
        for i in ["Fine-tuned a distil bert for patent classification", "Used the library transformers-interpret to explain the prediction"]:
            st.markdown(f" - {i}")
    with st.expander("Study of land registration - June-July 2024"):
        for i in ["Cleaned and analysing a data frame containing information on 2023 land registration", "Created supervised learning and non-supervised learning model"]:
            st.markdown(f" - {i}")
    with st.expander("Mathematical modelling - May 2023"):
        for i in ["Created a mathematical model to observe the evolution of prey and predator populations", "Used MATLAB"]:
            st.markdown(f" - {i}")
    with st.expander("Data base - April 2023"):
        for i in ["Created a data base with MySQL Workbench", "Stored the data of football matches"]:
            st.markdown(f" - {i}")
    with st.expander("Surveying users' needs - January-May 2024"):
        for i in ["Created an application to manage virtual queues", "•	Studied potential users' needs: Processing and interpretation of the gathered data", "Pitched our project to industry professionals: third place in the TechDay"]:
            st.markdown(f" - {i}")
    with st.expander("Graphs theory - mars 2024"):
        for i in ["Coded in Python", "Object Oriented programming", "Modelled graph for scheduling"]:
            st.markdown(f" - {i}")
    with st.expander("Transvers project - February-May 2023"):
        for i in ["Web scrapping: Used stockx-API to gather a large amount of data from the internet (brand of shoes)", "Programmed a Marketplace to resell shoes."]:
            st.markdown(f" - {i}")

with tab3:
    with st.expander("Commercial internship - January 2023"):
        for i in ["Internship in Henri SELMER's showroom (manufacturing and selling of saxophones and clarinets)", "Assisted customers", "Programmed a Marketplace to resell shoes."]:
            st.markdown(f" - {i}")
    with st.expander("Manual interns - June 2022"):
        st.markdown(" - Internship at SPAT G20 (Supermarket).")

with tab4:
    with st.expander("Informatic"):
        for i in ["Simulink", "MATLAB", "programming in Python", "HTML", "JavaScript", "Java", "C", "CSS","Mastering office (Word, Excel, PowerPoint, …)"]:
            st.markdown(f" - {i}")
    with st.expander("English"):
        st.markdown("Fluent (TOEIC: 945)")
    with st.expander("Story telling (June 2022)"):
        st.markdown("Finalist in the contest “Fairytale and storyteller”:  writing and reading a fairytale on tolerance and diversity.")

with tab5:
    with st.expander("Membre of the Pandora (From 2021)"):
        st.markdown("Meeting and discussions about video games on consoles.")
    with st.expander("Oral expression (From 2011 to 2018)"):
        st.markdown("Acting in different theatre associations. Taking part in several plays.")
    with st.expander("Member of the association Asian EFREI (From 2022)"):
        st.markdown("Meetings about the different Asian cultures.")
    with st.expander("interests"):
        for i in ["Visit of foreign countries and France's regions", "Coding", "Video games", "history", "Software engineering", "Artificial intelligence" ]:
            st.markdown(f" - {i}")




