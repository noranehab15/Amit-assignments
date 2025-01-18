import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

uploaded_file= r"tips (1).csv"
data=pd.read_csv(uploaded_file)

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
plot_type=st.radio("Select Plot Type :",["Scatter plot", "Line plot", "Histogram plot"])

if plot_type == "Scatter plot":
    st.subheader("Scatter Plot")
    fig=plt.figure()
    sns.scatterplot(x=x_axis,y=y_axis,data=data)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "Line plot":
    st.subheader("Line Plot")
    fig=plt.figure()
    sns.lineplot(x=x_axis,y=y_axis,data=data)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "Histogram plot":
    st.subheader("Histogram Plot")
    fig=plt.figure()
    sns.histplot(x=x_axis,data=data)
    plt.xlabel(x_axis)
    st.pyplot(fig)
st.header("Correlation Heatmap")
if st.button("Generate Heatmap"):
    fig=plt.figure()
    sns.heatmap(data.corr(numeric_only=True),annot=True,cmap="Blues")
    st.pyplot(fig)
st.write("Explore and analyze your data")
