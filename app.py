import streamlit as st
import numpy as np
import joblib

#load model
model = joblib.load('iris_model.pkl')

#page title
st.title('Iris Flower Prediction App')

st.header('Enter the measurements of the Iris flower:')

#input title
sepal_lenght=st.number_input('Sepal Length (cm)',min_values=0.0,max_values=10.0,values=5.0,step=0.1)
sepal_width=st.number_input('Sepal width (cm)',min_values=0.0,max_values=10.0,values=3.0,step=0.1)
petal_lenght=st.number_input('Petal Length (cm)',min_values=0.0,max_values=8.0,values=4.0,step=0.1)
petal_width=st.number_input('Petal Width (cm)',min_values=0.0,max_values=5.0,values=1.0,step=0.1)

#prediction
if st.button('predict'):
    input_data=np.array([[sepal_length,
                          sepal_width,
                          petal_length,
                          petal_lenght]]).astype(np.float64)
    prediction=model.predict(input_data)
    st.success(f'The predicted Iris species is : {prediction[0]}')
                          
