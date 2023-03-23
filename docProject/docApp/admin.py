from django.contrib import admin
from docApp.models import Doctore, Participants, Research

# Register your models here.

@admin.register(Doctore) 
class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ("lastName", "firstName", "specialty") 
    search_fields = ("firstName__startswith",)
    list_filter = ('specialty', 'state_of_residence', 'sex')
    fieldsets = (('Bio' , {
        'fields':(('firstName', 'lastName'), 'sex')
    }),
    ('Contact', {
        'fields': (('email', 'phone_number'), 'state_of_residence'),
        'classes': ('collapse',),
        'description': "This section contains contact details for each user. Might get updated down the line"
    }),
    ('Proffesional Details', {
        'fields': ('specialty', 'mdcn')
    }),
    ('Security', {
        'fields':('password',)
    }))
    # fields = [('firstName', 'lastName'), 'sex', ('email', 'phone_number', 'state_of_residence'), ('specialty', 'mdcn')]
admin.site.register(Participants)
admin.site.register(Research)