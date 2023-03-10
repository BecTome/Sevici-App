import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Sevici App",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Sevici App")
img_path = os.path.abspath("assets/img/sevici.jpg")
st.sidebar.image(img_path)

selector = st.sidebar.selectbox("Menú", ["Datos", 
                                         "Visualización", 
                                         "Filtrado"])

df_path = os.path.abspath("data/sevicidist.csv")
df = pd.read_csv(df_path, index_col=0)

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
    


