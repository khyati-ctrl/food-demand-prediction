# Swiggy Inventory Demand Forecaster

> 📄 **Click here to read the full Project Presentation & Detailed Write-up:
https://docs.google.com/document/d/1zM-Qt9T4IwRA5NfnVQ-JE8fMAg5tpQuHO7loOBqipnE/edit?usp=sharing**

## 📌 Project Overview
This project is an end-to-end Machine Learning pipeline designed to forecast monthly inventory demand for various menu items across Swiggy’s fulfillment centers. Built as a comprehensive data science lifecycle project for the **SRM Insider Club**, it transitions raw, highly volatile daily transactional data into actionable macro-level business forecasts.

We engineered a realistic synthetic dataset featuring weather impacts, promotional boosts, and a non-linear "viral marketing anomaly" to rigorously test and compare baseline statistical models against advanced tree-based algorithms. 

## ✨ Key Features
*   **Synthetic Data Generation:** A custom robust data pipeline simulating 12,000 real-world Swiggy transactions, incorporating business logic for weather (rain spikes), day-of-week trends, and discount code application.
*   **Exploratory Data Analysis (EDA):** Comprehensive visualizations uncovering temporal order patterns and isolating non-linear sales anomalies.
*   **Algorithmic Showdown:** A competitive modeling environment comparing Linear Regression and Random Forest against an XGBoost Regressor.
*   **Interactive Frontend Prototype:** A locally hosted Streamlit dashboard allowing warehouse managers to generate real-time inventory predictions without interacting with the codebase.

## 🛠️ Tech Stack
*   **Data Manipulation & Engineering:** `pandas`, `numpy`
*   **Data Visualization:** `matplotlib`, `seaborn`
*   **Machine Learning:** `scikit-learn`, `xgboost`
*   **Model Deployment/Frontend:** `streamlit`, `joblib`

## 🚀 How to Run the Project Locally

### 1. Clone the Repository
git clone [https://github.com/yourusername/swiggy-demand-forecaster.git](https://github.com/yourusername/swiggy-demand-forecaster.git)
cd swiggy-demand-forecaster

### 2. Install Dependencies
Ensure you have Python installed, then run:
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit joblib

### 3. Generate Data and Train the Model
Run the Jupyter Notebooks in sequential order to generate the dataset, view the EDA, and train the Machine Learning models.
Data_synthesis.ipynb
EDA.ipynb
Machine_Learning.ipynb (Running this will export the swiggy_xgboost_model.joblib file required for the app).

### 4. Launch the Streamlit Web App
Once the model is trained and saved, launch the interactive frontend dashboard:
streamlit run app.py

## 📂 Project Structure
* ├── data/
* │   └── swiggy_data_final.csv         # Generated dataset
* ├── notebooks/
* │   ├── Data_synthesis.ipynb       # Synthetic data logic
* │   ├── EDA.ipynb                  # Visual business insights
* │   └── Machine_Learning.ipynb     # ML pipeline and model showdown
* ├── app.py                            # Streamlit frontend application
* ├── swiggy_xgboost_model.joblib       # Serialized XGBoost model
* └── README.md

## 👥 The Team
* Jaswanth: Lead Data Engineer (Architecture & Synthetic Generation)
* Sneha: Lead Data Analyst (EDA & Anomaly Detection)
* Khyati: Lead Machine Learning Engineer and Frontend Developer (Model Training and Frontend Development)
