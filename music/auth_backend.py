from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class PasswordlessAuthBackend(ModelBackend):

	def authenticate(self, username = None):
		try:
			return User.objects.get(username = username)
		except:
			return None
    		
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except :
			return None


class OnlynameandsurnameAuth(ModelBackend):
	def authenticate(self, first_name = None, last_name = None):
		try:
			return User.objects.get(first_name = first_name, last_name = last_name)
		except:
			return None

#authenticate with first and last name, when recive username split with regex 
#at space, now have a list. first parameter in first name, second in last_name

#is auth recives both first and last name

#chance usermodel to only have name and surname. 