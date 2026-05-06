import streamlit as st
import pandas as pd
import os

st.title("🛡️ Real-Time Fraud Detection - Najwa 230104040082")

path = "stream_data/realtime_output/"
if os.path.exists(path) and any(f.endswith('.parquet') for f in os.listdir(path)):
    df = pd.read_parquet(path)
    st.metric("Total Transaksi", len(df))
    st.metric("Total Fraud", len(df[df["status"]=="FRAUD"]))
    st.dataframe(df.tail(10))
    st.bar_chart(df["status"].value_counts())
else:
    st.info("Menunggu data masuk dari Spark...")

