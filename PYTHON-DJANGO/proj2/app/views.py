# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import models
from django.views.decorators.csrf import csrf_exempt
from models import user
from django.http import HttpResponseRedirect

@csrf_exempt
def register(request):
	context={}
	if request.method=="GET":
		return render(request,'register.html');
	elif request.method=="POST":
		name=request.POST['username']
		if models.user.objects.filter(name=name).exists():
						context["message"]="User name already exists..";
						return render(request,'register.html',context)
		else:
			name=request.POST['username']
			password=request.POST['password']
			email=request.POST['email']
			age=request.POST['age']			
		
			obj1=models.user(name=name,password=password,email=email,age=age)
			obj1.save()
			return render(request,'registersuccess.html')

@csrf_exempt
def login(request):
	context={}
	if request.method=="GET":
		return render(request,'login.html',{});
	elif request.method=="POST":
		name=request.POST['username']
		password=request.POST['password']
		if user.objects.filter(name=name).exists():
			if user.objects.filter(password=password,name=name).exists():
				user_object=user.objects.get(name=name);
				return render(request,profile.html)
			else:
				return render(request,'register.html',context)
		else:
			  context["wrongname"]="User doesnt exist! ";
			  return render(request,'login.html',context)
