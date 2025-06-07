import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Configuration initiale
st.set_page_config(page_title="Tableau de bord Iris", layout="wide")

# Chargement des données
df = sns.load_dataset("iris")

# Mise en page en deux colonnes
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🌸 Tableau de bord interactif - Dataset Iris")

    # Aperçu
    st.subheader("🔍 Aperçu des données")
    st.dataframe(df.head())

    # Statistiques
    st.subheader("📊 Statistiques descriptives")
    st.dataframe(df.describe())

    # Filtrage par espèce
    st.subheader("🎯 Filtrage par espèce")
    species = st.multiselect("Choisir une ou plusieurs espèces", df["species"].unique(), default=df["species"].unique())
    filtered_df = df[df["species"].isin(species)]

    # Sélection de colonne numérique
    col_numeric = st.selectbox("📌 Sélectionner une colonne numérique", df.select_dtypes(include='number').columns)

    # Histogramme
    st.subheader("📈 Histogramme & KDE")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df[col_numeric], kde=True, ax=ax1)
    st.pyplot(fig1)

    # Boxplot
    st.subheader("📦 Boxplot")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x=filtered_df[col_numeric], ax=ax2)
    st.pyplot(fig2)

    # Matrice de corrélation
    st.subheader("🔗 Matrice de corrélation")
    fig3, ax3 = plt.subplots()
    sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

    # Outliers (IQR)
    st.subheader("🚨 Détection des Outliers (IQR)")
    q1 = filtered_df[col_numeric].quantile(0.25)
    q3 = filtered_df[col_numeric].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = filtered_df[(filtered_df[col_numeric] < lower_bound) | (filtered_df[col_numeric] > upper_bound)]

    st.write(f"**Bornes IQR** : {lower_bound:.2f} à {upper_bound:.2f}")
    st.write(f"**Nombre d'outliers détectés** : {outliers.shape[0]}")
    st.dataframe(outliers)

with col2:
    st.title("📄 Rapport automatique")

    st.markdown(f"""
    ### Espèces sélectionnées
    - {", ".join(species)}

    ### Colonne analysée : `{col_numeric}`

    **Statistiques :**
    - Moyenne : {filtered_df[col_numeric].mean():.2f}
    - Écart-type : {filtered_df[col_numeric].std():.2f}
    - Minimum : {filtered_df[col_numeric].min():.2f}
    - Maximum : {filtered_df[col_numeric].max():.2f}

    ### Analyse de la distribution
    - La distribution de `{col_numeric}` est visualisée via l’histogramme et le KDE.
    - Une courbe en cloche indique une distribution normale, tandis qu’une forme asymétrique ou avec plusieurs pics indique des sous-groupes.

    ### Outliers
    - Méthode utilisée : **IQR (Interquartile Range)**
    - Bornes : {lower_bound:.2f} à {upper_bound:.2f}
    - Nombre d’observations anormales : {outliers.shape[0]}

    ### Corrélations
    - La matrice de corrélation montre les relations linéaires entre les variables numériques du dataset filtré.

    ### Résumé :
    Ce tableau de bord permet une exploration interactive des données Iris, avec la possibilité de filtrer par espèce, de détecter des valeurs aberrantes et d’observer la structure statistique globale. Il constitue un outil idéal pour l’analyse exploratoire.
    """)
