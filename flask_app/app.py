import xgboost as xgb
import pandas as pd
import pickle
import numpy as np

from flask import Flask, request, jsonify, render_template


import os
print(os.listdir())
with open(f'../flask_app/model.pickle', 'rb') as handle:
    model = pickle.load(handle)

# Create flask app
flask_app = Flask(__name__)


@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    # features from request
    float_features = [float(x) for x in request.form.values()]
    # converting features
    columns = ['General government revenue | Percent of GDP',
               'General government total expenditure | National currency | Billions',
               'Gross national savings | Percent of GDP',
               'Total investment | Percent of GDP',
               'Unemployment rate | Percent of total labor force']
    values = pd.DataFrame([float_features], columns=columns)
    features = xgb.DMatrix(values)
    # features -> model
    prediction = model.predict(features).tolist()[0]

    # return {"results": prediction}
    return render_template("index.html", prediction_text="Predicted 'Gross domestic product per capita, current prices | U.S. dollars | Units' is : ${}".format(prediction), input_values=str(features))


@flask_app.route("/flask_app")
def test_ok():
    return {"result": "ok"}


if __name__ == "__main__":
    flask_app.run(debug=True)
