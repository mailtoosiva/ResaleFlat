import joblib
import pandas as pd

def load_model():
    return joblib.load("../models/resale_price_model.pkl")

def make_prediction(model, user_input):
    df = pd.DataFrame([user_input])
    return model.predict(df)[0]