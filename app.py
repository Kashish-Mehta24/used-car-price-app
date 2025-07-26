import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model and column names
model = joblib.load('used_car_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')  # ← 105 training columns

st.title("🚗 Used Car Price Prediction App")

st.write("Fill in the car details below:")

# User inputs
present_price = st.number_input("Present Price (in lakhs)", value=5.0)
kms_driven = st.number_input("KMs Driven", value=30000)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
age = st.slider("Car Age (in years)", 0, 25, value=5)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Create a single-row DataFrame from inputs
input_dict = {
    'Present_Price': present_price,
    'Kms_Driven': kms_driven,
    'Owner': owner,
    'car_age': age,
    'Fuel_Type_' + fuel_type: 1,
    'Seller_Type_' + seller_type: 1,
    'Transmission_' + transmission: 1
}

# Convert to DataFrame and match training columns
input_df = pd.DataFrame([input_dict])

# Add all other columns with 0 if missing
for col in model_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Ensure column order matches training
input_df = input_df[model_columns]

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    # Force prediction to never exceed present price
    prediction = min(prediction, present_price)

    st.success(f"💰 Estimated Selling Price: ₹{prediction:.2f} lakhs")
