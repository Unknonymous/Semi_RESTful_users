# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

#set email regex for validation
EMAILREGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

#create manager class to hold validator function
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['fname']) <= 2: 
            errors['first_name'] = 'first_name must be at least two characters'
        if post_data['lname'] == "":
            errors['last_name'] = 'last_name cannot be blank'
        if not EMAILREGEX.match(post_data['email']):
            errors['email'] = 'email is not properly formated.'
        return errors

class User(models.Model):
#auto-increment id is automatic
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default = None)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.first_name


#**place line below in table upon which validations will be run**
#objects = userManager()
#**looping method below here.
#or to loop through post_data
#class userManager(models.Manager):
#	def validate(self, post_data):
#		for key in post_data:
#			if post_data[key] == '':  
#				 print key + 'cannot be empty