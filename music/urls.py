from django.conf.urls import url
# from django.contrib import admin


from . import views

app_name = 'music'

urlpatterns = [
    #url(r'^$', views.index, name = 'index'), 
    url(r'^$', views.index2, name = 'index2'),
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail2, name='detail2'),


    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    ## microsoft tutorial

   	url(r'^artist/(?P<id>[0-9]+)/$', views.artistdetails, name = 'artistdetails'),
   	url(r'^artists/$', views.artist, name = 'artists'),

   	## user input create form ##
   	url(r'^create/$', views.create, name  = 'create'),
    ## home page with girls
    url(r'^home/$', views.home , name = 'home'),
    url(r'^test/$', views.test, name ='test'),
    url(r'^asynctest/$', views.asynctest, name = 'asynctest'),
    url(r'^king/$', views.king, name = 'king'),
    url(r'^log/$', views.log, name= 'log'),
    url(r'^cookietest/$', views.cooktest, name='cooktest'),
    url(r'^cookietest2/$', views.cooktest2, name='cooktest2'),
    url(r'^cookietest3/$', views.cooktest3, name='cooktest3'),

    ## user profile improoved test ### 
    url(r'^logV2/$', views.logV2, name='logV2'),
    ## test user log in 
    url(r'^logV3/$', views.logV3, name='logV3'),



]


# url(r'^album/(?P#indicatest parameter#<name>#indicates value passed name#[A-Za-z]#indicates expression for parameter))
# the inputter name value is passed to the method in view.py 