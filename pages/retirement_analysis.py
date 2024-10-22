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

st.markdown("Two years ago, a retirements reform was promulgated in France. In order to better for people to better understand the situation of people that where retiring prior to that time I have taken the oppurtinty offered by my course Data Visualistion to anaylyse the siutation between 2013 and 2020.")

@st.cache_data
def diff_kind_of_categories(dataset):
    res  = set(dataset["categorie_socioprofessionnelle"])
    len_res = len(list(res))
    return res, len_res


@st.cache_data
def opening_dataset():
    df_sub = pd.read_csv("./departretraite_parcsp.csv", delimiter = ';')
    #df_sub["annee"] = df_sub["annee"].map(lambda x : int(x * 100))
    return df_sub

df = opening_dataset()



st.markdown("## You can see below the dataset used for the visualisation")
st.markdown("I downloaded the data from the data.gov : ")
st.page_link("https://www.data.gouv.fr/fr/datasets/age-de-depart-a-la-retraite-et-conditions-de-fin-de-carriere-selon-la-categorie-socioprofessionnelle/#/resources", label="data.gov")


st.write(df)

with st.expander("See how it is done"):
    st.code("""
@st.cache_data
def diff_kind_of_categories(dataset):
    res  = set(dataset["categorie_socioprofessionnelle"])
    len_res = len(list(res))
    return res, len_res


@st.cache_data
def opening_dataset():
    df_sub = pd.read_csv("./departretraite_parcsp.csv", delimiter = ';')
    #df_sub["annee"] = df_sub["annee"].map(lambda x : int(x * 100))
    return df_sub

df = opening_dataset()



st.markdown("## You can see below the dataset used for the visualisation")
st.markdown("I downloaded the data from the data.gov : ")
st.page_link("https://www.data.gouv.fr/fr/datasets/age-de-depart-a-la-retraite-et-conditions-de-fin-de-carriere-selon-la-categorie-socioprofessionnelle/#/resources", label="data.gov")

st.write(df)
""")


set_categories, nb_categories = diff_kind_of_categories(df)

list_tabs = []
for i in sorted(list(set_categories)):
    list_tabs.append(i)

st.markdown(f"First thing first, let us see if the different kind the {nb_categories} categories and all years are equally present.")

st.markdown("As reminder, here are all the sociaprofessionnal categories : \n - " + "\n - ".join(set_categories))
st.markdown("The socioprofessionnal categories 7 and 8 are not present since thhey are people that are retired and people that are not employed.\nFor more information : https://www.insee.fr/fr/metadonnees/pcs2003/categorieSocioprofessionnelleAgregee/1?champRecherche=true")
with st.expander(" How it is made"):
    st.code("""
set_categories, nb_categories = diff_kind_of_categories(df)

list_tabs = []
for i in sorted(list(set_categories)):
    list_tabs.append(i)

st.markdown(f"First thing first, let us see if the different kind the {nb_categories} categories and all years are equally present.")

st.markdown("As reminder, here are all the sociaprofessionnal categories : \n - " + "\n - ".join(set_categories))

""")


colAlpha, colBeta = st.columns(2)


with colAlpha:
    fig1, ax1 = plt.subplots()
    ax1.hist((df["categorie_socioprofessionnelle"].map(lambda x: int(str(x)[0:1]))), bins = 100, color = 'g', alpha = 0.5)
    plt.title("histogram of the siocioprofessional categories")
    plt.xlabel("socioprofessional categories")
    plt.ylabel("Frequency")
    st.pyplot(fig1)
    with st.expander("How it is made"):
        st.code("""
    fig1, ax1 = plt.subplots()
    ax1.hist((df["categorie_socioprofessionnelle"].map(lambda x: int(str(x)[0:1]))), bins = 100, color = 'g', alpha = 0.5)
    plt.title("histogram of the siocioprofessional categories")
    plt.xlabel("socioprofessional categories")
    plt.ylabel("Frequency")
    st.pyplot(fig1)
""")




with colBeta:
    fig2, ax2 = plt.subplots()
    ax2.hist(df["annee"], bins = 100, range = (min(df["annee"]) , max(df["annee"])), color = 'g', alpha = 0.5, label = "annee")
    plt.title("histogram of the Year")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    st.pyplot(fig2)
    with st.expander("How it is made"):
        st.code("""
    fig2, ax2 = plt.subplots()
    ax2.hist(df["annee"], bins = 100, range = (min(df["annee"]) , max(df["annee"])), color = 'g', alpha = 0.5, label = "annee")
    plt.title("histogram of the Year")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    st.pyplot(fig2)
""")

