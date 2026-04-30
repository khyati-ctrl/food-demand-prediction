import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Swiggy Demand Forecaster", layout="centered")

# 2. Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('swiggy_xgboost_model.joblib')

model = load_model()

# 3. Application Header
st.title("Swiggy Inventory Demand Forecaster")
st.write("Enter the product details below to predict the required warehouse inventory for the upcoming month.")

# 4. User Inputs (Sidebar or Main Page)
st.subheader("Input Parameters")

# Dropdown for Product Selection
product_list = [
    "Chicken Biryani", "Veg Biryani", "Masala Dosa", "Idli", 
    "Pizza Margherita", "Pepperoni Pizza", "Veg Burger", "Chicken Burger", 
    "Pasta Alfredo", "Paneer Butter Masala", "Cold Coffee", "Lassi", 
    "Chocolate Cake", "Ice Cream"
]
selected_product = st.selectbox("Select Menu Item", product_list)

# Number input for the lag feature (Previous Month's Sales)
previous_sales = st.number_input("Previous Month's Sales Volume (Units)", min_value=0, value=100)

# 5. Prediction Logic
if st.button("Generate Forecast"):
    # Create a dataframe exactly like the one the model was trained on
    input_data = pd.DataFrame({
        'Product_Name': [selected_product],
        'lag_1_month': [previous_sales]
    })
    
    # Convert text to categorical data type for XGBoost
    input_data['Product_Name'] = input_data['Product_Name'].astype('category')
    
    # Run the prediction
    prediction = model.predict(input_data)
    final_quantity = int(np.clip(prediction[0], 0, None))
    
    # 6. Display Results
    st.success("Forecast Generated Successfully!")
    st.metric(label=f"Predicted Demand for {selected_product}", value=f"{final_quantity} Units")
    
    st.info("Recommendation: Alert the supply chain team to ensure sufficient raw materials are stocked to meet this expected demand.")