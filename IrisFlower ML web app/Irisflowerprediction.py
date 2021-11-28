import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App
**This application will help us in predicting the Iris flower type!**
""")

st.sidebar.header('User Input Parameters')

def ui_info():
    sepal_length = st.sidebar.slider('Sepal length', 5.0, 8.0, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.6, 4.0, 3.0)
    petal_length = st.sidebar.slider('Petal length', 2.2, 6.6, 2.2)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.8, 0.9)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    info = pd.DataFrame(data, index=[0])
    return info

df = ui_info()

st.subheader('UI parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_p = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_p)