st.markdown("Now that we saw the the socioprofessional categories are equaly represented.")
st.markdown("## Part 1 : When are people retiring ?")
st.markdown("Let us see the evolution of the conjonctural age to be retired and the proportion of people retired at 61.")

#essaie = sns.pairplot(df, hue="categorie_socioprofessionnelle")
#st.write(sns.pairplot(df, hue="categorie_socioprofessionnelle"))



st.markdown("The wideness of each slice is influenced by the proportion of people getting retired at 61.\nThe color is determined buy the conjonctural age of retirement.")
st.markdown("In order to do so we will see the evolution of two varibale of the dataset :\n - proportion_de_retraites_a_61_ans\n - age_conjoncturel_de_depart_a_la_retraite")

tabAlpha, tabBeta = st.tabs(["categorie by year ", "year by categorie"])

with tabAlpha:
    fig8 = pxex.icicle(df[df['categorie_socioprofessionnelle'] != '9 - Toutes CSP confondues'], path=[pxex.Constant("all"),'annee', 'categorie_socioprofessionnelle'], values='proportion_de_retraites_a_61_ans', color='age_conjoncturel_de_depart_a_la_retraite', hover_data=['annee', 'categorie_socioprofessionnelle', 'proportion_de_retraites_a_61_ans', 'age_conjoncturel_de_depart_a_la_retraite'], color_continuous_scale='RdBu', color_continuous_midpoint=np.average(df['age_conjoncturel_de_depart_a_la_retraite'], weights=df['proportion_de_retraites_a_61_ans']) )
    st.plotly_chart(fig8)

with tabBeta:
    fig3 = pxex.sunburst(df[df['categorie_socioprofessionnelle'] != '9 - Toutes CSP confondues'], path=['categorie_socioprofessionnelle', 'annee'], values='proportion_de_retraites_a_61_ans', color='age_conjoncturel_de_depart_a_la_retraite', hover_data=['annee', 'categorie_socioprofessionnelle', 'proportion_de_retraites_a_61_ans', 'age_conjoncturel_de_depart_a_la_retraite'], color_continuous_scale='RdBu', color_continuous_midpoint=np.average(df['age_conjoncturel_de_depart_a_la_retraite'], weights=df['proportion_de_retraites_a_61_ans']))
    st.plotly_chart(fig3)

with st.expander("How it is made"):
    st.code("""
tabAlpha, tabBeta = st.tabs(["categorie by year ", "year by categorie"])

with tabAlpha:
    fig8 = pxex.icicle(df[df['categorie_socioprofessionnelle'] != '9 - Toutes CSP confondues'], path=[pxex.Constant("all"),'annee', 'categorie_socioprofessionnelle'], values='proportion_de_retraites_a_61_ans', color='age_conjoncturel_de_depart_a_la_retraite', hover_data=['annee', 'categorie_socioprofessionnelle', 'proportion_de_retraites_a_61_ans', 'age_conjoncturel_de_depart_a_la_retraite'], color_continuous_scale='RdBu', color_continuous_midpoint=np.average(df['age_conjoncturel_de_depart_a_la_retraite'], weights=df['proportion_de_retraites_a_61_ans']) )
    st.plotly_chart(fig8)

with tabBeta:
    fig3 = pxex.sunburst(df[df['categorie_socioprofessionnelle'] != '9 - Toutes CSP confondues'], path=['categorie_socioprofessionnelle', 'annee'], values='proportion_de_retraites_a_61_ans', color='age_conjoncturel_de_depart_a_la_retraite', hover_data=['annee', 'categorie_socioprofessionnelle', 'proportion_de_retraites_a_61_ans', 'age_conjoncturel_de_depart_a_la_retraite'], color_continuous_scale='RdBu', color_continuous_midpoint=np.average(df['age_conjoncturel_de_depart_a_la_retraite'], weights=df['proportion_de_retraites_a_61_ans']))
    st.plotly_chart(fig3)
            

            """)

st.markdown("The socio-professionnal category 9 is not present since it represent all of the other socioprofessionnal category. By looking at this graph we can see two trend:\n1. The conjonctural retirement age is increasing for each category.\n2. The proportion of people retired at the age of 61 is decreasing in every categorires.")
#st.markdown("Futhermore, we can see that some socioprofessionnal categories have diffrentre conjonctureal restirement age and proportion of people retired at the age of 61.")
st.markdown("By comparing the different socioprofessional categories we can distinguish two kind :\n - the socioprofessionnal categories that tends rentire early : 4 (intermediary profession), 5 (Employee) and 5 (Worker)\n - the socioprofessionnal categories that retire late : 1 (Exploiting farmer), 2 (Craftmen, merchant and enterprise chief) and 3 (Cadres and superior intellectual profession)")




