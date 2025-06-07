import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

st.title("📌 Matrice de corrélation")

fig, ax = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
