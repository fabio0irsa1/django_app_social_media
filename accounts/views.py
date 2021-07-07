from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
from . import forms
from accounts.forms import UserCreateForm, ProfileForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import UserProfileInfo
from django.core.files.storage import default_storage

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# manipulate DateInput
import datetime

# Create your views here.

def SignUp(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserCreateForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            user.save()

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

            # Delay page redirect?
            return HttpResponseRedirect(reverse('login'))

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserCreateForm()
        profile_form = ProfileForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'accounts/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



@login_required
def Profile(request):

    access_user = request.user

    if request.method == 'POST':

        profile_form = ProfileUpdateForm(request.POST,request.FILES)
        
        if profile_form.is_valid():

            # Check which fields were changed and update them in the database
            if 'profile_pic' in request.FILES:
                file = request.FILES['profile_pic']
                file_name = default_storage.save(file.name, file)
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(profile_pic=file_name)

            if  len(request.POST['first_name']):
                print(len(request.POST['first_name']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(first_name=request.POST['first_name'])

            if  len(request.POST['last_name']):
                print(len(request.POST['last_name']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(last_name=request.POST['last_name'])

            if  len(request.POST['birth_date']):
                print(len(request.POST['birth_date']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(birth_date=request.POST['birth_date'])

            if  len(request.POST['location']):
                print(len(request.POST['location']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(location=request.POST['location'])

            if  len(request.POST['bio']):
                print(len(request.POST['bio']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(bio=request.POST['bio'])

            if  len(request.POST['website_link']):
                print(len(request.POST['website_link']))
                UserProfileInfo.objects.filter(pk=access_user.userprofileinfo.id).update(website_link=request.POST['website_link'])

            return HttpResponseRedirect(request.path)
    else:
        profile_form = ProfileUpdateForm(instance=request.user)

    context={'profile_form': profile_form, 'access_user': access_user}
    return render(request, 'accounts/profile.html',context )
