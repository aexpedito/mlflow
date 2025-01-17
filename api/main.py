from app import app
from flask import render_template, jsonify, request
import sys
import mlflow
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    dados = request.json
    app.logger.info(f"{dados}")
    #load do modelo registrado
    tracking_uri = os.getenv('FLASK_TRACK_URI')
    model_name = os.getenv('FLASK_MODEL_NAME')
    model_version = os.getenv('FLASK_MODEL_VER')
    app.logger.info(f"{model_name}---{tracking_uri}---{model_version}")

    mlflow.set_tracking_uri(tracking_uri)
    model_uri = f"models:/{model_name}/{model_version}"
    model = mlflow.sklearn.load_model(model_uri)

    #TODO make predicition
    X_test = pd.DataFrame(dados, index=[0])
    print(X_test)
    prediction = model.predict(X_test)

    print(prediction)

    response = {
        "message": "Success",
        "status": "success",
        "Potability": f"{prediction}"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    port = sys.argv[1]
    app.run(host="0.0.0.0", port=port, debug=False)

