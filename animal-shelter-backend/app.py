from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from ml.instance import Instance
from ml.predictor import Predictor

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    feature1 = request.json['feature1']
    feature2 = request.json['feature2']

    instance = Instance(feature1, feature2)
    predictor = Predictor()

    return "" + str(predictor.make_prediction(instance))

if __name__ == '__main__':
    app.run(debug=True)
