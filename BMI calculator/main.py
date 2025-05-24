import streamlit as st

# Title with emoji
st.title("⚖️ BMI Calculator")

# Inputs with emoji indicators
weight = st.number_input("🧍 Enter your weight in kgs:", min_value=0.0)
height = st.number_input("📏 Enter your height in meters:", min_value=0.0)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height * height)
        
        # Result display with emoji
        st.success(f"📊 Your BMI = {bmi:.1f}")
        
        # Category with appropriate emoji
        if bmi < 18.5:
            st.warning("⚠️ Underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.success("✅ Normal weight")
        elif bmi >= 25 and bmi < 30:
            st.warning("⚠️ Overweight")
        else:
            st.error("❌ Obese")
    else:
        st.error("❌ Please enter correct weight and height values")