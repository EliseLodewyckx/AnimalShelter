def split(dataset, trainSetProportion):
	startIndexForTestSet = int(len(dataset) * trainSetProportion)
	trainSet = dataset[0:startIndexForTestSet]
	testSet = dataset[startIndexForTestSet:]
	return (trainSet, testSet)
