from django.contrib import admin
from .models import Profile, AddContent, Like, Chat

admin.site.register(Profile)
admin.site.register(AddContent)
admin.site.register(Like)
admin.site.register(Chat)

