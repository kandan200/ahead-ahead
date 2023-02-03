from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = '<h1>Hello Doc, welcome to ahead ahead</h1><br><button>Sign in</button><button>Create Account</button>'
    return HttpResponse(text)

def signIn(request):
    form = "<html><body><h1>Welcome Back</h1><form><div><label for='email'>Email</label><input type='email' name='email'></div><div><label for='password'>Password</label><input type='password' name='password'></div><div><button type='submit'>Sign in</button></form></body></html>"
    return HttpResponse(form)

def signUp(request):
    return render(request, 'signUp.html')

def pathView(request, name, id):
    return HttpResponse(f'welcome {name}, your User ID is: {id}')

def qryView(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Welcome to the platform {}, your user ID is {}".format(name, id))

def submitSignUpForm(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        location = request.POST['location']
    return HttpResponse(f"Welcome {firstName} {lastName}. How is {location} today?")