import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.graph_objects as px


st.set_page_config(page_title="Uber Visualization", page_icon=":car:")

st.markdown("# Data visualisation")
st.sidebar.header("Data visualisaiton")


st.sidebar.success("Select a page above.")


st.sidebar.markdown("About me")
st.sidebar.link_button("Github", url="https://github.com/quentindamois")
st.sidebar.link_button("LinkedIn", url="www.linkedin.com/in/quentin-damois-6756a7222")
st.title("Quentin DAMOIS's Dashbord")

path2 = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/nyctrips/data.csv"


def get_hour(dt):
    return dt.hour #from the first note book

def get_minute(dt):
    return dt.minute 


@st.cache_data
def loading_the_data(path3):
    data3 = pd.read_csv(path3, delimiter = ',')
    data3["tpep_pickup_datetime"] = data3["tpep_pickup_datetime"].map(pd.to_datetime)
    data3["tpep_dropoff_datetime"] = data3["tpep_dropoff_datetime"].map(pd.to_datetime)
    data3["tpep_pickup_hour"] = data3["tpep_pickup_datetime"].map(get_hour)
    data3["tpep_dropoff_hour"] = data3["tpep_dropoff_datetime"].map(get_hour)
    data3["tpep_pickup_minute"] = data3["tpep_pickup_datetime"].map(get_minute)
    data3["tpep_dropoff_minute"] = data3["tpep_dropoff_datetime"].map(get_minute)
    return data3

data2 = loading_the_data(path2)

st.markdown("# You can see below the dataset used for the visualisation")


st.write(data2)

with st.expander("How it is made"):
    st.code("""

path2 = "https://raw.githubusercontent.com/uber-web/kepler.gl-data/master/nyctrips/data.csv"


def get_hour(dt):
    return dt.hour #from the first note book

def get_minute(dt):
    return dt.minute 


@st.cache_data
def loading_the_data(path3):
    data3 = pd.read_csv(path3, delimiter = ',')
    data3["tpep_pickup_datetime"] = data3["tpep_pickup_datetime"].map(pd.to_datetime)
    data3["tpep_dropoff_datetime"] = data3["tpep_dropoff_datetime"].map(pd.to_datetime)
    data3["tpep_pickup_hour"] = data3["tpep_pickup_datetime"].map(get_hour)
    data3["tpep_dropoff_hour"] = data3["tpep_dropoff_datetime"].map(get_hour)
    data3["tpep_pickup_minute"] = data3["tpep_pickup_datetime"].map(get_minute)
    data3["tpep_dropoff_minute"] = data3["tpep_dropoff_datetime"].map(get_minute)
    return data3

data2 = loading_the_data(path2)


""")


st.markdown("Now that we have looked at the dataset we will see how the different pickup and drop of on the map.")

colAlpha, colBeta = st.columns(2)

with colAlpha:
    size_matter = st.toggle("Change the size")
    if size_matter:
        size_point = "tips_amount"
    else :
        size_point = None
    size_point = st.selectbox("Choose the column to determine the size of the point", options=["tips_amount", "fare_amount", "total_amount", "passenger_count","trip_distance"], disabled= not(size_matter))


with colBeta:
    location_parameter = "pickup"
    location_parameter = st.radio(label="choose the location", options=["pickup","dropoff"])

map_fig = st.map(data=data2, latitude= location_parameter + "_latitude", longitude= location_parameter + "_longitude", size=size_point)

with st.expander("How it is made"):
    st.code("""

colAlpha, colBeta = st.columns(2)

with colAlpha:
    size_matter = st.toggle("Change the size")
    if size_matter:
        size_point = "tips_amount"
    else :
        size_point = None
    size_point = st.selectbox("Choose the column to determine the size of the point", options=["tips_amount", "fare_amount", "total_amount", "passenger_count","trip_distance"], disabled= not(size_matter))


with colBeta:
    location_parameter = "pickup"
    location_parameter = st.radio(label="choose the location", options=["pickup","dropoff"])

map_fig = st.map(data=data2, latitude= location_parameter + "_latitude", longitude= location_parameter + "_longitude", size=size_point)


""")

