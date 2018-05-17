from ml.instance import Instance
from ml.models import Model
from ml.animal import Animal
import os.path

class Predictor(object):

    def make_animal_prediction(self, animal):
        print("Making an animal prediction")
        if(animal.mix):
            mix = 'TRUE'
        else:
            mix = 'FALSE'

        instance = Instance(None, animal.animalType, animal.sex, animal.intact, animal.age, mix)

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../models/decisionTree.sav")
        model = Model.fromFile(path)

        return model.predict(instance)

if __name__ == '__main__':
    animal = Animal('Dog', 'Male', 'Intact', 1, 'TRUE')