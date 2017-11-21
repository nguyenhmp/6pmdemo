# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User
# Create your models here.
class Blog(models.Model):
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
