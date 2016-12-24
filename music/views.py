from django.shortcuts import render, get_object_or_404, render_to_response
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Album, Song, Album2, Artist, Artistform
import random

from .forms import UserForm, UserProfileForm, TestUserForm, TestUserProfileForm, FacebookUserForm, FacebookProfileForm

from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
import re


from django.http import Http404
from django.contrib.auth.decorators import login_required

import json


from django.contrib.auth import authenticate, login, logout


def index(request):
	all_albums = Album.objects.all()
	html = ''
	for album in all_albums:
		url = '/music/' + str(album.id) + '/'
		html += '<a href="' + url + '">' + album.album_title +  '</a><br>'
	return HttpResponse(html)

def detail(request, album_id):
	return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")


def index2(request):
	all_albums = Album.objects.all()
	context = {
		'all_albums':all_albums,
	}
	return render(request, 'index2.html', context)  ##with render shortcut

def detail2(request, album_id):
	album = get_object_or_404(Album, id=album_id)
	return render(request, 'detail.html', {'album':album})



def favorite(request, album_id):
	album = get_object_or_404(Album, id=album_id)
	try:
		selected_song = album.song_set.get(id=request.POST['song'])
	except:
		return render(request, 'detail.html', {
			'album':album, 
			'error_message': "You did not select a valid song",
			})

	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'detail.html', {'album':album})




def create(request):
	if request.method == "GET":
		form = Artistform()
		return render(request, 'create.html', { 'form' : form })
	elif request.method == "POST":
		
		##### getting items from post request
		request_dict = request.POST.dict()
		print request_dict
		for key,value in request_dict.iteritems():
			print key, value
		#####################################



		form = Artistform(request.POST, request.FILES)
		
		form.save(commit = False)

		#form.picture_of_artist = request.FILES['picture_of_artist']
		#print form.picture_of_artist

		form.save()


		return HttpResponseRedirect('/music/artists/')



def home(request):





	if request.method == "GET":
		users = FacebookProfile.objects.all()
		total_users = users.count()

		ids =[]
		for item in users:
			id_ = item.id

			ids.append(id_)

		ids_shuffled = random.sample(ids, 3)



		user_1 = FacebookProfile.objects.get(pk = ids_shuffled[0])
		user_2 = FacebookProfile.objects.get(pk = ids_shuffled[1])
		user_3 = FacebookProfile.objects.get(pk = ids_shuffled[2])

		#we need to do a test to see if what is passed is profile
		#I think it is . this neasn we can call by profile.user.name

	


		#we are passing the object of eeach user . for name we need to dive ddeper
		#

		return render(request, 'Homepage.html', { 'total_users' : total_users, 'user_1':user_1, 'user_2': user_2,\
			'user_3':user_3})



	if request.method == "POST":
	
		user_1 = request.POST.get('user_1')
		user_2 = request.POST.get('user_2')
		user_3 = request.POST.get('user_3')
		left_most_liked = [user_1, user_2, user_3]

		score = 3
		for item in left_most_liked:
			user =  Artist.objects.get(pk = item)
			user.score += score
			score -= 1
			user.times_called +=1
			user.level = float(user.score)/float(user.times_called)
			print user.name, user.score, user.times_called, user.level
			user.save()

		return HttpResponseRedirect('/music/home/')




def artistdetails(request, id):
	artists = Artist.objects.get(pk = id)
	if request.method == "POST":
		print 'detecting POST'
		if request.POST.get('delete'):
			print 'Found item in POST'
			is_it_true = request.POST.get('delete')
			print 'we have a delete'
			if is_it_true == 'True':
				print 'i want to delete'
				artist = Artist.objects.get(pk = id)
				artist.delete()
				return HttpResponseRedirect('/music/artists/')


	return render(request, 'artistdetaisl.html' , {'artists' : artists})

def artist(request):

	artists = Artist.objects.all();
	return render_to_response('artist.html', {'artists': artists} );


	#return HttpResponse('<html><head><title>Heloow!</title><body><h1>HII</h1></body></head></html>');

#@csrf_exempt
def test(request):
	if request.method == "GET":
		return render(request, 'base.html')

	if request.method == "POST":

		time = request.POST.get('time')
		series_position = request.POST.getlist('series_pos[]')
		user_1 = request.POST.get('user_1')
		user_2 = request.POST.get('user_2')
		user_3 = request.POST.get('user_3')
		print user_1, user_2, user_3
		#print time, series_position
		#return render(request, 'base.html')
		return HttpResponseRedirect('/music/test/')


@csrf_exempt
def asynctest(request):
	if request.method == "GET":
		
		numb = 1
		return render(request, 'Asyncronoysdata.html', {'numb': numb})
	if request.method == "POST" and request.is_ajax():
		print 'hi'
		numb = int(request.POST.get('numb'))
		print numb, type(numb)
		numb = numb +  1

		print numb
		return HttpResponse(json.dumps({'numb': numb}), content_type="application/json")


