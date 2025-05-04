import streamlit as st
from predictor import load_model, make_prediction

st.set_page_config(page_title="HDB Resale Price Predictor", layout="centered")

# Logging for debugging
st.write("App started")

# Load trained model
try:
    model = load_model()
    st.write("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("🏠 HDB Resale Price Predictor")
st.markdown("Use this app to estimate the resale price of an HDB flat in Singapore.")

# Input fields
user_input = {
    "town": st.selectbox("Town", ["ANG MO KIO", "BEDOK", "BUKIT BATOK", "CHOA CHU KANG"]),
    "flat_type": st.selectbox("Flat Type", ["3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"]),
    "storey_range": st.selectbox("Storey Range", ["01 TO 03", "04 TO 06", "07 TO 09", "10 TO 12"]),
    "floor_area_sqm": st.slider("Floor Area (sqm)", 30, 200, 90),
    "flat_model": st.selectbox("Flat Model", ["Model A", "Improved", "New Generation", "Simplified"]),
    "remaining_lease": st.slider("Remaining Lease (years)", 1, 99, 70)
}

if st.button("Predict Price"):
    try:
        predicted_price = make_prediction(model, user_input)
        st.success(f"Estimated Resale Price: SGD {predicted_price:,.2f}")
        st.write("Prediction complete")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
