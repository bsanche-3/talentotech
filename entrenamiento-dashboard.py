import streamlit as st
import pandas as pd
import numpy as np
import os
from google.generativeai import genai

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

# Selección del tipo de gráfico
graph_type = st.selectbox('Seleccione el tipo de gráfico', ['Línea', 'Barra', 'Área'])

# Mostrar la figura
if len(selected_variables) >= 2:
    if graph_type == 'Línea':
        st.line_chart(data[selected_variables])
    elif graph_type == 'Barra':
        st.bar_chart(data[selected_variables])
    elif graph_type == 'Área':
        st.area_chart(data[selected_variables])
else:
    st.warning('Por favor, seleccione al menos dos variables para la figura.')

# Crear botón para obtener análisis de la gráfica
if st.button("Obtener Análisis de Gráfica"):
    df_seleccionado = data[selected_variables]
    describe_df = df_seleccionado.describe().transpose()
    describe_values = describe_df.to_dict(orient="index")

    prompt = f"""
    Analiza y dame recomendaciones a partir de un análisis descriptivo de los siguientes datos:
    {describe_values}
    correspondiente a la gráfica de tipo {graph_type}.
    """
    
    def obtener_analisis_gemini(prompt):
        # Obtener la clave API desde la variable de entorno
        api_key = os.getenv('GEMINI_API_KEY_TALENTOTECH')

        if api_key is None:
            raise ValueError("La clave API de Gemini no está configurada. Asegúrate de configurar la variable de entorno 'GEMINI_API_KEY_TALENTOTECH'.")

        # Usar la API de Gemini
        client = genai.Client(api_key=api_key)

        # Definir el contexto para el modelo de Gemini
        sys_instruct = """
        Eres un asistente de análisis de datos. Tu tarea es proporcionar análisis descriptivos detallados y útiles para los datos proporcionados. 
        Asegúrate de explicar cualquier patrón, tendencia o anomalía que observes en los datos. 
        Proporciona recomendaciones basadas en el análisis cuando sea posible.
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction=sys_instruct,
                temperature=0.1
            ),
            contents=prompt,
        )

        return response.text.strip()

    analisis = obtener_analisis_gemini(prompt)
    st.write("Análisis de Gráfica:")
    st.write(analisis)
