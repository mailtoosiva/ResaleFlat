import os
import gdown
import joblib
import streamlit as st
import numpy as np

# Google Drive file ID from the link
file_id = '1GPkUTYfLiRt8iJcoT-jOiKlzBHL_uj4T'

# Construct the download URL for the file
download_url = f'https://drive.google.com/uc?id={file_id}'

# Directory to store the model file
model_directory = 'models'
os.makedirs(model_directory, exist_ok=True)

# Path to save the model
model_path = os.path.join(model_directory, 'resale_price_model.pkl')

# Download the file if it doesn't exist locally
if not os.path.exists(model_path):
    print("Model file not found locally. Downloading...")
    gdown.download(download_url, model_path, quiet=False)
else:
    print("Model file already exists. Skipping download.")

# Try to load the model
try:
    print(f"Attempting to load the model from: {model_path}")
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load the model: {e}")
    model = None

# If model is successfully loaded, define the Streamlit prediction interface
if model:
    st.title("Resale Flat Price Prediction")
    st.write("Enter the details to predict the resale price of a flat in Singapore.")

    # Define input fields for user to fill out
    town = st.text_input("Town:")
    flat_type = st.text_input("Flat Type:")
    storey_range = st.text_input("Storey Range:")
    floor_area_sqm = st.number_input("Floor Area (sqm):", min_value=0)
    flat_model = st.text_input("Flat Model:")
    remaining_lease = st.number_input("Remaining Lease (years):", min_value=0)

    # Button to trigger prediction
    if st.button("Predict Price"):
        input_data = [[town, flat_type, storey_range, floor_area_sqm, flat_model, remaining_lease]]
        try:
            predictions = model.predict(input_data)
            st.success(f"Predicted Resale Price: ${predictions[0]:,.2f}")
        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
else:
    print("Model is not loaded, skipping prediction.")


# def load_model():
#     return joblib.load("../models/resale_price_model.pkl")

# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]
