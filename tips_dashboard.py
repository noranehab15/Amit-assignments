import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

uploaded_file= r"C:\Users\HP\Desktop\project tips\data\tips (1).csv"
data=pd.read_csv(uploaded_file)

st.title("Tips Data Dashboard")
st.header('Data overview')
st.write("first data row of the dataset! ")
st.dataframe(data.head())
st.header("Data Overview")
st.write("First few rows of the dataset:")
st.dataframe(data.head())

# Data Summary
st.header("Summary Statistics")

st.dataframe(data.describe())

# Select Columns for Visualization
st.header("Data Visualization")
st.write("Select columns to visualize:")
x_axis=st.selectbox("X-axis",data.columns)
y_axis=st.selectbox("Y-axis",data.columns)
plot_type=st.radio("Select Plot Type :",["Scatter plot", "Bar plot", "Histogram plot"])
