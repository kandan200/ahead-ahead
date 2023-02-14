from django import forms 

class SignUpForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    age = forms.IntegerField(label='age')
    sex = forms.CharField(label='sex', max_length=50)
    location = forms.CharField(label='location', max_length=100)
    specialty = forms.CharField(label='spacialty', max_length=100)
    
