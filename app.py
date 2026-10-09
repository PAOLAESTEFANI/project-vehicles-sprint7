import streamlit as st
import pandas as pd
import plotly.express as px


st.title('VEHICULOS USADOS')

df = pd.read_csv("vehicles_us.csv")
st.dataframe(df)


df = pd.read_csv('vehicles_us.csv')  # leer los datos

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
   st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
   fig = px.histogram(df, x="odometer")

    # mostrar un gráfico Plotly interactivo
   st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(df, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)