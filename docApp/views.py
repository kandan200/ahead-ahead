from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView, ModelFormMixin
from docApp.forms import SignUpForm, SignInForm, ResearchForm, EditResearchForm, EditProfileForm, DeleteResearchForm, DeleteProfileForm, AddParticipantsForm, EditParticipantForm, DeleteParticipantForm
from django.urls import reverse, reverse_lazy
from docApp.models import Doctore, Research, Participants
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from docProject import settings
from django.core.mail import EmailMessage, send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

class SignInFormView(FormView):
    template_name = 'signIn.html'
    form_class = SignInForm

    def get(self, request):
        form = SignInForm()
        return render(request, 'signIn.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        id = request.POST['mdcn']
        password = request.POST['password']
        user = authenticate(username=id, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have succesfully logged in')
            return HttpResponseRedirect(reverse_lazy('docApp:user-profile', kwargs={'id':id}))
        else:
            messages.error(request, 'Bad Login credentials')
            return HttpResponseRedirect(reverse_lazy('docApp:home'))


class SignUpFormView(FormView):
    # i can use CreateView generic view to implement this view too
    template_name = 'signUp.html'
    form_class = SignUpForm
 # explore use of success_url attribute as a way to redirect after succesful saving of object to the model 

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signUp.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if request.POST['password'] == request.POST['confirm_password']:
            if form.is_valid():
                mdcn = form.cleaned_data['mdcn'] 
                password = form.cleaned_data['password']   
                email = form.cleaned_data['email']
                firstName = form.cleaned_data['firstName']
                form.save()

                #Aunthenticate the form manually before saving the form and creating user object

                user =User.objects.create_user(mdcn, email, password)
                user.save()

                # Welcome Email
                subject = "Welcome to Ahead Ahead"
                message = "Hello " + firstName + "!! \n" + "Welcome to Ahead Ahead!! \nThank you for creating an account with us\n. We will send you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
        

                messages.success(request, 'You have succesfully created and saved the user')
                return HttpResponseRedirect(reverse('docApp:sign-in'))

            else:
                return render(request, 'signUp.html', {'form': form})
        else:
            messages.error(request, 'Password and Confirm Password do not match')
            return HttpResponseRedirect(reverse('docApp:user-profile', kwargs={'id':mdcn}))



class StartResearchView(FormView):
    template_name = 'researchForm.html'
    form_class = ResearchForm

    def get(self, request, id):
        form = ResearchForm()
        user = Doctore.objects.get(pk=id)
        return render(request, 'researchForm.html', {'form': form, 'user':user})
    
    def post(self, request, id):
        form = ResearchForm(request.POST)
        if form.is_valid():
            form.save()
            doctor = Doctore.objects.get(pk=id)
            mdcn = doctor.mdcn
            id = form.cleaned_data['id']
            return HttpResponseRedirect(reverse('docApp:research-info', kwargs={'id':mdcn, 'r_id':id}))
        else:
            return render(request, 'researchForm.html', {'form': form})


class AddParticipantView(FormView):
    form_class = AddParticipantsForm

    def get(self, request, r_id):
        form = AddParticipantsForm()
        return render(request, 'addParticipant.html', {'form':form, 'r_id':r_id})
    
    def post(self, request, r_id):
        form = AddParticipantsForm(request.POST)
        if form.is_valid():
            form.save()
            p_id = form.cleaned_data['id']
            return HttpResponseRedirect(reverse('docApp:participant-info', kwargs={'r_id':r_id, 'p_id':p_id}))
        else:
            return render(request, 'addParticipant.html', {'form': form, 'r_id':r_id})


class ResearchDetails(DetailView):
    model = Research

    def get(self, request, id, r_id):
        research = Research.objects.get(pk=r_id)
        return render(request, 'researchDetail.html', {'research':research, 'id':id, 'r_id':r_id})
    

class ParticipantDetailsView(DetailView):
    model = Participants

    def get(self, request, r_id, p_id):
        participant = Participants.objects.get(pk=p_id)
        research = Research.objects.get(pk=r_id)
        return render(request, 'participantDetails.html', {'participant':participant, 'r_id':r_id, 'p_id':p_id, 'research':research})
    

class ProfileView(DetailView):
    model = Doctore

    def get(self, request, id):
        # if request.user.is_anonymous():
        #     raise PermissionDenied()
        user = Doctore.objects.get(pk=id)
        return render(request, 'profile.html', {'user':user})


class EditResearchView(ModelFormMixin, FormView):
    model = Research
    form_class = EditResearchForm

    def get(self, request, id, r_id):
        research = Research.objects.get(pk=r_id)
        form = EditResearchForm(instance=research)
        return render(request, 'editResearch.html', {'form':form, 'id':id, 'r_id':r_id})
    
    def post(self, request, id, r_id):
        research = Research.objects.get(pk=r_id)
        form = EditResearchForm(request.POST, instance=research)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('docApp:research-info', kwargs={'id':id, 'r_id':r_id}))


class EditParticipantView(ModelFormMixin, FormView):
    model = Participants
    form_class = EditParticipantForm

    def get(self, request, p_id, r_id):
        participant = Participants.objects.get(pk=p_id)
        form = EditParticipantForm(instance=participant)
        return render(request, 'editParticipant.html', {'form':form, 'p_id':p_id, 'r_id':r_id})
    
    def post(self, request, p_id, r_id):
        participant = Participants.objects.get(pk=p_id)
        form = EditParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('docApp:participant-info', kwargs={'p_id':p_id, 'r_id':r_id}))
        else:
            return render(request, 'editParticipant.html', {'form': form, 'r_id':r_id, 'p_id':p_id})


