import os
import json

class ConfigurationException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class Configuration():
	def __init__(self, filename):
		self.filename = filename
		self.json = None
		self.raw_format = None
		self.file = None

		self._load()

	def _load(self):
		if not (os.path.exists(self.filename)):
			raise ConfigurationException("File not found: " + self.filename)

		self.file = open(self.filename)
		self.raw_format = self.file.read()

		decoder = json.JSONDecoder()
		self.json = decoder.decode(self.raw_format)

		return True

	def __getitem__(self, index):
		return self.json[index]