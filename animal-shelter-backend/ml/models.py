import pickle

from sklearn import tree
from sklearn import ensemble
from sklearn import metrics

from datatransformation import fromCsv
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
		return Model(pickle.load(fileHandle))

	def predict(self, instance):
		return self.tree.predict([instance.getExtendedFeatures(self.extendedFeatureList)])[0]

	def store(self, filename):
		pickle.dump(self.tree, open(filename, 'wb'))


if __name__ == '__main__':
	instances = fromCsv.readCsv('../../data/train_preprocessed_split_mix_sex_color_breed.csv')
	trainSet, testSet = split(instances, 0.7)

	reportnames = ["none","balanced","5_1", "10_1", "30_1"]
	outcomeType = [
		# "All",
		"PosNeg"]
	classificationFunctionMap = {
		# "All" : [None, 'balanced', {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 5, 'Died': 5}, {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 10, 'Died': 10}, {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 30, 'Died': 30}],
		"PosNeg" : [None, 'balanced', {'Dead': 5, 'Alive': 1}, {'Dead': 10, 'Alive': 1}, {'Dead': 30, 'Alive': 1}]}
	extendedFeatureMap = {'primaryBreed': lambda instance: instance.getPrimaryBreed(),
						  'secondaryBreed': lambda instance: instance.getSecondaryBreed(),
						  'primaryColor': lambda instance: instance.getPrimaryColor(),
						  'secondaryColor': lambda instance: instance.getSecondaryColor(),
						  'primaryColorAddition': lambda instance: instance.getPrimaryColorAddition(),
						  'secondaryColorAddition': lambda instance: instance.getSecondaryColorAddition()}

	extendedFeatureCombinations = {
		'allPrimaries': ['primaryBreed', 'primaryColor', 'primaryColorAddition'],
		'allExtendedFeatures': ['primaryBreed', 'primaryColor', 'primaryColorAddition', 'secondaryBreed', 'secondaryColor', 'secondaryColorAddition'],
		'allBreedsAndColors': ['primaryBreed', 'primaryColor', 'secondaryBreed', 'secondaryColor'],
		'primaryBreedsAndColor': ['primaryBreed', 'primaryColor'],
		'primaryBreed': ['primaryBreed'],
		'primaryColor': ['primaryColor'],
		'basic': []
	}

	outcomeindex = 0
	for outcomeFunction in [
		# lambda instance: instance.getOutcome(),
		lambda instance: instance.getBinaryOutcome()]:

		nameindex = 0
		for classificationWeight in classificationFunctionMap[outcomeType[outcomeindex]]:
			for maxDepth in range(1, 5):
				classifiers = {
					# "decisionTree" : tree.DecisionTreeClassifier(class_weight=classificationWeight),
					"randomForest": ensemble.RandomForestClassifier(class_weight=classificationWeight, max_depth=maxDepth)}
				for classifierKey, classifierValue in classifiers.items():
					for extendedFeatureCombinationKey, extendedFeatureCombinationValue in extendedFeatureCombinations.items():
						print(str(classifierKey) + " " + str(maxDepth) + " " + extendedFeatureCombinationKey + " " + str(outcomeType[outcomeindex]) + " " + str(reportnames[nameindex]))
						modelTrain = ModelTrainer(trainSet)
						model = modelTrain.train(classifierValue, outcomeFunction, [extendedFeatureMap[feature] for feature in extendedFeatureCombinationValue])
						trueOutcomes = []
						predictedOutcomes = []
						for testInstance in testSet:
							trueOutcomes.append(outcomeFunction(testInstance))
							predictedOutcomes.append(model.predict(testInstance))

						reportFile = open('../reports/' + classifierKey + '_maxDepth' + str(maxDepth) + "_" + extendedFeatureCombinationKey + '_' + outcomeType[outcomeindex] + '_' + reportnames[nameindex] + '.txt', 'w')
						reportFile.write(metrics.classification_report(trueOutcomes, predictedOutcomes) + "\n")
						reportFile.write("accuracy: " + str(metrics.accuracy_score(trueOutcomes, predictedOutcomes)) + "\n")
						reportFile.write("confusion matrix:\n" + str(metrics.confusion_matrix(trueOutcomes, predictedOutcomes)))
						reportFile.close()
			nameindex += 1

		outcomeindex += 1
	# model.store('../models/decisionTree.sav')
