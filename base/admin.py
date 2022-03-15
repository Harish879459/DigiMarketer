from django.contrib import admin
from .models import Profile, Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profile)