from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from docApp.forms import SignUpForm, SignInForm
from django.urls import reverse
from docApp.models import Doctore
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

class SignInFormView(FormView):
    template_name = 'docApp:signIn.html'
    form_class = SignInForm

    def get(self, request):
        form = SignInForm()
        return render(request, 'docApp:signIn.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            doctore = Doctore.objects.get(email=email)
            id = doctore.mdcn
        return HttpResponseRedirect(reverse('docApp:user-profile', kwargs={'id':id}),  request)


class SignUpFormView(FormView):
    # i can use CreateView generic view to implement this view too
    template_name = 'docApp:signUp.html'
    form_class = SignUpForm
 # explore use of success_url attribute as a way to redirect after succesful saving of object to the model 

    def get(self, request):
        form = SignUpForm()
        return render(request, 'docApp:signUp.html', {'form': form})

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
    model = Doctore

    def get(self, request, id):
        # if request.user.is_anonymous():
        #     raise PermissionDenied()
        user = Doctore.objects.get(pk=id)
        return render(request, 'docApp:profile.html', {'user':user})


class EditProfileView(PermissionRequiredMixin, UpdateView):
    model = Doctore
    permission_required = 'docApp.change_UserProfile'
    permission_denied_message = '<h1>You need the update_UserProfile permision to edit this profile</h1>'
    # template_name = 'editProfile.html'
    fields = ['firstName', 'lastName', 'date_of_birth', 'email', 'phone_number', 'specialty', 'year_of_graduation', 'avatar', 'state_of_residence']
    
    def get(self, request):
        id = request.GET['id']
        self.object = get_object_or_404(Doctore, pk=id)
        pass
#look out for django generic edit views for create, edit, delete profile of doctor and also for entered data

def logout_view(request):
    logout(request)
    pass

class DeleteProfileView(DeleteView):   
    model = Doctore  
    success_url = '<int:id>/delete/success/'
    template_name = 'docApp:deleteprofile.html'

def DeleteProfileSuccessView(request):
    return render(request, 'succesful_delete.html')