from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pickle
import pandas as pd

app = Flask(__name__)
api = Api(app)

with open(r"C:\Users\MODUPE\data.pkl", "rb") as file:
    x,y = pickle.load(file)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

class Predict(Resource):
    def post(self):
        data = request.get_json()
        feature_names = x.columns
        input_data = []
        for feature in feature_names:
            input_data.append(data[feature])

        input_data = [input_data]
        prediction = model.predict(input_data)
        return {"prediction"  : prediction[0].tolist()}

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True)

