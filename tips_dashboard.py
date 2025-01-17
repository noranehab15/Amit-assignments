import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

uploaded_file= r"C:\Users\HP\Desktop\project tips\data\tips (1).csv"
data=pd.read_csv(uploaded_file)

st.title("Tips Data Dashboard")