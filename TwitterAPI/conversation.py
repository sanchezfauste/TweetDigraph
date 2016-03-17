from bs4 import BeautifulSoup
import requests

from Conversation.models import Tweet
from django.utils import timezone

class Conversation:

	def __init__(self, root_status_id, tweepy_api, verbose = False, save_on_load = False):
		self.root_conv_node = ConversationNode(
				tweepy_api.get_status(root_status_id))
		self.tweepy_api = tweepy_api
		self.verbose = verbose
		self.save_on_load = save_on_load
		#self.get_status_replies_recursive(self.root_conv_node)
		self.get_status_replies_iterative()

	def get_status_replies_recursive(self, conv_node):
		if self.verbose: conv_node.show()
		if self.save_on_load: conv_node.save()
		for status_id in conv_node.get_replies_ids():
			reply_status = self.tweepy_api.get_status(status_id)
			if reply_status.in_reply_to_status_id == conv_node.status.id:
				reply_conv_node = conv_node.add_reply(reply_status)
				self.get_status_replies_revursive(reply_conv_node)

	def get_status_replies_iterative(self):
		stack = [self.root_conv_node]
		while (len(stack)):
			conv_node = stack.pop()
			if self.verbose: conv_node.show()
			if self.save_on_load: conv_node.save()
			for status_id in conv_node.get_replies_ids():
				reply_status = self.tweepy_api.get_status(status_id)
				if reply_status.in_reply_to_status_id == conv_node.status.id:
					reply_conv_node = conv_node.add_reply(reply_status)
					stack.append(reply_conv_node)

	def show(self):
		self.root_conv_node.show_conversation()

	def save(self):
		self.root_conv_node.save_conversation()

class ConversationNode:

	def __init__(self, status, level = 0):
		self.status = status
		self.replies = []
		self.level = level

	def add_reply(self, status):
		reply = ConversationNode(status, self.level + 1)
		self.replies.append(reply)
		return reply

	def save(self):
		tweet = Tweet(id = self.status.id,
				username = self.status.user.screen_name,
				display_name = self.status.user.name,
				profile_image_url = self.status.user.profile_image_url,
				created_at = timezone.now(),
				text = self.status.text,
				retweet_count = self.status.retweet_count,
				favourites_count = self.status.favorite_count)
		try:
			if self.status.in_reply_to_status_id:
				tweet.in_reply_to_status_id = Tweet.objects.get(pk=self.status.in_reply_to_status_id)
		except:
			pass
		tweet.save()

	def save_conversation(self):
		self.save()
		for reply in self.replies:
			reply.save_conversation()

	def show(self):
		print "  " * self.level + self.status.text

	def show_conversation(self):
		self.show()
		for reply in self.replies:
			reply.show_conversation()

	def get_replies_ids(self):
		url = "https://twitter.com/" + self.status.user.screen_name \
				+ "/status/" + str(self.status.id)
		req = requests.get(url)
		if req.status_code == 200:
			html = BeautifulSoup(req.text, 'html.parser')
			conversations = html.find_all('li', {'class':'ThreadedConversation'})
			conversations += html.find_all('div', \
					{'class':'ThreadedConversation--loneTweet'})
			replies = []
			for conversation in conversations:
				first_tweet = conversation.find('li', {'class':'js-stream-item ' \
						+ 'stream-item stream-item expanding-stream-item\n'})
				replies.append(first_tweet.get('data-item-id'))
			return replies
		else:
			print "Error getting status replies ids. HTTP status:", req.status_code
			return list()
