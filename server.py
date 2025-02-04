from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    print("get_location_names called")
    locs = util.get_location_names()
    print(locs)
    response = jsonify({
        'locations': locs
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    print("-----------------------------------------------------------------------------------")
    print(request.form)  # This will print the submitted form data to the console
    
    # Check if the key exists before accessing it
    try:
        Total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        balcony = int(request.form['balcony'])
        availability_day = int(request.form['availability_day'])
        availability_month = int(request.form['availability_month'])
        size_bhk = int(request.form['size_bhk'])
        area_type = int(request.form['area_type'])
        location = request.form['location']
    except KeyError as e:
        return f"Missing key in form data: {str(e)}", 400
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(area_type, Total_sqft, bath, balcony, availability_day, availability_month, size_bhk, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__=='__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)