# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length =30)
	password = models.CharField(max_length= 30)
	email= models.CharField(max_length =30)
	age=models.CharField(max_length=30)

	def __str__(self):
		return self.name+" "+self.password

class products(models.Model):
	name = models.CharField(max_length =30)
	price = models.CharField(max_length= 30)
	producttype= models.CharField(max_length =30)
	rating=models.CharField(max_length=30)

	
	def __str__(self):
		return self.name+" "+self.price
