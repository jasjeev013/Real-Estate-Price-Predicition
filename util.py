import json
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


__locations = None
__data_columns = None
__model = None
__scalar = None

def get_estimated_price(area_type, total_sqft, bath, balcony, availability_day, availability_month, size_bhk, location):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
        
    x = np.zeros(len(__data_columns))
    x[0] = area_type
    x[1] = total_sqft
    x[2] = bath
    x[3] = balcony
    x[4] = availability_day
    x[5] = availability_month
    x[6] = size_bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    # Standard scaling the input features
    x_scaled = __scalar.transform([x])  # Ensure __scaler is fitted beforehand

    return round(__model.predict(x_scaled)[0], 2)
def get_location_names():
    print("get_location_names called")
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    
    with open("columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[7:]
    
    global __model
    with open("bangalore_house_price_prediction_model.pickle",'rb') as f:
        __model = pickle.load(f)
        
    global __scalar
    with open("scaler.pickle",'rb') as f:
        __scalar = pickle.load(f)
        
    print("loading saved artifacts...done") 
    
    
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price(1,1000,2,2,1,1,2,'1st Phase JP Nagar'))
    print(get_estimated_price(1,1000,3,3,1,1,3,'1st Phase JP Nagar'))
    print(get_estimated_price(1,1000,2,2,1,1,2,'Indira Nagar'))
    print(get_estimated_price(1,1000,3,3,1,1,3,'Indira Nagar'))
    
    
