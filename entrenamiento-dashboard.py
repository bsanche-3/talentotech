import streamlit as st
import pandas as pd
import numpy as np

# Título del dashboard
st.title('Agroindustria en Colombia')

# Generar datos aleatorios
np.random.seed(42)  # Para resultados reproducibles
data = pd.DataFrame(
    np.random.randn(150, 8),
    columns=['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5', 'Variable 6', 'Variable 7', 'Variable 8']
)

# Mostrar los datos en la aplicación de Streamlit
st.write("Datos aleatorios de agroindustria en Colombia")
st.write(data)

# Selección de variables para la figura
selected_variables = st.multiselect('Seleccione las variables para la figura', data.columns, default=data.columns[:2])

# Mostrar la figura
if len(selected_variables) >= 2:
    st.line_chart(data[selected_variables])
else:
    st.warning('Por favor, seleccione al menos dos variables para la figura.')

# Ejecutar el archivo con el comando: streamlit run entrenamiento-dashboard.py
