import pandas as pd
import numpy as np
import joblib
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    logging.info("Reading and combining all CSV files...")
    csv_files = [
        # "../data/Resale_Flat_Prices_Based_on_Approval_Date_1990_1999.csv",
        # "../data/Resale_Flat_Prices_Based_on_Approval_Date_2000_Feb2012.csv",
        # "../data/Resale_Flat_Prices_Based_on_Registration_Date_From_Jan_2015_to_Dec_2016.csv",
        # "../data/Resale_Flat_Prices_Based_on_Registration_Date_From_Mar_2012_to_Dec_2014.csv",
        "Resale_flat_prices_based_on_registration_date_from_Jan-2017_onwards.csv"
    ]
    
    df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
    logging.info(f"Combined dataset shape: {df.shape}")

    logging.info("Performing feature engineering...")
    df['month'] = pd.to_datetime(df['month'])
    df['year'] = df['month'].dt.year
    df['remaining_lease'] = df['lease_commence_date'] + 99 - df['year']

    X = df[['town', 'flat_type', 'storey_range', 'floor_area_sqm', 'flat_model', 'remaining_lease']]
    y = df['resale_price']

    logging.info("Setting up preprocessing pipeline...")
    categorical_features = ['town', 'flat_type', 'storey_range', 'flat_model']
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ], remainder='passthrough')

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    logging.info("Splitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logging.info("Training model...")
    pipeline.fit(X_train, y_train)

    logging.info("Evaluating model...")
    y_pred = pipeline.predict(X_test)
    logging.info(f"MAE: {mean_absolute_error(y_test, y_pred):,.2f}")
    logging.info(f"MSE: {mean_squared_error(y_test, y_pred):,.2f}")
    logging.info(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")
    logging.info(f"R2 Score: {r2_score(y_test, y_pred):.4f}")

    logging.info("Saving model to disk...")
    Path("models").mkdir(exist_ok=True)
    joblib.dump(pipeline, "models/resale_price_model.pkl")
    logging.info("Model saved successfully at models/resale_price_model.pkl")

except Exception as e:
    logging.error(f"An error occurred: {e}")