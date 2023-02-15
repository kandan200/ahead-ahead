from django import forms 
from django.forms import ModelForm
from docApp.models import UserProfile
from django.forms.widgets import NumberInput


class SignUpForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'