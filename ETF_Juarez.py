import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import sqlite3

DATA_URL=('data/etf_sql.csv')
@st.cache(persist=True)
def load_data():
    data=pd.read_csv(DATA_URL)
    return data

proyecto_data=load_data()


st.title("GRAFICAS")
st.markdown('El Tablero Presenta Información del Proyecto')
st.sidebar.title("Status del Proyecto ETF Juárez")
st.sidebar.markdown("Seleccionar información:")
st.sidebar.selectbox('Seleccionar Semana del Proyecto',['Semana'])

select=st.sidebar.selectbox('Seleccionar Gráfica',['Grafica'])

st.sidebar.radio("Planificado", ('PV','PV%'))
st.sidebar.radio("Ejecutado", ('AC','AC%'))
st.sidebar.radio("Indicadores", ('CPI','SPI','TCPI'))
st.sidebar.radio("Pronostico", ('VAL($)','VAC(%)','VAC(t)','Duración Estimada'))
st.sidebar.checkbox("Presentar Grafica", True, key=1)
st.sidebar.selectbox('Seleccionar Contratista',['Contratista'])
