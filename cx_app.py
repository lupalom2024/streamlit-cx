
import streamlit as st
import pyodbc
import pandas as pd
from utils.database import *
from utils.functions import *
import plotly.express as px

st.set_page_config(page_title="Dashboard CX", layout="wide")

st.title("Dashboard CX")

st.markdown("""
            <style>
            .stButton button {
                width: 100%; 
            }
            >/style>
            """, unsafe_allow_html=True)

st.sidebar.title("Portal")
st.sidebar.markdown("---")

inventory_trend_btn = st.sidebar.button("Inventory Trend")

print("paso 1")

#if inventory_trend_btn:
col1, col2, col3 = st.columns(3)
with col1:
    uploaded_file = st.file_uploader("Please choice the data file", type="csv")

col1, col2 = st.columns(2)
with col1:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        try:
            df.set_index("Nombre",inplace=True)
            df_transpuesta = df.T 
            st.title("Inventory Trend")
            st.write(" ") 
            st.line_chart(df_transpuesta)
        except Exception as e:
            st.error(f"Error to processing data: {e}")

with col2:
    if uploaded_file is not None:
        df_melted = pd.melt(df, id_vars="Nombre", var_name="Mes", value_name="Valor")
        fig = px.line(
            df_melted,
            x="Mes",
            y="Valor",
            color="Nombre",
            markers=True,
            labels={"Valor": "Valor", "Mes": "Mes", "Nombre": "Línea"}
            )