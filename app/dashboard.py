import streamlit as st
import pandas as pd

st.set_page_config(page_title="SecureFed Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ SecureFed: Privacy-Preserving Healthcare Analytics")
st.markdown("### My Final-Year Project Dashboard")
st.markdown("---")

# A simple table showing how our project works
df = pd.DataFrame({
    "Model Type": ["Centralized Hospital Data", "SecureFed (Federated)", "SecureFed + Private (DP)"],
    "Is Data Shared?": ["Yes (Risky)", "No (Safe)", "No (Maximum Privacy)"],
    "Accuracy": ["96.5%", "94.7%", "89.5%"]
})

st.subheader("How Our Project Compares")
st.dataframe(df, use_container_width=True)

st.success("🎉 Success! Your project dashboard is running locally and looks great for your review.")