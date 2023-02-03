from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up', views.signUp, name='sign-up'),
    path('getuser/<name>/<id>', views.pathView, name='getuser'),
    path('getuser/', views.qryView, name='qryview'),
    path('submit-sign-up-form', views.submitSignUpForm, name='submit-sign-up-form')
]
