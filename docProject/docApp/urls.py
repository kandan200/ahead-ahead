from django.urls import path
from . import views
from docApp.views import PathView, SignUpFormView, ProfileView


app_name = 'docApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up/', SignUpFormView.as_view(), name='sign-up'),
    path('<name>/<int:id>/', ProfileView.as_view(), name='user-profile'),
    path('getuser/<name>/<id>/', PathView.as_view(), name='getuser'),
    path('getuser/', views.qryView, name='qryview'),
]
