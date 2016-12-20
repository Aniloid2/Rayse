
from music.models import UserProfile, TestUserProfile, FacebookProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm): #tick
  

    class Meta:
        model = User
        fields = ('username',)

class UserProfileForm(forms.ModelForm): #tick
	"""docstring for UserProfileForm"""
	class Meta:
		model= UserProfile
		fields= ('id', 'name', 'year_formed', 'webpull')




class TestUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)

class TestUserProfileForm(forms.ModelForm):
    class Meta:
        model = TestUserProfile
        fields = ('website',)


#facebook api linkage
class FacebookUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class FacebookProfileForm(forms.ModelForm):
    class Meta:
        model = FacebookProfile
        fields = ('id', 'name', 'year_formed', 'webpull',)