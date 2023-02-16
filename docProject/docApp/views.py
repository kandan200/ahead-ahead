from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from docApp.forms import SignUpForm
from django.urls import reverse
from docApp.models import UserProfile
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    text = '<h1>Hello Doc, welcome to ahead ahead</h1><br><button>Sign in</button><button>Create Account</button>'
    return HttpResponse(text)

def signIn(request):
    form = "<html><body><h1>Welcome Back</h1><form><div><label for='email'>Email</label><input type='email' name='email'></div><div><label for='password'>Password</label><input type='password' name='password'></div><div><button type='submit'>Sign in</button></form></body></html>"
    return HttpResponse(form)

class SignUpFormView(FormView):
    template_name = 'signUp.html'
    form_class = SignUpForm

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signUp.html', {'form': form})

    def post(self, request):
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data['email']
            # password = form.clean['password']
            id = form.cleaned_data['mdcn']           
            # user = authenticate(request, username=email , password=password)
            # if user is not None:
                # login(request, user)
                # return HttpResponseRedirect(reverse('docApp:user-profile', kwargs={'id':id}),  request)
            # else:
                # Return an 'invalid login' error message.
                # pass
        return HttpResponseRedirect(reverse('docApp:user-profile', kwargs={'id':id}),  request)

class ProfileView(DetailView):
    model = UserProfile

    def get(self, request, id):
        # if request.user.is_anonymous():
        #     raise PermissionDenied()
        user = UserProfile.objects.get(pk=id)
        return render(request, 'profile.html', {'user':user})


class EditProfileView(PermissionRequiredMixin, UpdateView):
    model = UserProfile
    permission_required = 'docApp.change_UserProfile'
    permission_denied_message = '<h1>You need the update_UserProfile permision to edit this profile</h1>'
    # template_name = 'editProfile.html'
    fields = ['firstName', 'lastName', 'date_of_birth', 'email', 'phone_number', 'specialty', 'year_of_graduation', 'avatar', 'state_of_residence']
    
    def get(self, request):
        id = request.GET['id']
        self.object = get_object_or_404(UserProfile, pk=id)
        pass
#look out for django generic edit views for create, edit, delete profile of doctor and also for entered data

def logout_view(request):
    logout(request)
    pass
