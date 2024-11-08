import streamlit as st
from sklearn.datasets import load_iris
st.write("Hello, world!")
st.write("Night")
st.balloons()
data=load_iris(as_frame=True).frame
st.write(data.head())