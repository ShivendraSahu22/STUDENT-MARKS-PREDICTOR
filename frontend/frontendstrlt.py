import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"  # Update with your FastAPI server URL

st.title("STUDENT MARKS PREDICTOR")
st.markdown("Enter your details below:")

# Input fields
number_courses = st.number_input("Number of Courses", min_value=1, max_value=10, value=3)
time_study = st.number_input("Time Spent Studying (hours)", min_value=0.0, value=2.0)

if st.button("Predict Student Marks"):
    input_data = {
        "number_courses": number_courses,
        "time_study": time_study
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200:
            st.success(f"Predicted Student Marks: {result['predicted_marks']}")
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")