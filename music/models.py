#from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length = 250)
	genre= models.CharField(max_length = 250)
	album_logo = models.CharField(max_length = 1000)
	def __str__(self):
		return self.album_title + '-' +self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_title = models.CharField(max_length = 250)
	song_title = models.CharField(max_length = 250)
	is_favorite = models.BooleanField(default = False)

	def __str__(self):
		return self.song_title

#### microsoft tutorial

class Artist(models.Model):
	id = models.PositiveIntegerField(primary_key = True)
	name = models.CharField(max_length=50, null = True)
	year_formed = models.PositiveIntegerField(default = 0)
	delete_db = models.BooleanField(default = False)
	webpull= models.CharField(max_length =1000, null = True)
	#picture_of_artist = models.ImageField(upload_to = 'static/Artists/' , null= True, blank=True)
	score = models.PositiveIntegerField(default = 0, editable = True)
	times_called = models.PositiveIntegerField(default = 0, editable = True)
	level = models.FloatField(default = 0, editable =True)

	@classmethod
	def create(cls, id_, name, year_formed, webpull):
		book = cls(id = id_, name = name, year_formed = year_formed, webpull= webpull)
		return book





class Artistform(ModelForm):
	class Meta:
		model = Artist;
		fields = ['name', 'year_formed', 'webpull']


class Profileform(ModelForm):
	class Meta:
		model = Artist;
		fields = ['id','name', 'webpull']



class Album2(models.Model):
	name = models.CharField("album", max_length = 50)
	artist = models.ForeignKey(Artist)


#### User Profiles ###

class UserProfile(models.Model): #tick

	user = models.OneToOneField(User)

	id = models.PositiveIntegerField(primary_key = True)
	name = models.CharField(max_length = 200, null = True)
	year_formed = models.PositiveIntegerField(default = 0)
	webpull= models.CharField(max_length =1000, null = True)


	# @classmethod
	# def create(self, id_, name, year_formed, webpull):
	# 	self.id = id_
	# 	self.year_formed = year_formed
	# 	self.webpull = webpull
	
	# 	print 'updated'



class TestUserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.CharField( max_length= 300, blank=True)
    

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


#user profiles not a Test
class FacebookProfile(models.Model):
	user = models.OneToOneField(User)


	id = models.PositiveIntegerField(primary_key = True)
	name = models.CharField(max_length = 200, null = True)
	year_formed = models.PositiveIntegerField(default = 0)
	webpull= models.CharField(max_length =1000, null = True)