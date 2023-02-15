from django.contrib import admin
from docApp.models import UserProfile


@admin.register(UserProfile) 
class AdminUser(admin.ModelAdmin): 
    list_display = ("lastName", "firstName") 
    search_fields = ("firstName__startswith",)
# Register your models here.

# admin.site.register(UserProfile)