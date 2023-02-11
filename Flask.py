
#flask helps to write a python service which can serve http requests

from flask import Flask, request, jsonify
import util

app = Flask(__name__)



@app.route('/hi',methods=['GET'])
def hi():
    if request.method == 'GET':
        try:
            total_sqft = float(request.form.get('Squareft'))
        except ValueError:
            return "Invalid total square footage value"
        location = request.form.get('uiLocations')
        bhk = int(request.form.get('uiBHK'))
        bath = int(request.form.get('uiBathrooms'))

        response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    else:
        return "This endpoint only accepts POST requests."

@app.route('/get_location_names')
def get_location_names():
    print("into get_loc")
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        print("fgfgdf")
        print(request.form)
        print("f")
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # print("load finished, now next step")
    app.run(debug=True )