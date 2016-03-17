from __future__ import unicode_literals

from django.db import models

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

	def __str__(self):
		return str(self.id)