class EditProfileView(PermissionRequiredMixin, FormView):
    model = Doctore
    permission_required = 'docApp.change_UserProfile'
    permission_denied_message = '<h1>You need the update_UserProfile permision to edit this profile</h1>'
    template_name = 'editProfile.html'
    form_class = EditProfileForm    

    def get(self, request, id):
        doctor = get_object_or_404(Doctore, pk=id)
        form = EditProfileForm(instance=doctor)
        return render(request, 'editProfile.html', {'form':form, 'id':id})
    
    def post(self, request, id):
        doctor = get_object_or_404(Doctore, pk=id)
        form = EditProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('docApp:user-profile', kwargs={'id':id}))


class DeleteResearchView(DeleteView):   
    model = Research  
    form_class = DeleteResearchForm
    
    def get(self, request, id, r_id):
        research = Research.objects.get(pk=r_id)
        form = DeleteResearchForm(instance=research)
        return render(request, 'deleteResearch.html', {'form':form, 'id':id, 'r_id':r_id})
    
    def post(self, request, id, r_id):
        research = Research.objects.get(pk=r_id)
        research.delete()
        return HttpResponseRedirect(reverse_lazy('docApp:delete-research-success', kwargs={'id':id}))


class DeleteParticipantView(DeleteView):
    model = Participants
    form_class = DeleteParticipantForm

    def get(self, request, r_id, p_id):
        participant = Participants.objects.get(pk=p_id)
        form = DeleteParticipantForm(instance=participant)
        return render(request, 'deleteParticipant.html', {'form':form, 'p_id':p_id, 'r_id':r_id})
    
    def post(self, request, r_id, p_id):
        participant = Participants.objects.get(pk=p_id)
        participant.delete()
        return HttpResponseRedirect(reverse_lazy('docApp:delete-participant-success', kwargs={'r_id':r_id}))

        
class DeleteProfileView(DeleteView):   
    model = Doctore  
    form_class = DeleteProfileForm

    def get(self, request, id):
        doctor = Doctore.objects.get(pk=id)
        form = DeleteProfileForm(instance=doctor)
        return render(request, 'deleteProfile.html', {'form':form, 'id':id})
    
    def post(self, request, id):
        doctor = Doctore.objects.get(pk=id)
        doctor.delete()
        return HttpResponseRedirect(reverse_lazy('docApp:delete-profile-success'))

def DeleteProfileSuccessView(request):
    return render(request, 'profile_succesful_delete.html')


def DeleteResearchSuccessView(request, id):
    return render(request, 'succesful_delete.html', {'id':id})


def DeleteParticipantSuccessView(request, r_id):
    research= Research.objects.get(pk=r_id)
    mdcn = research.doctor.mdcn
    return render(request, 'participant_succesful_delete.html', {'r_id':r_id, 'mdcn':mdcn})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out succesfully.")
    return redirect('home')