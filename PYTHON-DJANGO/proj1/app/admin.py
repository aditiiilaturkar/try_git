# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(user)
admin.site.register(book)
admin.site.register(issued_book)

