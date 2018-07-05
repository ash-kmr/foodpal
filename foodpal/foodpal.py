import requests

class FoodPal(object):
	def __init__(self):
		self.apikey = None
		self.predictionUrl = 'http://0.0.0.0:8000/requestclassify/'
		self.checkapikey = 'http://0.0.0.0:8000/checkapikey/'
		self.callsleft = 'http://0.0.0.0:8000/callsleft/'
		self.data = {}
		pass


	def getDishList(self):
		pass

	def getPrediction(self, filepath):
		"""
		Function to get the prediction for a particular image.
		
		Inputs:
			filepath : path of the image file

		Outputs:
			response : JsonResponse containing the predictions.
		"""
		imageFile = open(filepath, 'rb')
		read = imageFile.read()
		imageBytes = bytearray(read)
		files = {'image': imageBytes}
		response = requests.post(url=self.predictionUrl, data=self.data, files=files)
		return response.json()

	def setApiKey(self, apikey):
		"""
		function to set the api key as one of the variables of
		class. It also verifies whether the given api is valid
		or not.

		Inputs:
			key : Apikey

		Outputs:
			None
		"""
		data = {'apikey':apikey}
		response = requests.post(url=self.checkapikey, data=data)
		assert response.json()['response'] == 'valid', "Error: Apikey not set"
		self.apikey = apikey
		self.data = data
		return True

	def getCallsLeft(self):
		"""
		function to tell the user how many api calls are left
		for the day.

		Inputs:
			None

		Outputs:
			calls : Number of calls left
		"""
		assert self.apikey != None, 'Apikey not set'
		response = requests.post(url=self.callsleft, data=self.data)
		return response.json()['response']


