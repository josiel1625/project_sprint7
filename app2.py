import pandas as pd
import streamlit as st
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

st.header('Relación Autos')

start_button = st.button('Ejecutar Histograma')

if start_button:
    st.write('Número de autos procesándose')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig)

buton_inicial = st.button('Ejecutar Dispersión')

if buton_inicial:
    st.write('Dispersión de distribución precios - fabricantes de autos')
    fig1 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig1.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig1)
