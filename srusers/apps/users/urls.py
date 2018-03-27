from django.conf.urls import url
from . import views

urlpatterns = [
    # GET request to /users - calls the index method to display all the users. 
    # This will need a template.
    url(r'^users/$', views.index, name='list'),
    
    # GET request to /users/new - calls the new method to display a form allowing users to create a new user. 
    # This will need a template.
    url(r'^users/new$', views.new, name='newUser'),

    # POST to /users/create - calls the create method to insert a new user record into our database. 
    # This POST should be sent from the form on the page /users/new. 
    # Have this redirect to /users/<id> once created.
    url(r'^users/create$', views.create, name='createUser'),

    #GET /users/<id> - calls the show method to display the info for a particular user with given id. 
    #This will need a template.
    url(r'^users/(?P<id>\d+)$', views.show, name='show_user'),
    
    # GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. 
    # This will need a template.
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name='editUser'),
    
    # POST /users/update - calls the update method to process the submitted form sent from /users/<id>/edit. 
    # Have this redirect to /users/<id> once updated.
    url(r'^users/update$', views.update, name='updateUser'),
    
    # GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
    # Have this redirect back to /users once deleted.
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy, name='userDelete'),
]