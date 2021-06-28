import json

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request


def make_prediction(features):
    prediction = model.predict(features)

    return prediction

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(
        message='Success! Hello from server.'
    )

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)

        # make prediction, exclude the result column
        result = make_prediction(df.iloc[:, :-1])

        print(result)
        res_list = result.tolist()
        
        return jsonify(result=json.dumps(res_list))

    else:
        return jsonify(
            message='Error'
        )
    

if __name__ == '__main__':
    model = joblib.load('data/rf_model.pkl')
    print('rf_model loaded!')

    app.run(host='0.0.0.0', debug=True)
