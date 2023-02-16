from django import forms 
from django.forms import ModelForm
from docApp.models import UserProfile


class SignUpForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
    }