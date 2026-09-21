import streamlit as st
import joblib
import numpy as np

#load model
model = joblib.load('iris_model.pkl')

#page title
st.title('Iris Flower Prediction App')

st..header('Enter the measurements of the Iris flower:')
