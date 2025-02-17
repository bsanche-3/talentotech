import streamlit as st
import pandas as pd
import numpy as np

# Título del dashboard
st.title('Agroindustria en Colombia')

# Generar datos aleatorios
np.random.seed(42)  # Para resultados reproducibles
data = pd.DataFrame(
    np.random.randn(150, 8),
    columns=['Producción de Café', 'Producción de Cacao', 'Producción de Palma', 'Exportaciones de Café', 'Exportaciones de Cacao', 'Exportaciones de Palma', 'Consumo Interno de Café', 'Consumo Interno de Cacao']
)

# KPIs principales
col1, col2, col3 = st.columns(3)
col1.metric("📊 Producción Total", f"{data[['Producción de Café', 'Producción de Cacao', 'Producción de Palma']].sum().sum():,.2f} Tn")
col2.metric("🚢 Exportaciones Totales", f"{data[['Exportaciones de Café', 'Exportaciones de Cacao', 'Exportaciones de Palma']].sum().sum():,.2f} Tn")
col3.metric("💰 Consumo Interno Total", f"{data[['Consumo Interno de Café', 'Consumo Interno de Cacao']].sum().sum():,.2f} Tn")

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
