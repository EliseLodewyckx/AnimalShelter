from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from ml.animal import Animal
from ml.predictor import Predictor

app = Flask(__name__)
CORS(app)


# @app.route("/predict", methods=["POST"])
# def predict():
#     feature1 = request.json['feature1']
#     feature2 = request.json['feature2']
#
#     instance = Instance(feature1, feature2)
#     predictor = Predictor()
#
#     return "" + str(predictor.make_prediction(instance))

@app.route("/predict", methods=["POST"])
def predict_animal():
    animal = Animal(
        request.json['animalType'],
        request.json['sex'],
        request.json['intact'],
        request.json['age'])

    return Predictor().make_animal_prediction(animal)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
