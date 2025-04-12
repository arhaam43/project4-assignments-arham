# Python Streamlit BMI calculator in just 6 mints project-8
import streamlit as st

# Set the title of the app
st.title("💪 BMI Calculator")

# Input for user height (in centimeters)
height_cm = st.number_input("Enter your height (cm):", min_value=0.0, format="%.2f")

# Input for user weight (in kilograms)
weight_kg = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

# Calculator BMI
if st.button("Calculator BMI"):
    if height_cm > 0 or weight_kg > 0:
        # Convert height to meters
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        st.success(f"Your BMI is: {bmi: .2f}")

        # Determine category
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid values for weight and height.")