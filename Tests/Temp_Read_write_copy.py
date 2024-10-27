import json
from abc import ABC,abstractmethod

class ReadWrite(ABC):
	@abstractmethod
	def read(self, fileName):
		pass
	@abstractmethod
	def write(self, fileName, text):
		pass
	@abstractmethod
	def reset(self, fileName):
		pass
class JsonReadWrite(ReadWrite):
	@staticmethod
	def read(fileName):
		try:
			with open(fileName, "r") as file:
				return json.load(file)
		except:
			return([])

	@staticmethod
	def write(fileName, data):

		try:
			with open(fileName, "w") as file:
				json.dump(data,file)
			return True
		except:
			pass
		return False

	@staticmethod
	def reset(fileName):
		try:
			with open(fileName, "w") as file:
				file.write("{}")
			return True
		except:
			pass
