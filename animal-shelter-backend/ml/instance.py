class Instance(object):
	def __init__(self, outcome, animalType, sex, intact, ageInYears, mix, primaryBreed, secondaryBreed, primaryColor,
				 secondaryColor, primaryColorAddition, secondaryColorAddition):
		self.outcome = outcome
		self.animalType = animalType
		self.sex = sex
		self.intact = intact
		self.ageInYears = ageInYears
		self.mix = int(mix == 'TRUE')
		self.primaryBreed = primaryBreed
		self.secondaryBreed = secondaryBreed
		self.primaryColor = primaryColor
		self.secondaryColor = secondaryColor
		self.primaryColorAddition = primaryColorAddition
		self.secondaryColorAddition = secondaryColorAddition

	def getOutcome(self):
		return self.outcome

	def getBinaryOutcome(self):
		if (self.outcome == 'Euthanasia' or self.outcome == 'Died'):
			return 'Dead'
		else:
			return 'Alive'

	def clearOutcome(self):
		self.outcome = None

	def getFeatures(self):
		return [hashFeature(self.animalType), hashFeature(self.sex), hashFeature(self.intact), self.ageInYears, self.mix]



	def getPrimaryBreed(self):
		return self.primaryBreed

	def getSecondaryBreed(self):
		return self.secondaryBreed

	def getPrimaryColor(self):
		return self.primaryColor

	def getSecondaryColor(self):
		return self.secondaryColor

	def getPrimaryColorAddition(self):
		return self.primaryColorAddition

	def getSecondaryColorAddition(self):
		return self.secondaryColorAddition

	def getExtendedFeatures(self, listOfExtendedFeatures):
		features = self.getFeatures()
		for feature in listOfExtendedFeatures:
			features.append(hashFeature(feature(self)))

		return features

	def __str__(self) -> str:
		return "{, outcome: " + str(self.outcome) \
			   + ", animalType: " + str(self.animalType) \
			   + ", sex: " + str(self.sex) \
			   + ", intact: " + str(self.intact) \
			   + ", ageInYears: " + str(self.ageInYears) \
			   + ", mix: " + str(self.mix) + "}"

def hashFeature(featureValue):
	if(featureValue == None):
		return None
	else:
		return hash(featureValue)