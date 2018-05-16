import csv
from ml.instance import Instance

def readCsv(filename):
	instances = []
	with open(filename, 'r') as csvfile:
		train = csv.DictReader(csvfile, delimiter=';')
		for line in train:
			instance = Instance(line['OutcomeType'], line['AnimalType'], line['Sex'], line['Intact'], line['AgeInYears'], line['Mix'])
			instances.append(instance)

	return instances

if __name__ == '__main__':
    readCsv('../../data/train_removeColumns_mix.csv')
