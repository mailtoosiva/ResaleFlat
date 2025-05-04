Markdown

# HDB Resale Price Predictor (Singapore)

## Overview

This project aims to develop and deploy a machine learning model that predicts the resale prices of Housing and Development Board (HDB) flats in Singapore. The web application, built using Streamlit, allows users to input various flat details and receive an estimated resale price.

## Motivation

Estimating the resale value of an HDB flat in Singapore can be complex due to the numerous factors influencing prices, such as location, flat type, size, and lease duration. This predictive model provides a user-friendly tool to help potential buyers and sellers gain a better understanding of the market value.

## Project Scope

The project encompasses the following stages:

1.  **Data Collection and Preprocessing:** Gathering historical HDB resale flat transaction data from the Singapore Housing and Development Board (HDB) and preparing it for machine learning.
2.  **Feature Engineering:** Extracting and creating relevant features from the raw data to improve model accuracy.
3.  **Model Selection and Training:** Choosing and training an appropriate machine learning regression model (currently a Random Forest Regressor) on the historical data.
4.  **Model Evaluation:** Assessing the model's performance using relevant regression metrics.
5.  **Streamlit Web Application:** Building an interactive web interface using Streamlit for users to input flat details.
6.  **Deployment:** Deploying the Streamlit application online (e.g., on Streamlit Community Cloud, Render, etc.).
7.  **Testing and Validation:** Ensuring the application functions correctly and provides reasonable predictions.

## Data Source

The historical HDB resale flat transaction data is located in the `data/` directory.

## Workflow and Execution

To run this project, follow these steps from the project root directory (`ResaleFlat/`):

1.  **Clone the GitHub Repository:**
    ```bash
    git clone <your_github_repository_url>
    cd ResaleFlat
    ```
    *(Replace `<your_github_repository_url>` with the actual URL of your repository)*

2.  **Set up the Environment:**
    It's recommended to create a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure your `requirements.txt` file in the project root lists all necessary packages: `pandas`, `scikit-learn`, `joblib`, `streamlit`, `huggingface-hub`)*

4.  **Train the Model:**
    Navigate to the `app/` directory and run the training script:
    ```bash
    cd app
    python train_model.py
    ```
    This script will:
    * Load and combine the HDB resale price datasets from the `../data/` directory.
    * Perform feature engineering.
    * Set up a preprocessing pipeline.
    * Train the machine learning model.
    * Save the trained model to `app/models/resale_price_model.pkl`.

5.  **Run the Streamlit Application:**
    Navigate back to the project root directory (`ResaleFlat/`) and run the Streamlit app:
    ```bash
    streamlit run app/streamlit_app.py
    ```
    This will open the web application in your default web browser.

6.  **Use the Application:**
    In the web application, you can select the details of an HDB flat (Town, Flat Type, Storey Range, Floor Area, Flat Model, Remaining Lease) using the provided dropdowns and slider. Click the "Predict Price" button to get an estimated resale price.

## Project Structure

ResaleFlat/
├── app/
│   ├── predictor.py             # Prediction logic
│   ├── streamlit_app.py         # Streamlit application
│   └── train_model.py           # Model training script
├── data/
│   ├── Resale_Flat_Prices_Based_on_Approval_Date_1990_1999.csv
│   ├── Resale_Flat_Prices_Based_on_Approval_Date_2000_Feb2012.csv
│   ├── Resale_Flat_Prices_Based_on_Registration_Date_From_Jan_2015_to_Dec_2016.csv
│   ├── Resale_Flat_Prices_Based_on_Registration_Date_From_Mar_2012_to_Dec_2014.csv
│   └── Resale_flat_prices_based_on_registration_date_from_Jan-2017_onwards.csv
├── requirements.txt
└── README.md


## Coding Standards

This project adheres to the PEP 8 coding standards for Python.


## Project Evaluation

The success of this project will be evaluated based on:

* The accuracy of the resale price predictions.
* The usability and intuitiveness of the Streamlit web application.
* The proper implementation of the project workflow and adherence to coding standards.
* The quality of the project documentation and the demo video.

## Maintainability and Portability

* **Maintainable:** The code is well-organized within the `app/` directory, separating the different components of the application. Clear variable names and comments enhance readability. Logging is implemented in the `predictor.py` and `train_model.py` scripts to aid in debugging and monitoring.
* **Portable:** The project primarily relies on standard Python libraries, making it portable across different operating systems as long as Python and the necessary libraries are installed. The use of relative paths for data loading within `train_model.py` also contributes to portability.

## GitHub Repository

The complete code for this project is available on GitHub at https://github.com/mailtoosiva/ResaleFlat. The repository is public for anyone to review.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests with any improvements or bug fixes.

## License
