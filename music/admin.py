from django.contrib import admin
from music.models import UserProfile, TestUserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TestUserProfile)