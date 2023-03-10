import streamlit as st
from src.utils import load_image
import pandas as pd
from PIL import Image
import plotly.express as px

st.title("Sevici App")

img = Image.open("./assets/img/sevici.jpg")
st.sidebar.image(img)

selector = st.sidebar.selectbox("Menú", ["Datos", 
                                         " Visualización", 
                                         "Filtrado"])

if selector == "Datos":
    st.text("Número de bicis Sevici en Sevilla")
    df = pd.read_csv("data/sevicidist.csv", index_col=0)

    st.dataframe(df)

    cap_dist = df.groupby("Distrito")["CAPACITY"].sum()
    cap_dist.index.name = "Distrito"
    cap_dist.name = "Capacidad"

    fig = px.bar(cap_dist, y="Capacidad")
    st.plotly_chart(fig)



