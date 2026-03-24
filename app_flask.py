from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import random
import sqlite3
from database import store_sensor_data

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/smart_irrigation_model.pkl')

# Dummy function to simulate real-time sensor data
def get_sensor_data():
    return {
        "soil_moisture": random.uniform(0, 100),
        "temperature": random.uniform(15, 35),
        "humidity": random.uniform(30, 80)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sensors_data', methods=['GET'])
def get_sensors_data():
    data = get_sensor_data()
    return jsonify(data)

@app.route('/predict_irrigation', methods=['POST'])
def predict_irrigation():
    data = request.get_json()

    # Extract data from the request
    soil_moisture = data['soil_moisture']
    temperature = data['temperature']
    humidity = data['humidity']

    # Store the sensor data in the database
    store_sensor_data(soil_moisture, temperature, humidity)

    # Predict irrigation need based on the model
    prediction = model.predict([[soil_moisture, temperature, humidity]])

    # Return the prediction result
    irrigation_needed = prediction[0]
    return jsonify({'irrigation_needed': irrigation_needed})

if __name__ == '__main__':
    app.run(debug=True)
