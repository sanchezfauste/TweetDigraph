import tweepy
from config import Config

class Singleton(object):

	_instance = None
	
	def __new__(cls, *args, **kwargs):

		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)

		return cls._instance

class Twitter(Singleton):
	conf = Config("TwitterAPI/config.ini")
	auth = tweepy.OAuthHandler(conf.consumer_key,
			conf.consumer_secret)
	api = tweepy.API(auth)