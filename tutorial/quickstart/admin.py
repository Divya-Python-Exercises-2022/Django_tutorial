#from django.contrib import admin

# Register your models here.
from django.contrib import admin

from tutorial.quickstart.models import Book
admin.site.register(Book)
