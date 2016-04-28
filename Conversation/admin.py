from django.contrib import admin
from .models import Tweet, UserConversation

admin.site.register(Tweet)
admin.site.register(UserConversation)
