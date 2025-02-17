import streamlit as st
import pandas as pd
import munpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

#1 Configuaracion incial de la aplicacion
st.set_page_config(
  page_title = "Dashboard Interactivo",
  page_ icon=":)",
  layaut="wide"
)
st.title("Dashboard Interactivo con Streamlit")
st.sidebar.title("Opciones de Navegacion")
