import streamlit as st
import seaborn as sns
import pandas as pd

df = sns.load_dataset("iris")

st.title("🚨 Détection d'outliers")

species = st.multiselect("Filtrer par espèce", df["species"].unique(), default=df["species"].unique())
filtered_df = df[df["species"].isin(species)]

col = st.selectbox("Choisir une variable numérique", filtered_df.select_dtypes(include="number").columns)

q1 = filtered_df[col].quantile(0.25)
q3 = filtered_df[col].quantile(0.75)
iqr = q3 - q1

borne_inf = q1 - 1.5 * iqr
borne_sup = q3 + 1.5 * iqr

outliers = filtered_df[(filtered_df[col] < borne_inf) | (filtered_df[col] > borne_sup)]

st.write(f"**Bornes IQR :** {borne_inf:.2f} à {borne_sup:.2f}")
st.write(f"**Nombre d'outliers :** {outliers.shape[0]}")
st.dataframe(outliers)
