import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Título y descripción
st.header('Análisis de anuncios de vehículos usados')

st.write(
    'Esta aplicación permite explorar los anuncios de venta '
    'de vehículos mediante gráficos interactivos.'
)

# Botones para construir los gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Histograma
if hist_button:
    st.write('Distribución del kilometraje de los vehículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del odómetro'
    )

    st.plotly_chart(fig, width='stretch')

# Gráfico de dispersión
if scatter_button:
    st.write('Relación entre el precio y el kilometraje')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs. kilometraje'
    )

    st.plotly_chart(fig, width='stretch')