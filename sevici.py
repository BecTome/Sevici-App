import streamlit as st
from src.utils import load_image
import pandas as pd
from PIL import Image
import plotly.express as px

st.set_page_config(
    page_title="Sevici App",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Sevici App")

img = Image.open("./assets/img/sevici.jpg")
st.sidebar.image(img)

selector = st.sidebar.selectbox("Menú", ["Datos", 
                                         "Visualización", 
                                         "Filtrado"])

df = pd.read_csv("data/sevicidist.csv", index_col=0)

if selector == "Datos":

    st.metric("Número de bicis Sevici en Sevilla",
              df["CAPACITY"].sum(), 
              20)

    st.dataframe(df)

    cap_dist = df.groupby("Distrito")["CAPACITY"].sum()
    cap_dist.index.name = "Distrito"
    cap_dist.name = "Capacidad"

    fig = px.bar(cap_dist, y="Capacidad")
    st.plotly_chart(fig, use_container_width=True)

elif selector == "Visualización":
    st.map(df[["LAT", "LON"]])

elif selector == "Filtrado":
    area_type = st.sidebar.radio("Seleccione una opción de filtro:",
                                    ["Calle", "Capacidad & Distrito"])
    
    if area_type == "Calle":
        street_sel = st.sidebar.selectbox("Calles", sorted(df.CALLE.unique()))

        df_calle = df[df.CALLE == street_sel]
        st.dataframe(df_calle)
        st.map(df_calle)
    


