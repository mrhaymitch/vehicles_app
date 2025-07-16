# Vehicles App 🚗📊

Esta es una aplicación web interactiva construida con **Streamlit**, que permite explorar un conjunto de datos de anuncios de venta de vehículos en EE. UU.

## Funcionalidad

- Visualización tabular de los datos
- Histograma de kilometraje (`odometer`)
- Diagrama de dispersión (`odometer` vs `price`)
- Opciones interactivas mediante botones o casillas de verificación

## Estructura del proyecto

- `app.py`: Interfaz web construida con Streamlit
- `EDA.ipynb`: Análisis exploratorio con Plotly Express
- `vehicles.csv`: Fuente de datos
- `requirements.txt`: Paquetes necesarios
- `notebooks/`: Carpeta con el notebook del análisis

## Cómo ejecutar la aplicación

Desde la terminal, activar el entorno virtual y correr:

streamlit run app.py

