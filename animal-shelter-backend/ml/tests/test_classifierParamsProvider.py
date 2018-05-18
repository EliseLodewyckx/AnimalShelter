import unittest

from ml.classifierParamsProvider import ClassifierParamProvider

class ClassifierParamsProviderTest(unittest.TestCase):
    def setUp(self):
        self.paramProvider = ClassifierParamProvider()

    # test_ prefix is important to run the test
    def test_getOutComeTypes(self):
        self.assertEqual(self.paramProvider.getOutComeTypes(),
                         ['PosNeg'])

    def test_getClassificationWeightFunctionMap(self):
        self.assertEqual(self.paramProvider.getClassificationWeightFunctionMap(),
                         {"PosNeg": [None, 'balanced', {'Dead': 5, 'Alive': 1}, {'Dead': 10, 'Alive': 1},
                                     {'Dead': 30, 'Alive': 1}]
                          })

    def test_getExtendedFeatureMap(self):
        self.maxDiff = None

        result = self.paramProvider.getExtendedFeatureMap()

        self.assertCountEqual(result.keys(),
                              ['primaryBreed', 'secondaryBreed', 'primaryColor', 'secondaryColor',
                               'primaryColorAddition',
                               'secondaryColorAddition'])

        # Ways to assert lambda in values
        # self.assertCountEqual(result.values(), [lambda instance: instance.getPrimaryBreed(),
        #                                         lambda instance: instance.getSecondaryBreed(),
        #                                         lambda instance: instance.getPrimaryColor(),
        #                                         lambda instance: instance.getSecondaryColor(),
        #                                         lambda instance: instance.getPrimaryColorAddition(),
        #                                         lambda instance: instance.getSecondaryColorAddition()])

    def test_getExtendedFeatureCombinations(self):
        self.assertCountEqual(self.paramProvider.getExtendedFeatureCombinations(), {
            'allPrimaries': ['primaryBreed', 'primaryColor', 'primaryColorAddition'],
            'allExtendedFeatures': ['primaryBreed', 'primaryColor', 'primaryColorAddition', 'secondaryBreed',
                                    'secondaryColor', 'secondaryColorAddition'],
            'allBreedsAndColors': ['primaryBreed', 'primaryColor', 'secondaryBreed', 'secondaryColor'],
            'primaryBreedsAndColor': ['primaryBreed', 'primaryColor'],
            'primaryBreed': ['primaryBreed'],
            'primaryColor': ['primaryColor'],
            'basic': []
        })

    ## check equality lamda
    # def test_getOutcomeFunctions(self):
    #     self.assertIn(self.paramProvider.getOutcomeFunctions(), lambda instance: instance.getBinaryOutcome())

    def test_getClassifiers(self):
        result = self.paramProvider.getClassifiers(5, 1)
        self.assertCountEqual(result.keys(), ["randomForest", "dummyClassifier"])

