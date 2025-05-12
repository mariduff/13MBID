import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Lectura de datos
df = pd.read_csv("../../data/final/datos_finales.csv", sep=";")

# Configuración de la página
st.set_page_config(
    page_title="Herramienta de visualizacion de datos - 13MBID",
    page_icon="📊",
    layout="wide",
)

# Título de la aplicación
st.title("Herramienta de visualizacion de datos - 13MBID")
st.write("Esta aplicacion permite explotar y visualizar los datos del proyecto en curso.")
st.write("Desarrollado por MJ")
st.markdown('------')

# Gráficos
st.header("Gráficos")
st.subheader("Caracterizacion de los creditos otorgados:")

# Cantidad de créditos por objetivo del mismo
creditos_x_objetivo = px.histogram(df, x='objetivo_credito',
                                   title='Conteo de créditos por objetivo')
creditos_x_objetivo.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')

# Visualización
st.plotly_chart(creditos_x_objetivo, use_container_width=True)
