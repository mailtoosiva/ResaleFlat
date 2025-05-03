import streamlit as st
from predictor import load_model, make_prediction

# Load trained model
model = load_model()

st.title("HDB Resale Price Predictor")
st.markdown("Estimate the resale price of an HDB flat in Singapore")

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
    predicted_price = make_prediction(model, user_input)
    st.success(f"Estimated Resale Price: SGD {predicted_price:,.2f}")