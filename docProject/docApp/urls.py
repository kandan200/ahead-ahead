from django.urls import path
from . import views
from docApp.views import SignUpFormView, ProfileView, EditProfileView, DeleteProfileView, SignInFormView


app_name = 'docApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', SignInFormView.as_view(), name='sign-in'),
    path('sign-up/', SignUpFormView.as_view(), name='sign-up'),
    path('<int:id>/', ProfileView.as_view(), name='user-profile'),
    path('<int:id>/edit/', EditProfileView.as_view(), name='edit-profile'),
    path('log-out/', views.logout_view, name='log-out'),
    path('<int:id>/delete/', DeleteProfileView.as_view(), name='delete-profile'),
    path('<int:id>/delete/success/', views.DeleteProfileSuccessView, name='delete-profile-success'),

]
