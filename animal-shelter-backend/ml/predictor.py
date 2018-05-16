class Predictor(object):
    def make_prediction(self, instance):
        print("wut")
        if (instance.feature1 > instance.feature2):
            return 1
        return 0

    def make_animal_prediction(self, animal):
        print("Making an animal prediction")
        if (animal.intact == True):
            return "Adoption"
        if (animal.age > 10):
            return "Died"
        if (animal.animalType == 'Dog'):
            return "Euthanasia"
        if (animal.sex == "Female"):
            return "Transfer"
        return "ReturnToOwner"
