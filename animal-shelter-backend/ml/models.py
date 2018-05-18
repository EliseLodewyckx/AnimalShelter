import pickle

from sklearn import metrics
from sklearn import tree

from datatransformation import fromCsv
from ml.classifierParamsProvider import ClassifierParamProvider
from ml.datasetSplitter import split


class ModelTrainer(object):
    def __init__(self, trainData):
        self.trainData = trainData

    def train(self, classifier, outcomeFunction, extendedFeatureList):
        features = [instance.getExtendedFeatures(extendedFeatureList) for instance in self.trainData]
        outcomes = [outcomeFunction(instance) for instance in self.trainData]
        treeModel = classifier
        treeModel.fit(features, outcomes)
        return Model(treeModel, extendedFeatureList)


class Model(object):
    def __init__(self, tree, extendedFeatureList):
        self.tree = tree
        self.extendedFeatureList = extendedFeatureList

    @classmethod
    def fromFile(cls, filename):
        fileHandle = open(filename, 'rb')
        return Model(pickle.load(fileHandle), [])

    def predict(self, instance):
        return self.tree.predict([instance.getExtendedFeatures(self.extendedFeatureList)])[0]

    def visualise(self):
        tree.export_graphviz(self.tree, out_file='../visualisation/tree.dot')

    def store(self, filename):
        pickle.dump(self.tree, open(filename, 'wb'))


def generateReports(csv_train_data, reportPath):
    instances = fromCsv.readCsv(csv_train_data)
    trainSet, testSet = split(instances, 0.7)
    chosenWeights = ["none", "balanced", "5_1", "10_1", "30_1"]

    paramProvider = ClassifierParamProvider()
    outcomeTypes = paramProvider.getOutComeTypes()
    classificationWeightFunctionMap = paramProvider.getClassificationWeightFunctionMap()
    extendedFeatureMap = paramProvider.getExtendedFeatureMap()
    extendedFeatureCombinations = paramProvider.getExtendedFeatureCombinations()

    outcomeindex = 0

    for outcomeFunction in paramProvider.getOutcomeFunctions():
        nameindex = 0
        for classificationWeight in classificationWeightFunctionMap[outcomeTypes[outcomeindex]]:
            for maxDepth in range(1, 5):
                classifiers = paramProvider.getClassifiers(maxDepth, classificationWeight)
                for classifierKey, classifierValue in classifiers.items():
                    create_and_test_model(reportPath, chosenWeights, classifierKey, classifierValue,
                                          extendedFeatureCombinations, extendedFeatureMap, maxDepth,
                                          nameindex, outcomeFunction, outcomeTypes, outcomeindex, testSet,
                                          trainSet)
            nameindex += 1

        outcomeindex += 1


def create_and_test_model(reportPath, chosenWeights, classifierKey, classifierValue, extendedFeatureCombinations,
                          extendedFeatureMap, maxDepth, nameindex, outcomeFunction, outcomeTypes,
                          outcomeindex, testSet, trainSet):
    for extendedFeatureCombinationKey, extendedFeatureCombinationValue in extendedFeatureCombinations.items():
        reportName = generateReportName(classifierKey, maxDepth, extendedFeatureCombinationKey, outcomeTypes,
                                        chosenWeights, outcomeindex, nameindex)
        print(reportName)
        model = train_model(classifierValue, extendedFeatureCombinationValue, extendedFeatureMap, outcomeFunction,
                            trainSet)

        test_model(model, outcomeFunction, reportName, reportPath, testSet)


def test_model(model, outcomeFunction, reportName, reportPath, testSet):
    trueOutcomes = []
    predictedOutcomes = []
    for testInstance in testSet:
        trueOutcomes.append(outcomeFunction(testInstance))
        predictedOutcomes.append(model.predict(testInstance))
    reportToFile(predictedOutcomes, reportName, reportPath, trueOutcomes)


def train_model(classifierValue, extendedFeatureCombinationValue, extendedFeatureMap, outcomeFunction, trainSet):
    modelTrain = ModelTrainer(trainSet)
    model = modelTrain.train(classifierValue, outcomeFunction,
                             [extendedFeatureMap[feature] for feature in
                              extendedFeatureCombinationValue])
    return model


def reportToFile(predictedOutcomes, reportName, reportPath, trueOutcomes):
    reportFile = open(reportPath + reportName + '.txt', 'w')
    reportFile.write(metrics.classification_report(trueOutcomes, predictedOutcomes) + "\n")
    reportFile.write(
        "accuracy: " + str(metrics.accuracy_score(trueOutcomes, predictedOutcomes)) + "\n")
    reportFile.write(
        "confusion matrix:\n" + str(metrics.confusion_matrix(trueOutcomes, predictedOutcomes)))
    reportFile.close()


def generateReportName(classifierKey, maxDepth, extendedFeatureCombinationKey, outcomeTypes, chosenWeights,
                       outcomeindex, nameindex):
    return str(classifierKey) + \
           "_maxDepth" + str(maxDepth) + \
           "_" + extendedFeatureCombinationKey + \
           "_" + str(outcomeTypes[outcomeindex]) + "_" + str(chosenWeights[nameindex])


def generateModel():
    instances = fromCsv.readCsv('../../data/train_preprocessed_split_mix_sex_color_breed.csv')
    trainSet, testSet = split(instances, 0.7)

    modelTrain = ModelTrainer(trainSet)
    model = modelTrain.train(tree.DecisionTreeClassifier(class_weight='balanced'),
                             lambda instance: instance.getBinaryOutcome(), [])
    model.visualise()
    model.store('../models/decisionTree.sav')


if __name__ == '__main__':
    # generateModel()
    generateReports('../../data/train_preprocessed_split_mix_sex_color_breed.csv', "../reports/")
