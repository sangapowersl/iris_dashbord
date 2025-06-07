import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

st.title("📊 Visualisation interactive")

species = st.multiselect("Filtrer par espèce", df["species"].unique(), default=df["species"].unique())
filtered_df = df[df["species"].isin(species)]

col = st.selectbox("Choisir une variable", filtered_df.select_dtypes(include="number").columns)

tab1, tab2 = st.tabs(["Histogramme + KDE", "Boxplot"])

with tab1:
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df[col], kde=True, ax=ax1)
    st.pyplot(fig1)

with tab2:
    fig2, ax2 = plt.subplots()
    sns.boxplot(x=filtered_df[col], ax=ax2)
    st.pyplot(fig2)

#git push -u origin main
