from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):

	id = models.BigIntegerField(primary_key=True)
	username = models.CharField(max_length=30)
	display_name = models.CharField(max_length=30)
	profile_image_url = models.URLField()
	created_at = models.DateTimeField()
	text = models.TextField()
	in_reply_to_status_id = models.ForeignKey("self", blank=True, null=True)
	retweet_count = models.IntegerField()
	favourites_count = models.IntegerField()
	sentiment = models.IntegerField(default=0)
	lang = models.CharField(max_length=10)

	def __str__(self):
		return str(self.id)

class UserConversation(models.Model):

	root_tweet = models.ForeignKey(Tweet)
	user = models.ForeignKey(User, default=1)
	def __unicode__(self):
		return str(self.root_tweet.id)
	def get_absolute_url(self):
		return "/conversation/" + str(self.root_tweet.id)
