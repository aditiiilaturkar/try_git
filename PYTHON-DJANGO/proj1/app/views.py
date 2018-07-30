# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from app import models
from django.views.decorators.csrf import csrf_exempt
from models import user
from models import book
from models import issued_book
from reportlab.pdfgen import canvas
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
from datetime import datetime,timedelta


def fee_receipt(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	return_id=request.GET['return_id']
	bookname=request.GET['bookname']
	student_name=request.GET['student_name']
	obj=models.issued_book.objects.get(issued_book=bookname)
	issue_date=obj.issue_date;
	issue_date=str(issue_date)

	return_date=obj.return_date;	
	return_date=str(return_date)

	delta= obj.return_date-obj.issue_date;
	total_fine=(delta.days-15)*30;
	var=str(total_fine)	
	delta=str(delta)
	p = canvas.Canvas(response)

	p.drawString(150, 800, "PUNE INSTITUTE OF COMPUTER TECHNOLOGY")
	p.drawString(225, 770, "STUDENT LIBRARY")
	p.drawString(240, 740, "FINE-RECEIPT")
	p.drawString(150, 690, "Student name :"+student_name)
	p.drawString(150, 660, "Issued book :"+bookname)

	p.drawString(150, 630, "Issued date :"+issue_date)
	p.drawString(150, 600, "Return date :"+return_date)
	p.drawString(150, 570, "Total Fine Rs:"+var	+" /- only")



	p.showPage()
	p.save()
	return response
			

@csrf_exempt
def returned(request):
	issued_id=request.GET['issued_id'];
	issued_book.objects.get(id=issued_id).delete()
	bookname=request.GET['bookname'];
	obj=book.objects.get(bookname=bookname)
	copies=obj.copies
	copies=copies+1;
	book.objects.filter(bookname=bookname).update(copies=copies)


	return redirect("/current_status/")


@csrf_exempt
def register(request):
	
	if request.method=="GET":
		return render(request,'register.html');
	elif request.method=="POST":

		Name=request.POST['name'];
		if models.user.objects.filter(name=Name).exists():
			return render(request,'register.html');	        
		else:
			Name=request.POST['name'];
			Password=request.POST['password'];
			Email=request.POST['email'];
			try:
				Usertype=request.POST['usertype']
			except:
				context={}
				context['usertypeerror']="Please select one option..!!"
				return render(request,'register.html',context);	
			obj1=models.user(name=Name,password=Password,email=Email,usertype=Usertype)
			obj1.save()

			return redirect("/login/")

@csrf_exempt
def add_new_book(request):
	if request.method=="GET":
		return render(request,'add_new_book.html');
	elif request.method=="POST":
		bookname=request.POST['bookname'];
		Author=request.POST['author'];
		subject=request.POST['subject'];
		rating=request.POST['rating'];
		copies=request.POST['copies'];
		summary=request.POST['summary'];
		context={}
		obj1=models.book(bookname=bookname,author=Author,subject=subject,rating=rating,copies=copies,summary=summary)
		obj1.save()

		return redirect("/login/")

			
@csrf_exempt
def login(request):
	if "username" in request.session:
		if request.session["authority"]=="librarian":	
			return redirect("/lib_profile/")
		if request.session["authority"]=="student":	
			return redirect("/student_profile/")
	context={}
	if request.method=="GET":
		return render(request,'login.html');
	elif request.method=="POST":
		name=request.POST['name'];
		password=request.POST['password'];
		if user.objects.filter(name=name).exists():
			if user.objects.filter(password=password,name=name).exists():
				user_object=user.objects.get(name=name);
				request.session["username"]=user_object.name;
				request.session["authority"]=user_object.usertype;
				if user_object.usertype=="librarian":
					return redirect("/lib_profile/")
				if user_object.usertype=="student":
					return redirect("/student_profile/")
			else:
				context["wrongpass"]="wrong password..!"
				return render(request,'login.html',context)
		else:
			context["wrongname"]="User doesnt exist! "
    		return render(request,'login.html',context)

        
@csrf_exempt
def student_profile(request):
	if "username" in request.session and request.session["authority"]=="student":
		context={}
		try:
			context['error']=request.GET['error']
		except:
			pass
		context["booktable"]=models.book.objects.all()
		context["username"]=request.session["username"]
		context["usertype"]=request.session["authority"]
		obj=models.user.objects.get(name=request.session["username"])
		context["email"]=obj.email
		return render(request,'student_profile.html',context);
	else:
		return redirect("/login/")

@csrf_exempt
def lib_profile(request):
	if "username" in request.session  and request.session["authority"]=="librarian":	    
		context={}
		context["books"]=models.issued_book.objects.all();
		context["booktable"]=models.book.objects.all()
		context["username"]=request.session["username"]
		context["usertype"]=request.session["authority"]

		obj=models.user.objects.get(name=request.session["username"])
		context["email"]=obj.email
		return render(request,'lib_profile.html',context);
	else:
		return redirect("/login/")

		 
@csrf_exempt
def start(request):
	if "name" in request.session :	    
		context={}
		context["usertype"]=request.session["usertype"]
	if request.session["authority"]=="student":
		return redirect("/student_profile/")
	elif request.session["authority"]=="librarian":
		return redirect("/lib_profile/")
	else:
		return redirect("/login/")

@csrf_exempt
def logout(request):
	if "username" in request.session :
		del request.session["username"];
	return redirect("/login/")

@csrf_exempt
def library(request):
		try:
			parameter=request.GET['input']
		except:
			parameter='all'
		try:
			request.session['authority']=request.GET['authority']
		except:
			pass
		context={}
	
		context["username"]=request.session['username']
		if models.book.objects.filter(bookname=parameter).exists():
			context["books"]=models.book.objects.filter(bookname=parameter);
		elif models.book.objects.filter(subject=parameter).exists():
			context["books"]=models.book.objects.filter(subject=parameter);
		elif models.book.objects.filter(author=parameter).exists():	
			context["books"]=models.book.objects.filter(author=parameter);
		elif parameter=='all':
			context["books"]=models.book.objects.all();
		context['authority']=request.session['authority']
		if context['authority']=="student":
			return render(request,'student_library.html',context);
		else:
			return render(request,'librarian_library.html',context);
				

@csrf_exempt
def remove_account(request):
	#request.session['username']=request.GET['username'];
	username=request.session['username'];
	obj=user.objects.get(name=username);
	obj.delete();
	return redirect("/logout/");

@csrf_exempt
def picked_up(request):
	issued_id=request.GET['issued_id'];
	issued_book.objects.filter(id=issued_id).update(status="picked")
	return redirect("/current_status/")


@csrf_exempt
def booked(request):
	context={};
	book_id=request.GET['book_id'];

	book_id=int(book_id)
	obj=book.objects.get(id=book_id)
	copies=obj.copies
	copies=copies-1;
	bookname=obj.bookname;
	name=request.session['username'];
	obj2=models.issued_book(id=book_id,issued_book=bookname,student_name=name);
	obj2.save();
	book.objects.filter(id=book_id).update(copies=copies)
	return render(request,'booked.html',context);
	
@csrf_exempt
def cancel(request):
	context={};
	book_id=request.GET['book_id'];
	book_id=int(book_id)
	obj=book.objects.get(id=book_id)
	copies=obj.copies
	copies=copies+1;
	obj=book.objects.filter(id=book_id).update(copies=copies)
	obj1=issued_book.objects.filter(id=book_id)
	obj1.delete();
	return redirect("/current_status/")

@csrf_exempt
def edit_prof(request):
	if request.method == "GET":
		return render(request,'edit.html',{})
	else:
		username=request.session['username'];
		obj=user.objects.get(name=username);
		obj.delete();
		Name=request.POST['name'];
		Password=request.POST['password'];
		Email=request.POST['email'];
		Usertype=request.POST['usertype'];
		obj1=models.user(name=Name,password=Password,email=Email,usertype=Usertype)
		obj1.save()
		context={}
		try:
			request.session['authority']=request.GET['authority']
		except:
			pass
		context['authority']=request.session['authority']
		context['name']=obj1.name;
		context['usertype']=obj1.usertype;
		context['email']=obj1.email;
		if context['authority']=="Student":
			return render(request,'student_profile.html',context);
		else:
			return render(request,'lib_profile.html',context);
	
 
@csrf_exempt
def current_status(request):
	context={};
	try:
		request.session['authority']=request.GET['authority']
	except:
		pass
	try:
		request.session['username']=request.GET['username']
	except:
		pass

	if  request.session['authority'] =="student":
		context['authority']="student"
		username=request.session['username']		
		context["books"]=models.issued_book.objects.filter(student_name=username);
		context["username"]=request.session['username']
		return render(request,'student_status.html',context)	
	else:
		context['authority']="librarian"
		context["issued_books"]=models.issued_book.objects.all();
		return render(request,'lib_status.html',context)

		
@csrf_exempt
def book_summary(request):
	context={}
	book_id=request.GET["book_id"];
	name=request.session['username']
	print book_id;
	obj=book.objects.get(id=book_id);
	context["summary"]=obj.summary;
	context["name"]=name;
	return render(request,'summary.html',context);
