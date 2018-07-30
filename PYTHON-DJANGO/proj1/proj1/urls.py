"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from models import User
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.start),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^student_profile/', views.student_profile),
    url(r'^lib_profile/', views.lib_profile),
    url(r'^logout/', views.logout),
    url(r'^book_summary/', views.book_summary),
    url(r'^library/', views.library),
    url(r'^edit_profile/', views.edit_prof),
    url(r'^remove_account/', views.remove_account),
    url(r'^booked/', views.booked),
    url(r'^cancel/', views.cancel),
    url(r'^picked_up/', views.picked_up),
    url(r'^returned/', views.returned),
    url(r'^add_new_book/', views.add_new_book),
    url(r'^current_status/', views.current_status),
    url(r'^fee_receipt/', views.fee_receipt),



]
