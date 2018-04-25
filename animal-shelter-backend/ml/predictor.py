

class Predictor(object):

	def make_prediction(self, instance):
		print("wut")
		if(instance.feature1 > instance.feature2):
			return 1
		return 0
