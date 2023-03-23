from django import forms 
from django.forms import ModelForm
from docApp.models import Doctore, Research, Participants


class SignUpForm(ModelForm):
    class Meta:
        model = Doctore
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
        'confirm_password': forms.PasswordInput(),

    }

class SignInForm(ModelForm):
    class Meta:
        model = Doctore
        fields = [
            'mdcn',
            'password',
        ]
        widgets = {
        'password': forms.PasswordInput(),
    }

class EditProfileForm(ModelForm):
    class Meta:
        model = Doctore
        fields = ['firstName', 'lastName', 'email', 'phone_number', 'specialty', 'state_of_residence']


class DeleteProfileForm(ModelForm):
    class Meta:
        model = Doctore
        fields =[]


class ResearchForm(ModelForm):
    class Meta:
        model = Research
        fields = '__all__'
        widgets = { 
            'start_date':forms.SelectDateWidget(),
        }

class EditResearchForm(ModelForm):
    class Meta:
        model = Research
        fields = ['title', 'sample_size']

class DeleteResearchForm(ModelForm):
    class Meta:
        model = Research
        fields =[]


class AddParticipantsForm(ModelForm):
    class Meta:
        model = Participants
        fields = '__all__'
        widgets = { 
            'presentation_date':forms.SelectDateWidget(),
        }


class EditParticipantForm(ModelForm):
    class Meta:
        model = Participants
        exclude =['id']

class DeleteParticipantForm(ModelForm):
    class Meta:
        model = Participants
        fields = []