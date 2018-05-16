import pickle

from sklearn import tree

from datatransformation import fromCsv
from ml.datasetSplitter import split


class ModelTrainer(object):

	def __init__(self, trainData):
		self.trainData = trainData

	def train(self):
		features = [instance.getFeatures() for instance in self.trainData]
		outcomes = [instance.getOutcome() for instance in self.trainData]
		treeModel = tree.DecisionTreeClassifier()
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
		print(str(instance))
		return self.tree.predict([instance.getFeatures()])[0]

	def store(self, filename):
		pickle.dump(self.tree, open(filename, 'wb'))


if __name__ == '__main__':
	instances = fromCsv.readCsv('../../data/train_preprocessed.csv')
	trainSet, testSet = split(instances, 0.7)
	modelTrain = ModelTrainer(trainSet)
	model = modelTrain.train()
	for testInstance in testSet:
		testInstance.clearOutcome()
		print(str(testInstance) + " " + model.predict(testInstance))
	model.store('../models/decisionTree.sav')
