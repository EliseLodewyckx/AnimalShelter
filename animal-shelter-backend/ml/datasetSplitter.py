def split(dataset, trainSetProportion):
	startIndexForTestSet = int(len(dataset) * (1 - trainSetProportion))
	trainSet = dataset[0:startIndexForTestSet]
	testSet = dataset[startIndexForTestSet:]
	return (trainSet, testSet)
