import streamlit as st
import pandas as pd
import plotly.express as px

#leer los datos del archivo CSV
car_data = pd.read_csv('Notebook/vehicles_us.csv')

#encabezado de la aplicación
st.title('Análisis Exploratorio de Datos de Autos Usado')

st.write('Vista previa:')
st.write(car_data.head())

#boton para generar el histograma
hist_button = st.button('Generar Histograma')

if hist_button:
    st.write ('Creacion de un histograma para el conjunto de datos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Checkbox para el histograma
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Checkbox para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)