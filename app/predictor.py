import os
import joblib
import requests
import pandas as pd

def load_model():
    model_path = "models/resale_price_model.pkl"
    if not os.path.exists(model_path):
        os.makedirs("models", exist_ok=True)
        url = "https://huggingface.co/mailtoosiva/resale-price-predictor/resolve/main/models/resale_price_model.pkl"
        r = requests.get(url, stream=True)
        if r.status_code != 200:
            raise Exception(f"Download failed: {r.status_code}")
        with open(model_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return joblib.load(model_path)


def make_prediction(model, user_input):
    df = pd.DataFrame([user_input])
    return model.predict(df)[0]




# import joblib
# import pandas as pd

# def load_model():
#     return joblib.load("models/resale_price_model.pkl")

# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]