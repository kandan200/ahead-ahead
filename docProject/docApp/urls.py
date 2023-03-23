from django.urls import path
from . import views
from docApp.views import SignUpFormView, ProfileView, EditProfileView, DeleteProfileView, SignInFormView, StartResearchView, ResearchDetails, EditResearchView, DeleteResearchView, AddParticipantView, ParticipantDetailsView, EditParticipantView, DeleteParticipantView


app_name = 'docApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in/', SignInFormView.as_view(), name='sign-in'),
    path('sign-up/', SignUpFormView.as_view(), name='sign-up'),
    path('<int:id>/', ProfileView.as_view(), name='user-profile'),
    path('<int:id>/edit/', EditProfileView.as_view(), name='edit-profile'),
    path('log-out/', views.logout_view, name='log-out'),
    path('<int:id>/delete/', DeleteProfileView.as_view(), name='delete-profile'),
    path('delete/success/', views.DeleteProfileSuccessView, name='delete-profile-success'),
    path('<int:id>/research/', StartResearchView.as_view(), name='start-research'),
    path('<int:id>/research/<str:r_id>/details/', ResearchDetails.as_view(), name='research-info'),
    path('<int:id>/research/<str:r_id>/edit/', EditResearchView.as_view(), name='edit-research'),
    path('<int:id>/research/<str:r_id>/delete/', DeleteResearchView.as_view(), name='delete-research'),
    path('<int:id>/research/delete/success/', views.DeleteResearchSuccessView, name='delete-research-success'),
    path('research/<str:r_id>/participant/', AddParticipantView.as_view(), name='add-participant'),
    path('research/<str:r_id>/participant/<str:p_id>/', ParticipantDetailsView.as_view(), name='participant-info'),
    path('research/<str:r_id>/participant/<str:p_id>/edit/', EditParticipantView.as_view(), name='edit-participant'),
    path('<str:r_id>/participant/delete/success/', views.DeleteParticipantSuccessView, name='delete-participant-success'),
    path('research/<str:r_id>/participant/<str:p_id>/delete/', DeleteParticipantView.as_view(), name='delete-participant'),
]
