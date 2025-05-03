import os
import joblib
import requests

MODEL_URL = "https://drive.google.com/uc?export=download&id=1GPkUTYfLiRt8iJcoT-jOiKlzBHL_uj4T"
MODEL_PATH = "models/resale_price_model.pkl"

def download_model():
    os.makedirs("models", exist_ok=True)
    if not os.path.exists(MODEL_PATH):
        print("⬇️ Downloading model...")
        response = requests.get(MODEL_URL)
        if response.status_code == 200:
            with open(MODEL_PATH, "wb") as f:
                f.write(response.content)
            print("✅ Model downloaded.")
        else:
            print(f"❌ Failed to download model. Status: {response.status_code}")
    else:
        print("✅ Model file already exists. Skipping download.")

def load_model():
    download_model()
    try:
        print(f"Loading model from: {MODEL_PATH}")
        return joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return None
