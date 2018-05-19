import unittest
import os

from unittest.mock import MagicMock
from ml.classifierParamsProvider import ClassifierParamProvider
from sklearn import dummy

from ml.models import generateReportName, reportToFile, generateReports


class ClassifierParamsProviderTest(unittest.TestCase):
    def setUp(self):
        classifierKey = "Classifier"
        maxDepth = 5
        extendedFeatureCombinationKey = "Everything"
        outcomeTypes = ["AliveDead"]
        chosenWeights = ["10_0"]
        outcomeindex = 0
        nameindex = 0

        self.report_name = generateReportName(classifierKey, maxDepth, extendedFeatureCombinationKey,
                                              outcomeTypes,
                                              chosenWeights,
                                              outcomeindex, nameindex)

    def test_generateReportName(self):
        self.assertEqual(self.report_name, "Classifier_maxDepth5_Everything_AliveDead_10_0")

    def test_reportToFile(self):
        print("Assert file created")

        reportToFile(['1', '2', '1'], self.report_name, "", ['1', '2', '1'])

        self.assertTrue(os.path.exists(self.report_name + ".txt"))

        os.remove(self.report_name + ".txt")

    def test_generateReport(self):
        paramProvider = ClassifierParamProvider()

        paramProvider.getChosenWeights = MagicMock(return_value=["balanced"])
        paramProvider.getOutComeTypes = MagicMock(return_value=["PosNeg"])
        paramProvider.getClassificationWeightFunctionMap = MagicMock(return_value={"PosNeg": ['balanced']})
        paramProvider.getExtendedFeatureMap = MagicMock(
            return_value={'primaryBreed': lambda instance: instance.getPrimaryBreed()})
        paramProvider.getExtendedFeatureCombinations = MagicMock(return_value={'primaryBreed': ['primaryBreed']})
        paramProvider.getClassifiers = MagicMock(return_value={"dummyClassifier": dummy.DummyClassifier()})
        paramProvider.getMaxDepthRange = MagicMock(return_value= range(1,2))

        reportPath = "reports/"
        generateReports("./data/first_items_from_train_data_to_test.csv", reportPath, paramProvider)

        self.assertTrue(os.path.exists(reportPath + "dummyClassifier_maxDepth1_primaryBreed_PosNeg_balanced.txt"))
        self.assertEqual(len(os.listdir(reportPath)), 1)
        os.remove(reportPath + "dummyClassifier_maxDepth1_primaryBreed_PosNeg_balanced.txt")
        self.assertFalse(os.listdir(reportPath))

