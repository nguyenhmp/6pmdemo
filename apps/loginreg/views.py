# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.
def index(req):
	return render(req, "loginreg/index.html")

def register(req):
	result = User.objects.validation(req.POST) # (True, ""), (False, [Errors])
	if result[0]:
		#valid
		hashed_pw = bcrypt.hashpw(req.POST["password"].encode(), bcrypt.gensalt())
		User.objects.create(first_name=req.POST["first_name"],last_name=req.POST["last_name"],email=req.POST["email"],password=hashed_pw)
		messages.error(req, "Thanks for registering please login")
		return redirect('/')
		#hash password, register user and add to database
	else:
		errors = result[1]
		for error in errors:
			messages.error(req, error)
		#send error messages and redirect
		return redirect('/')

def login(req):
	result = User.objects.loginValidation(req.POST)
	if result[0]:
		# go to database, check for user, check for password
		user = User.objects.filter(email=req.POST["email"]) #returns an array
		if len(user) == 0:
			messages.error(req, "email does not exist")
		else:
			user = user[0]
			if user.checkpw(req.POST["password"]):
				req.session["user_id"] = user.id
				messages.error(req, "yay logged in...my app doesnt do anything...yet")
			else:
				messages.error(req, "incorrect password")
			#check password
	else:
		messages.error(req, "email and password cant be blank")
	return redirect('/')

