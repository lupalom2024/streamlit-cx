
import streamlit as st
import streamlit as st1
import pyodbc
import pandas as pd
from utils.database import *
from utils.functions import *
import plotly.express as px

st.set_page_config(page_title="Dashboard CX", layout="wide")

#st.title("Dashboard CX")

st.markdown("""
            <style>
            .stButton button {
                width: 100%; 
            }
            >/style>
            """, unsafe_allow_html=True)

st.sidebar.title("Portal")
st.sidebar.markdown("---")

psaz_data_btn = st.sidebar.button("CX BC Psaz")
uploaded_file = st.file_uploader("Please choice the data file", type="csv", key=1)

#col1, col2 = st.columns(2)
#with col1:
if uploaded_file is not None:
    st.header("CX BC Psaz")
    st.write(" ") 

    try:
        @st.cache_data
        def load_csv(uploaded_file):
            return pd.read_csv(uploaded_file)

        df = load_csv(uploaded_file)
        st.write("Preview data file (Last 10 records):")
        st.dataframe(df.tail(10))
        required_columns = ["Period", "OTBSpend"]
        filtered_df = df[required_columns]

        try:
            if "Period" not in df.columns:
                st.error("Error file.")
            else:                 
                grouped_data = filtered_df.groupby("Period").sum()
#                st.line_chart(grouped_data)
        except Exception as e:
            st.error(f"Error to processing data: {e}")
    except Exception as e:
        st.error(f"Error to processing data: {e}")

st.sidebar.markdown("---")
st.sidebar.write("")

inventory_trend_btn = st.sidebar.button("Inventory Trend")
uploaded_file = st.sidebar.file_uploader("Please choice the data file", type="csv", key=2)

#col1, col2 = st.columns(2)
#with col1:
if uploaded_file is not None:
    st.title("Inventory Trend")
    st.write(" ") 
    try:
        @st.cache_data
        def load_csv(uploaded_file):
            return pd.read_csv(uploaded_file)

        df = load_csv(uploaded_file)
        st.write("Preview data file (Last 10 records):")
        st.dataframe(df.tail(10))
        try:
            df = df.sort_values(by="Nombre")
            df.set_index("Nombre",inplace=True)
            df_transpuesta = df.T 
#            st.line_chart(df_transpuesta)
        except Exception as e:
            st.error(f"Error to processing data: {e}")
    except Exception as e:
        st.error(f"Error to processing data: {e}")