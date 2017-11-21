# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
# Create your models here.
class UserManager(models.Manager):
	#.all .get .filter .exclude .include
	def validation(self, data):
		#data is a dictionary
		errors = []
		if len(data["first_name"]) == 0:
			errors.append("first name is required")
		if len(data["last_name"]) == 0:
			errors.append("last name is required")
		if data["email"] == "":
			errors.append("email is required")
		if data["password"] == "":
			errors.append("password is required")
		if len(errors) == 0:
			return True,
		else:
			return False, errors
	def loginValidation(self, data):
		errors = []
		if data["email"] == "":
			errors.append("email is required")
		if data["password"] == "":
			errors.append("password is required")
		if len(errors) == 0:
			return True,
		else:
			return False, errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def fullName(self):
		return self.first_name + " " + self.last_name
	def checkpw(self, data):
		return bcrypt.checkpw(data.encode(), self.password.encode())