def king(request):
	if request.method == 'GET':
		users = Artist.objects.all()
		list_users = []
		for item in users:
			list_users.append(item)



		for passnum in range(len(list_users)-1,0,-1):
			for i in range(passnum):
				if list_users[i].level>list_users[i+1].level:
					temp = list_users[i]
					list_users[i] = list_users[i+1]
					list_users[i+1] = temp
		
	

		winner = list_users.pop()
		print winner.name
		return render(request, "king.html", {'winner': winner})





def log(request):
	if request.method == 'GET':

		return render(request, "log.html")
	if request.method == "POST":

	
		name = request.POST.get('name')
		id_ = request.POST.get('id')
		birthday = request.POST.get('year_formed')
		webpull = request.POST.get('webpull')

		returned_users = Artist.objects.filter(id = id_)
		if returned_users.count() == 0:
			print 'This user has no account'
			if birthday == "undefined":
				print 'im emplty'	
				year_formed = random.randint(1993,1998)
			else:
				year_formed = re.findall(r"[0-9][0-9][0-9][0-9]$", birthday)[0]
			
			new_art = Artist.create(id_, name, year_formed, webpull)

			print new_art.id, new_art.name, new_art.year_formed, new_art.webpull
			new_art.save()
	
		elif returned_users.count() >0:
			print 'actualy has account'


		return HttpResponseRedirect('/music/home/')


def cooktest(request):
	if request.method == 'GET':
		#request.session.set_test_cookie()

		return_headder =  render(request, "Cookiestest.html")
		return_headder.set_cookie('visits', 0)
		

		return return_headder
		
	
def cooktest2(request):
	if request.method == "GET":
		cook = int(request.COOKIES['visits'])
		print cook
		return_headder = render(request, "cookiestest2.html")
		return_headder.set_cookie('visits', cook + 1)


		#if request.session.test_cookie_worked():
			# print ">> Test succes"
			# print request.COOKIES
			# request.session.delete_test_cookie()
		return return_headder

def cooktest3(request):
	if request.method == "GET":
		cook = int(request.COOKIES['visits'])
		print cook
		return_headder = render(request, "cookiestest3.html")
		return_headder.set_cookie('visits', cook + 1)

		## at log store id of user in cookie and carry to home,
		# at home if_auth is not true return to log if true procede
		
		return return_headder




### User Profile improoved test ### 



def logV2(request):
	if request.method == 'GET':
		print 'im here'

		return render(request, "logV2.html")
	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		print first_name, last_name

		facebook_user = FacebookUserForm(data=request.POST)
		facebook_profile = FacebookProfileForm()

		has_account = authenticate(first_name = first_name, last_name = last_name)

		if has_account:
			print 'this has account'
			login(request, has_account)
			return HttpResponseRedirect('/music/home/')
		else:
			id_ = request.POST.get('id')
			year_formed = request.POST.get('year_formed')
			webpull = request.POST.get('webpull')

			print id_, year_formed, webpull

			print facebook_user

			user = facebook_user.save()
			profile = facebook_profile.save(commit = False)
			profile.user = user
			profile.webpull = webpull
			profile.id = id_

			## steal birtday fucntion from log 
			# move to new database facebook (neeed to change all artists to facebookprofile)
			profile.year_formed = year_formed
			profile.save()
			
			

			#authenticate user. then log him in.
			#user = authenticate(username = profile.user.username)
			now_has_account = authenticate(first_name = first_name, last_name = last_name)
			login(request, now_has_account)


			#profile.save()
			return HttpResponseRedirect('/music/home/')






		#what we want to do is..
		#initialise the form.
		#get all values from form raw
		#have to save the forms. especialy user one
		#link userform to profile


		


def logV3(request):
	registered = False
	if request.method == 'POST':
		#create a form object
		user_form = TestUserForm(data=request.POST)
		profile_form = TestUserProfileForm()
		print user_form
		#get rawvalues or data= to save directly
		username = request.POST.get("username")
		website = request.POST.get('website')

		#Must save object to database first
		user = user_form.save()
		#we can change the username
		user.username = username
		print user.username
		print 'Username changed:', user.username
		#but then we must save
		user.save()
		profile = profile_form.save(commit=False)
		#put user fields in profile
		profile.user = user
		#can be done before initial save
		profile.save()
		print 'profile website: ',profile.website
		print 'username form profile:', profile.user.username
		profile.website = website
		print 'Website changed :', profile.website
		#but again if parameters changed they must be resaved
		profile.save()

		registered = True

	else:
		print 'this is form generation'
		user_form = TestUserForm()
		print 'this is the user form', user_form
		profile_form = TestUserProfileForm()


	return render(request,
	            'logV3.html',
	            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



def user_login(request):
    # Like before, obtain the context for the user's request.
    #context = RequestContext(request)
    # print context

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get('username')
        print username
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
       
        user = authenticate(username=username)

        #have to go backwords in the model to get profilefields
        
        profile = user.testuserprofile
        print profile.website


        login(request, user)
        
        return render(request, "login_try_view.html")
    if request.method == 'GET':
    	print 'im here'
    	return render(request, "login_try_view.html")





def logout_try(request):
	if request.user.is_authenticated():
		logout(request)
		
	return render(request, "login_try_view.html")
