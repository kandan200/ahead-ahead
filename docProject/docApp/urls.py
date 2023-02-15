from django.urls import path
from . import views
from docApp.views import SignUpFormView, ProfileView, EditProfileView


app_name = 'docApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up/', SignUpFormView.as_view(), name='sign-up'),
    path('<int:id>/', ProfileView.as_view(), name='user-profile'),
    path('<int:id>/edit/', EditProfileView.as_view(), name='edit-profile'),
]
