from sklearn import dummy
from sklearn import ensemble


class ClassifierParamProvider:
    def __init__(self):
        self.outcomeType = [
            # "All",
            "PosNeg"]
        self.classificationWeightFunctionMap = {
            # "All" : [None, 'balanced', {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 5, 'Died': 5}, {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 10, 'Died': 10}, {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 30, 'Died': 30}],
            "PosNeg": [None, 'balanced', {'Dead': 5, 'Alive': 1}, {'Dead': 10, 'Alive': 1}, {'Dead': 30, 'Alive': 1}]
        }
        self.extendedFeatureMap = {'primaryBreed': lambda instance: instance.getPrimaryBreed(),
                                   'secondaryBreed': lambda instance: instance.getSecondaryBreed(),
                                   'primaryColor': lambda instance: instance.getPrimaryColor(),
                                   'secondaryColor': lambda instance: instance.getSecondaryColor(),
                                   'primaryColorAddition': lambda instance: instance.getPrimaryColorAddition(),
                                   'secondaryColorAddition': lambda instance: instance.getSecondaryColorAddition()}

        self.extendedFeatureCombinations = {
            'allPrimaries': ['primaryBreed', 'primaryColor', 'primaryColorAddition'],
            'allExtendedFeatures': ['primaryBreed', 'primaryColor', 'primaryColorAddition', 'secondaryBreed',
                                    'secondaryColor', 'secondaryColorAddition'],
            'allBreedsAndColors': ['primaryBreed', 'primaryColor', 'secondaryBreed', 'secondaryColor'],
            'primaryBreedsAndColor': ['primaryBreed', 'primaryColor'],
            'primaryBreed': ['primaryBreed'],
            'primaryColor': ['primaryColor'],
            'basic': []
        }

        self.outComeFunctions = [
            # lambda instance: instance.getOutcome(),
            lambda instance: instance.getBinaryOutcome()]

    def getOutComeTypes(self):
        return self.outcomeType

    def getClassificationWeightFunctionMap(self):
        return self.classificationWeightFunctionMap

    def getExtendedFeatureMap(self):
        return self.extendedFeatureMap

    def getExtendedFeatureCombinations(self):
        return self.extendedFeatureCombinations

    # test this  + getClassifiers
    def getOutcomeFunctions(self):
        return self.outComeFunctions

    def getClassifiers(self, maxDepth, classificationWeight):
        return {
            # "decisionTree" : tree.DecisionTreeClassifier(class_weight=classificationWeight),
            "randomForest": ensemble.RandomForestClassifier(class_weight=classificationWeight,
                                                            max_depth=maxDepth),
            "dummyClassifier": dummy.DummyClassifier()}
