import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("models/best_model.pkl")

st.title("Student Exam Score Predictor")
st.write("Predict a student's exam score based on study habits and lifestyle.")

# Inputs
study_hours = st.number_input(
    "Study Hours per Day", min_value=0.0, max_value=24.0, value=2.0
)
self_study_hours = st.number_input(
    "Self-Study Hours per Day", min_value=0.0, max_value=24.0, value=1.0
)
sleep_hours = st.number_input(
    "Sleep Hours per Day", min_value=0.0, max_value=24.0, value=7.0
)
focus_index = st.slider("Focus Index (0-1)", 0.0, 1.0, 0.5)
burnout_level = st.slider("Burnout Level (0-1)", 0.0, 1.0, 0.2)
productivity_score = st.number_input("Productivity Score (0-100)", 0, 100, 50)
mental_health_score = st.number_input("Mental Health Score (0-100)", 0, 100, 50)
screen_time_hours = st.number_input("Screen Time Hours per Day", 0.0, 24.0, 2.0)
social_media_hours = st.number_input("Social Media Hours per Day", 0.0, 24.0, 1.0)
gaming_hours = st.number_input("Gaming Hours per Day", 0.0, 24.0, 1.0)

# Predict button
if st.button("Predict Exam Score"):
    input_data = np.array(
        [
            [
                study_hours,
                self_study_hours,
                sleep_hours,
                focus_index,
                burnout_level,
                productivity_score,
                mental_health_score,
                screen_time_hours,
                social_media_hours,
                gaming_hours,
            ]
        ]
    )

    prediction = model.predict(input_data)
    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")
