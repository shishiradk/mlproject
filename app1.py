import streamlit as st
import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page title
st.set_page_config(page_title="Student Score Predictor")

st.title("🎓 Student Performance Predictor")
st.markdown("Fill out the form below to predict **math score** based on student details:")

# Collect input data
gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# Predict button
if st.button("Predict Math Score"):
    # Create data instance
    input_data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    df = input_data.get_data_as_data_frame()
    st.write("📄 Input Data", df)

    # Predict
    pipeline = PredictPipeline()
    try:
        prediction = pipeline.predict(df)
        st.success(f"🎯 Predicted Math Score: **{prediction[0]:.2f}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
