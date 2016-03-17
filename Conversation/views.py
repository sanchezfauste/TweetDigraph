from django.shortcuts import render
from django.http import HttpResponse, Http404

from TwitterAPI.conversation import Conversation
from TwitterAPI.twitter_api import Twitter
from models import Tweet

def show(request, pk):
	try:
		root_tweet = Tweet.objects.get(pk=pk)
	except:
		raise Http404("This Conversation does not exist")
	return render(request, 'conversation.html',
				  {'root_tweet':root_tweet,
				  'replies':get_replies(root_tweet)})

def download(request, pk):
	conversation = Conversation(pk, Twitter().api, save_on_load=True)
	return HttpResponse("Imported!")

def get_conversation(root_tweet):
	stack = [(root_tweet, 0)]
	tweet = None
	conversation = []
	while (len(stack)):
		tweet = stack.pop()
		conversation.append(tweet)
		for reply in Tweet.objects.all().filter(in_reply_to_status_id=tweet[0].id):
				# (tweet, level)
			stack.append((reply, tweet[1] + 1))
	return conversation

def get_replies(root_tweet):
	replies = []
	conversation = get_conversation(root_tweet)
	for i in xrange(1, len(conversation)):
		actual_reply = conversation[i]
		next_reply = conversation[i+1] if i + 1 < len(conversation) else actual_reply
			# tweet, new_ul|close_li, close_n_ul_li
		replies.append((actual_reply[0],
				1 if next_reply[1] > actual_reply[1] else 0,
				range(actual_reply[1] - next_reply[1]) if actual_reply[1] - next_reply[1] > 0 else []))
	return replies