#TODO : implement a Isotype Grid with a slider to select the year


#used with help from the documentaion and https://medium.com/dataexplorations/how-to-add-emojis-to-an-altair-chart-f9bc02da3a4b

st.markdown("Let us see the evolution of the proportion of people in retirement at 61 over time.")

df_by_year = df.sort_values(by="annee")
fig4 = pxex.line(df_by_year, x="annee", y="proportion_de_retraites_a_61_ans", color='categorie_socioprofessionnelle')
st.plotly_chart(fig4)

with st.expander("How it is made"):
    st.code("""

df_by_year = df.sort_values(by="annee")
fig4 = pxex.line(df_by_year, x="annee", y="proportion_de_retraites_a_61_ans", color='categorie_socioprofessionnelle')
st.plotly_chart(fig4)


""")

st.markdown("We can see the proprotion keep decreasing over the year.\nWe can also see that the proportion augmented in 2018 for the following categories :\n - 8 Agriculteur exploitant / algricultural exploitement\n - 2 Artisan, Commercant, chef d'entreprise/Craftmen, merchant, entreprise chief\n - 6 Ouvrier / worker\n\nMorevoer we also see that the categorie '8 Agriculteur exploitant / algricultural exploitement' has also increased in 2020.")
st.markdown("Overall we conclude that the proportion of people in retirement at 61 has decreased from 2013 to 2020.")


st.markdown("Now that we have seen that people are getting in retirement later in their life, we are going to look at the cause of this phenomenom with the other variables.")

st.markdown("## Part 2 : Are people spending more time looking for a job ?")

st.markdown("Now we will look at mean time in employement (outside of cumul) and without")


st.markdown("you can change the tab to see a specific socioprofessional categories.")
list_of_tabs = st.tabs(list_tabs)

