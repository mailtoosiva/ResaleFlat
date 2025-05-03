import streamlit as st
import pandas as pd
from predictor import load_model

st.set_page_config(page_title="HDB Resale Price Predictor", layout="centered")

# Load model
model = load_model()

st.title("🏠 HDB Resale Price Prediction App")

if model is None:
    st.error("❌ Model could not be loaded. Please try again later.")
    st.stop()

# Input form
with st.form("prediction_form"):
    st.subheader("📋 Enter Flat Details")

    town = st.selectbox("Town", ["ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH", "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST", "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"])
    flat_type = st.selectbox("Flat Type", ["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI GENERATION"])
    storey_range = st.selectbox("Storey Range", ["01 TO 03", "04 TO 06", "07 TO 09", "10 TO 12", "13 TO 15", "16 TO 18", "19 TO 21", "22 TO 24", "25 TO 27", "28 TO 30", "31 TO 33", "34 TO 36", "37 TO 39", "40 TO 42", "43 TO 45", "46 TO 48", "49 TO 51"])
    floor_area_sqm = st.slider("Floor Area (sqm)", 30, 200, 90)
    flat_model = st.selectbox("Flat Model", ["Improved", "New Generation", "Model A", "Standard", "Simplified", "Model A2", "Premium Apartment", "Maisonette", "Apartment", "Adjoined flat", "Terrace", "DBSS", "Type S1", "Type S2"])
    lease_commence_date = st.slider("Lease Commence Year", 1966, 2023, 1999)

    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert inputs to dataframe
    input_data = pd.DataFrame({
        "town": [town],
        "flat_type": [flat_type],
        "storey_range": [storey_range],
        "floor_area_sqm": [floor_area_sqm],
        "flat_model": [flat_model],
        "lease_commence_date": [lease_commence_date]
    })

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Resale Price: SGD {prediction:,.0f}")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
