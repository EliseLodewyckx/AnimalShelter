import pickle

from sklearn import tree
from sklearn import metrics

from datatransformation import fromCsv
from ml.datasetSplitter import split


class ModelTrainer(object):

	def __init__(self, trainData):
		self.trainData = trainData

	def train(self, classificationWeight):
		features = [instance.getFeatures() for instance in self.trainData]
		outcomes = [instance.getOutcome() for instance in self.trainData]
		# treeModel = tree.DecisionTreeClassifier(class_weight='balanced')
		treeModel = tree.DecisionTreeClassifier(class_weight=classificationWeight)
		treeModel.fit(features, outcomes)
		return Model(treeModel)

class Model(object):

	def __init__(self, tree):
		self.tree = tree

	@classmethod
	def fromFile(cls, filename):
		fileHandle = open(filename, 'rb')
		return Model(pickle.load(fileHandle))

	def predict(self, instance):
		return self.tree.predict([instance.getFeatures()])[0]

	def store(self, filename):
		pickle.dump(self.tree, open(filename, 'wb'))


if __name__ == '__main__':
	instances = fromCsv.readCsv('../../data/train_preprocessed_1_split_mix_and_sex.csv')
	trainSet, testSet = split(instances, 0.7)

	reportnames = ["none","balanced","5_1", "10_1"]
	nameindex = 0
	for classificationWeight in [None, 'balanced', {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 5, 'Died': 5}, {'Return_to_owner': 1, 'Adoption': 1, 'Transfer': 1, 'Euthanasia': 10, 'Died': 10}]:
		modelTrain = ModelTrainer(trainSet)
		model = modelTrain.train(classificationWeight)
		trueOutcomes = []
		predictedOutcomes = []
		for testInstance in testSet:
			trueOutcomes.append(testInstance.getOutcome())
			predictedOutcomes.append(model.predict(testInstance))

		reportFile = open('../reports/decisionTree_' + reportnames[nameindex] + '.txt', 'w')
		nameindex += 1
		reportFile.write(metrics.classification_report(trueOutcomes, predictedOutcomes) + "\n")
		reportFile.write("accuracy: " + str(metrics.accuracy_score(trueOutcomes, predictedOutcomes)) + "\n")
		reportFile.write("confusion matrix:\n" + str(metrics.confusion_matrix(trueOutcomes, predictedOutcomes)))
		reportFile.close()
	# model.store('../models/decisionTree.sav')
