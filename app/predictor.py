import os
import joblib
import requests

MODEL_DIR = "models"
MODEL_FILE = "resale_price_model.pkl"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)

def download_model():
    url = "https://drive.usercontent.google.com/download?id=1GPkUTYfLiRt8iJcoT-jOiKlzBHL_uj4T&export=download"
    os.makedirs(MODEL_DIR, exist_ok=True)
    print("📦 Downloading model...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("✅ Model downloaded.")
    else:
        raise Exception(f"❌ Failed to download model. Status code: {response.status_code}")

def load_model():
    if not os.path.exists(MODEL_PATH):
        download_model()
    print(f"📂 Loading model from: {MODEL_PATH}")
    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"❌ Failed to load the model: {e}")
        return None


# def load_model():
#     return joblib.load("../models/resale_price_model.pkl")

# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]
