import streamlit as st
import seaborn as sns
import pandas as pd

df = sns.load_dataset("iris")

st.title("🔍 Aperçu du jeu de données")
st.write(df.head())

st.subheader("📈 Statistiques descriptives")
st.write(df.describe())
