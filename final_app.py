import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import numpy as np
from gmplot import gmplot
import numpy as np


# reading csv file
Meteorite_Landings = pd.read_csv('Meteorite_Landings.csv')

st.write(Meteorite_Landings)



tab1, tab2, tab3, tab4 = st.tabs(['Introduction', 'Meteorite Landings through the years', 'Box Plot', 'tbd'])

with tab1:

    
    st.markdown("<h2 style='text-align: center; color: grey;'>This application allows you to see Meteorite Landings through the years.</h2>", unsafe_allow_html=True)

    st.subheader("About the Dataset")
    st.markdown('The dataset used in this analysis was obtained through The Meteoritical Society which contains information on all of the known meteorites.')
    st.markdown('This dataset consists of 34, 513 meteorites and includes the following field: name, location, mass, and the year that was found/fell')

with tab2:
    Meteorite_Landings = pd.read_csv('Meteorite_Landings.csv')
    st.write(Meteorite_Landings)

## Box plot
alt.Chart(Meteorite_Landings).mark_boxplot().encode(
    x = alt.X('Year'),
    y = alt.Y('mass')
).properties(
    width = 500,
    title = 'Boxplot between Year vs Mass')

with tab3:
    ## Line chart
    alt.Chart(Meteorite_Landings).mark_line(point=True)\
        .encode(
                x='Month_of_Stop',
                y='count',
                tooltip = alt.Tooltip(['Month_of_Stop','count'])
                ).properties(width = 1000)


