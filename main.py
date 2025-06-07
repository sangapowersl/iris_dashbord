import streamlit as st

st.set_page_config(page_title="Tableau de bord Iris", layout="wide")
st.title("🌸 Tableau de bord professionnel - Dataset Iris")

st.markdown("""
Bienvenue sur le **Tableau de bord Iris**.  
Utilisez les onglets à gauche pour naviguer entre les analyses suivantes :

- 🔍 Aperçu et statistiques descriptives  
- 📊 Visualisation interactive  
- 🚨 Détection d'outliers (valeurs aberrantes)  
- 📌 Matrice de corrélation

Ce tableau de bord est alimenté par **Python**, **pandas**, **seaborn** et **Streamlit**.
""")
