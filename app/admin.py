from django.contrib import admin
from django.apps import apps
from .models import *
My_models = [data, password_resets]

admin.site.register(My_models)

# Register your models here.
