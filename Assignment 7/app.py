# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load('diabetes_model.pkl')

# Set up Streamlit app
st.set_page_config(page_title="Diabetes Progression Predictor", layout="wide")
st.title("🩺 Diabetes Progression Predictor")

st.markdown("Provide input values for each feature to predict disease progression.")

# Input widgets
def user_input_features():
    age = st.slider('Age', -0.1, 0.2, 0.05)
    sex = st.selectbox('Sex', [0.0, 1.0])  # 0.0 for female, 1.0 for male
    bmi = st.slider('BMI', 0.0, 0.2, 0.1)
    bp = st.slider('Blood Pressure', 0.0, 0.2, 0.1)
    s1 = st.slider('S1 (TC)', -0.1, 0.1, 0.01)
    s2 = st.slider('S2 (LDL)', -0.2, 0.2, 0.01)
    s3 = st.slider('S3 (HDL)', -0.2, 0.2, -0.01)
    s4 = st.slider('S4 (TCH)', -0.1, 0.1, 0.01)
    s5 = st.slider('S5 (LTG)', -0.2, 0.3, 0.02)
    s6 = st.slider('S6 (GLU)', -0.1, 0.1, 0.01)
    
    data = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'bp': bp,
        's1': s1,
        's2': s2,
        's3': s3,
        's4': s4,
        's5': s5,
        's6': s6
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Prediction
prediction = model.predict(input_df)[0]
st.subheader("📈 Predicted Disease Progression:")
st.success(f"{prediction:.2f} units")

# Feature Importance
st.subheader("📊 Feature Importances:")
feat_imp = model.feature_importances_
columns = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
imp_df = pd.DataFrame({'Feature': columns, 'Importance': feat_imp})

fig, ax = plt.subplots()
sns.barplot(data=imp_df, y="Feature", x="Importance", palette="coolwarm", ax=ax)
st.pyplot(fig)
