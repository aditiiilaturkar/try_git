# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime,timedelta
# Create your models here.




class user(models.Model):
	name = models.CharField(max_length =30,blank=False)
	password = models.CharField(max_length= 30,blank=False)
	email= models.CharField(max_length =30)
	#username = models.CharField(max_length =30,blank=False)

	TYPES= (
	    ('librarian', 'librarian'),
	    ('student', 'student'),
	    )
	usertype=models.CharField(max_length =30,default="aaa",choices=TYPES)

	def __str__(self):
		return self.name

class book(models.Model):
	bookname= models.CharField(max_length =30)
 	author=models.CharField(max_length =30)
	subject=models.CharField(max_length =30)
	rating=models.CharField(max_length =30)
	summary=models.CharField(max_length =100)
 	copies=models.IntegerField(default=0)

	def __str__(self):
		return self.bookname


class issued_book(models.Model):
	issued_book= models.CharField(max_length =30)
	student_name=models.CharField(max_length =30)
	issue_date=models.DateTimeField(default=datetime.now(),blank=True)
	return_date=models.DateTimeField(default=datetime.now()+ timedelta(days=15),blank=True)
	status= models.CharField(max_length =30,default="not_picked")
	def __str__(self):
		return self.issued_book+self.status;

