import streamlit as st
import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load model
with open("bangalore_house_price_prediction_model.pickle", "rb") as f:
    model = pickle.load(f)

# Load columns
with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]
    locations = data_columns[7:]

# Load scaler
with open("scaler.pickle", "rb") as f:
    scaler = pickle.load(f)

# Streamlit UI
st.title("Bangalore House Price Prediction")

# Inputs
area_type = st.selectbox("Select Area Type", ["Built-up Area", "Carpet Area", "Plot Area", "Super built-up Area"])
total_sqft = st.number_input("Total Square Feet", min_value=100.0, step=10.0)
bath = st.slider("Number of Bathrooms", 0, 10, 2)
balcony = st.slider("Number of Balconies", 0, 5, 1)
availability_day = st.number_input("Availability Day", min_value=1, max_value=31, step=1)
availability_month = st.number_input("Availability Month", min_value=1, max_value=12, step=1)
size_bhk = st.slider("BHK", 1, 10, 2)
location = st.selectbox("Select Location", locations)

# Preprocessing
area_type_map = {"Built-up Area": 0, "Carpet Area": 1, "Plot Area": 2, "Super built-up Area": 3}
input_data = np.zeros(len(data_columns))
input_data[0] = area_type_map[area_type]
input_data[1] = total_sqft
input_data[2] = bath
input_data[3] = balcony
input_data[4] = availability_day
input_data[5] = availability_month
input_data[6] = size_bhk
if location in locations:
    input_data[locations.index(location) + 7] = 1

# Scaling
scaled_input = scaler.transform([input_data])
print(scaled_input[0][0:9])
# Prediction
if st.button("Predict Price"):
    prediction = model.predict(scaled_input)[0]
    st.success(f"Predicted Price: ₹{prediction:,.2f} lakhs")
