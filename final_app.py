import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import numpy as np


@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://raw.githubusercontent.com/elagua29/Meteorite_Landings/main/Meteorite_Landings.csv")
st.dataframe(df)

st.button("Rerun")



tab1, tab2 = st.tabs(['Introduction', 'Meteorite Landings through the years'])


#Sidebar

year_meteor = st.sidebar.slider("Pick a year",min_value=700, max_value=2023, value=100, step=10)

with tab1:
    st.image = Image.open('image1.webp')




    st.markdown("<h2 style='text-align: center; color: grey;'>This application allows you to see Meteorite Landings through the years.</h2>", unsafe_allow_html=True)

    st.subheader("About the Dataset")
    st.markdown('The dataset used in this analysis was obtained through The Meteoritical Society which contains information on all of the known meteorites.')
    st.markdown('This dataset consists of 34, 513 meteorites and includes the following field: name, location, mass, and the year that was found/fell')
   
with tab2:
    Meteorite_Landings = pd.read_csv('Meteorite_Landings.csv')
    st.write(Meteorite_Landings)

st.sidebar.header("Pick two variables for this scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",Meteorite_Landings.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",Meteorite_Landings.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(Meteorite_Landings, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip= [x_val,y_val])

st.altair_chart(scatter, use_container_width=True)

corr = round(Meteorite_Landings[x_val].corr(Meteorite_Landings[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")
