# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	username = models.CharField(max_length = 16)

class UserPassword(models.Model):
	user = models.ForeignKey(User)
	password = models.CharField(max_length = 32)



