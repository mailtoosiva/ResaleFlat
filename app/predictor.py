import os
import joblib
import requests

def load_model():
    model_path = "models/resale_price_model.pkl"
    if not os.path.exists(model_path):
        os.makedirs("models", exist_ok=True)
        url = "https://huggingface.co/mailtoosiva/resale-price-predictor/resolve/main/models/resale_price_model.pkl"
        print("Downloading model from Hugging Face...")
        r = requests.get(url)
        with open(model_path, 'wb') as f:
            f.write(r.content)
    return joblib.load(model_path)










# import joblib
# import pandas as pd

# def load_model():
#     return joblib.load("models/resale_price_model.pkl")

# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]