import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

wine_df = pd.read_csv('winequality-red.csv')

X = wine_df.drop('quality',axis=1)
y = wine_df['quality'].apply(lambda yval:1 if yval>=7 else 0)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=3)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

X_test_prediction = model.predict(X_test)
print(accuracy_score(X_test_prediction, Y_test))

#------------------ code for web app-----------------
st.title("Wine Quality Prediction Model")
input_text = st.text_input('Enter all Wine Features')
input_text_list = input_text.split(',')
np_df=np.asarray(input_text_list)
features = np.asarray(input_text_list)
prediction = model.predict(features.reshape(1,-1))
if prediction[0] ==1:
    st.write("It's a Good Quality Wine")
else:
    st.write("It's a Bad Quality Wine")

















