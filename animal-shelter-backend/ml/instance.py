class Instance(object):

	def __init__(self, outcome, animalType, sex, intact, ageInYears, mix):
		self.outcome = outcome
		self.animalType = animalType
		self.sex = sex
		self.intact = intact
		self.ageInYears = ageInYears
		self.mix = int(mix == 'TRUE')

	def getOutcome(self):
		return self.outcome

	def clearOutcome(self):
		self.outcome = None

	def getFeatures(self):
		return [hash(self.animalType), hash(self.sex), hash(self.intact), self.ageInYears, self.mix]


	def __str__(self) -> str:
		return "{, outcome: " + str(self.outcome) + ", animalType: " + str(self.animalType) + ", sex: " + str(self.sex) + ", intact: " + str(self.intact) + ", ageInYears: " + str(self.ageInYears) + ", mix: "+ str(self.mix) + "}"