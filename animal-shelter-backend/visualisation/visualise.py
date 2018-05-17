from os import listdir
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

if __name__ == '__main__':
	allFiles = listdir('../reports')
	recallList = []
	accuracyList = []
	precisionList = []
	summaryReport = open('../visualisation/summary.txt', 'w')
	for report in allFiles:
		if("PosNeg" in report):
			reportHandle = open('../reports/' + report, 'r')
			lines = reportHandle.readlines()
			precision = float(lines[3].split()[1])
			recall = float(lines[3].split()[2])
			accuracy = float(lines[7].split()[1])
			precisionList.append(precision)
			recallList.append(recall)
			accuracyList.append(accuracy)
			if(recall > 0.6 and accuracy > 0.6 and precision > 0.15):
				summaryReport.write(str(recall) + " " + str(accuracy) + " " + str(precision) + " " + report + "\n")
	plt.scatter(recallList, precisionList)
	plt.ylabel("Precision")

	# plt.scatter(recallList, accuracyList)
	# plt.ylabel("Accuracy")
	plt.xlabel("Recall")
	plt.xlim(0,1)
	plt.ylim(0,1)
	plt.show()



