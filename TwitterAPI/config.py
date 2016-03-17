import ConfigParser
import os.path

class Config:

	def __init__(self, config_file = "config.ini"):
		if os.path.isfile(config_file):
			print("Loading config from file: " + config_file)
			self.load_config_file(config_file)
		else:
			print("Creating new config file on: " + config_file)
			print("Please edit config file and rerun the application.")
			self.create_config_file(config_file)
			exit(0)

	def load_config_file(self, config_file):
		config = ConfigParser.ConfigParser()
		config.read(config_file)
		self.consumer_key = config.get("Consumer", "consumer_key")
		self.consumer_secret = config.get("Consumer", "consumer_secret")

	def create_config_file(self, config_file):
		config_file = open(config_file, "w")
		config = ConfigParser.ConfigParser()
		config.add_section("Consumer")
		config.set("Consumer", "consumer_key")
		config.set("Consumer", "consumer_secret")
		config.write(config_file)
		config_file.close()
