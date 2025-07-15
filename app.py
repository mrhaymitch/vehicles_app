import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Exploración de datos de vehículos")

# Cargar el archivo CSV
df = pd.read_csv("vehicles.csv")

# Mostrar primeras filas
st.write("Vista previa de los datos:")
st.dataframe(df.head())

# Casilla para histograma
build_histogram = st.checkbox("Construir histograma del odómetro")

if build_histogram:
    st.write("Histograma de kilometraje")
    fig = px.histogram(df, x="odometer", title="Distribución de kilometraje")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión (odómetro vs precio)")

if build_scatter:
    st.write("Relación entre kilometraje y precio por condición del vehículo")
    fig = px.scatter(df, x="odometer", y="price", color="condition",
                     title="Dispersión: kilometraje vs precio")
    st.plotly_chart(fig, use_container_width=True)
