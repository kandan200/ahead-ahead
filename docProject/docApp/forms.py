from django import forms 
from django.forms import ModelForm
from docApp.models import Doctore


class SignUpForm(ModelForm):
    class Meta:
        model = Doctore
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
    }

class SignInForm(ModelForm):
    class Meta:
        model = Doctore
        fields = [
            'email',
            'password',
        ]
        widgets = {
        'password': forms.PasswordInput(),
    }
