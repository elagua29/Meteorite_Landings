import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt


@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

    df = load_data("https://raw.githubusercontent.com/elagua29/Meteorite_Landings/main/Meteorite_Landings.csv")
    st.dataframe(df)

st.subheader("Meteorite Data")

tab1, tab2, tab3, tab4 = st.tabs(['Introduction', 'Scatter Plot', 'Source', 'Bar Chart'])



with tab1:
    Meteorite_Data = pd.read_csv('Meteorite_Data.csv')
    
    st.markdown("<h2 style='text-align: center; color: grey;'>This application allows you to see Meteorite Landings through the years.</h2>", unsafe_allow_html=True)

    st.subheader("About the Dataset")
    st.markdown('The dataset used in this analysis was obtained through The Meteoritical Society which contains information on all of the known meteorites.')
    st.markdown('This dataset consists of 34, 513 meteorites and includes the following field: name, location, mass, and the year that was found/fell')
   
with tab2:


    st.sidebar.header("Pick two variables for this scatterplot")
    x_val = st.sidebar.selectbox("Pick your x-axis",Meteorite_Data.select_dtypes(include=np.number).columns.tolist())
    y_val = st.sidebar.selectbox("Pick your y-axis",Meteorite_Data.select_dtypes(include=np.number).columns.tolist())

    scatter = alt.Chart(Meteorite_Data, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip= [x_val,y_val])

    st.altair_chart(scatter, use_container_width=True)

    corr = round(Meteorite_Data[x_val].corr(Meteorite_Data[y_val]),2)
    st.write(f"The correlation between {x_val} and {y_val} is {corr}")


with tab3:
    Meteorite_Data = pd.read_csv('Meteorite_Data.csv')
    st.write (Meteorite_Data)

with tab4:
    # Initialize the lists for X and Y
    Meteorite_Data = pd.read_csv('Meteorite_Data.csv')
  
    df = pd.DataFrame(Meteorite_Data)
  
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
  
    # Plot the data using bar() method
    plt.bar(X, Y, color='g')
    plt.title("Fall Throught the Years")
    plt.xlabel("Year")
    plt.ylabel("Mass(g)")
  
    # Show the plot
    plt.show()
