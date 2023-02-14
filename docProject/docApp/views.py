from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from docApp.forms import SignUpForm
from django.urls import reverse

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

    def form_valid(self, request):
        name = request.POST['firstName']
        id = request.POST['id']
        url = reverse('user-profile')
        return HttpResponseRedirect(url)


class ProfileView(View):
    def post(self, request):
        pass


class PathView(View):
    def get(self, request, name, id):
        return HttpResponse(f"<h1>Hello {name}, welcome to the platform. Your ID number is {id}</h1>")

def qryView(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Welcome to the platform {}, your user ID is {}".format(name, id))


#look out for django generic edit views for create, edit, delete profile of doctor and also for entered data
