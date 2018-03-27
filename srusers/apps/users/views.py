# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

#views detailed below

# GET request to /users - calls the index method to display all the users. 
# This will need a template.
def index(request):
    context = {'users': User.objects.all()}   #context must be a dict rather than QuerySet.
    return render(request, 'users/index.html', context)

#GET /users/<id> - calls the show method to display the info for a particular user with given id. 
#This will need a template.
def show(request, id):
    single = {'user': User.objects.get(id=id)}   #context must be a dict rather than QuerySet.
    return render(request, 'users/show.html', single)

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. 
# This will need a template.
def edit(request, id):
    single = {'user': User.objects.get(id=id)} #context must be a dict rather than QuerySet.
    return render(request, 'users/edit_user.html', single)

# POST /users/update - calls the update method to process the submitted form sent from /users/<id>/edit. 
# Have this redirect to /users/<id> once updated.
def update(request):
    #check for errors in submitted data
    request.session['id'] = request.POST['id']
    errors = User.objects.validate(request.POST)
    if not errors == {}:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("users:editUser", kwargs={'id': request.session['id']} ))

    #call and edit user data
    tweakUser = User.objects.get(id=request.session['id'])
    tweakUser.first_name = request.POST['fname']
    tweakUser.last_name = request.POST['lname']
    tweakUser.email = request.POST['email']
    tweakUser.save()
    
    return redirect(reverse("users:show_user", kwargs={'id': tweakUser.id} ))

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. 
# This will need a template.
def new(request):
    return render(request, 'users/new_user.html')

# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. 
# Have this redirect to /users/<id> once created.
def create(request):
    errors = User.objects.validate(request.POST)
    if not errors == {}:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("users:newUser"))
    
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    
    newUser = User.objects.create(first_name=first_name, last_name=last_name, email=email )
    
    #return redirect( '/users/' + str(newUser.id) )
    return redirect(reverse ("users:show_user", kwargs={'id': newUser.id}))

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
# Have this redirect back to /users once deleted.
def destroy(request, id):

    marked = User.objects.get(id=id)
    marked.delete()
    #response ='Hello, I am the index seed.' + id
    return redirect(reverse('users:list'))