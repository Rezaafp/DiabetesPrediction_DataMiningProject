import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

# Membuat sidebar
st.sidebar.title("Navigasi")

# Membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Load data set
df,x,y = load_data()

#kondisi call app function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df,x,y)
else:
    Tabs[page].app()

