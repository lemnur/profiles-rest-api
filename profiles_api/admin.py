from django.contrib import admin

from . import models #lol you need .import for the profiles to show
# Register your models here.

admin.site.register(models.UserProfile) #make our model visible with the admin interface
