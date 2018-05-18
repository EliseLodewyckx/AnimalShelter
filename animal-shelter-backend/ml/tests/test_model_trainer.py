import unittest

import numpy
from sklearn import dummy

from ml.models import ModelTrainer, Model
from ml.instance import Instance


class ModelTrainterTest(unittest.TestCase):
    print("Here should be a test")

    ## Look at how to define the values
    # def test_train(self):
    #     classifier = dummy.DummyClassifier()
    #     treeModel = classifier
    #     featureList = [object]
    #     treeModel.fit(numpy.reshape(featureList, (1, -1)), [])
    #
    #     self.assertEqual(
    #         ModelTrainer([self.create_empty_instance(), self.create_empty_instance()]).train(classifier, lambda instance: instance.getPrimaryBreed(),
    #                                                                                          featureList),
    #                      Model(tree="", extendedFeatureList=featureList))


    def create_empty_instance(self):
        return Instance("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l")
