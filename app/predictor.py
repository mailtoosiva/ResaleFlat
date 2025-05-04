from huggingface_hub import hf_hub_download
import joblib
import os
import logging
import pandas as pd  # ✅ Added missing import

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def load_model():
    logger.info("Loading model...")
    try:
        # Use Hugging Face Hub to download the model
        model_path = hf_hub_download(
            repo_id="mailtoosiva/resale-price-predictor",
            filename="models/resale_price_model.pkl"
        )
        logger.info(f"Model downloaded to: {model_path}")
        
        # Load the model
        model = joblib.load(model_path)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

def make_prediction(model, user_input):
    try:
        df = pd.DataFrame([user_input])
        prediction = model.predict(df)[0]
        logger.info(f"Prediction successful: {prediction}")
        return prediction
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise


# import os
# import joblib
# import requests
# import pandas as pd


# def load_model():
#     model_path = "models/resale_price_model.pkl"
#     if not os.path.exists(model_path):
#         print("Model not found locally. Downloading from Hugging Face...")
#         os.makedirs("models", exist_ok=True)
#         url = "https://huggingface.co/mailtoosiva/resale-price-predictor/resolve/main/models/resale_price_model.pkl"
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(model_path, 'wb') as f:
#                 f.write(response.content)
#         else:
#             raise Exception(f"Failed to download model. HTTP Status Code: {response.status_code}")
#     return joblib.load(model_path)



# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]




# import joblib
# import pandas as pd

# def load_model():
#     return joblib.load("models/resale_price_model.pkl")

# def make_prediction(model, user_input):
#     df = pd.DataFrame([user_input])
#     return model.predict(df)[0]