st.markdown("We can see that each uber travel has differents parameter. Now lets see the frequnency of the different variables of a travel.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["fare_amount", "tip_amount", "total_amount", "passenger_count", "trip_distance"])


with tab1:
    col7, col8 = st.columns(2)
    col7.metric("Maximum", f"{max(data2['fare_amount'])} $")
    col8.metric("Minimum", f"{min(data2['fare_amount'])} $")
    fig1, ax1 = plt.subplots()
    ax1.hist(data2["fare_amount"], bins = 100, range = (min(data2["fare_amount"]) , max(data2["fare_amount"])), color = 'g', alpha = 0.5, label = "fare_amount")
    plt.title("histogram fare amount")
    plt.xlabel("fare amount")
    plt.ylabel("Frequency")
    st.pyplot(fig1)



with tab2:
    col9, col10 = st.columns(2)
    col9.metric("Maximum", f"{max(data2['tip_amount'])} $")
    col10.metric("Minimum", f"{min(data2['tip_amount'])} $")
    fig2, ax2 = plt.subplots()
    ax2.hist(data2["tip_amount"], bins = 100, range = (min(data2["tip_amount"]) , max(data2["tip_amount"])), color = 'g', alpha = 0.5, label = "tip_amount")
    plt.title("histogram tip amount")
    plt.xlabel("tip amount")
    plt.ylabel("Frequency")
    st.pyplot(fig2)

with tab3:
    col11, col12 = st.columns(2)
    col11.metric("Maximum", f"{max(data2['total_amount'])} $")
    col12.metric("Minimum", f"{min(data2['total_amount'])} $")
    fig3, ax3 = plt.subplots()
    ax3.hist(data2["total_amount"], bins = 100, range = (min(data2["total_amount"]) , max(data2["total_amount"])), color = 'g', alpha = 0.5, label = "total_amount")
    plt.title("histogram total amount")
    plt.xlabel("total amount")
    plt.ylabel("Frequency")
    st.pyplot(fig3)

with tab4:
    col13, col14 = st.columns(2)
    col13.metric("Maximum", f"{max(data2['passenger_count'])} personne")
    col14.metric("Minimum", f"{min(data2['passenger_count'])} personne")
    figAlpha, axAlpha = plt.subplots()
    axAlpha.hist(data2["passenger_count"], range = (min(data2["passenger_count"]) , max(data2["passenger_count"])), bins = 100, color = 'g', alpha = 0.5, label = "passenger_count")
    plt.title("histogram passenger count")
    plt.xlabel("passenger count")
    plt.ylabel("Frequency")
    st.pyplot(figAlpha)

with tab5:
    col15, col16 = st.columns(2)
    col15.metric("Maximum", f"{max(data2['trip_distance'])} km")
    col16.metric("Minimum", f"{min(data2['trip_distance'])} km")
    figBeta, axBeta = plt.subplots()
    axBeta.hist(data2["trip_distance"], bins = 100, range = (min(data2["trip_distance"]) , max(data2["trip_distance"])), color = 'g', alpha = 0.5, label = "trip_distance")
    plt.title("histogram trip distance")
    plt.xlabel("trip distance")
    plt.ylabel("Frequency")
    st.pyplot(figBeta)

with st.expander("How it is made"):
    st.code("""

tab1, tab2, tab3, tab4, tab5 = st.tabs(["fare_amount", "tip_amount", "total_amount", "passenger_count", "trip_distance"])


with tab1:
    col7, col8 = st.columns(2)
    col7.metric("Maximum", f"{max(data2['fare_amount'])} $")
    col8.metric("Minimum", f"{min(data2['fare_amount'])} $")
    fig1, ax1 = plt.subplots()
    ax1.hist(data2["fare_amount"], bins = 100, range = (min(data2["fare_amount"]) , max(data2["fare_amount"])), color = 'g', alpha = 0.5, label = "fare_amount")
    plt.title("histogram fare amount")
    plt.xlabel("fare amount")
    plt.ylabel("Frequency")
    st.pyplot(fig1)



with tab2:
    col9, col10 = st.columns(2)
    col9.metric("Maximum", f"{max(data2['tip_amount'])} $")
    col10.metric("Minimum", f"{min(data2['tip_amount'])} $")
    fig2, ax2 = plt.subplots()
    ax2.hist(data2["tip_amount"], bins = 100, range = (min(data2["tip_amount"]) , max(data2["tip_amount"])), color = 'g', alpha = 0.5, label = "tip_amount")
    plt.title("histogram tip amount")
    plt.xlabel("tip amount")
    plt.ylabel("Frequency")
    st.pyplot(fig2)

with tab3:
    col11, col12 = st.columns(2)
    col11.metric("Maximum", f"{max(data2['total_amount'])} $")
    col12.metric("Minimum", f"{min(data2['total_amount'])} $")
    fig3, ax3 = plt.subplots()
    ax3.hist(data2["total_amount"], bins = 100, range = (min(data2["total_amount"]) , max(data2["total_amount"])), color = 'g', alpha = 0.5, label = "total_amount")
    plt.title("histogram total amount")
    plt.xlabel("total amount")
    plt.ylabel("Frequency")
    st.pyplot(fig3)

with tab4:
    col13, col14 = st.columns(2)
    col13.metric("Maximum", f"{max(data2['passenger_count'])} personne")
    col14.metric("Minimum", f"{min(data2['passenger_count'])} personne")
    figAlpha, axAlpha = plt.subplots()
    axAlpha.hist(data2["passenger_count"], range = (min(data2["passenger_count"]) , max(data2["passenger_count"])), bins = 100, color = 'g', alpha = 0.5, label = "passenger_count")
    plt.title("histogram passenger count")
    plt.xlabel("passenger count")
    plt.ylabel("Frequency")
    st.pyplot(figAlpha)

with tab5:
    col15, col16 = st.columns(2)
    col15.metric("Maximum", f"{max(data2['trip_distance'])} km")
    col16.metric("Minimum", f"{min(data2['trip_distance'])} km")
    figBeta, axBeta = plt.subplots()
    axBeta.hist(data2["trip_distance"], bins = 100, range = (min(data2["trip_distance"]) , max(data2["trip_distance"])), color = 'g', alpha = 0.5, label = "trip_distance")
    plt.title("histogram trip distance")
    plt.xlabel("trip distance")
    plt.ylabel("Frequency")
    st.pyplot(figBeta)



""")

col1, col2 = st.columns(2)


yAxis = xAxis = "passenger_count"
with col1:
    xAxis = st.selectbox(label="Select x :", options=("passenger_count", "trip_distance", "fare_amount", "tip_amount", "total_amount"))
   
with col2:
    yAxis = st.selectbox(label="Select y :", options=("passenger_count", "trip_distance", "fare_amount", "tip_amount", "total_amount"))

figm, axm = plt.subplots()
axm.scatter(data2[xAxis], data2[yAxis], s=0.4)
st.pyplot(figm)

with st.expander("How it is made"):
    st.code("""

col1, col2 = st.columns(2)


yAxis = xAxis = "passenger_count"
with col1:
    xAxis = st.selectbox(label="Select x :", options=("passenger_count", "trip_distance", "fare_amount", "tip_amount", "total_amount"))
   
with col2:
    yAxis = st.selectbox(label="Select y :", options=("passenger_count", "trip_distance", "fare_amount", "tip_amount", "total_amount"))

figm, axm = plt.subplots()
axm.scatter(data2[xAxis], data2[yAxis], s=0.4)
st.pyplot(figm)

""")

col1, col2, col3 = st.columns(3)


yAxis1 = "fare_amount"
xAxis1 = "passenger_count"
type_metrics = "mean"

with col1:
    xAxis1 = st.selectbox(label="Select x :", options=("passenger_count", "trip_distance", "tpep_pickup_hour", "tpep_dropoff_hour", "tpep_pickup_minute", "tpep_dropoff_minute", "trip_distance"))
   
with col2:
    yAxis1 = st.selectbox(label="Select y :", options=("fare_amount", "tip_amount", "total_amount"))

with col3:
    type_metrics = st.radio(label="choose the metrics you want to use", options=["mean","min", "max", "median"])

temp_data = eval(f"data2.groupby(xAxis1).{type_metrics}()")


plot = px.Figure(data=[px.Scatter(
    y=temp_data[yAxis1],
    mode='lines')
])
plot.update_layout(
    title=f"{type_metrics} {yAxis1} by {xAxis1}",
    xaxis_title=xAxis1,
    yaxis_title=yAxis1,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
st.plotly_chart(plot)

with st.expander("How it is made"):
    st.code("""

col1, col2, col3 = st.columns(3)


yAxis1 = "fare_amount"
xAxis1 = "passenger_count"
type_metrics = "mean"

with col1:
    xAxis1 = st.selectbox(label="Select x :", options=("passenger_count", "trip_distance", "tpep_pickup_hour", "tpep_dropoff_hour", "tpep_pickup_minute", "tpep_dropoff_minute", "trip_distance"))
   
with col2:
    yAxis1 = st.selectbox(label="Select y :", options=("fare_amount", "tip_amount", "total_amount"))

with col3:
    type_metrics = st.radio(label="choose the metrics you want to use", options=["mean","min", "max", "median"])

temp_data = eval(f"data2.groupby(xAxis1).{type_metrics}()")


plot = px.Figure(data=[px.Scatter(
    y=temp_data[yAxis1],
    mode='lines')
])
plot.update_layout(
    title=f"{type_metrics} {yAxis1} by {xAxis1}",
    xaxis_title=xAxis1,
    yaxis_title=yAxis1,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
st.plotly_chart(plot)

""")