for i in range(len(list_of_tabs)):
    with list_of_tabs[i]:
        col3, col4 = st.columns(2)
        col3.metric(f"duree_moyenne_en_emploi_hors_cumul", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul'])} ", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul']) - max(df[(df['annee'] == 2013) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul']):.3f} ")
        col4.metric(f"duree_moyenne_sans_emploi_ni_retraite", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite'])} ", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite']) - max(df[(df['annee'] == 2013) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite']):.3f} ")
        fig5 = go.Figure(data=[go.Bar(name=f"{j}", x=(df[(df["categorie_socioprofessionnelle"] == (sorted(list(set_categories)))[i - 1])]["annee"]), y=(df[(df["categorie_socioprofessionnelle"] == (sorted(list(set_categories)))[i - 1])][j])) for j in ("duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite")])
        fig5.update_layout(barmode='group')
        st.plotly_chart(fig5)

with st.expander("How it is made"):
    st.code("""
list_of_tabs = st.tabs(list_tabs)

for i in range(len(list_of_tabs)):
    with list_of_tabs[i]:
        col3, col4 = st.columns(2)
        col3.metric(f"duree_moyenne_en_emploi_hors_cumul", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul'])} ", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul']) - max(df[(df['annee'] == 2013) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_en_emploi_hors_cumul']):.3f} ")
        col4.metric(f"duree_moyenne_sans_emploi_ni_retraite", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite'])} ", f"{max(df[(df['annee'] == 2020) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite']) - max(df[(df['annee'] == 2013) & (df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['duree_moyenne_sans_emploi_ni_retraite']):.3f} ")
        fig5 = go.Figure(data=[go.Bar(name=f"{j}", x=(df[(df["categorie_socioprofessionnelle"] == (sorted(list(set_categories)))[i - 1])]["annee"]), y=(df[(df["categorie_socioprofessionnelle"] == (sorted(list(set_categories)))[i - 1])][j])) for j in ("duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite")])
        fig5.update_layout(barmode='group')
        st.plotly_chart(fig5)
""")

st.markdown("As you can see in the graph, the mean duration in employement is increasing. This mean that people are spending more time at the same job.\nMoreover, we can see that except that categories 2, 3 and 4 all categories are  spending more times outsides of emplyoment.\nThis may be due to people having a harder time finding employement.")

st.markdown("## Part 3 : Does the duration spend working influence the age of retirment ?")

st.markdown("By looking at a scatter plot of the proportion of people spend in employent or not in employement and the variable related to the age of peple we can see that there is relation betweent the four variable.\n ")

# use a list of categorie
list_cat = sorted(list(set_categories))

col5, col6, col7 = st.columns(3)

with col5:
    choice_x = st.selectbox(label="x", options=["duree_moyenne_sans_emploi_ni_retraite", "duree_moyenne_en_emploi_hors_cumul"], index=0)

with col6:
    list_y_parameter = filter(lambda x: x != choice_x, ["age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans", "duree_moyenne_en_emploi_hors_cumul"])
    choice_y = st.selectbox(label="y", options=list_y_parameter, index=0)
    

with col7:
    list_size_parameter=  filter(lambda x: x != choice_x and x != choice_y, [None, "age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"])
    choice_s = st.selectbox(label="size", options=list_size_parameter, index=0)

@st.cache_data
def make_list_annee(df_sub):
    return sorted(list(set(df["annee"])))

years = make_list_annee(df)


fig10 = pxex.scatter(df, x=choice_x, y=choice_y,
	         animation_frame="annee", color="categorie_socioprofessionnelle", size=choice_s,
                 hover_name="categorie_socioprofessionnelle", range_y=[min(df[choice_y])/1.00015,max(df[choice_y])*(1.00015)], range_x=[min(df[choice_x])/1.00015,max(df[choice_x])*(1.00015)])
st.plotly_chart(fig10)


with st.expander("How it is made"):
    st.code("""
list_cat = sorted(list(set_categories))

col5, col6, col7 = st.columns(3)

with col5:
    choice_x = st.selectbox(label="x", options=["duree_moyenne_sans_emploi_ni_retraite", "duree_moyenne_en_emploi_hors_cumul"], index=0)

with col6:
    list_y_parameter = filter(lambda x: x != choice_x, ["age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans", "duree_moyenne_en_emploi_hors_cumul"])
    choice_y = st.selectbox(label="y", options=list_y_parameter, index=0)
    

with col7:
    list_size_parameter=  filter(lambda x: x != choice_x and x != choice_y, [None, "age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"])
    choice_s = st.selectbox(label="size", options=list_size_parameter, index=0)

@st.cache_data
def make_list_annee(df_sub):
    return sorted(list(set(df["annee"])))

years = make_list_annee(df)


fig10 = pxex.scatter(df, x=choice_x, y=choice_y,
	         animation_frame="annee", color="categorie_socioprofessionnelle", size=choice_s,
                 hover_name="categorie_socioprofessionnelle", range_y=[min(df[choice_y])/1.00015,max(df[choice_y])*(1.00015)], range_x=[min(df[choice_x])/1.00015,max(df[choice_x])*(1.00015)])
st.plotly_chart(fig10)
            
""")


st.markdown("We can see a relation between the retirement age and the time people spend in and outside of employement.\nThe socioprofessional categories spending more time without a job will retire later.")

st.markdown("## Part 4 : What about the health condition once they are retired ?")
#st.markdown("As we can see above the time in employement outsied of cumul is increasing.")
st.markdown("you can change the tab to see a specific socioprofessional categories.")



list_of_tabs_1 = st.tabs(list_tabs)

for i in range(len(list_of_tabs)):
    with list_of_tabs_1[i]:
        fig6 = go.Figure(data=[go.Bar(name=f"{j}", x=(df[(df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['annee']), y=(df[(df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])][j])) for j in ('proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite', 'proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite')])
        fig6.update_layout(barmode='group')
        st.plotly_chart(fig6)


with st.expander("How it is made"):
    st.code("""



list_of_tabs_1 = st.tabs(list_tabs)

for i in range(len(list_of_tabs)):
    with list_of_tabs_1[i]:
        fig6 = go.Figure(data=[go.Bar(name=f"{j}", x=(df[(df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])]['annee']), y=(df[(df['categorie_socioprofessionnelle'] == (sorted(list(set_categories)))[i - 1])][j])) for j in ('proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite', 'proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite')])
        fig6.update_layout(barmode='group')
        st.plotly_chart(fig6)



""")
st.markdown("""We by looking  the diffeent bar plot we can infer several things :
            \n - The categories 2 (Craftmen, merchant and enterprise chief) and 5 (Employee) have years where the amount of people limited the first years is greater than people that limited but not strongly during the first year.
            \n - The category 4 (intermdiary profession) have a low proportion of people stringly during the first year of retirement.
            """)
#st.markdown("In order to have have comprehensive look at the evolotion those two parameter we will visulise their evolution over time")

st.markdown("Since we saw that the porpotion of limited people was different for each category let us compare them over time")

y_parameter_selected = st.radio(label="Select a parameter", options=["proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"], index=0)



fig7 = pxex.bar(df.sort_values(by="annee"), x="categorie_socioprofessionnelle", y=y_parameter_selected, color="categorie_socioprofessionnelle",
  animation_frame="annee", animation_group="categorie_socioprofessionnelle")

st.plotly_chart(fig7)

with st.expander("How it is made"):
    st.code("""
y_parameter_selected = st.radio(label="Select a parameter", options=["proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"], index=0)



fig7 = pxex.bar(df.sort_values(by="annee"), x="categorie_socioprofessionnelle", y=y_parameter_selected, color="categorie_socioprofessionnelle",
  animation_frame="annee", animation_group="categorie_socioprofessionnelle")

st.plotly_chart(fig7)

""")

st.markdown("When looking at the proportion of people stronly limited during the first year of retirement:\n - We can see that the proportion of the category 4 (exploiting farmer) is decreasing.\n - While the proportion of the category 6 (Worker) is increasing.\nThis two trends are inverted in 2018.")

st.markdown("We can see that the proportion of people that are limited not strongly during the first years is slowy decreasing until 2015 where the number are increasing for every category. Since 2016, the remain stable.")


st.markdown("## Conclusion : What can we learn from this analysis ?")
st.markdown("People are working more in the same job and have a harder time finding employement.\nThis goes with the fact that the proportion of people not strongly limited during the first yeat of employement.")


st.markdown("#### Annexes")
with st.expander("For more experimentation"):
    colkDelta, colGamma, colSigma = st.columns(3)
    yAxis = xAxis = "annee"
    cCategorie = sorted(list_tabs)[0]
    with colkDelta:
        xAxis = st.selectbox(label="Select x :", options=("annee","categorie_socioprofessionnelle","proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite","proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite","age_conjoncturel_de_depart_a_la_retraite","proportion_de_retraites_a_61_ans","duree_moyenne_en_emploi_hors_cumul","duree_moyenne_sans_emploi_ni_retraite"))
   
    with colGamma:
        yAxis = st.selectbox(label="Select y :", options=("annee","categorie_socioprofessionnelle","proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite","proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite","age_conjoncturel_de_depart_a_la_retraite","proportion_de_retraites_a_61_ans","duree_moyenne_en_emploi_hors_cumul","duree_moyenne_sans_emploi_ni_retraite"))

    with colSigma:
        cCategorie = st.selectbox(label="Select z :", options=tuple(sorted(list_tabs)))

    ctemp_df  = df[df["categorie_socioprofessionnelle"] == cCategorie]

    figm, axm = plt.subplots()
    axm.scatter(ctemp_df[xAxis], ctemp_df[yAxis], s=0.4)
    st.pyplot(figm)

with st.expander("How it is made"):
    st.code("""
with st.expander("For more experimentation"):
    colkDelta, colGamma, colSigma = st.columns(3)
    yAxis = xAxis = "annee"
    cCategorie = sorted(list_tabs)[0]
    with colkDelta:
        xAxis = st.selectbox(label="Select x :", options=("annee","categorie_socioprofessionnelle","proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite","proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite","age_conjoncturel_de_depart_a_la_retraite","proportion_de_retraites_a_61_ans","duree_moyenne_en_emploi_hors_cumul","duree_moyenne_sans_emploi_ni_retraite"))
   
    with colGamma:
        yAxis = st.selectbox(label="Select y :", options=("annee","categorie_socioprofessionnelle","proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite","proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite","age_conjoncturel_de_depart_a_la_retraite","proportion_de_retraites_a_61_ans","duree_moyenne_en_emploi_hors_cumul","duree_moyenne_sans_emploi_ni_retraite"))

    with colSigma:
        cCategorie = st.selectbox(label="Select z :", options=tuple(sorted(list_tabs)))

    ctemp_df  = df[df["categorie_socioprofessionnelle"] == cCategorie]

    figm, axm = plt.subplots()
    axm.scatter(ctemp_df[xAxis], ctemp_df[yAxis], s=0.4)
    st.pyplot(figm)
    """)