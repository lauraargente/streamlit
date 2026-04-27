import streamlit as st
import pandas as pd

st.title('🔍 Mini Data Explorer')
st.write('Explora datos conmigo')

df = pd.read_csv("datos.csv")
st.write("Primeras filas:", df.head())
st.write("Estadísticas:", df.describe())

columna = st.selectbox("Elige una columna:", df.columns)

st.bar_chart(df[columna].value_counts())